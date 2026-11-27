# 🛡️ Vibe Coding Guardrail (`vibe-coder`)

[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)](https://github.com/stefanasemota/vibe-coding-guardrail)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://github.com/stefanasemota/vibe-coding-guardrail)
[![Python](https://img.shields.io/badge/Python-3.9%2B%20stdlib--only-3776AB?logo=python&logoColor=white)]()
[![Gemini](https://img.shields.io/badge/Antigravity-Native%20Plugin-8E75B2?logo=google-gemini&logoColor=white)]()

**Vibe Coding Guardrail** is a zero-dependency Python plugin built natively for **Google Antigravity**. It combines deterministic lifecycle hooks (`hooks.json`), a lean **3-Stage Loop**, and **6 skills** to keep AI-assisted coding fast, isolated, and auditable across any language stack.

---

## ⚡ Install as a Native Antigravity Plugin

Symlink this repository into `~/.gemini/config/plugins/` so `plugin.json`, `hooks.json`, `rules/AGENTS.md`, and all **6 skills** activate automatically in **every workspace**:

```bash
mkdir -p ~/.gemini/config/plugins
ln -sfn "$(pwd)" ~/.gemini/config/plugins/vibe-coding-guardrail
```

> **Upgrading from v1.x?** Remove legacy loose symlinks in `~/.gemini/config/skills/` and `~/.gemini/antigravity/skills/` that pointed to `.agent/skills/`, then run `/aos-vibecode-update` to sync `AGENTS.md` and remove stale workspace `.agent/skills/` overrides.

---

## 🔁 The 3-Stage Loop & Deterministic Hooks

| Stage | Goal | Gate / Enforcement |
| :--- | :--- | :--- |
| **Stage 1 — Scope & Plan** | Inspect repo, confirm isolated branch, draft `docs/feature/<slug>/plan.md` | Single configurable gate: `pause` (interactive default) or `advisory` (unattended audits) |
| **Stage 2 — Build & Verify** | Atomic micro-patches (`aos-vibecode`), native tests (`aos-verify`), `decision.md` ADR | `hooks/branch_guard.py` (`PreToolUse`) blocks direct commits/pushes to `main`/`master` |
| **Stage 3 — Audit & PR** | Security sweep (`aos-check-for-security-issues`), Conventional Commits, Draft PR | `hooks/adr_check.py` (`Stop`) validates reverse-chronological `[DD.MM.YYYY]` ADRs |

### Lifecycle Hooks (`hooks.json`)
- **`hooks/session_start.py` (`SessionStart`):** 100% local and read-only branch check (never runs `git fetch` or mutates `.git/`). Warns if on a protected or already-merged branch.
- **`hooks/branch_guard.py` (`PreToolUse`):** Deterministically blocks `git commit`/`git push` to `main`/`master` and `--no-verify` bypasses.
- **`hooks/adr_check.py` (`Stop`):** Validates `[DD.MM.YYYY]` reverse-chronological ordering and required fields (`Origin`, `Context`, `Decision`, `Impact`) whenever `decision.md` is modified.

See [`Architecture.md`](Architecture.md) for the full v2.0 diagram and repository structure.

---

## 💬 Skills Included (6 Skills)

1. **`vibe-coder`** — 3-Stage orchestrator with a single configurable gate (`pause` vs `advisory`):
   ```text
   Start a vibe-coder session: [describe your feature, fix, or refactor].
   ```
2. **`aos-vibecode`** — Atomic micro-patch implementation (`<= 50` lines per logical unit):
   ```text
   Run aos-vibecode: implement [feature] from INITIATIVE.md in atomic micro-patches.
   ```
3. **`aos-verify`** — Stack-aware lint, typecheck, 3-point static audit, unit tests, and build gate:
   ```text
   Run aos-verify: validate lint rules, types, unit tests, and build.
   ```
4. **`aos-check-for-security-issues`** — Defensive security sweep (secrets, `.gitignore`, boundaries, CVEs):
   ```text
   Run aos-check-for-security-issues: scan staged changes and dependencies for secrets or vulnerabilities.
   ```
5. **`aos-audit-project`** — Repository structure & metadata auditor (`aos-audit.md`):
   ```text
   Run aos-audit-project: audit this repository against Architecture.md and ask which optimizations to apply.
   ```
6. **`aos-vibecode-update`** — Plugin updater, on-demand `git fetch --prune` + merged branch cleanup, and project `AGENTS.md` sync:
   ```text
   /aos-vibecode-update
   ```

---

## ⏱️ Weekly Wednesday Automations (`advisory` Mode)

- **Every Wednesday at 09:00 (`aos-audit-project`):**
  ```text
  /schedule Every Wednesday at 09:00, run aos-audit-project in advisory mode: audit this repository against Architecture.md and update aos-audit.md without modifying application code.
  ```
- **Every Wednesday at 09:30 (`aos-check-for-security-issues`):**
  ```text
  /schedule Every Wednesday at 09:30, run aos-check-for-security-issues in advisory mode: scan the repository and dependencies for hardcoded secrets, missing .gitignore exclusions, or insecure rules and summarize findings.
  ```

---

## 🧪 Verification & Developer Guide

Run the zero-dependency Python test suite (skill-drift check + hook unit tests):

```bash
python3 -m unittest discover -s tests -v
```

See [`dev.md`](dev.md) for local setup, hook testing, and operational guidelines.

---

Powered by <a href="https://github.com/stefanasemota/vibe-coding-guardrail">aos Vibe Coding Guardrail</a> | Fuel the Project - Buy me a coffee: <a href="https://buymeacoffee.com/stephanasex">https://buymeacoffee.com/stephanasex</a>
