---
name: caveman-compress
description: >
  Locally compress a natural-language memory or notes file into caveman format
  to save input tokens without external CLIs or telemetry. Trigger: /caveman-compress.
---

# Caveman Compress

> *Vendored from [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) (Apache-2.0, see [`LICENSE`](./LICENSE)). Adapted for 100% local, zero-telemetry Antigravity execution — no external CLI, proxy binary, or third-party provider scripts.*

## Purpose

Compress natural-language files (notes, todos, preferences) into terse caveman-speak to reduce input tokens while preserving all technical accuracy, code blocks, paths, and structure. Runs 100% locally using the active Antigravity agent's own file tools.

- **Secrets refusal:** Refuse to read or compress files whose names look like secrets (`.env*`, `credentials`, `secrets`, `.netrc`, `*service-account*.json`, `*key*.json`, `*.pem`) or whose contents hold credentials/private keys.
- **Backup before overwrite:** Before overwriting the target file, save a human-readable backup as `<filename>.original.md` in an out-of-tree backup directory (or confirm with the user where to store it) so skill auto-loaders do not re-ingest backups as live files.

## Guardrail Exemptions (NEVER Compress)

Refuse compression and leave the file untouched if the target matches any of these protected guardrail artifacts:
- `decision.md` (immutable ADR ledger)
- `docs/feature/*/plan.md` (implementation plans)
- Security and project audit reports (`aos-check-for-security-issues`, `aos-audit-project`, `aos-audit.md`)

## Trigger

`/caveman-compress <filepath>` or when the user asks to compress a natural-language memory/notes file.

**Requires an explicit filepath.** If the user pastes raw text instead of naming a file, do NOT improvise an inline overwrite — ask for the filepath or offer to save the text to a file first. Never leak agent reasoning or commentary into the compressed file.

## Local Process (Zero-CLI)

1. Verify `<filepath>` is an allowed natural-language file (not a secret, not a code/config file, and not a Guardrail Exemption).
2. Read the target file locally.
3. Save a readable backup before overwriting (outside skill auto-load paths).
4. Compress the prose locally following the **Compression Rules** below, leaving all code blocks, inline code, URLs, paths, commands, dates, and numbers untouched.
5. Verify the compressed output preserves every heading, code block, negation (`not`/`never`/`no`/`only`), and technical identifier, then write the compressed file and report the before/after line/word reduction.

## Compression Rules

### Remove
- Articles: a, an, the
- Filler: just, really, basically, actually, simply, essentially, generally
- Pleasantries: "sure", "certainly", "of course", "happy to", "I'd recommend"
- Hedging: "it might be worth", "you could consider", "it would be good to"
- Redundant phrasing: "in order to" → "to", "make sure to" → "ensure", "the reason is because" → "because"
- Connective fluff: "however", "furthermore", "additionally", "in addition"

### Preserve EXACTLY (never modify)
- Code blocks (fenced ``` and indented)
- Inline code (`backtick content`)
- URLs and links (full URLs, markdown links)
- File paths (`/src/components/...`, `./config.yaml`)
- Commands (`npm install`, `git commit`, `docker build`)
- Technical terms (library names, API names, protocols, algorithms)
- Proper nouns (project names, people, companies)
- Dates, version numbers, numeric values
- Environment variables (`$HOME`, `NODE_ENV`)

### Preserve Structure
- All markdown headings (keep exact heading text, compress body below)
- Bullet point hierarchy (keep nesting level)
- Numbered lists (keep numbering)
- Tables (compress cell text, keep structure)
- Frontmatter/YAML headers in markdown files

### Compress
- Use short synonyms: "big" not "extensive", "fix" not "implement a solution for", "use" not "utilize"
- Fragments OK: "Run tests before commit" not "You should always run tests before committing"
- Drop "you should", "make sure to", "remember to" — just state the action
- Merge redundant bullets that say the same thing differently
- Keep one example where multiple examples show the same pattern

CRITICAL RULE:
Anything inside ``` ... ``` must be copied EXACTLY.
Do not:
- remove comments
- remove spacing
- reorder lines
- shorten commands
- simplify anything

Inline code (`...`) must be preserved EXACTLY.
Do not modify anything inside backticks.

If file contains code blocks:
- Treat code blocks as read-only regions
- Only compress text outside them
- Do not merge sections around code

## Boundaries

- ONLY compress natural-language files (`.md`, `.txt`, `.typ`, `.typst`, `.tex`, extensionless)
- NEVER modify: `.py`, `.js`, `.ts`, `.json`, `.yaml`, `.yml`, `.toml`, `.env`, `.lock`, `.css`, `.html`, `.xml`, `.sql`, `.sh`
- NEVER compress Guardrail Exemptions (`decision.md`, `docs/feature/*/plan.md`, `aos-audit.md`, or outputs of `aos-check-for-security-issues` / `aos-audit-project`)
- If file has mixed content (prose + code), compress ONLY the prose sections
- If unsure whether something is code or prose, leave it unchanged
- Never compress `*.original.md` backup files (skip them)
