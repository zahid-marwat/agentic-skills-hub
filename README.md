# Agentic Skills Hub

![Validation](https://github.com/zahid-marwat/agentic-skills-hub/actions/workflows/validate.yml/badge.svg)

A curated, searchable library of reusable skills for AI coding agents and
vibe-coding tools. Each skill is isolated, documented, attributed, and
validated so it can be reused without hunting through many repositories.

## What is here?

- **Original starter skills** that are maintained in this repository.
- **Source records** for public skill ecosystems, including licensing and
  redistribution notes.
- **Generated indexes** for browsing and command-line discovery.
- **Validation in CI** to keep metadata, layout, and links healthy.

The initial collection is intentionally small. We will add third-party skills
only after checking the source license and preserving required attribution.

## Categories

| Category | Focus |
| --- | --- |
| [Coding](skills/coding/) | Review, debugging, refactoring, architecture |
| [Frontend](skills/frontend/) | React, accessibility, responsive UI |
| [Security](skills/security/) | Secure coding and dependency hygiene |
| [Productivity](skills/productivity/) | Planning and codebase exploration |

Browse the generated [SKILLS_INDEX.md](SKILLS_INDEX.md), or search locally:

```bash
python scripts/search-skills.py react
python scripts/search-skills.py --category frontend
python scripts/search-skills.py --tag debugging
```

## Repository structure

```text
skills/          Individual skills, one directory per skill
agents/          Reusable personas and orchestration workflows
instructions/    Shared repository and coding instructions
templates/       Templates for new skills and agents
sources/         Source, license, and attribution records
scripts/         Indexing, search, and validation tools
docs/            Usage and contribution documentation
.github/         Issue templates and GitHub Actions
AGENTS.md        Mandatory agent and contributor intake instructions
```

Every skill contains `SKILL.md` and `metadata.json`. Optional
`references/` and `examples/` directories hold supporting material.

## Use a skill

Skills follow the portable [Agent Skills](https://agentskills.io/) shape where
possible. Copy a skill directory into the convention used by your agent, or
point the agent at its `SKILL.md`. See [docs/installing-skills.md](docs/installing-skills.md)
for Claude Code, Codex, Cursor, Gemini CLI, and GitHub Copilot notes.

Compatibility is documented conservatively: a platform is listed only when
the skill format or workflow has been verified for that environment.

## Add a skill

1. Copy [templates/skill](templates/skill) to a category directory.
2. Write the instructions and complete `metadata.json`.
3. Add source and license evidence under `sources/` when the skill is adapted.
4. Run `python scripts/validate-skills.py`.
5. Regenerate indexes with `python scripts/build-index.py`.

See [docs/adding-skills.md](docs/adding-skills.md) and
[CONTRIBUTING.md](CONTRIBUTING.md).

External imports must also follow [the skill intake policy](docs/skill-intake-policy.md);
unverified skills remain source references rather than copied content.

## Licensing and attribution

Repository-authored skills are MIT licensed unless their directory states
otherwise. Third-party material remains under its original license and is not
copied here unless redistribution is permitted. Every adapted skill must
retain notices and identify its source repository, path, commit, and changes.
See [docs/source-attribution.md](docs/source-attribution.md).

## Status and limitations

This is an early, useful foundation rather than a claim that every listed
agent supports every skill. Indexes are generated from metadata, and external
source records are references until a skill is independently verified for
redistribution.
