---
name: aos-check-for-security-issues
description: Defensive security audit sub-skill for the vibe-coder protocol. Use before committing or opening a pull request to scan for hardcoded secrets, API tokens, service account keys, unvalidated inputs, insecure security rules, and vulnerable dependencies.
---

# `aos-check-for-security-issues` — Engine-Neutral Defensive Security Audit Sub-Skill

## Purpose
Prevents credential leaks, injection vectors, privilege escalations, and client-bundle exposure from entering version control during rapid vibe-coding sessions.

## Active Profile Consumption
Reads `review_depth` and `gate_behavior` from [`../vibe-coder/profiles/profile-antigravity.md`](../vibe-coder/profiles/profile-antigravity.md) (or `.agent/skills/vibe-coder/profiles/profile-antigravity.md` / active `$PROFILE`) to execute an engine-neutral security pass prior to commit.

---

## Security Audit Checklist

1. **Secrets & Credential Hygiene:**
   * Scan staged and untracked files for hardcoded API keys, tokens, `.pem` certificates, or service account files (`*service-account*.json`, `*key*.json`).
   * Confirm `.gitignore` excludes `.env*`, `.firebase/`, `.genkit/*`, and key files.
   * Ensure test configurations inject dummy keys (`mock-key-for-testing`) rather than real credentials.

2. **Server/Client Boundary & Input Sanitization:**
   * Verify server-only modules (admin SDKs, repositories, AI flows) import `server-only` or reside strictly in server actions/repositories so credentials and heavy SDKs never leak into client bundles.
   * Validate all external inputs, AI outputs, and user mutations against strict schemas (e.g., `zod`) before persisting to the database.

3. **Database & BaaS Security Rules (e.g., `firestore.rules`):**
   * Verify every collection enforces authentication (`request.auth != null`).
   * Enforce strict ownership checks on user documents (`request.auth.uid == resource.data.ownerId` on read/write and `request.resource.data.ownerId == request.auth.uid` on create).
   * Restrict shared catalog writes to verified admin roles.

4. **Dependency & CI Governance Audit:**
   * Enforce the **Dependency Lockdown Rule** (`AGENTS.md`): never install new packages without explicit human approval, and audit `package.json` for known CVEs (`npm audit`).
   * Ensure pre-commit hooks and CI governance checks are never bypassed (`--no-verify` is prohibited).
