---
name: secure-coding
description: Apply a practical secure-coding checklist to changes involving input, auth, secrets, data, and dependencies.
---

# Secure coding

Review trust boundaries first. Treat all external input, credentials, tokens,
files, URLs, and serialized data as untrusted until explicitly validated.

## Checklist

- Use parameterized queries and context-appropriate output encoding.
- Validate type, size, format, and authorization at the server boundary.
- Store secrets in a managed secret store or environment, never source control.
- Enforce authentication and object-level authorization on every protected path.
- Use safe file and URL handling; prevent traversal, SSRF, and unsafe redirects.
- Pin and audit dependencies using the repository's standard tooling.
- Avoid leaking secrets or sensitive data in logs and error responses.
- Add regression tests for any security-sensitive fix and document residual risk.

## Agent instructions

For delegating or invoking this skill from another agent or conversation, see [USE_INSTRUCTIONS.md](USE_INSTRUCTIONS.md).
