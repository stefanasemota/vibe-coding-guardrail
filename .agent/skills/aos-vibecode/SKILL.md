---
name: aos-vibecode
description: Rapid feature delivery sub-skill for the vibe-coder protocol. Use when translating product specifications or user stories from initiative.md and docs/specs/ into minimal, working code increments via micro-patches while preserving runtime state, routes, and architectural boundaries.
---

# `aos-vibecode` — Rapid Feature Delivery Sub-Skill

## Purpose
Translates product intent from `initiative.md`, `docs/rule-book.md`, and feature specs (`docs/specs/*.md`) into minimal, working code increments without destabilizing the existing application.

## Execution Rules

1. **Micro-Patch Discipline:**
   * Favor small, atomic patches (≤ 50 lines per change where feasible) over sweeping multi-file rewrites.
   * Keep diffs focused on a single concern per iteration and commit using Conventional Commits (`feat`, `fix`, `refactor`, etc. per `AGENTS.md`).

2. **Schema-First & Domain Grounding:**
   * Define deterministic **Zod schemas** (`z.object(...)`) as strict contracts before implementing AI flows (e.g., Genkit / Gemini) or database writes.
   * Enforce domain invariants from `docs/rule-book.md` (such as content-hash deduplication, quota limits, and token usage metadata).

3. **Shift-Left Repository Pattern & SSR Performance:**
   * **Strict Layering:** Direct use of `firebase-admin` or client `firestore` SDKs inside `src/app/` (UI routes) or `src/components/` is forbidden. Route all data access through encapsulated repositories in `src/repositories/`.
   * **Prevent CSR Waterfalls:** Prefer async React Server Components (RSC) and Server Actions (`src/modules/**/actions.ts`) over `'use client'` + `useEffect` data-fetching waterfalls.
   * **Singleton Backend SDKs:** Ensure `firebase-admin` is initialized via a cached Singleton (`src/lib/firebase-admin.ts`) and listed in `serverExternalPackages` in `next.config.ts`.
   * **Auth Safety:** Protect client-side OAuth redirect handlers (`getRedirectResult`) with a `useRef` lock to prevent double-execution under React 19 / Next.js 15 Strict Mode.

4. **Progressive Mobile-First UI Polish:**
   * Design for mobile usability first (390px viewport without horizontal scroll, high-contrast palettes, accessible tap targets, optimistic UI loaders for high-latency networks).

5. **Decision Traceability:**
   * Append every architectural choice, UX trade-off, or dependency addition to `decision.md` before concluding the step.
