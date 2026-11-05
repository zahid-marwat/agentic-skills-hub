---
name: debugging-playbook
description: Diagnose software failures systematically from symptoms to a verified minimal fix.
---

# Debugging playbook

Treat a failure as evidence, not a guess. Reproduce it, isolate the smallest
failing boundary, and verify the fix against the original symptom.

## Workflow

1. Capture the exact command, inputs, environment, and complete error.
2. Reproduce with the smallest deterministic case.
3. Form a short list of hypotheses and test the highest-signal one first.
4. Inspect the failing path and its assumptions; avoid unrelated refactors.
5. Add or update a regression test, then run the narrowest relevant suite.
6. Report the root cause, change, verification, and remaining limitations.

## Agent instructions

For delegating or invoking this skill from another agent or conversation, see [USE_INSTRUCTIONS.md](USE_INSTRUCTIONS.md).
