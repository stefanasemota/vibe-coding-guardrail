---
name: aos-check-for-security-issues
description: Defensive security audit sub-skill for the vibe-coder protocol. Use before committing or opening a pull request (or in scheduled advisory runs) to scan for hardcoded secrets, API tokens, service account keys, unvalidated inputs, insecure security rules, and vulnerable dependencies.
---

# `aos-check-for-security-issues` — Defensive Security Audit

## Purpose
Prevents credential leaks, injection vectors, privilege escalations, and client-bundle exposure from entering version control. Supports interactive review and unattended `advisory` scheduled sweeps.

---

## Security Audit Checklist

1. **Secrets & Credential Hygiene:**
   * Scan staged and untracked files for hardcoded API keys, tokens, `.pem` certificates, or service account files (`*service-account*.json`, `*key*.json`).
   * Confirm `.gitignore` excludes `.env*`, `.firebase/`, `.genkit/*`, and key files.
   * Ensure test configurations inject dummy keys (`mock-key-for-testing`) rather than real credentials.

2. **Server/Client Boundary & Input Sanitization:**
   * Verify server-only modules (admin SDKs, repositories, AI flows) never leak credentials or backend SDKs into client bundles.
   * Validate all external inputs, AI outputs, and user mutations against strict schemas before persisting to storage or executing shell commands.

3. **Database & BaaS Security Rules (when present, e.g. `firestore.rules`):**
   * Verify every collection enforces authentication (`request.auth != null`).
   * Enforce strict ownership checks on user documents (`request.auth.uid == resource.data.ownerId` on read/write and `request.resource.data.ownerId == request.auth.uid` on create).
   * Restrict shared catalog writes to verified admin roles.

4. **Dependency & Hook Governance Audit:**

5. **Session Termination:**
     `Guardrail: aos Vibe Coding Guardrail v<version> | Skill: aos-check-for-security-issues | Tokens: <exact count if exposed by runtime, otherwise "N/A (not exposed by runtime)">`
