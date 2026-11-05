# Using the ui-ux-pro-max skill

This document instructs agents, orchestrators, and subagents on how to delegate to or invoke the `ui-ux-pro-max` skill across agent conversations.

## When to delegate to this skill

Delegate to this skill when:
- Designing a new web, mobile, or desktop interface and needing vetted UI styles (80 styles), color palettes (192 palettes), or font pairings (74 pairings).
- Implementing UI for a specific framework or stack (22 supported stacks, including React, Next.js, Vue, Svelte, Tailwind, Flutter, React Native, Swift).
- Reviewing UI components against 119 canonical UX guidelines (accessibility, touch targets, layout shifts, form feedback).
- Searching for charts, motion presets (GSAP), or curated icons.

Do **not** use this skill for:
- Non-visual backend logic, databases, or cloud infrastructure.

## Required context to pass

The calling agent must provide:
1. **Product type / domain**: (e.g. Fintech, SaaS, Developer Tools, Health, E-commerce).
2. **Technology stack**: (e.g. `react`, `tailwind`, `nextjs`, `flutter`).
3. **Specific design decision needed**: Style selection, color palette, typography pairing, component UX, or chart type.
4. **Target files**: Components or stylesheets to generate or update.

## Invocation methods

### Method 1: Subagent delegation (multi-agent workflow)

When launching a UI design subagent (via `invoke_subagent`):

```json
{
  "role": "UI/UX Intelligence Specialist",
  "prompt": "You are a UI/UX specialist following skills/frontend/ui-ux-pro-max/SKILL.md.\n\nProduct: <insert domain, e.g. SaaS Analytics Dashboard>\nStack: <insert stack, e.g. React + Tailwind CSS>\nTarget task: Select style, color palette, and font pairing, then construct the component layout.\n\nInstructions:\n1. Query the search tool: `python skills/frontend/ui-ux-pro-max/scripts/search.py '<keyword>' --domain <domain>`\n2. Follow the 10-tier priority order in SKILL.md (Accessibility first, then touch targets, performance, style, layout).\n3. Consult references/quick-reference.md for UX guidelines.\n4. Deliver the completed design specifications and component code."
}
```

### Method 2: Conversation prompt injection

If activating within a single conversation:

```text
Activate the ui-ux-pro-max skill (skills/frontend/ui-ux-pro-max/SKILL.md).
Query the local catalogs for <domain/topic> using `python skills/frontend/ui-ux-pro-max/scripts/search.py`. Apply the vetted style profile, typography pairings, color tokens, and pre-delivery UX checklist to <target-file>.
```

## Available catalog CLI tool

The skill includes a fast, zero-dependency Python search script:

```bash
# Search across all catalogs
python skills/frontend/ui-ux-pro-max/scripts/search.py "fintech"

# Target a specific domain: style, color, typography, ux, chart, motion, stack
python skills/frontend/ui-ux-pro-max/scripts/search.py "dashboard" --domain style
python skills/frontend/ui-ux-pro-max/scripts/search.py "healthcare" --domain color
python skills/frontend/ui-ux-pro-max/scripts/search.py "modern" --domain typography
python skills/frontend/ui-ux-pro-max/scripts/search.py "react" --domain stack
```

## Expected output format

The delegated agent must return:
1. **Selected Design System Profile**:
   - Style Name & Archetype (e.g., Clean SaaS, Bento Grid, Modern Minimal).
   - Color Palette tokens (Primary, Secondary, Background, Accent, Surface).
   - Typography Pairing (Heading font + Body font with fallback stack).
2. **Implemented UI Component**: Framework code incorporating semantic classes and responsive layout.
3. **UX Checklist Validation**: Confirmation of touch target sizes (>= 44x44px), contrast ratios (>= 4.5:1), and zero layout shifts.

## Caller verification checklist

Before accepting the output, the calling agent must check:
- [ ] Color tokens have passed contrast checks against background surfaces.
- [ ] Mobile-first responsiveness and breakpoints are implemented.
- [ ] Pre-delivery checklist from `references/pro-rules.md` is satisfied.

