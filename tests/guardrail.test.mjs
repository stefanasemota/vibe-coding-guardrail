import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { installGuardrail } from '../bin/init-guardrail.mjs';
import { createProfileFile } from '../bin/aos-create-profile.mjs';

const rootDir = process.cwd();

test('Prerequisite core documentation and reference files exist and are non-empty', () => {
  const requiredFiles = [
    'README.md',
    'CHANGELOG.md',
    'initiative.md',
    'dev.md',
    'decision.md',
    'AGENTS.md',
    'ai-rules.json',
    '.gitignore',
    '.nvmrc',
    '.agent/skills/README.md',
    '.agent/skills/vibe-coder/profiles/_schema.md',
    '.agent/skills/vibe-coder/profiles/profile-antigravity.md',
    '.agent/skills/vibe-coder/profiles/profile-automation.md',
    'docs/reference-architecture.md',
  ];
  for (const file of requiredFiles) {
    const filePath = path.join(rootDir, file);
    assert.equal(fs.existsSync(filePath), true, `Missing required file: ${file}`);
    const stat = fs.statSync(filePath);
    assert.ok(stat.size > 0, `File is empty: ${file}`);
  }
});

test('Engine profile _schema.md, profile-antigravity.md, and profile-automation.md define all 7 required contract fields', () => {
  const schemaContent = fs.readFileSync(
    path.join(rootDir, '.agent/skills/vibe-coder/profiles/_schema.md'),
    'utf8'
  );
  const profileContent = fs.readFileSync(
    path.join(rootDir, '.agent/skills/vibe-coder/profiles/profile-antigravity.md'),
    'utf8'
  );
  const automationProfileContent = fs.readFileSync(
    path.join(rootDir, '.agent/skills/vibe-coder/profiles/profile-automation.md'),
    'utf8'
  );

  const requiredFields = [
    'engine_name',
    'execution_mode',
    'max_patch_size',
    'patch_strategy',
    'type_safety',
    'gate_behavior',
    'review_depth',
  ];

  for (const field of requiredFields) {
    assert.match(schemaContent, new RegExp(field), `Missing ${field} in _schema.md`);
    assert.match(profileContent, new RegExp(`^${field}:`, 'm'), `Missing ${field} in profile-antigravity.md`);
    assert.match(automationProfileContent, new RegExp(`^${field}:`, 'm'), `Missing ${field} in profile-automation.md`);
  }
  assert.match(automationProfileContent, /gate_behavior:\s*"advisory"/);
});

test('AGENTS.md and ai-rules.json enforce strict Git strategy, execution discipline, and Conventional Commits', () => {
  const agentsMd = fs.readFileSync(path.join(rootDir, 'AGENTS.md'), 'utf8');
  assert.match(agentsMd, /Never work on `main`/);
  assert.match(agentsMd, /Test on the branch/);
  assert.match(agentsMd, /Push, do not merge/);
  assert.match(agentsMd, /Verify before writing/);
  assert.match(agentsMd, /Look Before You Leap/);
  assert.match(agentsMd, /Dependency Lockdown/);
  assert.match(agentsMd, /Fix your own bugs/);
  assert.match(agentsMd, /Documentation Sync/);
  assert.match(agentsMd, /Explain the Fix/);
  assert.match(agentsMd, /Zero AI Slop/);

  const aiRules = JSON.parse(fs.readFileSync(path.join(rootDir, 'ai-rules.json'), 'utf8'));
  assert.equal(aiRules.gitStrategy?.neverWorkOnMain, true);
  assert.equal(aiRules.gitStrategy?.pushDoNotMerge, true);
  assert.equal(aiRules.style?.noAiSlop, true);
  assert.ok(aiRules.executionDiscipline?.lookBeforeYouLeap);
  assert.ok(aiRules.executionDiscipline?.dependencyLockdown);
  assert.ok(aiRules.executionDiscipline?.documentationSync);
  assert.ok(aiRules.executionDiscipline?.explainTheFix);
  assert.ok(aiRules.conventionalCommits?.allowedTypes?.includes('feat'));
});

