# 🛡️ Vibe Coding Guardrail (`vibe-coder`)

[![Protocol](https://img.shields.io/badge/protocol-vibe--coder%20%7C%207--Phase%20FDD-blue.svg)](.agent/skills/vibe-coder/SKILL.md)
[![Benchmark](https://img.shields.io/badge/benchmark-stefanasemota-0F172A.svg)](https://github.com/stefanasemota/vibe-coding-guardrail)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**Vibe Coding Guardrail** is a standardized agentic orchestration framework and skill suite for rapid prototyping and disciplined 7-Phase Feature-Driven Development (FDD). It pairs the speed of AI-assisted "vibe coding" with production-grade engineering guardrails proven across **stefanasemota** projects.

---

## ⚡ Run `vibe-coder` by Default Across All Projects in Antigravity

Install the skill suite once into your global `~/.gemini/antigravity/skills/` directory so `vibe-coder` and all `aos-*` sub-skills run by default across **every project session** in Google Antigravity:

```bash
mkdir -p ~/.gemini/antigravity/skills
cp -R .agent/skills/* ~/.gemini/antigravity/skills/
```

To install the skills and commit rules (`AGENTS.md`) directly into a specific repository workspace instead:

```bash
npx github:stefanasemota/vibe-coding-guardrail /path/to/your-project
```

---

## 🏗️ Architectural Summary

The guardrail enforces a **7-Phase Feature-Driven Development (FDD) Loop** with explicit gateway checkpoints (Phases 3, 4, and 6) via `.agent/skills/vibe-coder/SKILL.md` and four coordinated sub-skills:

```
                      ┌──────────────────────────┐
                      │  7-Phase FDD Orchestrator│
                      │      (vibe-coder)        │
                      └────────────┬─────────────┘
                                   │
       ┌───────────────────┬───────┴───────────┬────────────────────┐
       ▼                   ▼                   ▼                    ▼
┌─────────────────┐ ┌─────────────────┐ ┌─────────────┐ ┌──────────────────┐
│aos-audit-project│ │  aos-vibecode   │ │ aos-verify  │ │aos-check-for-    │
│ (Audit & Fix)   │ │ (Implementation)│ │ (Validation)│ │security-issues   │
└─────────────────┘ └─────────────────┘ └─────────────┘ └──────────────────┘
       │                   │                   │                    │
       └───────────────────┴───────┬───────────┴────────────────────┘
                                   ▼
                      ┌──────────────────────────┐
                      │   Session Termination    │
                      │(decision.md + Draft PR)  │
                      └──────────────────────────┘
```

### Skill Suite (`.agent/skills/`)
| Skill | Path | Responsibility |
| :--- | :--- | :--- |
| **`vibe-coder`** | `.agent/skills/vibe-coder/SKILL.md` | Master orchestrator running the 7-Phase FDD loop, scaffolding checks, Git branch isolation, `decision.md` logging, and Draft PR hand-off. |
| **`aos-audit-project`** | `.agent/skills/aos-audit-project/SKILL.md` | Audits any project against Architectural Summary expectations, proposes optimizations, asks which to apply, and writes `aos-audit.md`. |
| **`aos-vibecode`** | `.agent/skills/aos-vibecode/SKILL.md` | Translates `initiative.md` and `docs/feature/[feature-name]/plan.md` into atomic FDD micro-patches (≤ 50 lines) while preserving runtime state. |
| **`aos-verify`** | `.agent/skills/aos-verify/SKILL.md` | Executes lint, build, 3-point static review, and automated unit test checks before completion. |
| **`aos-check-for-security-issues`** | `.agent/skills/aos-check-for-security-issues/SKILL.md` | Audits dependencies, secrets, input validation, and security rules prior to commit. |

### Required Repository Metadata
Every repository governed by `vibe-coder` maintains:
- `README.md` — High-level pitch, architectural summary, quick-start commands, runtime scripts, and standard community attribution footer.
- `initiative.md` — Initial seed prompt, product brief, and reference architecture goals.
- `dev.md` — Antigravity installation guide, local development environment setup, environment variable specs, and execution instructions.
- `decision.md` (or `docs/decisions.md`) — Immutable chronological ledger of architectural, UX, and implementation choices.
- `docs/feature/[feature-name]/plan.md` — 7-Phase FDD execution checklist and micro-feature breakdown.
- `package.json` — Standardized author metadata, keywords, repository link, and scripts (`dev`, `build`, `test`, `test:unit`, `lint`).

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

---

Powered by <a href="https://github.com/stefanasemota/vibe-coding-guardrail">aos Vibe Coding Guardrail</a> | Fuel the Project - Buy me a coffee: <a href="https://buymeacoffee.com/stephanasex">https://buymeacoffee.com/stephanasex</a>
