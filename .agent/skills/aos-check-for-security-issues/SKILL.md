---
name: aos-check-for-security-issues
description: Defensive security audit sub-skill for the vibe-coder protocol. Use before committing or opening a pull request to scan for hardcoded secrets, API tokens, service account keys, unvalidated inputs, insecure security rules, and vulnerable dependencies.
---

# `aos-check-for-security-issues` — Defensive Security Audit Sub-Skill

## Purpose
Prevents credential leaks, injection vectors, privilege escalations, and client-bundle exposure from entering version control during rapid vibe-coding sessions.

## Security Audit Checklist

1. **Secrets & Credential Hygiene:**
   * Scan staged and untracked files for hardcoded API keys, tokens, `.pem` certificates, or service account files (`*service-account*.json`, `*key*.json`).
   * Confirm `.gitignore` excludes `.env*`, `.firebase/`, `.genkit/*`, and key files.
   * Ensure test configurations (`vitest.config.mts`) inject dummy keys (`mock-key-for-testing`) rather than real credentials.

2. **Server/Client Boundary & Input Validation:**
   * Verify server-only modules (`firebase-admin`, repositories, Genkit flows) import `server-only` or reside strictly in server actions/repositories so credentials and heavy SDKs never leak into client bundles.
   * Validate all LLM outputs and user mutations against strict `zod` schemas before persisting to the database.

3. **Firestore & BaaS Security Rules (`firestore.rules`):**
   * Verify every collection enforces authentication (`request.auth != null`).
   * Enforce strict ownership checks on user documents (e.g., `request.auth.uid == resource.data.ownerId` on read/write and `request.resource.data.ownerId == request.auth.uid` on create).
   * Restrict shared catalog writes to verified admin roles (`exists(/databases/$(database)/documents/roles_admin/$(request.auth.uid))`).
   * Delegate any modifications to `firestore.rules` to the `firestore-rules-author` subagent and audit with `firebase-security-rules-auditor`.

4. **Dependency & CI Governance Audit:**
   * Audit new dependencies in `package.json` for necessity, license compatibility, and known CVEs (`npm audit`).
   * Ensure pre-commit hooks (`.husky/pre-commit`, `.husky/commit-msg`) and CI governance checks (`standard-check.yml`) are never bypassed (`--no-verify` is prohibited).
