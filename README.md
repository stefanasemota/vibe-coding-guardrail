# 🛡️ Vibe Coding Guardrail (`vibe-coder`)

[![Protocol](https://img.shields.io/badge/protocol-vibe--coder-blue.svg)](.agent/skills/vibe-coder/SKILL.md)
[![Benchmark](https://img.shields.io/badge/benchmark-stefanasemota-0F172A.svg)](https://github.com/stefanasemota/vibe-coding-guardrail)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Vibe Coding Guardrail** is a standardized agentic orchestration framework and skill suite for rapid prototyping and disciplined iterative delivery. It pairs the speed of AI-assisted "vibe coding" with production-grade engineering guardrails proven across **stefanasemota** projects.

---

## 🏗️ Architectural Summary

The guardrail enforces a 5-stage session protocol via `.agent/skills/vibe-coder/SKILL.md` and three coordinated sub-skills:

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

### Skill Suite (`.agent/skills/`)
| Skill | Path | Responsibility |
| :--- | :--- | :--- |
| **`vibe-coder`** | `.agent/skills/vibe-coder/SKILL.md` | Master orchestrator enforcing scaffolding, Git branch isolation, decision logging, and PR hand-off. |
| **`aos-vibecode`** | `.agent/skills/aos-vibecode/SKILL.md` | Translates `initiative.md` into micro-patches (≤ 50 lines) while preserving runtime state and architectural layers. |
| **`aos-verify`** | `.agent/skills/aos-verify/SKILL.md` | Executes lint, build, and automated unit test checks before completion. |
| **`aos-check-for-security-issues`** | `.agent/skills/aos-check-for-security-issues/SKILL.md` | Audits dependencies, secrets, input validation, and security rules prior to commit. |

### Required Repository Metadata
Every repository governed by `vibe-coder` maintains four foundational root documents:
- `README.md` — High-level pitch, architectural summary, quick-start commands, and runtime scripts.
- `initiative.md` — Initial seed prompt, product brief, and reference architecture goals.
- `dev.md` — Antigravity installation guide, local development environment setup, environment variable specs, and execution instructions.
- `decision.md` — Immutable chronological ledger of architectural, UX, and implementation choices.

---

## 🚀 Quick-Start Commands & Runtime Scripts

See [`dev.md`](dev.md) for full instructions on **how to install and use these skills with Antigravity**.

```bash
# Verify guardrail scaffolding and run automated unit tests
npm test

# Run unit test suite directly
npm run test:unit

# Lint skill definitions and project metadata
npm run lint

# Validate build / protocol readiness
npm run build

# Inspect current guardrail session status
npm run dev
```

---

## 🏛️ Reference Benchmark from stefanasemota projects

This guardrail distills engineering practices proven across **stefanasemota** projects:
- **Shift-Left Repository Pattern:** Strict separation between UI components (`src/app/`, `src/components/`) and data repositories (`src/repositories/`).
- **Conventional Commits (`AGENTS.md`):** Enforced semantic commit prefixes (`feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `style`, `perf`).
- **Quality Gates:** Vitest unit testing (> 90% target coverage on repositories/lib), Cucumber/Playwright E2E separation, and zero-warning ESLint enforcement.
- **Defensive Security:** Strict `.gitignore` exclusions for `.env*`, `*service-account*.json`, and `*key*.json`.
