# 📋 Architectural & Implementation Decision Log (`decision.md`)

Reverse-chronological ledger (newest at top, oldest at bottom) of all architectural, UX, and implementation choices governed by the `vibe-coder` protocol. Date format: `[DD.MM.YYYY]`.

---

### [01.11.2026] - Add `profile-automation.md`, Weekly Wednesday Automations & Release `v1.1.0`
- **Origin:** Human Request | Agent Proposal
- **Context:** Unattended scheduled runs in the Antigravity Automations tab require a profile that does not pause waiting for interactive human confirmation (`gate_behavior: "advisory"`), along with clear recipes for weekly Wednesday audits (`aos-audit-project` & `aos-check-for-security-issues`) and creating custom profiles for specific AI models.
- **Decision:** Created `.agent/skills/vibe-coder/profiles/profile-automation.md`, documented Weekly Wednesday Automations and custom AI model profile creation in `README.md`, `.agent/skills/README.md`, and `dev.md`, bumped version to `1.1.0` (`package.json`, `README.md`, `CHANGELOG.md`), and expanded `tests/guardrail.test.mjs`.
- **Impact:** `.agent/skills/vibe-coder/profiles/profile-automation.md`, `README.md`, `.agent/skills/README.md`, `dev.md`, `package.json`, `CHANGELOG.md`, `decision.md`, `aos-audit.md`, `tests/guardrail.test.mjs`.

### [01.11.2026] - Symlink Global Skills for Live Cross-Project Updates
- **Origin:** Human Request
- **Context:** Static copies (`cp -R`) in `~/.gemini/antigravity/skills/` and `~/.gemini/config/skills/` required manual re-copying after skill updates and did not resolve `../vibe-coder/profiles/profile-antigravity.md` relative to global skill directories when used in external repositories without a local `.agent/skills/` copy.
- **Decision:** Replaced static copies in `~/.gemini/antigravity/skills/` and `~/.gemini/config/skills/` with direct symlinks (`ln -sfn`) to `.agent/skills/*`, updated `README.md` and `dev.md` global installation instructions to use symlinks, and updated all `aos-*` sub-skills to resolve `../vibe-coder/profiles/profile-antigravity.md` relative to the skill directory.
- **Impact:** `README.md`, `dev.md`, `.agent/skills/*/SKILL.md`, `decision.md`.

### [01.11.2026] - Prepare `v1.0.0` Release & `CHANGELOG.md`
- **Origin:** Human Request
- **Context:** With the 7-Phase FDD Orchestrator, Engine Profile architecture, 4 `aos-*` sub-skills, CLI utilities, and strict AI workflow rules complete and verified, the project is ready for its first tagged release (`v1.0.0`).
- **Decision:** Created `CHANGELOG.md` (`[1.0.0] - 01.11.2026`), added `CHANGELOG.md` verification to `tests/guardrail.test.mjs`, and prepared annotated tag `v1.0.0` and GitHub Release.
- **Impact:** `CHANGELOG.md`, `decision.md`, `aos-audit.md`, `docs/feature/release-v1.0.0/plan.md`, `tests/guardrail.test.mjs`.

### [01.11.2026] - Decouple Engine-Neutral 7-Phase FDD Workflow Chassis from Engine Profiles
- **Origin:** Human Request | Agent Proposal
- **Context:** The `.agent/skills/` suite needed to separate engine-neutral workflow orchestration (7-phase FDD loop, checkpoint gates, Git isolation, `decision.md`) from model-specific engine parameters (`max_patch_size`, `patch_strategy`, `type_safety`, `review_depth`, `gate_behavior`).
- **Decision:** Created `.agent/skills/vibe-coder/profiles/_schema.md` and default production profile `.agent/skills/vibe-coder/profiles/profile-antigravity.md`, refactored `vibe-coder/SKILL.md` and all 4 `aos-*` sub-skills to consume profile parameters dynamically without hardcoded model dependencies, added `aos-create-profile` (`bin/aos-create-profile.mjs`), documented the architecture in `.agent/skills/README.md` and root `README.md`, and expanded `tests/guardrail.test.mjs`.
- **Impact:** `.agent/skills/vibe-coder/profiles/_schema.md`, `.agent/skills/vibe-coder/profiles/profile-antigravity.md`, `.agent/skills/README.md`, `.agent/skills/*/SKILL.md`, `bin/aos-create-profile.mjs`, `package.json`, `README.md`, `decision.md`, `aos-audit.md`, `tests/guardrail.test.mjs`.

