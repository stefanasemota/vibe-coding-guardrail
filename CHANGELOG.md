# Changelog (`CHANGELOG.md`)

All notable changes to **Vibe Coding Guardrail** are documented in this file. Date format: `DD.MM.YYYY`.

---

## [1.1.0] - 01.11.2026

### Added
- **Unattended Scheduled Automation Profile (`profile-automation.md`):**
  - Added `.agent/skills/vibe-coder/profiles/profile-automation.md` (`gate_behavior: "advisory"`, report-only mode) for unattended background execution in the Antigravity Automations tab.
- **Weekly Wednesday Guardrail Automations:**
  - Documented `/schedule` recipes in `README.md` and `dev.md` for running **Weekly Architecture Drift Audit (`aos-audit-project`)** and **Weekly Security & Secret Sweep (`aos-check-for-security-issues`)** every Wednesday (`09:00` and `09:30`).
- **Custom AI Model Profile Creation Guide:**
  - Added end-to-end examples in `README.md` and `.agent/skills/README.md` showing how to scaffold custom profiles for specific AI models (e.g., `claude-sonnet`, `gemini-flash`) via `aos-create-profile` and invoke sessions with `$PROFILE=<name>`.
- **Live Global Skill Symlinks (`ln -sfn`):**
  - Updated global skill setup to use direct symbolic links and relative profile paths (`../vibe-coder/profiles/profile-antigravity.md`) so updates in this repository are immediately active across all projects.

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
