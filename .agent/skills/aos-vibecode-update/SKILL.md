---
name: aos-vibecode-update
description: Updates the Vibe Coding Guardrail global plugin, refreshes skill symlinks, and updates AGENTS.md/ai-rules.json across the current project or all git repositories in a parent folder. Use when the user runs /aos-vibecode-update or asks to update vibe-coder.
---

# `aos-vibecode-update` — Plugin & Workspace Updater

## Active Profile Consumption
Respect `gate_behavior` from [`../vibe-coder/profiles/profile-antigravity.md`](../vibe-coder/profiles/profile-antigravity.md) (or active `$PROFILE`).

## Update Steps

1. **Pull Latest Plugin & Refresh Global Symlinks:**
   - Resolve the plugin root (`~/.gemini/config/plugins/vibe-coding-guardrail`, or the current repository if inside `vibe-coding-guardrail`).
   - Run `git -C <plugin-root> pull origin main` and read `version` from `plugin.json`.
   - Refresh global skill symlinks:
     ```bash
     ln -sfn "<plugin-root>/.agent/skills/"* ~/.gemini/antigravity/skills/
     ln -sfn "<plugin-root>/.agent/skills/"* ~/.gemini/config/skills/
     ```

2. **Update Target Project(s):**
   - **Parent folder (multiple git repos, e.g. `~/Developer`):**
     - Global Plugin mode: `node "<plugin-root>/bin/init-guardrail.mjs" --all --clean-local-skills .`
     - Workspace Copy mode: `node "<plugin-root>/bin/init-guardrail.mjs" --all .`
   - **Single project:**
     - Global Plugin mode: remove stale `.agent/skills/` if present, then refresh `AGENTS.md` and `ai-rules.json` from `<plugin-root>`.
     - Workspace Copy mode: `node "<plugin-root>/bin/init-guardrail.mjs" .`

3. **Optional Doc Alignment:**
   - Report the updated version and modified projects, and ask if the user wants to run `aos-audit-project` to align `decision.md`, `Architecture.md`, and `README.md`.

4. **Session Termination:**
   - End the response by reading `version` from `plugin.json` (or `package.json`) and outputting:
     `Guardrail: aos Vibe Coding Guardrail v<version> | Skill: aos-vibecode-update | Tokens: <exact count if exposed by runtime, otherwise "N/A (not exposed by runtime)">`
