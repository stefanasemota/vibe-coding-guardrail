---
name: aos-vibecode-update
description: Updates the Vibe Coding Guardrail Antigravity plugin, runs on-demand Git branch pruning and obsolete merged branch cleanup, and syncs AGENTS.md across the current project or all git repositories in a parent folder. Use when the user runs /aos-vibecode-update, asks to update vibe-coder, or wants to clean up merged branches.
---

# `aos-vibecode-update` — Plugin Updater & On-Demand Git Hygiene

## 1. Update the Global Antigravity Plugin
1. Resolve the plugin root (`~/.gemini/config/plugins/vibe-coding-guardrail`, or the current repository if inside `vibe-coding-guardrail`).
   ```bash
   git -C "<plugin-root>" pull origin main
   python3 -c 'import json, pathlib; print(json.loads(pathlib.Path("plugin.json").read_text())["version"])'
   ```

---

## 2. On-Demand Obsolete Git Branch Cleanup
Remote network operations and branch deletions live here (never at `SessionStart` so offline/sandboxed sessions stay fast and read-only):

1. Prune stale remote tracking refs:
   ```bash
   git fetch --prune
   ```
2. Delete **local** branches already merged into the base branch (`main`/`master`/`development`), excluding protected branches (`main`, `master`, `development`, `develop`) and the currently checked-out branch:
   ```bash
   git branch --merged main | grep -Ev '^\*|^\s*(main|master|development|develop)$' | xargs -r git branch -d
   ```
3. List merged **remote** (`origin/*`) branches (excluding `HEAD` and protected branches) and **prompt for explicit human confirmation** before deleting (`git push origin --delete <branch>`). Skip remote deletion in unattended `advisory` runs.

---

## 3. Sync Target Project(s)
When updating a single repository or all git repositories under a parent folder (e.g., `~/Developer`):


---

## 4. Session Termination
Read `version` from `plugin.json` and end the response with:
`Guardrail: aos Vibe Coding Guardrail v<version> | Skill: aos-vibecode-update`
*(Only append `| Tokens: <exact count or "N/A (not exposed by runtime)">` when `VIBE_CODER_SHOW_TOKENS=true`; default `false`.)*
