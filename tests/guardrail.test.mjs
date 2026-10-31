import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { installGuardrail } from '../bin/init-guardrail.mjs';

const rootDir = process.cwd();

test('Prerequisite core documentation and reference files exist and are non-empty', () => {
  const requiredFiles = [
    'README.md',
    'initiative.md',
    'dev.md',
    'decision.md',
    'AGENTS.md',
    '.gitignore',
    '.nvmrc',
    'docs/reference-architecture.md',
  ];
  for (const file of requiredFiles) {
    const filePath = path.join(rootDir, file);
    assert.equal(fs.existsSync(filePath), true, `Missing required file: ${file}`);
    const stat = fs.statSync(filePath);
    assert.ok(stat.size > 0, `File is empty: ${file}`);
  }
});

test('README.md includes global skill installation and required community footer links', () => {
  const readme = fs.readFileSync(path.join(rootDir, 'README.md'), 'utf8');
  assert.match(readme, /~\/\.gemini\/antigravity\/skills\//);
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
});

test('vibe-coder and all 4 orchestrated sub-skills exist with valid YAML frontmatter', () => {
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
    assert.match(content, /^---\n([\s\S]*?)description:\s*.+\n([\s\S]*?)---/m, `Invalid frontmatter in ${skill}/SKILL.md`);
  }
});

test('decision.md contains dated entries matching protocol schema', () => {
  const content = fs.readFileSync(path.join(rootDir, 'decision.md'), 'utf8');
  assert.match(content, /### \[\d{4}-\d{2}-\d{2}\] - .+/);
  assert.match(content, /- \*\*Origin:\*\*/);
  assert.match(content, /- \*\*Context:\*\*/);
  assert.match(content, /- \*\*Decision:\*\*/);
  assert.match(content, /- \*\*Impact:\*\*/);
});

test('bin/init-guardrail.mjs copies .agent/skills/ (including aos-audit-project) and AGENTS.md into a target directory', () => {
  const pkg = JSON.parse(fs.readFileSync(path.join(rootDir, 'package.json'), 'utf8'));
  assert.equal(pkg.bin?.['init-guardrail'], './bin/init-guardrail.mjs');

  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'guardrail-test-'));
  try {
    const result = installGuardrail(tmpDir);
    assert.equal(fs.existsSync(path.join(result.targetDir, 'AGENTS.md')), true);
    assert.equal(fs.existsSync(path.join(result.targetDir, '.agent', 'skills', 'vibe-coder', 'SKILL.md')), true);
    assert.equal(fs.existsSync(path.join(result.targetDir, '.agent', 'skills', 'aos-audit-project', 'SKILL.md')), true);
    assert.equal(fs.existsSync(path.join(result.targetDir, '.agent', 'skills', 'aos-vibecode', 'SKILL.md')), true);
    assert.equal(fs.existsSync(path.join(result.targetDir, '.agent', 'skills', 'aos-verify', 'SKILL.md')), true);
    assert.equal(
      fs.existsSync(path.join(result.targetDir, '.agent', 'skills', 'aos-check-for-security-issues', 'SKILL.md')),
      true
    );
  } finally {
    fs.rmSync(tmpDir, { recursive: true, force: true });
  }
});