### [01.11.2026] - Standardize `DD.MM.YYYY` Date Format Across All Docs, Skills & Tests
- **Origin:** Human Request
- **Context:** The date format needed to be corrected from `MM.DD.YYYY` to `DD.MM.YYYY` (e.g., `[01.11.2026]` and `[31.10.2026]`) across `decision.md`, `aos-audit.md`, `README.md`, all `.agent/skills/`, and `tests/guardrail.test.mjs`.
- **Decision:** Updated all dates and templates to `DD.MM.YYYY` (`### [DD.MM.YYYY] - Title` in `decision.md`, `DD.MM.YYYY` in `aos-audit.md`), updated the date parser in `tests/guardrail.test.mjs` to parse `DD.MM.YYYY` (`dd`, `mm`, `yyyy`) while verifying newest-to-oldest order, and synced global skills.
- **Impact:** `decision.md`, `aos-audit.md`, `README.md`, `.agent/skills/vibe-coder/SKILL.md`, `.agent/skills/aos-audit-project/SKILL.md`, `.agent/skills/aos-vibecode/SKILL.md`, `docs/feature/date-format-and-readme-prompts/plan.md`, `tests/guardrail.test.mjs`.

### [01.11.2026] - Fuse Strict AI Workflow & Git Rules into `AGENTS.md` and Vendor-Neutral `ai-rules.json`
- **Origin:** Human Request
- **Context:** The guardrail needed strict operational rules (*Never work on main*, *Test on the branch*, *Push, do not merge*, *Verify before writing*, *Look Before You Leap*, *Dependency Lockdown*, *Fix your own bugs*, *Commit atomicity*, *Documentation Sync*, *Explain the Fix*, and *Zero AI Slop*) fused into `AGENTS.md` alongside a vendor-neutral JSON manifest (`ai-rules.json`) and enforced across `vibe-coder`, `aos-audit-project`, and `aos-vibecode`.
- **Decision:** Fused the rules into `AGENTS.md` and `ai-rules.json`, embedded them in `.agent/skills/vibe-coder/SKILL.md`, `.agent/skills/aos-audit-project/SKILL.md`, and `.agent/skills/aos-vibecode/SKILL.md`, updated `bin/init-guardrail.mjs` to distribute `ai-rules.json`, updated `aos-audit.md`, expanded `tests/guardrail.test.mjs` (`7/7` passing), and synced global skills.
- **Impact:** `AGENTS.md`, `ai-rules.json`, `.agent/skills/vibe-coder/SKILL.md`, `.agent/skills/aos-audit-project/SKILL.md`, `.agent/skills/aos-vibecode/SKILL.md`, `bin/init-guardrail.mjs`, `README.md`, `dev.md`, `aos-audit.md`, `decision.md`, `docs/feature/strict-ai-workflow-rules/plan.md`, `tests/guardrail.test.mjs`.

### [31.10.2026] - Enforce Default 5-Badge Header Row in `README.md`, `vibe-coder`, `aos-audit-project`, and `aos-vibecode`
- **Origin:** Human Request
- **Context:** Audited and vibecoded repositories needed a standardized 5-badge header row (`Version`, `License`, `Build Status`, `Firebase`/Stack, and `Gemini` or whichever AI provider is used) enforced by `vibe-coder`, `aos-audit-project`, and `aos-vibecode`.
- **Decision:** Added the 5-badge header row to `README.md`, codified the 5-badge requirement into `.agent/skills/vibe-coder/SKILL.md`, `.agent/skills/aos-audit-project/SKILL.md`, and `.agent/skills/aos-vibecode/SKILL.md`, updated `tests/guardrail.test.mjs` and `aos-audit.md`, and synced the updated skills into `~/.gemini/antigravity/skills/` and `~/.gemini/config/skills/`.
- **Impact:** `README.md`, `.agent/skills/vibe-coder/SKILL.md`, `.agent/skills/aos-audit-project/SKILL.md`, `.agent/skills/aos-vibecode/SKILL.md`, `aos-audit.md`, `decision.md`, `docs/feature/readme-default-badges/plan.md`, `tests/guardrail.test.mjs`, `~/.gemini/antigravity/skills/`, `~/.gemini/config/skills/`.

### [31.10.2026] - Enable Automatic Model Invocation in `vibe-coder` Frontmatter & Global Config Root
- **Origin:** Agent Proposal
- **Context:** The YAML frontmatter snippet included `disable-model-invocation: true`, which prevented Antigravity from exposing `vibe-coder` in `<skills>` for automatic model activation, and Antigravity's global discovery also scans `~/.gemini/config/skills/`.
- **Decision:** Removed `disable-model-invocation: true` from `.agent/skills/vibe-coder/SKILL.md`, added a regression assertion in `tests/guardrail.test.mjs`, and synced all 5 skills to both `~/.gemini/antigravity/skills/` and `~/.gemini/config/skills/`.
- **Impact:** `.agent/skills/vibe-coder/SKILL.md`, `README.md`, `dev.md`, `decision.md`, `tests/guardrail.test.mjs`, `~/.gemini/antigravity/skills/`, `~/.gemini/config/skills/`.

