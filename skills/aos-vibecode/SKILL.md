---
name: aos-vibecode
description: Translate product specs or user stories from INITIATIVE.md, docs/rule-book.md, and docs/feature/[feature-name]/plan.md into minimal, working code increments via atomic micro-patches while preserving runtime state and architectural boundaries. Use when implementing or patching features in Stage 2 of vibe-coder or standalone.
---

# `aos-vibecode` — Rapid Atomic Micro-Patch Delivery

## 1. Micro-Patch Implementation Loop


2. **Apply Atomic Micro-Patch:** Keep each logical diff concise (`<= 50` lines per surgical unit), preserving surrounding code and exports. Implement in sequence: types/contracts -> domain logic -> UI/API wiring.
3. **Per-Patch Verification Gate:** Run the repository's relevant build, typecheck, or unit test command after each micro-patch and fix any failures before starting the next patch.
4. **Stack-Specific Guardrails (Conditional):**
   - *When scaffolding or updating docs:* Follow [`../../references/scaffolding-templates.md`](../../references/scaffolding-templates.md).
   `Guardrail: aos Vibe Coding Guardrail v<version> | Skill: aos-vibecode | Tokens: <exact count if exposed by runtime, otherwise "N/A (not exposed by runtime)">`

---

## 2. Gotchas

* **Patch size overflow:** If a feature unit exceeds `50` lines, split it into sequential micro-patches rather than rewriting a module in one edit.
* **Dependency Lockdown:** Never install `npm` or `pip` packages without explicit human approval first.
