#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import readline from 'node:readline/promises';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const packageRoot = path.resolve(path.dirname(__filename), '..');

export function generateProfileMarkdown({
  engineName,
  executionMode = 'parallel-subagents',
  maxPatchSize = 50,
  patchStrategy = 'surgical-unified-diff',
  typeSafety = 'strict',
  gateBehavior = 'explicit-pause-and-wait',
  reviewDepth = 'multi-aspect-audit',
}) {
  return `---
engine_name: "${engineName}"
execution_mode: "${executionMode}"
max_patch_size: ${Number(maxPatchSize)}
patch_strategy: "${patchStrategy}"
type_safety: "${typeSafety}"
gate_behavior: "${gateBehavior}"
review_depth: "${reviewDepth}"
---

# Engine Profile: \`${engineName}\`

## Operating Constraints
- **Execution Mode:** \`${executionMode}\`
- **Max Patch Size:** \`<= ${Number(maxPatchSize)} lines\`
- **Patch Strategy:** \`${patchStrategy}\`
- **Type Safety:** \`${typeSafety}\`
- **Gate Behavior:** \`${gateBehavior}\` (Phases 3, 4, and 6)
- **Review Depth:** \`${reviewDepth}\`
`;
}

export function createProfileFile({
  name,
  maxPatchSize = 50,
  reviewDepth = 'multi-aspect-audit',
  gateBehavior = 'explicit-pause-and-wait',
  targetRoot = packageRoot,
}) {
  const cleanName = String(name || '')
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9-_]/g, '-');
  if (!cleanName) {
    throw new Error('Profile name is required (usage: aos-create-profile <name>)');
  }

  const profilesDir = path.join(targetRoot, '.agent', 'skills', 'vibe-coder', 'profiles');
  fs.mkdirSync(profilesDir, { recursive: true });

  const filePath = path.join(profilesDir, `profile-${cleanName}.md`);
  const content = generateProfileMarkdown({
    engineName: cleanName,
    maxPatchSize,
    reviewDepth,
    gateBehavior,
  });
  fs.writeFileSync(filePath, content, 'utf8');
  return { filePath, cleanName };
}

async function runCli() {
  const argName = process.argv[2];
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  try {
    const name = argName || (await rl.question('1. Engine name (e.g. fast-proto): ')).trim();
    const patchInput = (await rl.question('2. Max patch size in lines [50]: ')).trim();
    const reviewInput = (
      await rl.question('3. Review depth (multi-aspect-audit | quick-lint) [multi-aspect-audit]: ')
    ).trim();
    const gateInput = (
      await rl.question('4. Gate strictness (explicit-pause-and-wait | advisory) [explicit-pause-and-wait]: ')
    ).trim();

    const { filePath } = createProfileFile({
      name,
      maxPatchSize: patchInput ? Number(patchInput) : 50,
      reviewDepth: reviewInput || 'multi-aspect-audit',
      gateBehavior: gateInput || 'explicit-pause-and-wait',
      targetRoot: process.cwd(),
    });
    console.log(`✅ Created engine profile: ${filePath}`);
  } finally {
    rl.close();
  }
}

if (process.argv[1] && path.resolve(process.argv[1]) === __filename) {
  runCli();
}
