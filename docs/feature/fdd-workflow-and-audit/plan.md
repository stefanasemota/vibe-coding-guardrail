# Feature Plan: 7-Phase FDD Workflow, `aos-audit-project` Sub-Skill & README Enhancements

## FDD Micro-Feature Decomposition
Format: `<action> <result> <by | for | of> <a | an> <object>`

1. **FDD-1:** `Document global-skill-installation and community-footer for the project README`
2. **FDD-2:** `Create architecture-compliance-auditor and aos-audit.md generator for a target repository` (`.agent/skills/aos-audit-project/SKILL.md`)
3. **FDD-3:** `Integrate the 7-Phase FDD protocol and 4-sub-skill orchestration into the vibe-coder skill` (`.agent/skills/vibe-coder/SKILL.md`)
4. **FDD-4:** `Validate 5-skill suite, README footer, package.json metadata, and global skill synchronization for the guardrail test suite` (`tests/guardrail.test.mjs` & `~/.gemini/antigravity/skills/`)

---

## 7-Phase Execution Checklist

- [x] **Phase 1: Discovery & FDD Decomposition** — Initialized `docs/feature/fdd-workflow-and-audit/plan.md` and decomposed into 4 FDD units.
- [x] **Phase 2: Targeted Codebase Exploration** — Inspected `.agent/skills/*/SKILL.md`, `README.md`, `dev.md`, `decision.md`, `bin/init-guardrail.mjs`, and `tests/guardrail.test.mjs`.
- [x] **Phase 3: Clarifying Questions & Spec Freeze** — Confirmed canonical root `decision.md` (with `docs/decisions.md` alias), root `aos-audit.md` output, and unified 7-Phase FDD protocol in `.agent/skills/vibe-coder/SKILL.md`.
- [x] **Phase 4: Architecture & Trade-Offs Matrix** — Approved Approach C (Pragmatic Balance) and logged ADR in `decision.md`.
- [x] **Phase 5: Incremental FDD Implementation** — Implemented FDD-1 through FDD-4 and synced `~/.gemini/antigravity/skills/`.
- [x] **Phase 6: Automated Quality & Security Review** — Ran `npm test`, `npm run lint`, and 3-point static check (`6/6` tests passing, zero critical or minor issues).
- [x] **Phase 7: Delivery, Decision Logging & Summary** — Finalize `decision.md`, mark plan complete, push branch, and open Draft PR.