### [31.10.2026] - Integrate 7-Phase FDD Workflow, `aos-audit-project` Sub-Skill, and Standard Package/README Metadata
- **Origin:** Human Request | Agent Proposal
- **Context:** The guardrail needed a dedicated project structure auditor (`aos-audit-project` generating `aos-audit.md`), the 7-Phase Feature-Driven Development (FDD) loop with explicit gateway checkpoints integrated into `vibe-coder`, global `~/.gemini/antigravity/skills/` installation instructions and attribution/support footer in `README.md`, and standardized `author`, `keywords`, and `repository` fields in `package.json` across all audited and vibecoded projects.
- **Decision:** Selected Approach C (Pragmatic Balance): created `.agent/skills/aos-audit-project/SKILL.md`, merged the 7-Phase FDD protocol and `package.json` / `README.md` standards into `.agent/skills/vibe-coder/SKILL.md`, updated `README.md` and `package.json` (`v1.0.0`), synced all 5 skills to `~/.gemini/antigravity/skills/`, and expanded `tests/guardrail.test.mjs` (`6/6` tests).
- **Impact:** `.agent/skills/vibe-coder/SKILL.md`, `.agent/skills/aos-audit-project/SKILL.md`, `README.md`, `package.json`, `decision.md`, `docs/feature/fdd-workflow-and-audit/plan.md`, `tests/guardrail.test.mjs`, `~/.gemini/antigravity/skills/`.

### [31.10.2026] - Add `init-guardrail` CLI Installer (`bin/init-guardrail.mjs`)
- **Origin:** Human Request
- **Context:** Users adopting `vibe-coding-guardrail` needed a single command (`npx` / CLI script) to copy `.agent/skills/` and `AGENTS.md` into a target repository without manual file copying.
- **Decision:** Implemented a zero-dependency ES module CLI script in `bin/init-guardrail.mjs` (≤ 35 lines), registered `"bin": { "init-guardrail": "./bin/init-guardrail.mjs" }` in `package.json`, updated `initiative.md` and `dev.md`, and added an isolated temporary-directory unit test in `tests/guardrail.test.mjs`.
- **Impact:** `bin/init-guardrail.mjs`, `package.json`, `initiative.md`, `dev.md`, `decision.md`, `tests/guardrail.test.mjs`.

### [31.10.2026] - Standardize Repository Scaffolding & Community Documentation
- **Origin:** Human Request | Agent Proposal
- **Context:** Section 1 and Section 2 of the `vibe-coder` protocol require a Git repository initialized on an isolated branch (`chore/vibe-coder-scaffold`), core documentation files (`README.md`, `initiative.md`, `dev.md`, `decision.md`), a hardened `.gitignore`, and a standardized `package.json` (`dev`, `build`, `test`, `test:unit`, `lint`) sanitized for public community release.
- **Decision:** Initialized Git on branch `chore/vibe-coder-scaffold`, documented the Shift-Left Repository pattern, RSC performance rules, Zod grounding schemas, and dual-environment Vitest/ESLint gates from `stefanasemota` reference projects, added an Antigravity installation and usage guide to `dev.md`, and created a zero-dependency Node.js test suite (`tests/guardrail.test.mjs`) to verify protocol compliance automatically.
- **Impact:** `README.md`, `initiative.md`, `dev.md`, `decision.md`, `docs/reference-architecture.md`, `.nvmrc`, `AGENTS.md`, `.gitignore`, `package.json`, `tests/guardrail.test.mjs`, `.agent/skills/aos-*/SKILL.md`.

### [31.10.2026] - Initialize `vibe-coder` Skill and Sub-Skill Triad
- **Origin:** Human Request
- **Context:** The workspace contained a draft `SKILL.md` describing the `vibe-coder` protocol and needed to be structured into a valid Antigravity workspace skill directory (`.agent/skills/vibe-coder/SKILL.md`) alongside its three orchestrated sub-skills (`aos-vibecode`, `aos-verify`, `aos-check-for-security-issues`).
- **Decision:** Extracted the clean YAML frontmatter and protocol specification into `.agent/skills/vibe-coder/SKILL.md`, removed the temporary root `SKILL.md` wrapper, and authored dedicated `SKILL.md` definitions for `aos-vibecode`, `aos-verify`, and `aos-check-for-security-issues`.
- **Impact:** `.agent/skills/vibe-coder/SKILL.md`, `.agent/skills/aos-vibecode/SKILL.md`, `.agent/skills/aos-verify/SKILL.md`, `.agent/skills/aos-check-for-security-issues/SKILL.md`.
