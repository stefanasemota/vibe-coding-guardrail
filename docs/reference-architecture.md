# 🏛️ Reference Architecture from `stefanasemota` Projects

This document distills the repository structure, documentation hierarchy, engineering rules, and quality gates proven across **stefanasemota** projects to serve as the reference template for `vibe-coder` sessions.

---

## 1. Repository & Documentation Hierarchy

Projects governed by `vibe-coder` complement root scaffolding (`README.md`, `initiative.md`, `dev.md`, `decision.md`, `AGENTS.md`) with a structured `docs/` directory that grounds AI agents in domain rules and architectural constraints:

```text
├── .agent/skills/                # Vibe-coder & AOS sub-skills (vibe-coder, aos-vibecode, aos-verify, aos-check-for-security-issues)
├── .github/workflows/            # CI governance (standard-check.yml), deployment, semantic-release
├── .husky/                       # Git hooks: commit-msg (commitlint) & pre-commit (lint-staged: eslint + vitest related)
├── docs/
│   ├── blueprint.md              # Core product features & UI/UX style guidelines (colors, typography, mobile layout)
│   ├── rule-book.md              # Non-negotiable domain & architectural invariants
│   ├── forensic_analysis.md      # SSR vs CSR latency analysis, bundle budgets, and Firebase Admin Singleton patterns
│   └── specs/                    # Feature-level specs with Zod grounding schemas & Definitions of Done (DoD)
├── src/
│   ├── ai/flows/                 # Genkit + Gemini structured AI flows
│   ├── app/                      # Next.js 15 App Router pages & layouts
│   ├── components/               # Mobile-first shadcn/ui & Radix primitives
│   ├── lib/                      # Shared utilities & Firebase Admin Singleton
│   ├── modules/                  # Domain modules & Next.js Server Actions
│   └── repositories/             # Shift-Left Data Access Layer (encapsulated Firestore access)
├── test/ & tests/                # Vitest unit/integration tests + Cucumber/Playwright E2E features
├── AGENTS.md                     # Conventional Committer enforcement table
├── firestore.rules               # Role- and ownership-based Cloud Firestore Security Rules
├── eslint.config.mjs             # Flat ESLint config (no-explicit-any: error, unused-imports: error)
├── vitest.config.mts             # Dual node/jsdom environment globs + v8 coverage (>90% target)
└── package.json                  # Node 22 engine, standardized dev/build/lint/test scripts
```

---

## 2. Core Architectural & Domain Rules

1. **Shift-Left Repository Pattern:**
   - Direct imports of `firebase-admin` or client `firestore` SDKs in `src/app/` and `src/components/` are strictly forbidden.
   - All persistence operations must go through `src/repositories/`.
2. **React Server Components (RSC) over CSR Waterfalls:**
   - Avoid top-level `'use client'` + `useEffect` data fetching on route pages, which inflates First Load JS and causes client-side spinner waterfalls.
   - Fetch data in `async` Server Components using a cached `firebase-admin` Singleton (`src/lib/firebase-admin.ts`) and keep `serverExternalPackages: ["firebase-admin"]` in `next.config.ts`.
3. **Deterministic AI Grounding (`docs/specs/*.md`):**
   - Ground Gemini/Genkit flows in explicit domain standards and validate every LLM output against strict `zod` schemas before persisting to the database.
   - Track AI token usage (Input, Output, Total) and deterministic content hashes to prevent duplicate records and enforce per-user quotas.
4. **Auth Redirect Lock:**
   - Protect Firebase Auth redirect handlers (`getRedirectResult`) with a `useRef` lock to prevent double-execution under React 19 / Next.js 15 Strict Mode.

---

## 3. Quality Gates & Tooling Benchmark

- **Node Runtime:** Locked to Node `22` via `.nvmrc` and `package.json#engines`.
- **Commit Hygiene (`AGENTS.md` + `.husky/commit-msg`):**
  - Enforced by `@commitlint/config-conventional` and released via `semantic-release`.
- **Pre-Commit Gate (`.husky/pre-commit` + `lint-staged`):**
  - Runs `eslint --max-warnings=0 --no-warn-ignored` and `vitest related --run` on staged `*.{js,jsx,ts,tsx}` files.
- **Test Isolation (`vitest.config.mts`):**
  - Maps backend/logic tests (`src/modules/**`, `**/*.server.test.ts`, `test/logic/**`) to the `node` environment and UI tests (`src/components/**`, `src/app/**`) to `jsdom`, while excluding `tests/e2e/**` (run separately via `npm run test:e2e` with Cucumber + Playwright).
