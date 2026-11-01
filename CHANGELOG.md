# Changelog (`CHANGELOG.md`)

All notable changes to **Vibe Coding Guardrail** are documented in this file. Date format: `DD.MM.YYYY`.

---

## [1.0.0] - 01.11.2026

### Added
- **Engine-Neutral 7-Phase FDD Orchestrator (`vibe-coder`):**
  - 7-Phase Feature-Driven Development (FDD) loop with explicit human checkpoints at Phase 3 (Spec Freeze), Phase 4 (Architecture Matrix), and Phase 6 (Quality & Security Review).
  - Interchangeable Engine Profile architecture (`.agent/skills/vibe-coder/profiles/_schema.md` and default `.agent/skills/vibe-coder/profiles/profile-antigravity.md`).
- **Coordinated Sub-Skill Suite (`.agent/skills/`):**
  - `aos-audit-project`: Audits repositories against Architectural Summary expectations and generates `aos-audit.md`.
  - `aos-vibecode`: Translates `initiative.md` and `docs/feature/<name>/plan.md` into surgical micro-patches (`<= 50` lines).
  - `aos-verify`: Runs project-native linters, builds, unit tests, and 3-point static reviews (Simplicity/DRY, Functional Correctness, Conventions).
  - `aos-check-for-security-issues`: Audits secrets, `.gitignore` rules, server/client boundaries, schema validation, and dependencies.
- **Strict AI Workflow & Git Rules (`AGENTS.md` & `ai-rules.json`):**
  - Enforces *Never work on main*, *Test on the branch*, *Push, do not merge*, *Verify before writing*, *Look Before You Leap*, *Dependency Lockdown*, *Fix your own bugs*, *Commit atomicity*, *Documentation Sync*, *Explain the Fix*, *Zero AI Slop*, and *Conventional Commits*.
- **CLI Utilities (`bin/`):**
  - `init-guardrail` (`bin/init-guardrail.mjs`): Copies `.agent/skills/`, `AGENTS.md`, and `ai-rules.json` into any target project directory.
  - `aos-create-profile` (`bin/aos-create-profile.mjs`): Scaffolds custom engine profiles adhering to `_schema.md`.
- **Standardized Scaffolding & Automated Test Suite:**
  - Core docs (`README.md`, `initiative.md`, `dev.md`, `decision.md` ordered newest-to-oldest with `[DD.MM.YYYY]` dates, `aos-audit.md`) and `tests/guardrail.test.mjs` (`8/8` checks passing).
