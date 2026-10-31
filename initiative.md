# 🚀 Initiative: Vibe Coding Guardrail (`vibe-coder`)

## 1. Seed Prompt & Problem Statement

Rapid AI-assisted prototyping ("vibe coding") often degrades as projects scale: repositories drift in structure, commits land directly on `main` without tests, architectural decisions vanish into chat transcripts, and credentials or client-side waterfalls creep into production code.

**Vibe Coding Guardrail** solves this by packaging a repeatable, self-enforcing agent skill (`vibe-coder`) and sub-skill triad (`aos-vibecode`, `aos-verify`, `aos-check-for-security-issues`) that any new or existing repository can adopt immediately.

---

## 2. Product Brief & Goals

1. **Standardized Project Scaffolding:**
   - Guarantee the presence and structure of `README.md`, `initiative.md`, `dev.md`, `decision.md`, `.gitignore`, and a normalized `package.json` (`dev`, `build`, `test`, `test:unit`, `lint`).
2. **Git Branch Isolation & PR Discipline:**
   - Prohibit direct commits to `main`/`master`.
   - Enforce scoped branches (`feature/<slug>`, `fix/<slug>`, `chore/<slug>`) and conclude sessions with human approval + Draft Pull Requests.
3. **Immutable Decision Ledger (`decision.md`):**
   - Log every architectural, UX, and dependency decision in real time with `Origin`, `Context`, `Decision`, and `Impact`.
4. **Coordinated Sub-Skill Execution:**
   - Separate rapid implementation (`aos-vibecode`), automated sanity/test verification (`aos-verify`), and defensive security auditing (`aos-check-for-security-issues`).

---

## 3. Reference Benchmark from stefanasemota projects

- **Reference Guardrails Adopted:**
  - **Conventional Commits (`AGENTS.md`):** Semantic commit enforcement via `commitlint` and `husky`.
  - **Shift-Left Repository Pattern:** Encapsulated data access in `src/repositories/` and `server-only` boundaries to prevent client-side bundle bloat and auth waterfalls.
  - **Layered Testing:** Fast unit testing (`vitest`) separated from E2E (`cucumber-js` / `playwright`).
  - **Secret & Artifact Hygiene:** Comprehensive `.gitignore` protecting Firebase, Genkit, Next.js, and service account credentials.
