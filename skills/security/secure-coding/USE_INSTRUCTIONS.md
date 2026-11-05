# Using the secure-coding skill

This document instructs agents, orchestrators, and subagents on how to delegate to or invoke the `secure-coding` skill across agent conversations.

## When to delegate to this skill

Delegate to this skill when:
- Authoring or modifying security-critical code paths: authentication, session handling, password hashing, and token verification.
- Writing queries, dynamic SQL, ORM operations, or data layer interactions.
- Implementing file uploads, file reading, URL fetching, proxying, or external webhooks (SSRF risks).
- Introducing new third-party dependencies or external API integrations.
- Performing a pre-merge security audit of any user-facing endpoint or change touching credentials/secrets.

Do **not** use this skill for:
- Routine CSS or visual styling adjustments with no user input or data handling.

## Required context to pass

The calling agent must provide:
1. **Target code / diff**: Files modified or being authored.
2. **Trust boundary**: Source of the input (e.g. public HTTP request, authenticated user, admin, internal service).
3. **Data sensitivity**: Whether PII, credentials, payment data, or health records are handled.
4. **Target stack**: Programming language, framework, database driver, and deployment environment.

## Invocation methods

### Method 1: Subagent delegation (multi-agent workflow)

When launching a security specialist subagent (via `invoke_subagent`):

```json
{
  "role": "Security Specialist",
  "prompt": "You are an application security specialist following skills/security/secure-coding/SKILL.md.\n\nTarget files:\n<insert files>\nTrust boundary:\n<insert details, e.g. public API endpoint receiving user JSON>\n\nAudit and harden the code against OWASP Top 10 risks:\n1. Input validation & parameterized queries (prevent SQL/NoSQL/command injection).\n2. Authentication & object-level authorization (prevent IDOR/BOLA).\n3. Secret & credential management (no hardcoded tokens/keys).\n4. Safe file and URL handling (prevent path traversal and SSRF).\n5. Context-aware output encoding (prevent XSS).\n\nDeliver an audit report and hardened code."
}
```

### Method 2: Conversation prompt injection

If activating within a single conversation:

```text
Activate the secure-coding skill (skills/security/secure-coding/SKILL.md).
Audit the following code against security trust boundaries. Treat all external input as untrusted. Verify authorization, input validation, secret hygiene, and query parameterization. Deliver specific code remedies for every finding.
```

## Expected output format

The delegated security agent must return:
1. **Security Vulnerability Assessment**:
   | Category | Severity | File & Line | Threat Description | Remediation |
   | --- | --- | --- | --- | --- |
   | Injection / Auth / SSRF / Secrets | Critical / High / Med | `file:line` | Exploit scenario | Hardened code snippet |
2. **Hardened Code / Diff**: Secure implementation enforcing parameterization and validation.
3. **Negative / Security Test Case**: Test script demonstrating that malicious input is rejected.

## Caller verification checklist

Before accepting the output, the calling agent must check:
- [ ] Queries use parameterization / prepared statements, never raw string interpolation.
- [ ] Authorization checks are performed on every endpoint prior to data access.
- [ ] No secrets, keys, or passwords appear in source code or sample test fixtures.
- [ ] Error messages do not leak internal stack traces or database structures.

