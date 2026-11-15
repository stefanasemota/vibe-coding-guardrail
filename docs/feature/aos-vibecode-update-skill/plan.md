# Feature Plan: `aos-vibecode-update` Skill

## FDD Micro-Features
- Create `.agent/skills/aos-vibecode-update/SKILL.md` to pull the latest plugin, refresh global symlinks, and update single or parent-folder projects via `init-guardrail.mjs`.
- Simplify `README.md` update instructions to `/aos-vibecode-update` and add it to the copy-paste prompts.
- Document `aos-vibecode-update` in `Architecture.md`.
- Add `aos-vibecode-update` test coverage in `tests/guardrail.test.mjs` and log ADR in `decision.md`.

## 7-Phase FDD Checklist
- [x] **Phase 1:** Discovery & FDD Decomposition (deleted merged local branch, created `feat/aos-vibecode-update-skill` from `origin/main`)
- [x] **Phase 2:** Targeted Codebase Exploration (`aos-vibecode/SKILL.md`, `README.md`, `Architecture.md`, `tests/guardrail.test.mjs`)
- [x] **Phase 3:** Clarifying Questions & Spec Freeze (deleted merged remote branch, confirmed `aos-vibecode-update` + `README.md` simplification)
- [x] **Phase 4:** Architecture & Trade-Offs Matrix (Approved: Approach C — Pragmatic Balance)
- [x] **Phase 5:** Incremental FDD Implementation
- [x] **Phase 6:** Automated Quality & Security Review (`aos-verify` & `aos-check-for-security-issues`)
- [x] **Phase 7:** Delivery, Decision Logging & Draft PR
