"""Validate skill layout, metadata, attribution, and internal markdown links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
REQUIRED_FIELDS = {
    "name",
    "description",
    "category",
    "tags",
    "source_repository",
    "original_path",
    "author",
    "license",
    "source_commit",
    "date_added",
    "last_verified",
    "adapted",
    "supported_agents",
    "admission_status",
}


def validate_links(markdown_path: Path) -> list[str]:
    errors = []
    for line_number, line in enumerate(markdown_path.read_text(encoding="utf-8").splitlines(), 1):
        for target in re.findall(r"\]\(([^)#]+)(?:#[^)]+)?\)", line):
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (markdown_path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{markdown_path.relative_to(ROOT)}:{line_number}: broken link {target}")
    return errors


def main() -> int:
    errors: list[str] = []
    identifiers: set[str] = set()
    for skill_dir in sorted(path for path in SKILLS_DIR.rglob("*") if path.is_dir()):
        if not (skill_dir / "SKILL.md").exists() and not (skill_dir / "metadata.json").exists():
            continue
        skill_file = skill_dir / "SKILL.md"
        metadata_file = skill_dir / "metadata.json"
        if not skill_file.exists() or not metadata_file.exists():
            errors.append(f"{skill_dir.relative_to(ROOT)}: requires SKILL.md and metadata.json")
            continue
        try:
            metadata = json.loads(metadata_file.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{metadata_file.relative_to(ROOT)}: invalid JSON: {exc}")
            continue
        missing = REQUIRED_FIELDS - metadata.keys()
        if missing:
            errors.append(f"{metadata_file.relative_to(ROOT)}: missing fields {sorted(missing)}")
        name = metadata.get("name", "")
        if not isinstance(name, str) or not NAME_PATTERN.fullmatch(name):
            errors.append(f"{metadata_file.relative_to(ROOT)}: name must be lowercase kebab-case")
        if name in identifiers:
            errors.append(f"{metadata_file.relative_to(ROOT)}: duplicate skill identifier {name}")
        identifiers.add(name)
        if name != skill_dir.name:
            errors.append(f"{metadata_file.relative_to(ROOT)}: name does not match directory")
        if not isinstance(metadata.get("tags"), list) or not all(isinstance(tag, str) for tag in metadata.get("tags", [])):
            errors.append(f"{metadata_file.relative_to(ROOT)}: tags must be a list of strings")
        repository = metadata.get("source_repository", "")
        if not isinstance(repository, str) or urlparse(repository).scheme not in {"http", "https"}:
            errors.append(f"{metadata_file.relative_to(ROOT)}: source_repository must be an HTTP(S) URL")
        if not metadata.get("license"):
            errors.append(f"{metadata_file.relative_to(ROOT)}: license is required")
        if metadata.get("admission_status") not in {"Approved", "Under Review", "Rejected"}:
            errors.append(
                f"{metadata_file.relative_to(ROOT)}: admission_status must be "
                "Approved, Under Review, or Rejected"
            )
        if metadata.get("admission_status") != "Approved":
            errors.append(
                f"{metadata_file.relative_to(ROOT)}: only Approved skills may be included"
            )
        errors.extend(validate_links(skill_file))

    if errors:
        print("\n".join(f"ERROR: {error}" for error in errors))
        return 1
    print(f"Validated {len(identifiers)} skills successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
