---
name: aos-verify
description: Automated sanity and test coverage sub-skill for the vibe-coder protocol. Use after implementing changes to validate imports, TypeScript types, ESLint rules, production builds, and unit/integration test suites before session completion.
---

# `aos-verify` — Automated Sanity & Test Coverage Sub-Skill

## Purpose
Verifies that every rapid-prototyping increment compiles cleanly, passes strict zero-warning lint gates, and maintains high unit and E2E test coverage before hand-off.

## Verification Checklist

1. **Static Analysis & Zero-Warning Lint Gate:**
   * Run `npm run lint` (`eslint --max-warnings=0`).
   * Enforce strict TypeScript hygiene:
     * `@typescript-eslint/no-explicit-any`: `"error"` (no untyped `any` escapes).
     * `unused-imports/no-unused-imports`: `"error"` (no dead imports).
   * Run `npx tsc --noEmit` (or `npm run typecheck`) to confirm zero type regressions across app and test configs (`tsconfig.json`, `tsconfig.e2e.json`).

2. **Layered Automated Test Suite:**
   * **Unit & Integration (`npm run test:unit` / `npm test`):**
     * Execute `vitest` with environment-matched globs (`node` for `src/modules/**`, `**/*.server.test.ts`, `test/logic/**`; `jsdom` for `src/components/**`, `src/app/**`).
     * Maintain **> 90% coverage** (`@vitest/coverage-v8`) across `src/repositories/` and `src/lib/`.
   * **BDD / End-to-End (`npm run test:e2e`, when applicable):**
     * Keep Cucumber (`@cucumber/cucumber`) and Playwright (`@playwright/test`) specs isolated in `test/e2e/features/*.feature` so unit test runs remain sub-second.

3. **Production Build Sanity:**
   * Run `npm run build` (`next lint && NODE_ENV=production next build`) to verify clean SSR/SSG compilation and monitor **First Load JS** bundle budgets per route.
