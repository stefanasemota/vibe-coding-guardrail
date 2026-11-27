# Changelog (`CHANGELOG.md`)

All notable changes to **Vibe Coding Guardrail** are documented in this file. Date format: `DD.MM.YYYY`.

---

## [2.0.0] - 27.11.2026

### Changed
- **Antigravity-Native Python Refactor (Zero External Dependencies):**
  - Removed Node.js runtime dependency (`package.json`, `.nvmrc`, `bin/init-guardrail.mjs`, `bin/aos-create-profile.mjs`, `tests/guardrail.test.mjs`) and multi-vendor abstractions (`ai-rules.json`, Engine Profile schemas).
  - Relocated canonical skills from `.agent/skills/` to `skills/` (all 6 skills preserved) and templates to `references/scaffolding-templates.md`.
  - Compressed `skills/vibe-coder/SKILL.md` from a 7-Phase, 3-gate loop into a 3-Stage Loop with a single configurable gate (`pause` vs `advisory`).
  - Moved remote `git fetch --prune` and obsolete merged branch cleanup strictly into `skills/aos-vibecode-update/SKILL.md`.

### Added
- **Deterministic Antigravity Lifecycle Hooks (`hooks.json` + `hooks/*.py`):**
  - `hooks/session_start.py` (`SessionStart`): 100% local, read-only branch check (never runs `git fetch` or mutates `.git/`).
  - `hooks/branch_guard.py` (`PreToolUse`): Deterministically blocks `git commit`/`git push` on `main`/`master` and `--no-verify` bypasses.
  - `hooks/adr_check.py` (`Stop`): Validates reverse-chronological `[DD.MM.YYYY]` ADR headings and required fields (`Origin`, `Context`, `Decision`, `Impact`) when `decision.md` is modified.
- **Single Source of Truth Python Test Suite (`tests/test_guardrail.py`):**
  - Zero-dependency `unittest` suite asserting zero skill-count/name drift across `skills/*/SKILL.md`, `plugin.json`, `README.md`, and `Architecture.md`, plus unit tests for all hooks and `decision.md`.

## [1.3.1] - 19.11.2026

### Changed
- **Skill Evaluation Hardening (`vibe-coder` & `aos-vibecode`):**
  - Extracted conditional README badge, `package.json`, and ADR templates into `.agent/skills/vibe-coder/references/scaffolding-templates.md`.
  - Moved the 7-Phase FDD workflow to the top of `vibe-coder/SKILL.md`, deduplicated `AGENTS.md` execution rules, tightened descriptions, and added `Gotchas`.
  - Scoped Next.js/Firebase rules conditionally in `aos-vibecode/SKILL.md` and added a per-patch verification gate.

## [1.3.0] - 15.11.2026

### Added
- **Session-Start Obsolete Branch Cleanup (`vibe-coder` & `AGENTS.md`):**
  - Enforced pruning stale refs (`git fetch --prune`), auto-deleting obsolete local merged branches, and prompting before deleting merged `origin/*` branches at session start.
- **Session Termination Telemetry (`vibe-coder` & all `aos-*` sub-skills):**
  - Standardized Session Termination footer displaying the active Guardrail version (`plugin.json`/`package.json`), skill name, and runtime token usage.

### Changed
- **Documentation Restructure (`Architecture.md`, `README.md`, `dev.md`):**
  - Extracted system diagram, skill/profile table, required metadata, and reference benchmarks into `Architecture.md`.
  - Added **Updating the Global Plugin & Verifying Your Version** to `README.md`.
  - Consolidated custom AI model profiles (`aos-create-profile`) and standard `package.json` scripts into `dev.md` with zero AI slop.

## [1.2.1] - 01.11.2026

### Added
- **Automatic Draft PR Workflow in `aos-audit-project` (Step 5):**
  - Added explicit **Step 5: Branch, Commit, Push & Open Draft PR** to `aos-audit-project/SKILL.md` so every standalone audit run automatically creates an isolated branch (`chore/aos-project-audit` if on `main`/`master`/`development`), runs tests, commits with a Conventional Commit, pushes to `origin`, and opens a Draft PR (`gh pr create --draft`).

## [1.2.0] - 01.11.2026

### Added
- **Antigravity Plugin Bundle (`plugin.json`):**
  - Packaged the repository as a self-contained, language-agnostic Antigravity Plugin (`plugin.json`, `rules/AGENTS.md`, `assets/logo.svg`, `skills/`) that enables all 5 skills and `AGENTS.md` rules across any workspace as a single toggleable unit.
- **Stack-Aware `package.json` & Legacy Date Migration:**
  - Updated `vibe-coder/SKILL.md` and `aos-audit-project/SKILL.md` to detect project stack first (enforcing `package.json` schema and optional `vibe-coding-guardrail` devDependency only in Node.js/TS repos, while using native toolchains in Python/Go/Rust/Swift/Android repos).
  - Added legacy date/order migration check in `aos-audit-project/SKILL.md` to flag and convert existing `[YYYY-MM-DD]` / `[MM.DD.YYYY]` dates or oldest-first ordering in `decision.md` and `aos-audit.md`.

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
