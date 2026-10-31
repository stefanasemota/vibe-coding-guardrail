---
name: vibe-coder
description: Enforces a structured vibe-coding and rapid-prototyping workflow across new or existing repositories. Use this skill when the user wants to scaffold, build, iterate on, or patch features fast while maintaining repository consistency. Automatically standardizes project setup (package.json, .gitignore, README.md, dev.md, initiative.md, decision.md), verifies git initialization and remote branches, enforces isolated feature/chore/fix branches, logs architectural choices to decision.md, and coordinates sub-skills (aos-vibecode, aos-verify, aos-check-for-security-issues) before publishing changes via draft pull requests.
---

# Vibe Coding Protocol & Workflow

When initializing a new application or iterating on an existing repository in a vibe-coding session, follow this standardized orchestration protocol.

---

## 1. Project Standardization & Scaffolding Checklist

Every project managed under this workflow must enforce a uniform directory structure and root metadata:

* **Core Documentation Files:**
  * `README.md`: High-level pitch, architectural summary, quick-start commands, and runtime scripts.
  * `initiative.md`: The initial seed prompt, product brief, or problem statement that launched the app.
  * `dev.md`: Local development environment setup, environment variable specs, and execution instructions.
  * `decision.md`: Chronological ledger of all architectural, UX, and implementation choices.
* **Configuration & Structure:**
  * Consistent `.gitignore` covering environment variables, dependency caches (`node_modules`, `.turbo`, etc.), and build artifacts (`dist`, `.next`, coverage).
  * Standardized `package.json` schema (`scripts` must uniformly provide `dev`, `build`, `test`, `test:unit`, and `lint`).
  * Automated testing suite setup: baseline unit test runners configured (e.g., Vitest/Jest), with optional end-to-end / integration harnesses clearly separated.

---

## 2. Git Lifecycle & Branch Management

Execute environment sanity checks before writing any code:

1. **Repository Inspection:**
   * Check for an existing Git repository (`git rev-parse --is-inside-work-tree`). If absent, run `git init`.
   * Check for an upstream remote (`git remote -v`). If no remote exists, prompt to configure or auto-link the GitHub remote.
2. **Branching Convention:**
   * Direct commits to `main` or `master` are strictly prohibited.
   * Classify the session goal and create a scoped branch using the pattern:
     * `feature/<short-slug>`
     * `fix/<short-slug>`
     * `chore/<short-slug>`
3. **Session Completion & Pull Requests:**
   * Conclude every session with explicit human confirmation/approval.
   * Push the working branch to the remote upstream and generate a **Draft Pull Request** (via GitHub CLI `gh pr create --draft` or direct branch push) with a concise bulleted summary of changes.

---

## 3. Mandatory Decision Logging (`decision.md`)

Maintain an immutable audit trail throughout the session. Every significant technical choice, design preference, pivot, or dependency addition must be appended immediately using the following schema:

```markdown
### [YYYY-MM-DD] - <Decision Title>
- **Origin:** Agent Proposal | Human Request
- **Context:** Brief description of the problem or opportunity.
- **Decision:** What was chosen and why.
- **Impact:** Files, packages, or architectural paths affected.

```

---

## 4. Sub-Skill Orchestration

Coordinate across three root sub-skills during the session lifecycle:

```
                  ┌──────────────────────┐
                  │   Planning Session   │
                  │  (Intent & Context)  │
                  └──────────┬───────────┘
                             │
            ┌────────────────┼────────────────┐
            ▼                ▼                ▼
   ┌─────────────────┐ ┌───────────┐ ┌──────────────────┐
   │  aos-vibecode   │ │aos-verify │ │aos-check-for-    │
   │ (Implementation)│ │(Validation│ │security-issues   │
   └─────────────────┘ └───────────┘ └──────────────────┘
            │                │                │
            └────────────────┼────────────────┘
                             ▼
                  ┌──────────────────────┐
                  │ Session Termination  │
                  │ (decision.md + Draft)│
                  └──────────────────────┘

```

1. **`aos-vibecode` (Rapid Feature Delivery):**
* Translates ideas from `initiative.md` into minimal, working code increments.
* Favors iterative micro-patches (≤ 50 lines per change where feasible) over large-file rewrites.
* Preserves existing runtime state, routes, and mock data without breaking changes.


2. **`aos-verify` (Automated Sanity & Test Coverage):**
* Runs local sanity checks: validates imports, syntax, lint rules, and builds.
* Executes unit tests and confirms critical user paths remain green before completion.


3. **`aos-check-for-security-issues` (Defensive Audit):**
* Audits new dependencies and scans for hardcoded secrets, API tokens, unvalidated inputs, or vulnerable patterns before any code is committed.



---

## 5. Session Execution Sequence

1. **Intake & Intent Discovery:** Review the prompt or update `initiative.md`. Categorize the task (`feature`, `fix`, or `chore`).
2. **Scaffold Check:** Ensure `README.md`, `dev.md`, `initiative.md`, and `decision.md` exist; confirm branch isolation.
3. **Draft & Refine (`aos-vibecode`):** Implement the changes incrementally with progressive UI polish.
4. **Audit & Test (`aos-verify` & `aos-check-for-security-issues`):** Run automated checks and patch any regressions or vulnerabilities.
5. **Log & Propose:** Append all key choices to `decision.md` with today's date.
6. **Hand-Off:** Seek final human review, push the branch, and open a Draft PR.
