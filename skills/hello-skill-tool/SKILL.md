---
name: hello-skill-tool
description: Reusable helper for pinned npx skills-add workflows and repository baseline checks.
user-invocable: true
---

# Hello Skill Tool

Use this skill when you need a quick, standardized check that a repository
follows a pinned `npx skills add` workflow.

## What this skill does

1. Verifies repository policy checks with `npm run doctor`.
2. Lists discoverable skills with `npx --yes skills add . --list`.
3. Summarizes whether the skills-add baseline workflow is healthy.

## Operating notes

- If dependencies are missing, run `npm ci` first.
- Keep output concise: include pass/fail plus next action.
- Prefer pinned `skills` CLI versions in CI.
