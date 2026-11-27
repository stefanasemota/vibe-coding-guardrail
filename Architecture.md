# 🏗️ Architecture (`Architecture.md`) — v2.0

**Vibe Coding Guardrail v2.0** is a zero-dependency **Python 3.9+ / 3.11+** plugin built natively for **Google Antigravity**. Deterministic safety checks run in native Antigravity lifecycle hooks (`hooks.json`), while the **3-Stage Orchestrator** (`vibe-coder`) coordinates 5 specialized `aos-*` skills plus 2 vendored Apache-2.0 token-compression skills (**8 skills total**).

```text
               ┌──────────────────────────────────────────────┐
               │        Antigravity Native Plugin Root        │
               │   plugin.json  |  hooks.json  |  rules/      │
               └──────────────────────┬───────────────────────┘
                                      │
          ┌───────────────────────────┼───────────────────────────┐
          ▼                           ▼                           ▼
┌────────────────────┐     ┌────────────────────┐     ┌────────────────────┐
│   SessionStart     │     │    PreToolUse      │     │        Stop        │
│ session_start.py   │     │  branch_guard.py   │     │   adr_check.py     │
│ (local read-only)  │     │ (block main/master)│     │ (validate ADR log) │
└────────────────────┘     └────────────────────┘     └────────────────────┘
                                      │
                                      ▼
               ┌──────────────────────────────────────────────┐
               │       3-Stage Loop (skills/vibe-coder)       │
               │ Stage 1: Scope & Plan (gate: pause|advisory) │
               │ Stage 2: Build & Verify (vibecode + verify)  │
               │ Stage 3: Audit & PR (security + Draft PR)    │
               └──────────────────────────────────────────────┘
```

---

## Component & Skill Inventory (8 Skills)

`skills/*/SKILL.md` on disk is the single source of truth enforced by `tests/test_guardrail.py`.

| Component | Path | Responsibility |
| :--- | :--- | :--- |
| **`plugin.json`** | `plugin.json` | Native Antigravity plugin manifest bundling `hooks.json`, `rules/AGENTS.md`, `assets/logo.svg`, and all 8 skills. |
| **`hooks.json`** | `hooks.json` | Native Antigravity lifecycle hook registry (`SessionStart`, `PreToolUse`, `Stop`). |
| **`session_start.py`** | `hooks/session_start.py` | 100% local, read-only branch check at startup (no `git fetch` or `.git/` writes). |
| **`branch_guard.py`** | `hooks/branch_guard.py` | Deterministically blocks `git commit`/`git push` on `main`/`master` and `--no-verify`. |
| **`adr_check.py`** | `hooks/adr_check.py` | Validates reverse-chronological `[DD.MM.YYYY]` ADRs and required fields when `decision.md` changes. |
| **`rules/AGENTS.md`** | `rules/AGENTS.md` | Concise repo-level workflow and Conventional Commits rules (symlinked to root `AGENTS.md`). |
| **`vibe-coder`** | `skills/vibe-coder/SKILL.md` | Compressed 3-Stage Orchestrator with a single configurable gate (`pause` vs `advisory`). |
| **`aos-vibecode`** | `skills/aos-vibecode/SKILL.md` | Implements approved plans in atomic `<= 50`-line micro-patches with per-patch verification. |
| **`aos-verify`** | `skills/aos-verify/SKILL.md` | Stack-aware static analysis, 3-point audit, unit tests, and build verification. |
| **`aos-check-for-security-issues`** | `skills/aos-check-for-security-issues/SKILL.md` | Defensive security audit for secrets, `.gitignore`, server/client boundaries, and CVEs. |
| **`aos-audit-project`** | `skills/aos-audit-project/SKILL.md` | Audits repository structure/metadata and generates `aos-audit.md` (`pause` or `advisory`). |
| **`aos-vibecode-update`** | `skills/aos-vibecode-update/SKILL.md` | Updates the plugin, runs on-demand `git fetch --prune` + merged branch cleanup, and syncs `AGENTS.md`. |
| **`caveman`** | `skills/caveman/SKILL.md` | Vendored (Apache-2.0, local/zero-telemetry) terse response voice with explicit guardrail exemptions. |
| **`caveman-compress`** | `skills/caveman-compress/SKILL.md` | Vendored (Apache-2.0, local/zero-telemetry) natural-language file compressor with explicit guardrail exemptions. |
| **`scaffolding-templates.md`** | `references/scaffolding-templates.md` | Shared templates for README badges/footer, Node `package.json`, and `[DD.MM.YYYY]` ADRs. |
| **`test_guardrail.py`** | `tests/test_guardrail.py` | Zero-dependency Python `unittest` suite enforcing zero skill drift and testing all hooks. |

---

## Required Repository Metadata

Repositories governed by `vibe-coder` maintain:
- `README.md` — Pitch, install/quick-start, 5-badge header row, and mandatory community footer.
- `Architecture.md` — System diagram, component table, and architectural boundaries.
- `INITIATIVE.md` (or `initiative.md`) — Product brief, seed prompt, or refactor spec.
- `dev.md` — Prerequisites, environment variables, and verification commands.
- `decision.md` — Reverse-chronological ADR ledger (`[DD.MM.YYYY]`, newest at top).
- `AGENTS.md` — Git strategy, execution discipline, and Conventional Commits.
- `docs/feature/<slug>/plan.md` — Concise Stage 1 implementation plan.
