# 🏗️ Architecture (`Architecture.md`)

**Vibe Coding Guardrail** decouples the **Engine-Neutral 7-Phase FDD Workflow Chassis** (`vibe-coder` + four `aos-*` sub-skills) from the **Interchangeable Engine Profile** ([`.agent/skills/vibe-coder/profiles/profile-antigravity.md`](.agent/skills/vibe-coder/profiles/profile-antigravity.md), validated by [`_schema.md`](.agent/skills/vibe-coder/profiles/_schema.md)).

```
                      ┌──────────────────────────────────┐
                      │         Engine Profile           │
                      │ (profiles/profile-antigravity.md)│
                      └─────────────────┬────────────────┘
                                        │ (Parameters)
                                        ▼
                      ┌──────────────────────────────────┐
                      │   7-Phase FDD Workflow Chassis   │
                      │          (vibe-coder)            │
                      └─────────────────┬────────────────┘
                                        │
       ┌───────────────────┬────────────┴──────┬────────────────────┐
       ▼                   ▼                   ▼                    ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────┐ ┌──────────────────┐
│aos-audit-project│ │  aos-vibecode   │ │ aos-verify  │ │aos-check-for-    │
│ (Audit & Fix)   │ │ (Implementation)│ │ (Validation)│ │security-issues   │
└─────────────────┘ └─────────────────┘ └─────────────┘ └──────────────────┘
       │                   │                   │                    │
       └───────────────────┴────────────┬──────┴────────────────────┘
                                        ▼
                      ┌──────────────────────────────────┐
                      │       Session Termination        │
                      │(decision.md + Draft PR + Footer) │
                      └──────────────────────────────────┘
```

---

## Skill Suite & Profile Architecture (`.agent/skills/`)

See [`.agent/skills/README.md`](.agent/skills/README.md) for the chassis/profile separation contract.

| Component | Path | Responsibility |
| :--- | :--- | :--- |
| **`plugin.json`** | `plugin.json` (`rules/AGENTS.md` + `skills/`) | Antigravity Plugin manifest bundling `rules/AGENTS.md`, `assets/logo.svg`, starter prompts, and all 5 skills. |
| **`profile-antigravity`** | `.agent/skills/vibe-coder/profiles/profile-antigravity.md` | Default production profile (`max_patch_size: 50`, `surgical-unified-diff`, `strict` type safety, pause-and-wait gates at Phases 3, 4, 6). |
| **`profile-automation`** | `.agent/skills/vibe-coder/profiles/profile-automation.md` | Unattended scheduled profile (`gate_behavior: advisory`, report-only mode) for Antigravity Automations. |
| **`_schema.md`** | `.agent/skills/vibe-coder/profiles/_schema.md` | Schema contract for custom profiles created via `aos-create-profile <name>`. |
| **`vibe-coder`** | `.agent/skills/vibe-coder/SKILL.md` | Master orchestrator running the 7-Phase FDD loop, branch cleanup/isolation, `decision.md` logging, and Draft PR hand-off. |
| **`aos-audit-project`** | `.agent/skills/aos-audit-project/SKILL.md` | Audits any project against architectural expectations, proposes optimizations, and writes `aos-audit.md`. |
| **`aos-vibecode`** | `.agent/skills/aos-vibecode/SKILL.md` | Consumes `max_patch_size` and `patch_strategy` to implement `initiative.md` and `plan.md` in atomic micro-patches. |
| **`aos-verify`** | `.agent/skills/aos-verify/SKILL.md` | Consumes `type_safety` and `review_depth` to run lint, build, 3-point static review, and unit tests. |
| **`aos-check-for-security-issues`** | `.agent/skills/aos-check-for-security-issues/SKILL.md` | Security audit inspecting dependencies, secrets, input validation, and security rules prior to commit. |

---

## Required Repository Metadata

Every repository governed by `vibe-coder` maintains:
- `README.md` — Pitch, install/update guide, prompts, 5-badge header row, and community footer.
- `Architecture.md` — System diagram, skill/profile table, metadata contract, and engineering benchmarks.
- `initiative.md` — Initial seed prompt, product brief, and reference architecture goals.
- `dev.md` — Prerequisites, custom AI model profiles, environment variables, standard scripts, and workflow.
- `decision.md` (or `docs/decisions.md`) — Reverse-chronological ADR ledger (newest at top) using `[DD.MM.YYYY]` dates.
- `AGENTS.md` & `ai-rules.json` — Strict Git branching, execution discipline, and Conventional Commits rules.
- `docs/feature/[feature-name]/plan.md` — 7-Phase FDD execution checklist and micro-feature breakdown.
- `package.json` *(Node.js/TS repos only)* — Standardized author metadata, keywords, repository link, and scripts (`dev`, `build`, `test`, `test:unit`, `lint`). Non-Node projects (`pyproject.toml`, `go.mod`, `Cargo.toml`, `Package.swift`, `build.gradle`) use their native manifest and test runner.

---

## Reference Benchmark (`stefanasemota` Projects)

- **Shift-Left Repository Pattern:** Strict separation between UI components (`src/app/`, `src/components/`) and data repositories (`src/repositories/`).
- **Conventional Commits (`AGENTS.md`):** Enforced semantic commit prefixes (`feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `style`, `perf`).
- **Quality Gates:** Unit testing (> 90% target coverage on repositories/lib), E2E separation, and zero-warning lint enforcement.
- **Defensive Security:** Strict `.gitignore` exclusions for `.env*`, `*service-account*.json`, and `*key*.json`.
