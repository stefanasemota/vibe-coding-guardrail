# 🛡️ Vibe Coding Guardrail (`vibe-coder`)

[![Version](https://img.shields.io/badge/version-1.2.1-blue.svg)](https://github.com/stefanasemota/vibe-coding-guardrail)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/stefanasemota/vibe-coding-guardrail)
[![Firebase](https://img.shields.io/badge/Firebase-Firestore%20%7C%20Auth%20%7C%20Hosting-FFCA28?logo=firebase&logoColor=white)]()
[![Gemini](https://img.shields.io/badge/Gemini-AI%20Powered-8E75B2?logo=google-gemini&logoColor=white)]()

**Vibe Coding Guardrail** is a language-agnostic Antigravity Plugin and 7-Phase Feature-Driven Development (FDD) skill suite for fast, disciplined AI-assisted coding.

---

## ⚡ Install & Run Across All Projects in Antigravity

### Option 1: Install as a Global Antigravity Plugin (`plugin.json` — Recommended)
Symlink this repository into `~/.gemini/config/plugins/` and your global skill directories so `rules/AGENTS.md` and all 5 skills are active in **every project** (Node.js, Python, Go, Rust, Swift/Xcode, Android):

```bash
mkdir -p ~/.gemini/config/plugins ~/.gemini/antigravity/skills ~/.gemini/config/skills
ln -sfn "$(pwd)" ~/.gemini/config/plugins/vibe-coding-guardrail
ln -sfn "$(pwd)/.agent/skills/"* ~/.gemini/antigravity/skills/
ln -sfn "$(pwd)/.agent/skills/"* ~/.gemini/config/skills/
```

#### Updating the Global Plugin & Verifying Your Version
Because Option 1 uses symlinks, pulling `main` updates your global plugin and skills immediately. Verify your active version at any time:

```bash
cd /path/to/vibe-coding-guardrail && git pull origin main
node -p "require('./plugin.json').version"
```

Compare against the [latest GitHub release](https://github.com/stefanasemota/vibe-coding-guardrail/releases) (or check the **Guardrail version** printed in the Session Termination footer).

#### Updating Existing Projects
1. Remove any stale local `.agent/skills/` copy inside the target project (`rm -rf /path/to/project/.agent/skills`) so it resolves the global plugin.
2. Run `aos-audit-project` in that project:
   ```text
   Run aos-audit-project: audit this repository against Architecture.md, migrate decision.md and aos-audit.md dates to DD.MM.YYYY with newest entries at the top, and ask which changes to apply.
   ```

### Option 2: Install into a Specific Workspace
Copy `.agent/skills/`, `AGENTS.md`, and `ai-rules.json` directly into a single repository:

```bash
npx github:stefanasemota/vibe-coding-guardrail /path/to/your-project
```

---

## 🏗️ Architecture

`vibe-coder` decouples the **7-Phase FDD Workflow Chassis** (`vibe-coder` + `aos-audit-project`, `aos-vibecode`, `aos-verify`, `aos-check-for-security-issues`) from the **Engine Profile** (`profile-antigravity.md`, `profile-automation.md`, or custom profiles).

See [`Architecture.md`](Architecture.md) for the full diagram, skill/profile table, required repository metadata, and engineering benchmarks.

---

## 💬 How to Use in Antigravity (Copy-Paste Prompts)

### 1. `vibe-coder` (Full 7-Phase FDD Orchestrator)
```text
Start a vibe-coder session: [describe your feature, fix, or new project idea].
```

### 2. `aos-audit-project` (Audit & Optimize Repository Structure)
```text
Run aos-audit-project: audit this repository against Architecture.md, show the optimization summary, and ask which changes to apply.
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

Use [`profile-automation.md`](.agent/skills/vibe-coder/profiles/profile-automation.md) (`$PROFILE=automation`, `gate_behavior: advisory`) for unattended weekly runs:

- **Every Wednesday at 09:00 (`aos-audit-project`):**
  ```text
  /schedule Every Wednesday at 09:00, run aos-audit-project with $PROFILE=automation: audit this repository against Architecture.md and update aos-audit.md without modifying application code.
  ```
- **Every Wednesday at 09:30 (`aos-check-for-security-issues`):**
  ```text
  /schedule Every Wednesday at 09:30, run aos-check-for-security-issues with $PROFILE=automation: scan the repository and dependencies for hardcoded secrets, missing .gitignore exclusions, or insecure rules and summarize findings.
  ```

---

## 🛠️ Developer & Operations Guide

See [`dev.md`](dev.md) for prerequisites, creating custom AI model profiles (`aos-create-profile`), environment variables, standard `package.json` scripts, and the session workflow.

---

Powered by <a href="https://github.com/stefanasemota/vibe-coding-guardrail">aos Vibe Coding Guardrail</a> | Fuel the Project - Buy me a coffee: <a href="https://buymeacoffee.com/stephanasex">https://buymeacoffee.com/stephanasex</a>
