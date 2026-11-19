---
name: vibe-coder
description: Orchestrate a 7-Phase Feature-Driven Development (FDD) workflow across new or existing repositories with explicit checkpoints, decision.md logging, and automated verification. Use when scaffolding, auditing, building, or iterating on features under the vibe-coding guardrail.
---

# Vibe Coding Protocol & Engine-Neutral 7-Phase FDD Orchestrator

The **human is the driver** and the **AI is the engine**. This orchestrator governs process, checkpoints, Git isolation, and decision logging while delegating model-specific parameters (`max_patch_size`, `patch_strategy`, `type_safety`, `review_depth`, `gate_behavior`) to an interchangeable **Engine Profile**.

---

## 0. Engine Profile Resolution

At session start, resolve the active Engine Profile before executing Phase 1:
1. If the user or environment specifies `$PROFILE`, load `.agent/skills/vibe-coder/profiles/profile-$PROFILE.md`.
2. Otherwise, load the default profile: [`.agent/skills/vibe-coder/profiles/profile-antigravity.md`](./profiles/profile-antigravity.md) (validated against [`_schema.md`](./profiles/_schema.md)).
3. Pass the resolved parameters (`execution_mode`, `max_patch_size`, `patch_strategy`, `type_safety`, `gate_behavior`, `review_depth`) to orchestrated sub-skills (`aos-audit-project`, `aos-vibecode`, `aos-verify`, `aos-check-for-security-issues`).

---

## 1. Engine-Neutral 7-Phase FDD Workflow

Execute these 7 phases sequentially. Respect `gate_behavior` from the active profile (default: pause for explicit human confirmation at **Phase 3**, **Phase 4**, and **Phase 6**).

### Phase 1: Discovery & FDD Decomposition
1. Resolve the active Engine Profile (Section 0), run **Session-Start Obsolete Branch Cleanup** (Section 2), and confirm Git branch isolation.
2. Initialize or update `docs/feature/[feature-name]/plan.md` with a 7-phase checklist.
3. Decompose the request into FDD micro-features: `<action> <result> <by | for | of> <a | an> <object>`.
4. If scope or constraints are ambiguous, confirm initial understanding before exploring.

### Phase 2: Targeted Codebase Exploration
1. Search the codebase using the profile's `execution_mode`:
   - **Path A:** Architecture, types, and abstraction patterns.
   - **Path B:** Existing similar features, state stores, or API routes.
   - **Path C:** Test fixtures, validation schemas, and UI layout conventions.
2. Read the critical relevant files (up to 5–10 on larger repos) to establish ground truth and summarize discovered patterns.

### Phase 3: Clarifying Questions & Spec Freeze (MANDATORY GATE)
**GATEWAY CHECKPOINT: Do not write code or finalize architecture until answered.**
1. Cross-reference discovered patterns against feature requirements.
2. Surface underspecified areas (edge cases, empty states, validation/failure modes, backward compatibility, schema extensions).
3. Present an organized list of questions and await human confirmation.

### Phase 4: Architecture & Trade-Offs Matrix (MANDATORY GATE)
1. Draft 3 concrete implementation paths:
   - **Approach A (Minimal Footprint):** Fastest implementation, reuses existing modules, minimal diff.
   - **Approach B (Clean Architecture):** Full domain isolation, modular abstractions, maximum testability.
   - **Approach C (Pragmatic Balance):** Balances clean abstractions with immediate implementation velocity.
2. Present a trade-off table (Files to create/modify, Risk/regression potential, Recommendation with justification).
3. Once approved, prepend the chosen direction to `decision.md` using `[DD.MM.YYYY]`.

### Phase 5: Incremental FDD Implementation (`aos-vibecode`)
**Requires Phase 4 approval.**
1. Delegate implementation to `aos-vibecode`, enforcing `max_patch_size` and `patch_strategy` from the active profile.
2. Implement atomic unit by atomic unit (types/contracts -> domain logic -> UI/API wiring), updating `docs/feature/[feature-name]/plan.md` after each unit.

### Phase 6: Automated Quality & Security Review (`aos-verify` & `aos-check-for-security-issues` — MANDATORY GATE)
1. Delegate validation to `aos-verify` (enforcing `type_safety` and `review_depth`) and `aos-check-for-security-issues`.
2. Categorize findings as **Critical** (must fix now) vs. **Minor / Technical Debt** (log for later) and ask whether to remediate immediately or proceed.

