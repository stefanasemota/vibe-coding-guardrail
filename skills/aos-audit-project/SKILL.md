---
name: aos-audit-project
description: Project architecture and scaffolding compliance auditor for the vibe-coder protocol. Use when inspecting any existing or new repository against Architectural Summary expectations (README.md + footer, initiative.md, dev.md, decision.md, stack manifests, .gitignore, AGENTS.md, Shift-Left Repository pattern), generating an optimization summary, asking which optimizations to apply (or running in unattended advisory mode), and outputting an aos-audit.md report.
---

# `aos-audit-project` — Architectural & Scaffolding Compliance Auditor

## Purpose

---

## 1. Audit Checklist (What to Inspect)

### A. Core Documentation Files

### B. Stack-Aware Manifest Check

### C. Git, AI Rules & Governance Hygiene
- Active Git repository with upstream remote and working branch isolated from `main`/`master`/`development`.
- `.gitignore` excluding `.env*`, build artifacts, virtual environments, `*service-account*.json`, `*key*.json`, and `*.pem`.

### D. Architectural Boundaries & Test Harness
- **Test Separation:** Fast unit test suite separated from slower E2E tests.

---

## 2. Execution Sequence

1. **Scan & Score:** Inspect every item in Section 1 without modifying files yet.
2. **Present Optimization Summary:** Output a markdown table showing each check (`✅ Pass`, `⚠️ Partial`, `❌ Missing`) and the proposed optimization.
3. **Gate (`pause` vs `advisory`):**
   - **Interactive (`pause`, default):** Ask the user which optimizations to apply.
5. **Branch, Commit, Push & Open Draft PR (When Changes Are Applied):**
   - Run the repository's native test/lint command to verify all checks pass.
   - Commit with a Conventional Commit (`chore(audit): apply aos-audit-project compliance optimizations`), push to `origin`, and open a Draft PR (`gh pr create --draft`). Leave final merge/review to the human.
6. **Session Termination:**
     `Guardrail: aos Vibe Coding Guardrail v<version> | Skill: aos-audit-project | Tokens: <exact count if exposed by runtime, otherwise "N/A (not exposed by runtime)">`
