# Feature Plan: Docs Restructure & Session Termination Telemetry

## FDD Micro-Features
- Extract architectural diagram, skill/profile table, required metadata, and reference benchmark into `Architecture.md`.
- Refine `README.md` to focus on pitch, global/workspace installation, plugin update/version verification, copy-paste prompts, and Wednesday automations (zero AI slop).
- Restructure `dev.md` to consolidate local setup, custom AI model profiles, environment variables, standard scripts, and session workflow (zero AI slop).
- Add standardized Session Termination footer (guardrail version + skill name + runtime token usage or `N/A`) to `vibe-coder` and all 4 `aos-*` sub-skills.
- Update `tests/guardrail.test.mjs` to verify `Architecture.md`, restructured `README.md` & `dev.md`, and Session Termination rules.

## 7-Phase FDD Checklist
- [x] **Phase 1:** Discovery & FDD Decomposition (deleted 4 merged local branches, created `feat/docs-restructure-session-telemetry` from `origin/main`)
- [x] **Phase 2:** Targeted Codebase Exploration (`README.md`, `dev.md`, `plugin.json`, `tests/guardrail.test.mjs`, 5 `SKILL.md` files)
- [x] **Phase 3:** Clarifying Questions & Spec Freeze (deleted 4 merged remote branches, confirmed doc split & non-fabricated token reporting)
- [x] **Phase 4:** Architecture & Trade-Offs Matrix (Approved: Approach C — Pragmatic Balance)
- [x] **Phase 5:** Incremental FDD Implementation
- [x] **Phase 6:** Automated Quality & Security Review (`aos-verify` & `aos-check-for-security-issues`)
- [x] **Phase 7:** Delivery, Decision Logging & Draft PR
