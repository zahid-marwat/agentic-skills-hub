# Using the replace-with-kebab-case-name skill

This document instructs agents, orchestrators, and subagents on how to delegate to or invoke this skill across agent conversations.

## When to delegate to this skill

Delegate to this skill when:
- [Describe specific scenarios, triggers, and conditions where this skill should be used]

Do **not** use this skill for:
- [Describe out-of-scope tasks or anti-patterns]

## Required context to pass

The calling agent must provide:
1. **Target files / scope**: [e.g. source files, diffs, or output paths]
2. **Intent / Goal**: [e.g. user requirements or acceptance criteria]
3. **Environment constraints**: [e.g. runtime, stack, or configurations]

## Invocation methods

### Method 1: Subagent delegation (multi-agent workflow)

When launching a subagent:

```json
{
  "role": "<Subagent Role Name>",
  "prompt": "You are a specialist following <path-to-skill>/SKILL.md.\n\nTask details:\n<insert context and task instructions>\n\nFollow all workflow rules and return the expected deliverables."
}
```

### Method 2: Conversation prompt injection

If activating within a single conversation:

```text
Activate the <skill-name> skill (<path-to-skill>/SKILL.md).
Execute the workflow described in SKILL.md for the following task: <insert task>.
```

## Expected output format

The delegated agent must return:
1. **Deliverables**: [e.g. code artifacts, reports, or test results]
2. **Verification Summary**: [e.g. evidence of checks performed]

## Caller verification checklist

Before accepting the output, the calling agent must check:
- [ ] [Verification criterion 1]
- [ ] [Verification criterion 2]

