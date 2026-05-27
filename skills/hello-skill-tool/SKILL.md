---
name: hello-skill-tool
description: Reusable helper for pinned npx workflows and simple repository smoke checks.
user-invocable: true
---

# Hello Skill Tool

Use this skill when you need a quick, standardized check that a repository is following
a pinned `npx` workflow and can run the sample hello command.

## What this skill does

1. Verifies repository policy checks with `npm run doctor`.
2. Runs local smoke command `npm run skill:hello:local` when available.
3. Summarizes whether pinned execution and baseline workflow are healthy.

## Operating notes

- If `npm` dependencies are missing, run `npm ci` first.
- Keep output concise: include pass/fail plus next action.
- Do not suggest unpinned `npx <package>` usage for CI/production workflows.