test('README.md includes default 5-badge header row, global skill installation, Antigravity usage prompts, Wednesday automations, custom model profile guide, and required community footer links', () => {
  const readme = fs.readFileSync(path.join(rootDir, 'README.md'), 'utf8');
  assert.match(readme, /\[!\[Version\]\(https:\/\/img\.shields\.io\/badge\/version-1\.2\.0-blue\.svg\)\]/);
  assert.match(readme, /\[!\[License\]\(https:\/\/img\.shields\.io\/badge\/license-MIT-green\.svg\)\]\(LICENSE\)/);
  assert.match(readme, /\[!\[Build Status\]\(https:\/\/img\.shields\.io\/badge\/build-passing-brightgreen\.svg\)\]/);
  assert.match(readme, /\[!\[Firebase\]\(https:\/\/img\.shields\.io\/badge\/Firebase-/);
  assert.match(readme, /\[!\[Gemini\]\(https:\/\/img\.shields\.io\/badge\/Gemini-AI%20Powered-/);
  assert.match(readme, /~\/\.gemini\/antigravity\/skills\//);
  assert.match(readme, /## 💬 How to Use in Antigravity/);
  assert.match(readme, /Start a vibe-coder session:/);
  assert.match(readme, /Run aos-audit-project:/);
  assert.match(readme, /Run aos-vibecode:/);
  assert.match(readme, /Run aos-verify:/);
  assert.match(readme, /Run aos-check-for-security-issues:/);
  assert.match(readme, /## ⏱️ Weekly Wednesday Automations/);
  assert.match(readme, /Every Wednesday/);
  assert.match(readme, /## 🧩 Creating a Custom Profile for a Particular AI Model/);
  assert.match(readme, /aos-create-profile/);
  assert.match(readme, /Powered by <a href="https:\/\/github\.com\/stefanasemota\/vibe-coding-guardrail">aos Vibe Coding Guardrail<\/a>/);
  assert.match(readme, /Fuel the Project - Buy me a coffee: <a href="https:\/\/buymeacoffee\.com\/stephanasex">https:\/\/buymeacoffee\.com\/stephanasex<\/a>/);
});

test('Standardized package.json metadata, author, keywords, repository, and scripts exist', () => {
  const pkg = JSON.parse(fs.readFileSync(path.join(rootDir, 'package.json'), 'utf8'));
  assert.ok(pkg.name, 'Missing package.json name');
  assert.ok(pkg.version, 'Missing package.json version');
  assert.ok(pkg.description, 'Missing package.json description');

  assert.deepEqual(pkg.author, {
    name: 'Stephan Asemota',
    email: 'stefan@asemota.ch',
    url: 'https://asemota.ch/',
  });

  const requiredKeywords = [
    'node',
    'npm',
    'project',
    'vibecoding tool',
    'https://sabiai.work/',
    '7-Phase Feature Development Workflow',
  ];
  for (const kw of requiredKeywords) {
    assert.ok(pkg.keywords?.includes(kw), `Missing required package.json keyword: ${kw}`);
  }

  assert.equal(pkg.repository?.type, 'git');
  assert.match(pkg.repository?.url || '', /^git\+https:\/\/github\.com/);

  const requiredScripts = ['dev', 'build', 'test', 'test:unit', 'lint'];
  for (const script of requiredScripts) {
    assert.ok(pkg.scripts?.[script], `Missing required package.json script: ${script}`);
  }

  const pluginJson = JSON.parse(fs.readFileSync(path.join(rootDir, 'plugin.json'), 'utf8'));
  assert.equal(pluginJson.name, 'vibe-coding-guardrail');
  assert.equal(pluginJson.version, pkg.version);
  assert.equal(pluginJson.logo, 'assets/logo.svg');
  assert.equal(Array.isArray(pluginJson.suggestedPrompts), true);
  assert.equal(pluginJson.suggestedPrompts.length, 3);
  assert.equal(fs.existsSync(path.join(rootDir, 'assets/logo.svg')), true);
  assert.equal(fs.existsSync(path.join(rootDir, 'rules/AGENTS.md')), true);
  assert.equal(fs.existsSync(path.join(rootDir, 'skills/vibe-coder/SKILL.md')), true);
});

test('vibe-coder and all 4 orchestrated sub-skills exist with valid YAML frontmatter and consume profile parameters', () => {
  const skills = [
    'vibe-coder',
    'aos-audit-project',
    'aos-vibecode',
    'aos-verify',
    'aos-check-for-security-issues',
  ];

  for (const skill of skills) {
    const skillPath = path.join(rootDir, '.agent', 'skills', skill, 'SKILL.md');
    assert.equal(fs.existsSync(skillPath), true, `Missing skill file: ${skillPath}`);
    const content = fs.readFileSync(skillPath, 'utf8');
    assert.match(content, /^---\nname:\s*.+\ndescription:\s*.+\n---/m, `Invalid frontmatter in ${skill}/SKILL.md`);
    assert.doesNotMatch(content, /disable-model-invocation:\s*true/, `${skill}/SKILL.md must not disable model invocation`);
    assert.match(content, /profile-antigravity\.md/, `${skill}/SKILL.md should reference active profile resolution`);
  }

  const auditSkill = fs.readFileSync(
    path.join(rootDir, '.agent/skills/aos-audit-project/SKILL.md'),
    'utf8'
  );
  assert.match(auditSkill, /5\.\s*\*\*Branch, Commit, Push & Open Draft PR/);
  assert.match(auditSkill, /gh pr create --draft/);
});

test('decision.md and aos-audit.md use DD.MM.YYYY date format and order decisions newest-to-oldest', () => {
  const content = fs.readFileSync(path.join(rootDir, 'decision.md'), 'utf8');
  assert.match(content, /### \[\d{2}\.\d{2}\.\d{4}\] - .+/);
  assert.doesNotMatch(content, /### \[\d{4}-\d{2}-\d{2}\]/, 'decision.md must not use YYYY-MM-DD');
  assert.match(content, /- \*\*Origin:\*\*/);
  assert.match(content, /- \*\*Context:\*\*/);
  assert.match(content, /- \*\*Decision:\*\*/);
  assert.match(content, /- \*\*Impact:\*\*/);

  const dateMatches = [...content.matchAll(/### \[(\d{2})\.(\d{2})\.(\d{4})\] - /g)];
  assert.ok(dateMatches.length >= 2, 'Expected at least 2 dated entries in decision.md');
  const timestamps = dateMatches.map(([, dd, mm, yyyy]) => {
    const day = Number(dd);
    const month = Number(mm);
    const year = Number(yyyy);
    assert.ok(day >= 1 && day <= 31, `Invalid day in DD.MM.YYYY: ${dd}`);
    assert.ok(month >= 1 && month <= 12, `Invalid month in DD.MM.YYYY: ${mm}`);
    return Date.UTC(year, month - 1, day);
  });
  for (let i = 1; i < timestamps.length; i++) {
    assert.ok(
      timestamps[i - 1] >= timestamps[i],
      `decision.md entries must be ordered newest (top) to oldest (bottom)`
    );
  }

  const auditContent = fs.readFileSync(path.join(rootDir, 'aos-audit.md'), 'utf8');
  assert.match(auditContent, /- \*\*Date:\*\* \d{2}\.\d{2}\.\d{4}/);
});

test('bin/init-guardrail.mjs and bin/aos-create-profile.mjs work as expected in isolated directories', () => {
  const pkg = JSON.parse(fs.readFileSync(path.join(rootDir, 'package.json'), 'utf8'));
  assert.equal(pkg.bin?.['init-guardrail'], './bin/init-guardrail.mjs');
  assert.equal(pkg.bin?.['aos-create-profile'], './bin/aos-create-profile.mjs');

  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'guardrail-test-'));
  try {
    const result = installGuardrail(tmpDir);
    assert.equal(fs.existsSync(path.join(result.targetDir, 'AGENTS.md')), true);
    assert.equal(fs.existsSync(path.join(result.targetDir, 'ai-rules.json')), true);
    assert.equal(fs.existsSync(path.join(result.targetDir, '.agent', 'skills', 'README.md')), true);
    assert.equal(
      fs.existsSync(path.join(result.targetDir, '.agent', 'skills', 'vibe-coder', 'profiles', '_schema.md')),
      true
    );
    assert.equal(
      fs.existsSync(
        path.join(result.targetDir, '.agent', 'skills', 'vibe-coder', 'profiles', 'profile-antigravity.md')
      ),
      true
    );

    const created = createProfileFile({
      name: 'custom-engine',
      maxPatchSize: 40,
      reviewDepth: 'quick-lint',
      gateBehavior: 'advisory',
      targetRoot: tmpDir,
    });
    assert.equal(fs.existsSync(created.filePath), true);
    const customContent = fs.readFileSync(created.filePath, 'utf8');
    assert.match(customContent, /engine_name: "custom-engine"/);
    assert.match(customContent, /max_patch_size: 40/);
    assert.match(customContent, /review_depth: "quick-lint"/);
    assert.match(customContent, /gate_behavior: "advisory"/);
  } finally {
    fs.rmSync(tmpDir, { recursive: true, force: true });
  }
});
