"""Search the generated skill index using only the Python standard library."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "skills-index.json"


def main() -> int:
    parser = argparse.ArgumentParser(description="Search agentic skills.")
    parser.add_argument("query", nargs="*", help="Text to find in name, description, category, or tags.")
    parser.add_argument("--category", help="Only show skills in this category.")
    parser.add_argument("--tag", help="Only show skills with this tag.")
    args = parser.parse_args()

    records = json.loads(INDEX.read_text(encoding="utf-8"))
    terms = [term.lower() for term in args.query]
    matches = []
    for record in records:
        haystack = " ".join(
            [record["name"], record["description"], record["category"], *record["tags"]]
        ).lower()
        if terms and not all(term in haystack for term in terms):
            continue
        if args.category and record["category"].lower() != args.category.lower():
            continue
        if args.tag and args.tag.lower() not in [tag.lower() for tag in record["tags"]]:
            continue
        matches.append(record)

    if not matches:
        print("No matching skills found.")
        return 1
    for record in matches:
        print(f"{record['name']} [{record['category']}]")
        print(f"  {record['description']}")
        print(f"  {record['path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