### Phase 7: Delivery, Decision Logging & Summary
1. Ensure `decision.md` has the prepended `[DD.MM.YYYY]` ADR at the top and mark all items in `docs/feature/[feature-name]/plan.md` completed.
2. Output the final summary (**Delivered FDD Items**, **Modified Files**, **Test Status**, **Next Steps**), push the branch + open a **Draft PR** (`gh pr create --draft`), and append the **Session Termination** footer (Section 2).

---

## 2. Git Lifecycle, Execution Rules & Session Termination

Follow `AGENTS.md` and `ai-rules.json` for execution discipline (`Verify before writing`, `Look Before You Leap`, `Dependency Lockdown`, `Fix your own bugs`, `Documentation Sync`, Conventional Commits). In addition:

1. **Session-Start Obsolete Branch Cleanup (MANDATORY):**
   - `git fetch --prune`
   - Delete **local** branches already merged into `<base>` (`main`/`master`/`development`), excluding protected branches (`main`, `master`, `development`, `develop`) and the current branch (`git branch --merged <base>` -> `git branch -d <branch>`).
   - List merged **remote** (`origin/*`) branches (excluding `HEAD` and protected branches) and **prompt the user for confirmation** before deleting (`git push origin --delete <branch>`). Skip remote deletion in unattended `advisory` runs.
2. **Branch Isolation (STRICT):**
   - Never work on `main`, `master`, or `development`.
   - Never commit to an already-merged branch: check `gh pr view --json state` or `git branch --merged origin/main`; if merged, branch fresh (`feature/<slug>`, `fix/<slug>`, `chore/<slug>`) from `origin/main` first.
   - **Push, Do Not Merge:** Open a Draft PR; leave final merge/review to the human.
3. **Session Termination (MANDATORY):**
   End every session (and standalone `aos-*` run) by reading `version` from `plugin.json` (or `package.json`) and outputting:
   `Guardrail: aos Vibe Coding Guardrail v<version> | Skill: <skill-name> | Tokens: <exact count if exposed by runtime, otherwise "N/A (not exposed by runtime)">`

---

## 3. Project Standardization & Decision Logging (Conditional)

If scaffolding a new repository, auditing project metadata, or logging a decision in `decision.md`, read [`references/scaffolding-templates.md`](./references/scaffolding-templates.md) for the exact `README.md` badge/footer snippets, `package.json` schema, and `[DD.MM.YYYY]` ADR template.

* **Core Docs:** `README.md`, `initiative.md`, `dev.md`, `decision.md` (newest at top), `docs/feature/[feature-name]/plan.md`, `.gitignore`, and `AGENTS.md` / `ai-rules.json`.
* **Stack Detection:**
  * **Non-Node (`pyproject.toml`, `go.mod`, `Cargo.toml`, `build.gradle`, `Package.swift`):** Skip `package.json` checks; map `aos-verify` to the native toolchain (`pytest`/`ruff`, `go test`, `cargo clippy`, `./gradlew test`).
  * **Node.js / TypeScript (`package.json` exists):** Enforce standardized metadata and scripts (`dev`, `build`, `test`, `test:unit`, `lint`).

---

## 4. Gotchas

* **Merged-branch trap:** Continuing work on an existing feature branch whose PR was already merged creates unmergeable/stale diffs—always check `gh pr view --json state` before editing.
* **Unattended `advisory` mode:** Never prompt for remote branch deletion or pause at Phase 3/4/6 gates when `gate_behavior: "advisory"` is active.
* **ADR date format:** Always prepend `[DD.MM.YYYY]` at the top of `decision.md`; `YYYY-MM-DD` or bottom-appended entries break `guardrail.test.mjs`.
* **Plugin updates:** Use sibling skill `aos-vibecode-update` (not `vibe-coder`) when the user asks to update the guardrail plugin or refresh global skill symlinks.

---

## 5. Subroutine: `aos-create-profile <name>`

When invoked (`aos-create-profile <name>` or `npx aos-create-profile <name>`), collect or default the 4 core parameters (`engine_name`, `max_patch_size=50`, `review_depth=multi-aspect-audit|quick-lint`, `gate_behavior=explicit-pause-and-wait|advisory`), validate against `.agent/skills/vibe-coder/profiles/_schema.md`, and emit `.agent/skills/vibe-coder/profiles/profile-<name>.md` (or run `node bin/aos-create-profile.mjs <name>`).
