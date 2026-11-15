# 🛡️ Vibe Coding Guardrail (`vibe-coder`)

[![Version](https://img.shields.io/badge/version-1.2.1-blue.svg)](https://github.com/stefanasemota/vibe-coding-guardrail)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/stefanasemota/vibe-coding-guardrail)
[![Firebase](https://img.shields.io/badge/Firebase-Firestore%20%7C%20Auth%20%7C%20Hosting-FFCA28?logo=firebase&logoColor=white)]()
[![Gemini](https://img.shields.io/badge/Gemini-AI%20Powered-8E75B2?logo=google-gemini&logoColor=white)]()

**Vibe Coding Guardrail** is a standardized agentic orchestration framework and skill suite for rapid prototyping and disciplined 7-Phase Feature-Driven Development (FDD). It pairs the speed of AI-assisted "vibe coding" with production-grade engineering guardrails proven across **stefanasemota** projects.

---

## ⚡ Run `vibe-coder` by Default Across All Projects in Antigravity

### Option 1: Install as a Global Antigravity Plugin (`plugin.json` — Recommended)
This repository ships as a complete, language-agnostic **Antigravity Plugin** ([`plugin.json`](plugin.json)) bundling `rules/AGENTS.md` + all 5 `skills/` as a single unit. Symlink the repository into `~/.gemini/config/plugins/` (and `~/.gemini/antigravity/skills/` / `~/.gemini/config/skills/`) so both the `AGENTS.md` rules and all 5 skills are active across **every project** (Node.js, Python, Go, Rust, Swift/Xcode, Android) without requiring a `package.json` in the target repo:

```bash
mkdir -p ~/.gemini/config/plugins ~/.gemini/antigravity/skills ~/.gemini/config/skills
ln -sfn "$(pwd)" ~/.gemini/config/plugins/vibe-coding-guardrail
ln -sfn "$(pwd)/.agent/skills/"* ~/.gemini/antigravity/skills/
ln -sfn "$(pwd)/.agent/skills/"* ~/.gemini/config/skills/
```

### Option 2: Install into a Specific Workspace
To copy `.agent/skills/`, `AGENTS.md`, and `ai-rules.json` directly into a single repository workspace instead:

```bash
npx github:stefanasemota/vibe-coding-guardrail /path/to/your-project
```

> **Updating Projects Previously Audited with an Older Version:**
> 1. Remove any stale local `.agent/skills/` copy inside that project (`rm -rf /path/to/project/.agent/skills`) so it uses your live global plugin/skills.
> 2. Open a new chat in that project and run:
>    `Run aos-audit-project: audit this repository against the Architectural Summary, migrate decision.md and aos-audit.md dates to DD.MM.YYYY with newest entries at the top, and ask which changes to apply.`

---

## 🏗️ Architectural Summary

The guardrail decouples the **Engine-Neutral 7-Phase FDD Workflow Chassis** (`vibe-coder` + four `aos-*` sub-skills) from the **Interchangeable Engine Profile** ([`.agent/skills/vibe-coder/profiles/profile-antigravity.md`](.agent/skills/vibe-coder/profiles/profile-antigravity.md), validated by [`_schema.md`](.agent/skills/vibe-coder/profiles/_schema.md)):

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

### Skill Suite & Profile Architecture (`.agent/skills/`)
See [`.agent/skills/README.md`](.agent/skills/README.md) for full details on the separation between the workflow chassis and engine profiles.

| Component | Path | Responsibility |
| :--- | :--- | :--- |
| **`plugin.json`** | `plugin.json` (`rules/AGENTS.md` + `skills/`) | Antigravity Plugin manifest bundling `rules/AGENTS.md`, `assets/logo.svg`, starter prompts, and all 5 skills into a single toggleable unit. |
| **`profile-antigravity`** | `.agent/skills/vibe-coder/profiles/profile-antigravity.md` | Default production engine profile (`max_patch_size: 50`, `surgical-unified-diff`, `strict` type safety, pause-and-wait gates at Phases 3, 4, 6). |
| **`profile-automation`** | `.agent/skills/vibe-coder/profiles/profile-automation.md` | Unattended scheduled automation profile (`gate_behavior: advisory`, report-only mode) for background runs in the Antigravity Automations tab. |
| **`_schema.md`** | `.agent/skills/vibe-coder/profiles/_schema.md` | Schema contract for custom profiles created via `aos-create-profile <name>`. |
| **`vibe-coder`** | `.agent/skills/vibe-coder/SKILL.md` | Engine-neutral master orchestrator running the 7-Phase FDD loop, scaffolding checks, Git branch isolation, `decision.md` logging, and Draft PR hand-off. |
| **`aos-audit-project`** | `.agent/skills/aos-audit-project/SKILL.md` | Audits any project against Architectural Summary expectations, proposes optimizations, asks which to apply, and writes `aos-audit.md`. |
| **`aos-vibecode`** | `.agent/skills/aos-vibecode/SKILL.md` | Consumes `max_patch_size` and `patch_strategy` from the active profile to translate `initiative.md` and `plan.md` into surgical micro-patches. |
| **`aos-verify`** | `.agent/skills/aos-verify/SKILL.md` | Consumes `type_safety` and `review_depth` to execute lint, build, 3-point static review, and automated unit test checks. |
| **`aos-check-for-security-issues`** | `.agent/skills/aos-check-for-security-issues/SKILL.md` | Engine-neutral security audit inspecting dependencies, secrets, input sanitization, and security rules prior to commit. |

### Required Repository Metadata
Every repository governed by `vibe-coder` maintains:
- `README.md` — High-level pitch, architectural summary, quick-start commands, runtime scripts, 5-badge header row, and standard community attribution footer.
- `initiative.md` — Initial seed prompt, product brief, and reference architecture goals.
- `dev.md` — Antigravity installation guide, local development environment setup, environment variable specs, and execution instructions.
- `decision.md` (or `docs/decisions.md`) — Reverse-chronological ledger (newest at top, oldest at bottom) of architectural, UX, and implementation choices using `[DD.MM.YYYY]` dates.
- `AGENTS.md` & `ai-rules.json` — Strict AI workflow, Git branching, execution discipline, and Conventional Commits rules (Markdown + vendor-neutral JSON).
- `docs/feature/[feature-name]/plan.md` — 7-Phase FDD execution checklist and micro-feature breakdown.
- `package.json` *(Stack-Aware — Node.js/TS repos only)* — Standardized author metadata, keywords, repository link, scripts (`dev`, `build`, `test`, `test:unit`, `lint`), and optional `vibe-coding-guardrail` devDependency. Non-Node projects (`pyproject.toml`, `go.mod`, `Cargo.toml`, `Package.swift`, `build.gradle`) use their native manifest and test runner.

---

## 💬 How to Use in Antigravity (Copy-Paste Prompts)

Use these simple, ready-to-copy prompts in the Google Antigravity chat pane to trigger the **7-Phase FDD Orchestrator** (`vibe-coder`) or any individual sub-skill:

### 1. `vibe-coder` (Full 7-Phase FDD Orchestrator)
```text
Start a vibe-coder session: [describe your feature, fix, or new project idea].
```

### 2. `aos-audit-project` (Audit & Optimize Repository Structure)
```text
Run aos-audit-project: audit this repository against the Architectural Summary, show the optimization summary, and ask which changes to apply.
```

### 3. `aos-vibecode` (Rapid Micro-Patch Implementation)
```text
Run aos-vibecode: implement [feature or task] from initiative.md in atomic micro-patches without breaking existing routes or state.
```

### 4. `aos-verify` (Sanity, Lint, Build & Unit Test Gate)
```text
Run aos-verify: validate imports, TypeScript types, zero-warning lint rules, unit tests, and the production build.
```

### 5. `aos-check-for-security-issues` (Defensive Security Audit)
```text
Run aos-check-for-security-issues: scan staged changes and dependencies for hardcoded secrets, missing input validation, or insecure rules before committing.
```

---

## ⏱️ Weekly Wednesday Automations (Antigravity Automations Tab)

Use [`profile-automation.md`](.agent/skills/vibe-coder/profiles/profile-automation.md) (`$PROFILE=automation`, `gate_behavior: advisory`) to run unattended background guardrails in the Antigravity **Automations** tab once a week **every Wednesday**:

### 1. Weekly Architecture Drift Audit (`aos-audit-project` — Every Wednesday)
Paste into Antigravity chat (or trigger via `/schedule`):
```text
/schedule Every Wednesday at 09:00, run aos-audit-project with $PROFILE=automation: audit this repository against the Architectural Summary and update aos-audit.md without modifying application code.
```

### 2. Weekly Security & Secret Sweep (`aos-check-for-security-issues` — Every Wednesday)
Paste into Antigravity chat (or trigger via `/schedule`):
```text
/schedule Every Wednesday at 09:30, run aos-check-for-security-issues with $PROFILE=automation: scan the repository and dependencies for hardcoded secrets, missing .gitignore exclusions, or insecure rules and summarize findings.
```

---

## 🧩 Creating a Custom Profile for a Particular AI Model

You can create a custom Engine Profile tailored to any AI model (for example `claude-sonnet` or `gemini-flash`) using the built-in `aos-create-profile` utility:

```bash
# Option 1: Interactive CLI prompt
npx aos-create-profile claude-sonnet

# Option 2: Non-interactive CLI with model-specific parameters
node bin/aos-create-profile.mjs gemini-flash \
  --max-patch-size=30 \
  --review-depth=quick-lint \
  --gate-behavior=explicit-pause-and-wait \
  --execution-mode=sequential-multi-turn
```

This generates `.agent/skills/vibe-coder/profiles/profile-gemini-flash.md` adhering to [`_schema.md`](.agent/skills/vibe-coder/profiles/_schema.md):

```markdown
---
engine_name: "gemini-flash"
execution_mode: "sequential-multi-turn"
max_patch_size: 30
patch_strategy: "surgical-unified-diff"
type_safety: "strict"
gate_behavior: "explicit-pause-and-wait"
review_depth: "quick-lint"
---
```

Activate your custom model profile in any session by passing `$PROFILE=<name>`:
```text
Start a vibe-coder session with $PROFILE=gemini-flash: implement the user notification preferences panel.
```

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
