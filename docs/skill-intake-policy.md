# Skill intake, verification, and contribution policy

This policy is mandatory before importing or adding any skill from an external
repository. Public availability does not automatically grant redistribution
permission.

## Required checks

1. **Source identification:** record the repository, URL, original path,
   author or organization, source commit/version, and collection date.
2. **License:** inspect repository and skill-specific notices. Confirm
   redistribution and modification rights; preserve required notices. If
   unclear or incompatible, do not copy the content.
3. **Quality:** confirm a clear purpose, actionable and accurate instructions,
   useful examples, maintenance relevance, and value beyond generic prompting.
4. **Duplicates:** search the index and compare functionality. Improve an
   existing skill instead of adding an equivalent copy.
5. **Security:** inspect scripts, shell commands, downloads, credentials,
   filesystem changes, privileged or destructive operations, and prompt
   injection. Never execute imported scripts merely to inspect them.
6. **Standardization:** use one skill directory with `SKILL.md`,
   `metadata.json`, and optional `references/` or `examples/`. Document any
   modifications and preserve attribution.
7. **Validation:** run the repository validation and index-generation scripts.

Every included skill must have metadata for `name`, `description`, `category`,
`tags`, `source_repository`, `original_path`, `author`, `license`,
`source_commit`, `date_added`, `last_verified`, `adapted`,
`supported_agents`, and `admission_status`. Use `null` or an explicit unknown
value when information is unavailable; never invent provenance.

## Contribution checklist

Each submission must state:

- Skill name and category.
- Original source URL and provenance.
- License verification result.
- Short description and quality assessment.
- Security review result.
- Duplicate check result.
- Modifications made.
- Admission status and validation results.

Use `Approved`, `Under Review`, or `Rejected`. Only `Approved` skills may be
included under `skills/`. Unresolved licensing or security concerns require a
source record under `sources/` instead.
