#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __filename = fileURLToPath(import.meta.url);
const packageRoot = path.resolve(path.dirname(__filename), '..');

function copyRootRules(targetDir) {
  const srcAgentsMd = path.join(packageRoot, 'AGENTS.md');
  const destAgentsMd = path.join(targetDir, 'AGENTS.md');
  fs.copyFileSync(srcAgentsMd, destAgentsMd);

  const srcAiRulesJson = path.join(packageRoot, 'ai-rules.json');
  const destAiRulesJson = path.join(targetDir, 'ai-rules.json');
  fs.copyFileSync(srcAiRulesJson, destAiRulesJson);

  return { destAgentsMd, destAiRulesJson };
}

export function installGuardrail(targetDirInput = process.argv[2] || '.') {
  const targetDir = path.resolve(process.cwd(), targetDirInput);

  if (!fs.existsSync(targetDir)) {
    fs.mkdirSync(targetDir, { recursive: true });
  }

  const srcSkillsDir = path.join(packageRoot, '.agent', 'skills');
  const destSkillsDir = path.join(targetDir, '.agent', 'skills');
  fs.cpSync(srcSkillsDir, destSkillsDir, { recursive: true });

  const { destAgentsMd, destAiRulesJson } = copyRootRules(targetDir);

  return { targetDir, destSkillsDir, destAgentsMd, destAiRulesJson };
}

export function installAllGuardrails(parentDirInput = '.', { cleanLocalSkills = false } = {}) {
  const parentDir = path.resolve(process.cwd(), parentDirInput);
  const realPackageRoot = fs.realpathSync(packageRoot);
  const updated = [];

  for (const entry of fs.readdirSync(parentDir, { withFileTypes: true })) {
    if (!entry.isDirectory() || entry.name.startsWith('.')) continue;

    const candidate = path.join(parentDir, entry.name);
    if (fs.realpathSync(candidate) === realPackageRoot) continue;
    if (!fs.existsSync(path.join(candidate, '.git'))) continue;

    if (cleanLocalSkills) {
      const localSkills = path.join(candidate, '.agent', 'skills');
      if (fs.existsSync(localSkills)) {
        fs.rmSync(localSkills, { recursive: true, force: true });
      }
      copyRootRules(candidate);
    } else {
      installGuardrail(candidate);
    }
    updated.push(candidate);
  }

  return { parentDir, updated };
}

if (process.argv[1] && path.resolve(process.argv[1]) === __filename) {
  const args = process.argv.slice(2);
  const isAll = args.includes('--all');
  const cleanLocalSkills = args.includes('--clean-local-skills');
  const targetArg = args.find((arg) => !arg.startsWith('--')) || '.';

  if (isAll) {
    const { parentDir, updated } = installAllGuardrails(targetArg, { cleanLocalSkills });
    const mode = cleanLocalSkills ? 'cleaned stale .agent/skills/ and updated rules' : 'updated skills and rules';
    console.log(`✅ Batch ${mode} in ${updated.length} git repo(s) under: ${parentDir}`);
    for (const dir of updated) {
      console.log(`   - ${path.basename(dir)}`);
    }
  } else {
    const { targetDir } = installGuardrail(targetArg);
    console.log(`✅ Installed vibe-coder skills (.agent/skills/), AGENTS.md, and ai-rules.json into: ${targetDir}`);
  }
}
