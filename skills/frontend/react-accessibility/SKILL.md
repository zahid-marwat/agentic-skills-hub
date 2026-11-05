---
name: react-accessibility
description: Review React interfaces for semantic HTML, keyboard access, focus management, and accessible feedback.
---

# React accessibility

Review the rendered experience, not only JSX. Prefer native HTML semantics
before adding ARIA, and ensure every interaction works without a mouse.

## Checklist

- Use headings, landmarks, labels, buttons, and links for their native purpose.
- Provide keyboard operation, visible focus, and logical focus order.
- Associate labels and error/help text with form controls.
- Give meaningful alternative text and do not duplicate decorative content.
- Expose loading, success, and error state changes to assistive technology.
- Respect reduced motion and adequate color contrast.
- Test with a keyboard and the project's existing accessibility tooling.
