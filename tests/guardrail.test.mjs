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

test('Standardized package.json scripts exist', () => {
  const pkg = JSON.parse(fs.readFileSync(path.join(rootDir, 'package.json'), 'utf8'));
  const requiredScripts = ['dev', 'build', 'test', 'test:unit', 'lint'];
  for (const script of requiredScripts) {
    assert.ok(pkg.scripts?.[script], `Missing required package.json script: ${script}`);
  }
});

test('vibe-coder and orchestrated sub-skills exist with valid YAML frontmatter', () => {
  const skills = [
    'vibe-coder',
    'aos-vibecode',
    'aos-verify',
    'aos-check-for-security-issues',
  ];

  for (const skill of skills) {
    const skillPath = path.join(rootDir, '.agent', 'skills', skill, 'SKILL.md');
    assert.equal(fs.existsSync(skillPath), true, `Missing skill file: ${skillPath}`);
    const content = fs.readFileSync(skillPath, 'utf8');
    assert.match(content, /^---\nname:\s*.+\ndescription:\s*.+\n---/m, `Invalid frontmatter in ${skill}/SKILL.md`);
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

test('bin/init-guardrail.mjs copies .agent/skills/ and AGENTS.md into a target directory', () => {
  const pkg = JSON.parse(fs.readFileSync(path.join(rootDir, 'package.json'), 'utf8'));
  assert.equal(pkg.bin?.['init-guardrail'], './bin/init-guardrail.mjs');

  const tmpDir = fs.mkdtempSync(path.join(os.tmpdir(), 'guardrail-test-'));
  try {
    const result = installGuardrail(tmpDir);
    assert.equal(fs.existsSync(path.join(result.targetDir, 'AGENTS.md')), true);
    assert.equal(fs.existsSync(path.join(result.targetDir, '.agent', 'skills', 'vibe-coder', 'SKILL.md')), true);
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
