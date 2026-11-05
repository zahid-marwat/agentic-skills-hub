# Using the debugging-playbook skill

This document instructs agents, orchestrators, and subagents on how to delegate to or invoke the `debugging-playbook` skill across agent conversations.

## When to delegate to this skill

Delegate to this skill when:
- An automated test fails, a runtime crash occurs, or an unexpected exception is thrown during development.
- A user reports a bug, defect, or unexpected software behavior.
- An agent encounters an error while executing a task and needs root cause diagnosis rather than random trial-and-error patching.

Do **not** use this skill for:
- Routine feature requests where behavior is working as specified.
- Large-scale architectural rewrites or broad style refactoring.

## Required context to pass

The calling agent must provide:
1. **Symptom & error output**: Full exception traceback, command output, exit codes, and relevant logs.
2. **Reproduction command**: The exact command or script that reliably reproduces the failure.
3. **Target scope**: Relevant source code files and test suites.
4. **Environment context**: Operating system, runtime version, and active dependencies.

## Invocation methods

### Method 1: Subagent delegation (multi-agent workflow)

When launching a debugger subagent (via `invoke_subagent` or task runner):

```json
{
  "role": "Debugging Specialist",
  "prompt": "You are a software debugger following skills/coding/debugging-playbook/SKILL.md.\n\nSymptom:\n<insert error traceback or symptom>\nReproduction Command:\n<insert command>\nRelevant Files:\n<insert files>\n\nIsolate the failure to the smallest deterministic reproduction. Formulate hypotheses, verify the root cause, apply a minimal fix, and run the narrowest test suite to prove the fix. Avoid unrelated refactorings. Report root cause, code change, and verification evidence."
}
```

### Method 2: Conversation prompt injection

If activating within a single conversation:

```text
Activate the debugging-playbook skill (skills/coding/debugging-playbook/SKILL.md).
Investigate the failure below systematically: reproduce it deterministically, isolate the root cause, implement the minimal fix, add or update a regression test, and provide verification evidence.
```

## Expected output format

The debugging agent must return:
1. **Root Cause Analysis**: Why the failure occurred and what assumption was violated.
2. **Minimal Reproduction**: The specific test case, input, or command that reproduces the failure.
3. **Patch / Diff**: The targeted code change that fixes the bug without collateral edits.
4. **Verification Proof**: Execution logs of the test suite running and passing before and after the fix.
5. **Residual Risk**: Any edge cases or limitations remaining.

## Caller verification checklist

Before accepting the debug resolution, the calling agent must check:
- [ ] The fix is minimal and directly addresses the isolated root cause.
- [ ] No unrelated files, styles, or dependencies were altered.
- [ ] A regression test exists and passes.

