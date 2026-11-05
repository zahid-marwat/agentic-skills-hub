# Contributing

1. Read [AGENTS.md](AGENTS.md) and
   [the intake policy](docs/skill-intake-policy.md).
2. Keep one skill per directory under `skills/<category>/<name>/`.
3. Use lowercase kebab-case names.
4. Include `SKILL.md`, complete `metadata.json`, attribution, and license
   evidence.
5. Do not copy third-party content until origin, quality, security, and
   redistribution rights are verified.
6. Run validation and index generation before opening a pull request.

```bash
python scripts/validate-skills.py
python scripts/build-index.py
```

Keep pull requests focused and explain whether content is original, adapted,
or an external reference only. Include the required intake checklist results
for every imported skill.
