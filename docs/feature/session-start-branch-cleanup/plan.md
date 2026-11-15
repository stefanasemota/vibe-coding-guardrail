# Feature Plan: Session-Start Obsolete Branch Cleanup

## FDD Micro-Features
- Enforce session-start pruning of stale remote-tracking refs for the active repository.
- Delete obsolete local branches merged into the base branch before starting a `vibe-coder` session.
- Prompt for human confirmation before deleting obsolete remote `origin/*` branches merged into the base branch.
- Sync branch cleanup rule into `AGENTS.md` and verify via `tests/guardrail.test.mjs`.

## 7-Phase FDD Checklist
- [x] **Phase 1:** Discovery & FDD Decomposition (`profile-antigravity.md` resolved, branch `feat/session-start-branch-cleanup` created from `main`)
- [x] **Phase 2:** Targeted Codebase Exploration (`vibe-coder/SKILL.md`, `AGENTS.md`, `tests/guardrail.test.mjs`, `decision.md`)
- [x] **Phase 3:** Clarifying Questions & Spec Freeze (Confirmed: both protocol + repo cleanup, auto-delete local merged + prompt for remote, branch from `main`)
- [x] **Phase 4:** Architecture & Trade-Offs Matrix (Approved: Approach C — Pragmatic Balance)
- [x] **Phase 5:** Incremental FDD Implementation
- [x] **Phase 6:** Automated Quality & Security Review (`aos-verify` & `aos-check-for-security-issues`)
- [x] **Phase 7:** Delivery, Decision Logging, Remote Branch Cleanup & Draft PR
