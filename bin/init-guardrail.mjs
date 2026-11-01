#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const packageRoot = path.resolve(path.dirname(__filename), '..');

export function installGuardrail(targetDirInput = process.argv[2] || '.') {
  const targetDir = path.resolve(process.cwd(), targetDirInput);

  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  const srcSkillsDir = path.join(packageRoot, '.agent', 'skills');
  const destSkillsDir = path.join(targetDir, '.agent', 'skills');
  fs.cpSync(srcSkillsDir, destSkillsDir, { recursive: true });

  const srcAgentsMd = path.join(packageRoot, 'AGENTS.md');
  const destAgentsMd = path.join(targetDir, 'AGENTS.md');
  fs.copyFileSync(srcAgentsMd, destAgentsMd);

  const srcAiRulesJson = path.join(packageRoot, 'ai-rules.json');
  const destAiRulesJson = path.join(targetDir, 'ai-rules.json');
  fs.copyFileSync(srcAiRulesJson, destAiRulesJson);

  return { targetDir, destSkillsDir, destAgentsMd, destAiRulesJson };
}

if (process.argv[1] && path.resolve(process.argv[1]) === __filename) {
  const { targetDir } = installGuardrail();
  console.log(`✅ Installed vibe-coder skills (.agent/skills/), AGENTS.md, and ai-rules.json into: ${targetDir}`);
}
