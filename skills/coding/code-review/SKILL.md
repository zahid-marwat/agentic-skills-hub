---
name: code-review
description: Perform a structured, evidence-based code review focused on correctness, security, and maintainability.
---

# Code review

Review the requested change as a skeptical maintainer. Read the surrounding
code, tests, configuration, and documentation before forming conclusions.

## Workflow

1. Establish the intended behavior from the request and existing tests.
2. Trace changed code through its callers, data boundaries, and failure paths.
3. Prioritize exploitable security issues, correctness regressions, data loss,
   compatibility breaks, and missing tests.
4. Report only actionable findings with file paths, line numbers, impact,
   confidence, and a minimal fix direction.
5. State what was checked and any remaining uncertainty.

Do not report style preferences as defects. Do not claim a test passed unless
you ran it.

## Agent instructions

For delegating or invoking this skill from another agent or conversation, see [USE_INSTRUCTIONS.md](USE_INSTRUCTIONS.md).
