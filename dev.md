# 🛠️ Local Development & Antigravity Usage Guide (`dev.md`)

This document outlines how to install and use the **Vibe Coding Guardrail** (`vibe-coder`) in Google Antigravity, along with local environment setup, configuration specifications, and execution workflows.

---

## 1. How to Install & Use with Antigravity

Antigravity automatically discovers skills placed in a repository's `.agent/skills/` directory or in your global user skill directory.

### Option A: Add to an Existing or New Project (Workspace Scope)
Run the included `init-guardrail` CLI script (or copy `.agent/skills/`, `AGENTS.md`, and `ai-rules.json` manually) into the root of your target repository:

```bash
# Using the CLI installer from a local clone or npx
npx github:stefanasemota/vibe-coding-guardrail /path/to/your-project
# Or from a local clone:
node bin/init-guardrail.mjs /path/to/your-project
```

### Option B: Install Globally Across All Projects (User Scope — Recommended)
Symlink the skills into your global Antigravity configuration so `vibe-coder` is available in every workspace automatically and immediately reflects any updates in this repository:

```bash
mkdir -p ~/.gemini/antigravity/skills ~/.gemini/config/skills
ln -sfn "$(pwd)/.agent/skills/"* ~/.gemini/antigravity/skills/
ln -sfn "$(pwd)/.agent/skills/"* ~/.gemini/config/skills/
```

### Starting a Vibe-Coding Session in Antigravity
Once installed, trigger the protocol in the Antigravity chat pane with any prompt such as:
- *"Start a new vibe session and check the repository scaffolding."*
- *"Use `vibe-coder` to scaffold this project and implement the next feature from `initiative.md`."*
- *"Review `.agent/skills/vibe-coder/SKILL.md`, check git status, and prepare the session."*

Antigravity will automatically:
1. Verify or create `README.md`, `initiative.md`, `dev.md`, and `decision.md`.
2. Enforce an isolated Git branch (`feature/<slug>`, `fix/<slug>`, or `chore/<slug>`).
3. Orchestrate `aos-vibecode` (micro-patches), `aos-verify` (tests & lint), and `aos-check-for-security-issues` (security audit).
4. Log architectural decisions in `decision.md` and prepare a Draft PR upon your confirmation.

---

## 2. Prerequisites & Runtime Environment

- **Node.js:** `v22.x` (pinned via `.nvmrc`)
- **Git:** `>= 2.39` with GitHub CLI (`gh`) authenticated for Draft PR creation
- **Agent Environment:** Antigravity IDE / CLI with workspace skill discovery enabled (`.agent/skills/`)

---

## 3. Environment Variable Specifications

For full-stack Next.js + Firebase + Genkit applications, create a `.env.local` file in the project root (never committed to Git):

```env
# Firebase Client SDK Configuration
NEXT_PUBLIC_FIREBASE_API_KEY=your_api_key
NEXT_PUBLIC_FIREBASE_AUTH_DOMAIN=your_project.firebaseapp.com
NEXT_PUBLIC_FIREBASE_PROJECT_ID=your_project_id
NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET=your_project.appspot.com
NEXT_PUBLIC_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
NEXT_PUBLIC_FIREBASE_APP_ID=your_app_id

# Firebase App Check (ReCAPTCHA v3)
NEXT_PUBLIC_RECAPTCHA_SITE_KEY=your_recaptcha_site_key

# Genkit / Google Gemini AI
GOOGLE_GENAI_API_KEY=your_gemini_api_key
```

> **Security Rule (`aos-check-for-security-issues`):** Never commit `.env*`, `*service-account*.json`, or `*key*.json` files. Verify `.gitignore` coverage before staging changes.

---

## 4. Standard Execution Scripts (`package.json`)

Every project under the `vibe-coder` protocol exposes five uniform scripts:

| Command | Description | Full-Stack Reference Equivalent |
| :--- | :--- | :--- |
| `npm run dev` | Runs guardrail session inspector (or starts app dev server) | `next dev --turbopack` |
| `npm run build` | Validates protocol integrity and builds artifacts | `next lint && NODE_ENV=production next build` |
| `npm test` | Runs full automated test suite | `vitest --coverage` |
| `npm run test:unit` | Runs baseline unit test suite | `node --test tests/guardrail.test.mjs` / `vitest run` |
| `npm run lint` | Validates skill frontmatter, markdown docs, and code style | `eslint .` |

---

## 5. Vibe-Coder Session Workflow

1. **Inspect & Branch:**
   ```bash
   git status
   git checkout -b chore/<short-slug> # or feature/<short-slug>, fix/<short-slug>
   ```
2. **Implement (`aos-vibecode`):**
   - Apply incremental micro-patches (≤ 50 lines where feasible) guided by `initiative.md`.
3. **Verify (`aos-verify`):**
   ```bash
   npm run lint && npm run test:unit && npm run build
   ```
4. **Audit (`aos-check-for-security-issues`):**
   - Confirm zero hardcoded secrets or unsafe dependencies.
5. **Log & Hand-Off:**
   - Append session decisions to `decision.md`.
   - After human confirmation, push branch and open a Draft PR:
     ```bash
     git push -u origin HEAD
     gh pr create --draft
     ```
