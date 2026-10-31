# Feature Plan: Default README Header Badges Across `vibe-coder`, `aos-audit-project`, and `aos-vibecode`

## FDD Micro-Feature Decomposition
Format: `<action> <result> <by | for | of> <a | an> <object>`

1. **FDD-1:** `Add 5-badge header row (Version, License, Build Status, Firebase, Gemini) for the root README.md`
2. **FDD-2:** `Enforce default README badge standards in the vibe-coder, aos-audit-project, and aos-vibecode skills`
3. **FDD-3:** `Validate the 5-badge header contract and sync global skills for the guardrail test suite`

---

## 7-Phase Execution Checklist

- [x] **Phase 1: Discovery & FDD Decomposition** — Created `fix/readme-default-badges` branch and initialized `docs/feature/readme-default-badges/plan.md`.
- [x] **Phase 2: Targeted Codebase Exploration** — Inspected `README.md`, `.agent/skills/vibe-coder/SKILL.md`, `.agent/skills/aos-audit-project/SKILL.md`, `.agent/skills/aos-vibecode/SKILL.md`, and `tests/guardrail.test.mjs`.
- [x] **Phase 3: Clarifying Questions & Spec Freeze** — Confirmed the 5-badge header row (`Version`, `License`, `Build Status`, `Firebase`/Stack, `Gemini`/AI Provider) across `README.md`, `vibe-coder`, `aos-audit-project`, and `aos-vibecode`.
- [x] **Phase 4: Architecture & Trade-Offs Matrix** — Approved Approach C (Pragmatic Balance).
- [x] **Phase 5: Incremental FDD Implementation** — Applied FDD-1 through FDD-3 and synced global skills.
- [x] **Phase 6: Automated Quality & Security Review** — Ran `npm test`, `npm run lint`, and 3-point static check (`6/6` passing, `0` issues).
- [x] **Phase 7: Delivery, Decision Logging & Summary** — Update `decision.md` and `aos-audit.md`, push branch, and open Draft PR.
