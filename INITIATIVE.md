# INITIATIVE.md — `vibe-coding-guardrail` v2.0 (Antigravity-Native Python Refactor)

## 1. Objective & Scope Reduction
Refactor `vibe-coding-guardrail` from v1.3.1 (Node.js multi-engine framework) into **v2.0**: a minimal, zero-dependency **Python 3.9+ / 3.11+** plugin built natively for **Google Antigravity**.

### What Was Removed
- Node.js runtime dependency (`package.json`, `package-lock.json`, `.nvmrc`, `tests/guardrail.test.mjs`).
- Custom distribution and profile CLIs (`bin/init-guardrail.mjs`, `bin/aos-create-profile.mjs`) in favor of Antigravity's native plugin system (`plugin.json` installed to `~/.gemini/config/plugins/` or `.agents/plugins/`).
- Multi-vendor abstraction layers (`ai-rules.json`, `_schema.md`, and custom profile scaffolding).

### What Is Preserved
- All core guardrails: Git branch isolation, immutable reverse-chronological `[DD.MM.YYYY]` ADR ledger (`decision.md`, preserving all 17 historical ADRs), security & project audits, and scheduled unattended automation support.
- Portable `SKILL.md` definitions under `skills/`.

---

## 2. Core v2.0 Architecture

### 1. Deterministic Python Lifecycle Hooks (`hooks.json` + `hooks/*.py`)
Deterministic enforcement runs natively via Antigravity lifecycle hooks (`hooks.json` at plugin root, communicating via JSON over `stdin`/`stdout`):
- **`hooks/session_start.py` (`SessionStart`):** 100% local and read-only. Never runs `git fetch --prune` or mutates `.git/` at startup. Checks `git branch --show-current` and warns if on a protected branch (`main`/`master`/`development`/`develop`) or a branch already merged into local `main`/`master`. Remote pruning and obsolete branch cleanup live in `aos-vibecode-update`.
- **`hooks/branch_guard.py` (`PreToolUse`):** Intercepts `run_command` git commit/push calls and deterministically blocks direct writes to `main`/`master` as well as `--no-verify` hook bypasses.
- **`hooks/adr_check.py` (`Stop`):** When `decision.md` was modified during the session, verifies reverse-chronological `[DD.MM.YYYY]` headings and required ADR fields (`Origin`, `Context`, `Decision`, `Impact`).

### 2. Compressed 3-Stage Orchestrator (`skills/vibe-coder/SKILL.md`)
1. **Stage 1 — Scope & Plan:** Inspect repo, confirm branch isolation, draft `docs/feature/<slug>/plan.md`. Single configurable gate: `pause` (default interactive) vs `advisory` (non-blocking scheduled audits).
2. **Stage 2 — Build & Verify:** Implement atomic increments (`aos-vibecode`), run native checks (`aos-verify`), and log architectural decisions in `decision.md`.
3. **Stage 3 — Audit & PR:** Run security checks (`aos-check-for-security-issues`) and open a Draft PR.

### 3. Single Source of Truth Enforcement (`tests/test_guardrail.py`)
Zero-dependency Python `unittest` suite (`python3 -m unittest discover -s tests -v`) scanning `skills/*/SKILL.md` on disk as the sole source of truth and asserting zero drift across `plugin.json`, `README.md`, and `Architecture.md`, plus full unit tests for all three hooks and `decision.md`.
