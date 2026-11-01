# 🛡️ AOS Skill Suite: Engine-Neutral Workflow Chassis & Engine Profiles

The `.agent/skills/` suite separates the **7-Phase FDD Workflow Chassis** (where the human is the driver) from the **Interchangeable Engine Profile** (where model-specific execution limits live).

---

## 1. Architecture & Separation of Concerns

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
                      │    (decision.md + Draft PR)      │
                      └──────────────────────────────────┘
```

### Workflow Chassis vs. Engine Profile
| Layer | Path | Responsibility |
| :--- | :--- | :--- |
| **Profile Schema Contract** | `vibe-coder/profiles/_schema.md` | Defines the 7 required profile fields (`engine_name`, `execution_mode`, `max_patch_size`, `patch_strategy`, `type_safety`, `gate_behavior`, `review_depth`). |
| **Default Production Profile** | `vibe-coder/profiles/profile-antigravity.md` | High-rigor baseline (`max_patch_size: 50`, `surgical-unified-diff`, `strict` type safety, `explicit-pause-and-wait` at Phases 3, 4, 6). |
| **Neutral Orchestrator** | `vibe-coder/SKILL.md` | Resolves the active profile (`profile-antigravity.md` or `$PROFILE`) and drives the 7-phase FDD loop, Git branch isolation, `decision.md` (`[DD.MM.YYYY]`), and Draft PR hand-off. |
| **Project Auditor** | `aos-audit-project/SKILL.md` | Audits any project against architectural summary expectations and generates `aos-audit.md`. |
| **Rapid Feature Delivery** | `aos-vibecode/SKILL.md` | Consumes `max_patch_size` and `patch_strategy` from the active profile to apply surgical micro-patches from `initiative.md` and `docs/feature/<name>/plan.md`. |
| **Verification Gate** | `aos-verify/SKILL.md` | Consumes `type_safety` and `review_depth` to run project-native linters, builds, unit tests, and 3-point static checks. |
| **Security Gate** | `aos-check-for-security-issues/SKILL.md` | Runs an engine-neutral security pass across secrets, `.gitignore`, boundaries, schemas, and dependencies. |

---

## 2. Scaffolding a Custom Engine Profile (`aos-create-profile`)

Generate a new profile adhering to `vibe-coder/profiles/_schema.md` via CLI or agent prompt:

```bash
npx aos-create-profile <name>
# or
node bin/aos-create-profile.mjs <name>
```
