# Feature Plan: Strict AI Workflow, Git & Execution Rules (`AGENTS.md`, `ai-rules.json`)

## FDD Micro-Feature Decomposition
Format: `<action> <result> <by | for | of> <a | an> <object>`

1. **FDD-1:** `Fuse Conventional-Commits and strict-workflow-rules into AGENTS.md and vendor-neutral ai-rules.json`
2. **FDD-2:** `Embed strict-git-and-execution-rules into the vibe-coder, aos-audit-project, and aos-vibecode skills`
3. **FDD-3:** `Update bin/init-guardrail.mjs to distribute AGENTS.md and ai-rules.json for target projects`
4. **FDD-4:** `Validate rule files, skill updates, and audit report in tests/guardrail.test.mjs and aos-audit.md`

---

## 7-Phase Execution Checklist

- [x] **Phase 1: Discovery & FDD Decomposition** — Branched `feature/strict-ai-workflow-rules` off `origin/main` (`7382bcc`), ran `npm test` baseline (`6/6`), and initialized `docs/feature/strict-ai-workflow-rules/plan.md`.
- [x] **Phase 2: Targeted Codebase Exploration** — Inspected `AGENTS.md`, `.agent/skills/*/SKILL.md`, `bin/init-guardrail.mjs`, `aos-audit.md`, and `tests/guardrail.test.mjs`.
- [x] **Phase 3: Clarifying Questions & Spec Freeze** — Confirmed fusion into canonical `AGENTS.md` + vendor-neutral `ai-rules.json` and applying all audit optimizations.
- [x] **Phase 4: Architecture & Trade-Offs Matrix** — Approved Approach C with neutral `ai-rules.json` filename.
- [x] **Phase 5: Incremental FDD Implementation** — Implemented FDD-1 through FDD-4 and synced global skills.
- [x] **Phase 6: Automated Quality & Security Review** — Ran `npm test`, `npm run lint`, and 3-point static check (`7/7` passing, `0` issues).
- [x] **Phase 7: Delivery, Decision Logging & Summary** — Update `decision.md` and `aos-audit.md`, push branch, and open Draft PR.
