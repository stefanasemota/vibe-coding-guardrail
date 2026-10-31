# 📋 Architectural & Implementation Decision Log (`decision.md`)

Chronological ledger of all architectural, UX, and implementation choices governed by the `vibe-coder` protocol.

---

### [2026-10-31] - Initialize `vibe-coder` Skill and Sub-Skill Triad
- **Origin:** Human Request
- **Context:** The workspace contained a draft `SKILL.md` describing the `vibe-coder` protocol and needed to be structured into a valid Antigravity workspace skill directory (`.agent/skills/vibe-coder/SKILL.md`) alongside its three orchestrated sub-skills (`aos-vibecode`, `aos-verify`, `aos-check-for-security-issues`).
- **Decision:** Extracted the clean YAML frontmatter and protocol specification into `.agent/skills/vibe-coder/SKILL.md`, removed the temporary root `SKILL.md` wrapper, and authored dedicated `SKILL.md` definitions for `aos-vibecode`, `aos-verify`, and `aos-check-for-security-issues`.
- **Impact:** `.agent/skills/vibe-coder/SKILL.md`, `.agent/skills/aos-vibecode/SKILL.md`, `.agent/skills/aos-verify/SKILL.md`, `.agent/skills/aos-check-for-security-issues/SKILL.md`.

### [2026-10-31] - Standardize Repository Scaffolding & Community Documentation
- **Origin:** Human Request | Agent Proposal
- **Context:** Section 1 and Section 2 of the `vibe-coder` protocol require a Git repository initialized on an isolated branch (`chore/vibe-coder-scaffold`), core documentation files (`README.md`, `initiative.md`, `dev.md`, `decision.md`), a hardened `.gitignore`, and a standardized `package.json` (`dev`, `build`, `test`, `test:unit`, `lint`) sanitized for public community release.
- **Decision:** Initialized Git on branch `chore/vibe-coder-scaffold`, documented the Shift-Left Repository pattern, RSC performance rules, Zod grounding schemas, and dual-environment Vitest/ESLint gates from `stefanasemota` reference projects, added an Antigravity installation and usage guide to `dev.md`, and created a zero-dependency Node.js test suite (`tests/guardrail.test.mjs`) to verify protocol compliance automatically.
- **Impact:** `README.md`, `initiative.md`, `dev.md`, `decision.md`, `docs/reference-architecture.md`, `.nvmrc`, `AGENTS.md`, `.gitignore`, `package.json`, `tests/guardrail.test.mjs`, `.agent/skills/aos-*/SKILL.md`.

### [2026-10-31] - Add `init-guardrail` CLI Installer (`bin/init-guardrail.mjs`)
- **Origin:** Human Request
- **Context:** Users adopting `vibe-coding-guardrail` needed a single command (`npx` / CLI script) to copy `.agent/skills/` and `AGENTS.md` into a target repository without manual file copying.
- **Decision:** Implemented a zero-dependency ES module CLI script in `bin/init-guardrail.mjs` (≤ 35 lines), registered `"bin": { "init-guardrail": "./bin/init-guardrail.mjs" }` in `package.json`, updated `initiative.md` and `dev.md`, and added an isolated temporary-directory unit test in `tests/guardrail.test.mjs`.
- **Impact:** `bin/init-guardrail.mjs`, `package.json`, `initiative.md`, `dev.md`, `decision.md`, `tests/guardrail.test.mjs`.

### [2026-10-31] - Integrate 7-Phase FDD Workflow, `aos-audit-project` Sub-Skill, and Standard Package/README Metadata
- **Origin:** Human Request | Agent Proposal
- **Context:** The guardrail needed a dedicated project structure auditor (`aos-audit-project` generating `aos-audit.md`), the 7-Phase Feature-Driven Development (FDD) loop with explicit gateway checkpoints integrated into `vibe-coder`, global `~/.gemini/antigravity/skills/` installation instructions and attribution/support footer in `README.md`, and standardized `author`, `keywords`, and `repository` fields in `package.json` across all audited and vibecoded projects.
- **Decision:** Selected Approach C (Pragmatic Balance): created `.agent/skills/aos-audit-project/SKILL.md`, merged the 7-Phase FDD protocol and `package.json` / `README.md` standards into `.agent/skills/vibe-coder/SKILL.md`, updated `README.md` and `package.json` (`v1.0.0`), synced all 5 skills to `~/.gemini/antigravity/skills/`, and expanded `tests/guardrail.test.mjs` (`6/6` tests).
- **Impact:** `.agent/skills/vibe-coder/SKILL.md`, `.agent/skills/aos-audit-project/SKILL.md`, `README.md`, `package.json`, `decision.md`, `docs/feature/fdd-workflow-and-audit/plan.md`, `tests/guardrail.test.mjs`, `~/.gemini/antigravity/skills/`.
