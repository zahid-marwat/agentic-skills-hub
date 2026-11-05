# Adding skills

Copy the template:

```text
templates/skill/ -> skills/<category>/<skill-name>/
```

Write focused instructions, complete metadata, and include source notices for
adapted content. Then run:

```bash
python scripts/validate-skills.py
python scripts/build-index.py
```
