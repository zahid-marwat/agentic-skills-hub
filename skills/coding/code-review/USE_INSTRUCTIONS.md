# Using the code-review skill

This document instructs agents, orchestrators, and subagents on how to delegate to or invoke the `code-review` skill across agent conversations.

## When to delegate to this skill

Delegate to this skill when:
- A coding agent has prepared a diff, patch, or pull request and needs an independent, skeptical review before committing or merging.
- A user asks to review changes, audit a PR, or check code for correctness, security vulnerabilities, or maintainability.
- Multi-agent workflows require a "Reviewer" or "Quality Gate" step before moving to deployment or user handover.

Do **not** use this skill for:
- Writing original code from scratch.
- Pure automated linting or formatting checks (use automated linters/formatters instead).
- Speculative aesthetic or stylistic criticism without functional impact.

## Required context to pass

The calling agent must provide:
1. **Target diff or branch**: The explicit `git diff` output, commit range, or list of modified file paths.
2. **Intent / Goal**: The issue, bug ticket, or user story that the change is intended to satisfy.
3. **Environment & test results**: The status of test execution (e.g., which tests passed or failed, or whether tests were not run).
4. **Constraints**: Key project conventions, supported runtime versions, or external dependencies.

## Invocation methods

### Method 1: Subagent delegation (multi-agent workflow)

When using an agent framework or subagent invocation tool (such as `invoke_subagent`), launch a dedicated reviewer subagent:

```json
{
  "role": "Code Reviewer",
  "prompt": "You are a skeptical, evidence-based code review agent. Follow the instructions in skills/coding/code-review/SKILL.md.\n\nReview the following changes against the original user goal:\nGoal: <insert goal>\nDiff / Modified Files:\n<insert diff or file paths>\n\nFocus on: security vulnerabilities, data loss risks, behavioral regressions, edge cases, and missing tests. Format your report with file paths, line ranges, impact severity, and minimal recommended fixes."
}
```

### Method 2: Conversation prompt injection

If activating in a single conversation or handover between conversational turns:

```text
Activate the code-review skill (skills/coding/code-review/SKILL.md).
Review the following code changes as a skeptical maintainer. Trace callers, data boundaries, and failure paths. Report only actionable findings with file paths, line numbers, impact, and minimal fix directions. Do not report cosmetic stylistic preferences.
```

## Expected output format

The reviewing agent must return:
1. **Summary**: High-level verdict (`Approved`, `Approved with minor suggestions`, or `Changes requested`).
2. **Actionable Findings Table**:
   | Severity | Location | Issue | Impact | Recommended Fix |
   | --- | --- | --- | --- | --- |
   | High / Medium / Low | `path/to/file:line` | Concise description | Regression / Security / Data loss | Minimal direction |
3. **Verification Summary**: What was checked (callers, types, boundary conditions, tests run) and any remaining uncertainty.

## Caller verification checklist

Before accepting the review output, the calling agent must check:
- [ ] Every reported issue cites a specific file path and line number.
- [ ] No stylistic preferences are classified as functional defects.
- [ ] The reviewer explicitly stated whether test suites were executed or only analyzed statically.

