# 🛠️ Developer & Operations Guide (`dev.md`)

Setup, custom model profiles, environment variables, runtime scripts, and session workflow for **Vibe Coding Guardrail** (`vibe-coder`).

---

## 1. Prerequisites

- **Node.js:** `v22.x` (pinned via `.nvmrc`)
- **Git:** `>= 2.39` with GitHub CLI (`gh`) authenticated for Draft PR creation
- **Antigravity:** IDE or CLI with plugin/skill discovery enabled

---

## 2. Installation & Updates

### Global Plugin (Recommended)
```bash
mkdir -p ~/.gemini/config/plugins ~/.gemini/antigravity/skills ~/.gemini/config/skills
ln -sfn "$(pwd)" ~/.gemini/config/plugins/vibe-coding-guardrail
ln -sfn "$(pwd)/.agent/skills/"* ~/.gemini/antigravity/skills/
ln -sfn "$(pwd)/.agent/skills/"* ~/.gemini/config/skills/
```

**Update & check active version:**
```bash
cd /path/to/vibe-coding-guardrail && git pull origin main
node -p "require('./plugin.json').version"
```

### Workspace Scope (Single Repository)
```bash
npx github:stefanasemota/vibe-coding-guardrail /path/to/your-project
# Or from a local clone:
node bin/init-guardrail.mjs /path/to/your-project
```

---

## 3. Creating a Custom Profile for a Particular AI Model

Generate a custom Engine Profile tailored to any model (e.g., `claude-sonnet`, `gemini-flash`) using `aos-create-profile`:

```bash
# Interactive CLI prompt
npx aos-create-profile claude-sonnet

# Non-interactive CLI with model-specific parameters
node bin/aos-create-profile.mjs gemini-flash \
  --max-patch-size=30 \
  --review-depth=quick-lint \
  --gate-behavior=explicit-pause-and-wait \
  --execution-mode=sequential-multi-turn
```

This writes `.agent/skills/vibe-coder/profiles/profile-gemini-flash.md` validated against [`_schema.md`](.agent/skills/vibe-coder/profiles/_schema.md):

```markdown
---
engine_name: "gemini-flash"
execution_mode: "sequential-multi-turn"
max_patch_size: 30
patch_strategy: "surgical-unified-diff"
type_safety: "strict"
gate_behavior: "explicit-pause-and-wait"
review_depth: "quick-lint"
---
```

Activate in any session with `$PROFILE=<name>`:
```text
Start a vibe-coder session with $PROFILE=gemini-flash: implement the user notification preferences panel.
```

---

## 4. Environment Variable Specifications

For full-stack Next.js + Firebase + Genkit apps, create `.env.local` in the project root (never committed to Git):

```env
# Firebase Client SDK
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

> **Security Rule (`aos-check-for-security-issues`):** Never commit `.env*`, `*service-account*.json`, or `*key*.json`.

---

## 5. Quick-Start Commands & Standard Scripts (`package.json`)

| Command | Guardrail Repo | Full-Stack Reference Equivalent |
| :--- | :--- | :--- |
| `npm test` | Runs full guardrail test suite | `vitest --coverage` |
| `npm run test:unit` | Runs `node --test tests/guardrail.test.mjs` | `vitest run` |
| `npm run lint` | Validates skill frontmatter, docs, and metadata | `eslint .` |
| `npm run build` | Validates protocol readiness | `next lint && NODE_ENV=production next build` |
| `npm run dev` | Runs guardrail verification suite | `next dev --turbopack` |

---

## 6. Vibe-Coder Session Workflow

1. **Clean & Branch:** Run `git fetch --prune`, delete obsolete local merged branches, confirm remote merged branch deletions, and branch from `origin/main` (`feature/<slug>`, `fix/<slug>`, `chore/<slug>`).
2. **Implement (`aos-vibecode`):** Apply atomic micro-patches (`<= max_patch_size`) guided by `initiative.md` and `plan.md`.
3. **Verify (`aos-verify`):** Run `npm run lint && npm run test:unit && npm run build` (or the native stack toolchain).
4. **Audit (`aos-check-for-security-issues`):** Confirm zero hardcoded secrets or unsafe dependencies.
5. **Log & Hand-Off:** Prepend `[DD.MM.YYYY]` ADR to `decision.md`, output the Session Termination footer (version + skill + token usage), push, and open a Draft PR (`gh pr create --draft`).
