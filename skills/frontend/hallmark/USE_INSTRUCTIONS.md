# Using the hallmark skill

This document instructs agents, orchestrators, and subagents on how to delegate to or invoke the `hallmark` skill across agent conversations.

## When to delegate to this skill

Delegate to this skill when:
- Creating a new web page, landing page, application interface, or promotional site that must avoid generic AI defaults (e.g. purple-to-blue gradients, icon tiles above headings, cards inside cards).
- Performing a visual redesign of an existing surface (`/hallmark redesign <path>`).
- Auditing UI against strict craft and anti-slop design floors (`/hallmark audit <path>`).

Do **not** use this skill for:
- Backend-only code, database schemas, or CLI scripts.
- Minor bug fixes on established design systems where introducing a new visual genre or theme would break brand consistency.

## Required context to pass

The calling agent must provide:
1. **Product brief**: What the page does, audience, domain, and primary user action.
2. **Target files**: Output file path(s) (e.g., `src/pages/Home.tsx` or `index.html`).
3. **Theme preference**: Selected theme from `references/themes/` (or request dealing 3 candidate themes).
4. **Scope**: Page, component, or full site.

## Invocation methods

### Method 1: Subagent delegation (multi-agent workflow)

When launching a frontend design subagent (via `invoke_subagent`):

```json
{
  "role": "Frontend Designer",
  "prompt": "You are a senior UI designer executing skills/frontend/hallmark/SKILL.md.\n\nBrief:\n- Audience: <insert audience>\n- Goal: <insert page goal>\n- Target path: <insert output path>\n\nStrictly enforce 'The Floor' (the 16 non-waivable craft rules in SKILL.md). Ensure all colors and fonts pass through :root tokens. After generating the page, run:\n`node skills/frontend/hallmark/scripts/sloplint.mjs <output-path> --render`\nFix every FAIL condition before returning."
}
```

### Method 2: Conversation prompt injection

If activating within a single conversation:

```text
Activate the hallmark skill (skills/frontend/hallmark/SKILL.md).
Design the requested interface following Hallmark's 16 non-waivable floor rules. Use CSS tokens for all colors and typography, ensure keyboard focus-visible and reduced-motion states, avoid generic AI slop patterns, and run `node skills/frontend/hallmark/scripts/sloplint.mjs` against the result.
```

## Available mechanical verification

Hallmark bundles a zero-dependency mechanical gate linter:

```bash
node skills/frontend/hallmark/scripts/sloplint.mjs <target-file-or-dir>
```

Flags:
- `--stage hero`: Check hero constraints (measure, visibility, copy length).
- `--stage page`: Check full-page gates (contrast, landmarks, token usage).
- `--json`: Output machine-readable JSON for automated agent parsing.

## Expected output format

The delegated agent must return:
1. **Designed Artifact**: Complete HTML/CSS, React, or framework component.
2. **Theme & Tokens**: Clear token declarations at `:root` (fonts, colors, spacing).
3. **Linter Report**: Output of `sloplint.mjs` confirming zero `FAIL` statuses.

## Caller verification checklist

Before accepting the output, the calling agent must check:
- [ ] No literal colors (hex, rgb) exist outside the `:root` or theme token block.
- [ ] No `transition: all` is used.
- [ ] Interactive controls include explicit `:focus-visible` styling.
- [ ] `node skills/frontend/hallmark/scripts/sloplint.mjs` runs with exit code 0.

