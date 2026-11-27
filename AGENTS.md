# AI Workflow, Git & Commit Rules (`AGENTS.md`)

Concise operational rules for AI coding agents. Deterministic branch protection and ADR checks are enforced natively by the guardrail plugin's lifecycle hooks; these rules govern everything else. Zero filler or AI slop.

---

## 1. Branching & Git Strategy
* **Never work on protected branches:** Always create a descriptive branch (`feature/<slug>`, `fix/<slug>`, `chore/<slug>`, `refactor/<slug>`) before editing code. Direct commits/pushes to `main`/`master` are blocked by the guardrail plugin's branch_guard hook.
* **No startup `git fetch`:** Keep session startup 100% local and read-only (enforced by the guardrail plugin's session_start hook). Run `/aos-vibecode-update` on demand to prune remotes and clean obsolete merged branches.
* **Test on the branch:** Ensure builds, linters, and tests pass on the isolated branch before pushing.
* **Push, do not merge:** Push the verified branch and open a Draft Pull Request (`gh pr create --draft`). Leave final review and merge to the human.

---

## 2. Execution Discipline
* **Verify before writing:** Read relevant existing code and confirm the baseline passes before editing.
* **Look Before You Leap:** Search (`find`/`grep`) for existing utilities, hooks, or components before creating new ones.
* **Dependency Lockdown:** Never install new `npm`, `pip`, or system packages without explicit human approval first.
* **Fix your own bugs:** If a build, lint, or test command fails after your edit, fix it autonomously before finishing.
* **Documentation Sync:** When changing CLI flags, hooks, skills, or setup steps, update `README.md`, `Architecture.md`, or `dev.md` in the same branch.
* **Decision Logging:** Prepend architectural decisions to the top of `decision.md` in `[DD.MM.YYYY]` format (`Origin`, `Context`, `Decision`, `Impact`), validated by the guardrail plugin's adr_check hook.

---

## 3. Conventional Commits & Atomicity
* **Commit atomicity:** Make small, logical commits as you progress.
* **Explain the Fix:** For `fix` commits, include a brief body stating root cause and fix.
* **Required Header Format:** `type(optional-scope): short description`

| Type | When to Use |
|---|---|
| `feat` | A new user-visible feature |
| `fix` | A bug fix (include root cause & fix summary) |
| `docs` | Documentation-only changes |
| `chore` | Build, config, or tooling changes |
| `refactor` | Code restructured with no behavior change |
| `test` | Adding or correcting tests |
| `style` | Formatting changes only |
| `perf` | Performance improvements |
