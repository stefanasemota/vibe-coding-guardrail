# Feature Plan: Add Explicit Step 5 (Branch, Commit, Push & Open Draft PR) to `aos-audit-project`

## FDD Micro-Feature Decomposition
Format: `<action> <result> <by | for | of> <a | an> <object>`

1. **FDD-1:** `Add Step 5 (Branch, Commit, Push & Open Draft PR) to .agent/skills/aos-audit-project/SKILL.md`
2. **FDD-2:** `Validate Step 5 Draft PR enforcement in tests/guardrail.test.mjs and log ADR in decision.md`
3. **FDD-3:** `Push feat/audit-auto-draft-pr and open a Draft PR for the repository`

---

## 7-Phase Execution Checklist

- [x] **Phase 1: Discovery & FDD Decomposition** — Branched `feat/audit-auto-draft-pr` off `origin/main` (`b1a52f9`), verified `npm test` baseline (`8/8`), and initialized `docs/feature/audit-auto-draft-pr/plan.md`.
- [x] **Phase 2: Targeted Codebase Exploration** — Inspected `.agent/skills/aos-audit-project/SKILL.md`, `skills/aos-audit-project/SKILL.md`, and `tests/guardrail.test.mjs`.
- [x] **Phase 3: Clarifying Questions (Mandatory Gate)** — Confirmed spec freeze for Step 5 in `aos-audit-project/SKILL.md`.
- [x] **Phase 4: Architecture Design & Trade-Offs (Mandatory Gate)** — Confirmed Pragmatic Balance and logged ADR in `decision.md`.
- [x] **Phase 5: Incremental FDD Implementation (`aos-vibecode`)** — Updated `aos-audit-project/SKILL.md`, `decision.md`, `aos-audit.md`, and `tests/guardrail.test.mjs`.
- [x] **Phase 6: Automated Quality & Security Review (`aos-verify` & `aos-check-for-security-issues`)** — Ran `npm test && npm run lint` (`8/8` passing) and verified global/plugin symlinks.
- [x] **Phase 7: Delivery, Decision Logging & Summary** — Commit on `feat/audit-auto-draft-pr`, push to `origin`, and open Draft PR.
