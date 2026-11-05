# Using the impeccable skill

This document instructs agents, orchestrators, and subagents on how to delegate to or invoke the `impeccable` skill across agent conversations.

## When to delegate to this skill

Delegate to this skill when:
- An existing frontend interface (web, mobile, or dashboard) needs visual critique, accessibility/heuristic auditing, or craft polish.
- An agent needs to make bland UI bolder, loud UI quieter, or improve visual hierarchy, typography, and motion.
- Designing a new product surface (`reference/new-work.md`) or extracting a design system (`DESIGN.md`).
- Multi-agent teams require a dedicated "Design Director" or "Finish Reviewer" before shipping frontend code.

Do **not** use this skill for:
- Backend services, databases, or CLI-only scripts.
- General non-visual code refactoring.

## Required context to pass

The calling agent must provide:
1. **Target component or page**: Source file path(s) (e.g. `src/components/PricingTable.tsx`).
2. **Action / Command verb**: One of `critique`, `audit`, `polish`, `bolder`, `quieter`, `harden`, `animate`, or `new-work`.
3. **Product context**: Existing `PRODUCT.md` or `DESIGN.md` if present; otherwise brief description of the product and its users.
4. **Surface mode**: `Persuade` (marketing/landing), `Operate` (dashboard/settings), `Read` (docs/articles), or `Experience` (portfolio/showcase).

## Invocation methods

### Method 1: Subagent delegation (multi-agent workflow)

When launching a design review or polish subagent (via `invoke_subagent`):

```json
{
  "role": "Design Director",
  "prompt": "You are a design director executing skills/frontend/impeccable/SKILL.md.\n\nTask: <insert command, e.g. 'critique and polish the pricing cards'>\nTarget files:\n<insert file paths>\nMode: Operate\n\nInstructions:\n1. Inspect the incumbent code and styling.\n2. Read skills/frontend/impeccable/reference/craft-floor.md before making any code modifications.\n3. Identify P0 (blocking) to P3 (polish) issues.\n4. Apply direct code refinements and return an actionable critique report."
}
```

### Method 2: Conversation prompt injection

If activating within a single conversation:

```text
Activate the impeccable skill (skills/frontend/impeccable/SKILL.md).
Execute `/impeccable <verb>` (e.g., critique, polish, audit) on <target-path>. Read reference/craft-floor.md before modifying any UI code, establish the surface mode, and provide ranked findings (P0-P3) with production-grade fixes.
```

## Available bundled subagent personas

The skill includes pre-defined agent personas in `agents/`:
- `impeccable-finish-reviewer.md`: Independent finish review in a clean context.
- `impeccable-asset-producer.md`: Generates SVGs, icons, and placeholder imagery.
- `impeccable-documenter.md`: Generates `DESIGN.md` and design tokens from existing code.
- `impeccable-manual-edit-applier.md`: Surgical edits to user-selected DOM nodes.

## Expected output format

The delegated agent must return:
1. **Critique / Audit Report**:
   - Heuristic score and surface mode.
   - Ranked findings from P0 (blocking issues: contrast, layout breaks) to P3 (polish).
2. **Code Changes**: Production-ready code updates respecting tokenization and the craft floor.
3. **Verification Summary**: Confirmation of checks run and remaining recommendations.

## Caller verification checklist

Before accepting the output, the calling agent must check:
- [ ] `reference/craft-floor.md` rules were respected (no purple-to-blue default gradients, no nested card slop).
- [ ] No arbitrary colors or unscaled font sizes were introduced.
- [ ] Accessibility contrast and keyboard focus states are preserved.

