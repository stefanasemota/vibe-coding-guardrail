# 🛠️ Developer & Operations Guide (`dev.md`)

Local setup, hook testing, and operational workflow for **Vibe Coding Guardrail v2.0** (`vibe-coder`).

---

## 1. Prerequisites

- **Python:** `3.9+` (tested on macOS system Python 3.9+ and Python 3.11+ — **zero external dependencies**, stdlib only)
- **Git:** `>= 2.39` with GitHub CLI (`gh`) authenticated for Draft PR creation
- **Antigravity:** IDE or CLI with native plugin discovery enabled

---

## 2. Installation & Updates

### Install as a Native Global Plugin
```bash
mkdir -p ~/.gemini/config/plugins
ln -sfn "$(pwd)" ~/.gemini/config/plugins/vibe-coding-guardrail
```

### Update Plugin & Sync Reference Projects
Run `/aos-vibecode-update` in Antigravity chat to:
1. Pull `origin/main` in `~/.gemini/config/plugins/vibe-coding-guardrail`.
2. Run on-demand `git fetch --prune` and clean up merged local/remote branches.
3. Remove stale local `.agent/skills/` overrides and refresh `AGENTS.md` across your projects.

Check the active plugin version at any time:
```bash
python3 -c 'import json, pathlib; print(json.loads(pathlib.Path("plugin.json").read_text())["version"])'
```

---

## 3. Running Tests & Validating Hooks

Run the full zero-dependency Python `unittest` suite:

```bash
python3 -m unittest discover -s tests -v
```

Manually smoke-test any hook over `stdin`/`stdout`:

```bash
# SessionStart (read-only local branch check)
echo '{"cwd": "."}' | python3 ./hooks/session_start.py

# PreToolUse (branch guard)
echo '{"cwd": ".", "toolCall": {"name": "run_command", "args": {"CommandLine": "git push origin main"}}}' | python3 ./hooks/branch_guard.py

# Stop (ADR format check on modified decision.md)
echo '{"cwd": ".", "continuationActive": false}' | python3 ./hooks/adr_check.py
```

---

## 4. Environment Variables (Reference Full-Stack Apps)

For full-stack Next.js + Firebase + Genkit reference apps governed by this plugin, keep secrets in `.env.local` (never committed to Git) and confirm `.gitignore` excludes `.env*`, `*service-account*.json`, `*key*.json`, and `*.pem`.

---

## 5. 3-Stage Session Workflow

1. **Stage 1 — Scope & Plan:** Confirm isolated branch (checked by `hooks/session_start.py`), inspect repo, draft `docs/feature/<slug>/plan.md`, and wait for approval in `pause` mode (or continue directly in `advisory` mode).
2. **Stage 2 — Build & Verify:** Implement atomic increments (`aos-vibecode`), run native tests/lint (`aos-verify`), and prepend `[DD.MM.YYYY]` ADRs to `decision.md`.
3. **Stage 3 — Audit & PR:** Run `aos-check-for-security-issues`, push the branch (protected by `hooks/branch_guard.py`), open a Draft PR (`gh pr create --draft`), and let `hooks/adr_check.py` verify `decision.md`.
