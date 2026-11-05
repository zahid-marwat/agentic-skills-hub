# Using the react-accessibility skill

This document instructs agents, orchestrators, and subagents on how to delegate to or invoke the `react-accessibility` skill across agent conversations.

## When to delegate to this skill

Delegate to this skill when:
- Creating or modifying interactive React components (modals, dropdowns, forms, drawers, tabs, accordion widgets).
- Auditing a React web application for accessibility (WCAG 2.1 AA compliance).
- Ensuring keyboard-only navigation, focus trapping, focus restoration, and screen-reader announcements work correctly.

Do **not** use this skill for:
- Non-React/non-DOM environments (unless reviewing general web semantic HTML).
- Pure backend or API code.

## Required context to pass

The calling agent must provide:
1. **Target component paths**: Source file(s) (e.g., `src/components/Modal.tsx`, `src/components/Form.tsx`).
2. **Interaction context**: How users open, interact with, and dismiss the component.
3. **Existing dependencies**: Whether the project uses component primitives with built-in accessibility (such as Radix UI, Headless UI, React Aria, or custom implementations).

## Invocation methods

### Method 1: Subagent delegation (multi-agent workflow)

When launching an accessibility review subagent (via `invoke_subagent`):

```json
{
  "role": "Accessibility Specialist",
  "prompt": "You are an accessibility specialist following skills/frontend/react-accessibility/SKILL.md.\n\nTarget components:\n<insert component paths>\n\nReview the rendered experience for:\n1. Semantic HTML elements (prefer native <button>, <a>, <dialog> over div with role).\n2. Keyboard navigation and visible focus rings.\n3. Form label associations (htmlFor / aria-labelledby / aria-describedby for errors).\n4. Focus management (focus trapping in modals, focus return on close).\n5. ARIA live regions for async notifications.\n\nProvide an audit report and minimal remediations."
}
```

### Method 2: Conversation prompt injection

If activating within a single conversation:

```text
Activate the react-accessibility skill (skills/frontend/react-accessibility/SKILL.md).
Audit the React components below for accessibility and keyboard navigation. Prioritize native HTML semantics over ARIA attributes. Deliver actionable fixes for focus management, contrast, and label associations.
```

## Expected output format

The reviewing agent must return:
1. **Accessibility Audit Table**:
   | Criteria | Status | Element / Line | Issue & Impact | Remediated JSX |
   | --- | --- | --- | --- | --- |
   | Keyboard / Focus / Semantic / ARIA | Pass / Fail | `Component.tsx:line` | Description | Fixed snippet |
2. **Focus Flow Diagram / Description**: Description of where focus enters, moves, and returns.
3. **Refactored Code / Diff**: Production-ready updates to components.

## Caller verification checklist

Before accepting the output, the calling agent must check:
- [ ] Native interactive elements (`<button>`, `<a>`, `<input>`) are used instead of clickable `<div>` elements.
- [ ] Every form control has a linked `<label>` or `aria-label`.
- [ ] Focus is not lost when modal/overlay components close.

