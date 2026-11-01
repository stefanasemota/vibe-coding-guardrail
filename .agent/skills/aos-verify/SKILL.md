---
name: aos-verify
description: Automated sanity and test coverage sub-skill for the vibe-coder protocol. Use after implementing changes to validate imports, TypeScript types, ESLint rules, production builds, and unit/integration test suites before session completion.
---

# `aos-verify` — Engine-Neutral Automated Sanity & Test Coverage Sub-Skill

## Purpose
Verifies that every rapid-prototyping increment compiles cleanly, passes lint gates, and maintains high unit and E2E test coverage before hand-off.

## Active Profile Consumption
Reads `type_safety` (`strict` | `permissive`) and `review_depth` (`multi-aspect-audit` | `quick-lint`) from `.agent/skills/vibe-coder/profiles/profile-antigravity.md` (or the active `$PROFILE`).

---

## Verification Checklist

1. **Static Analysis & Lint Gate (`type_safety`):**
   * Run `npm run lint` (`eslint --max-warnings=0`).
   * When `type_safety` is `strict`:
     * `@typescript-eslint/no-explicit-any`: `"error"` (no untyped `any` escapes).
     * `unused-imports/no-unused-imports`: `"error"` (no dead imports).
     * Run `npx tsc --noEmit` (or `npm run typecheck`) to confirm zero type regressions across app and test configs.

2. **3-Point Static Audit (`review_depth: multi-aspect-audit`):**
   * **Simplicity / DRY:** Identify redundant logic, dead imports, or unnecessary state.
   * **Functional Correctness:** Verify boundary conditions, error handling, and null safety.
   * **Conventions:** Confirm naming conventions, folder structures, `package.json` metadata, `README.md` badges/footer, and `decision.md` `[DD.MM.YYYY]` ordering align with the project.

3. **Layered Automated Test Suite:**
   * **Unit & Integration (`npm run test:unit` / `npm test`):**
     * Execute project unit tests (`vitest` or `node --test`) and maintain **> 90% coverage** across core logic and `src/repositories/`.
   * **BDD / End-to-End (`npm run test:e2e`, when applicable):**
     * Keep E2E specs (`@cucumber/cucumber` / `@playwright/test`) isolated in `test/e2e/features/*.feature` so unit test runs remain sub-second.

4. **Production Build Sanity:**
   * Run `npm run build` to verify clean compilation and monitor route bundle budgets.
