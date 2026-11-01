# Feature Plan: Engine-Neutral Workflow Chassis & Interchangeable Engine Profile Architecture

## FDD Micro-Feature Decomposition
Format: `<action> <result> <by | for | of> <a | an> <object>`

1. **FDD-1:** `Create _schema.md and default profile-antigravity.md for the vibe-coder profile architecture` (`.agent/skills/vibe-coder/profiles/`)
2. **FDD-2:** `Refactor vibe-coder/SKILL.md into an engine-neutral 7-Phase FDD orchestrator with profile resolution`
3. **FDD-3:** `Refactor aos-vibecode, aos-audit-project, aos-verify, and aos-check-for-security-issues to consume active profile parameters`
4. **FDD-4:** `Implement aos-create-profile subroutine and bin/aos-create-profile.mjs CLI utility for custom engine profiles`
5. **FDD-5:** `Document the workflow-chassis vs engine-profile architecture in .agent/skills/README.md and root README.md and verify in tests/guardrail.test.mjs`

---

## 7-Phase Execution Checklist

- [x] **Phase 1: Discovery & FDD Decomposition** — Branched `chore/engine-neutral-profile-architecture` off `origin/main` (`3b1402d`), verified `npm test` baseline (`7/7`), and initialized `docs/feature/engine-neutral-profile-architecture/plan.md`.
- [x] **Phase 2: Targeted Codebase Exploration** — Inspected `.agent/skills/*/SKILL.md`, `bin/init-guardrail.mjs`, `README.md`, `package.json`, and `tests/guardrail.test.mjs`.
- [x] **Phase 3: Clarifying Questions & Spec Freeze** — Confirmed `aos-create-profile` as both agent subroutine and CLI utility (`bin/aos-create-profile.mjs`), and documentation in both `.agent/skills/README.md` and root `README.md`.
- [x] **Phase 4: Architecture & Trade-Offs Matrix** — Approved Approach C (Pragmatic Balance).
- [x] **Phase 5: Incremental FDD Implementation** — Implemented FDD-1 through FDD-5 and synced global skills.
- [x] **Phase 6: Automated Quality & Security Review** — Ran `npm test`, `npm run lint`, and 3-point static check (`8/8` passing, `0` issues).
- [x] **Phase 7: Delivery, Decision Logging & Summary** — Prepend ADR to `decision.md` (`[01.11.2026]`), update `aos-audit.md`, push branch, and open Draft PR.
