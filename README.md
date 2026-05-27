# npx Skills Repo (Version-Controlled)

This repository is a minimal, reproducible setup for skills development and distribution using `npx`/`npm exec`.

## Goals
- Pin tool versions (no `latest` drift)
- Reproducible install (`npm ci` + lockfile)
- Controlled upgrades (PR-based)

## Structure
- `doc/PRD.md`: Product requirements
- `doc/MINIMUM_PRACTICE.md`: Executable baseline guide
- `doc/RELEASE.md`: Release/upgrade/rollback SOP
- `skills/`: Skills source and assets
- `scripts/doctor.mjs`: Repo policy checks

## Quick Start
1. `npm ci`
2. `npm run doctor`
3. `npm run skill:hello:local`

## Pinned npx Invocation Pattern
Use explicit versions:

```powershell
npx --yes <skill-tool-package>@<x.y.z> <args>
```

Never rely on implicit `latest` for production or CI usage.

## First Executable Skill Example
- Local development execution:
  - `npm exec --yes --package=./skills/hello-skill-tool -- otto-hello --topic "version-control" --who "team"`
- Registry consumption after publish (pinned):
  - `npx --yes otto-hello-skill-tool@0.1.0 --topic "release" --who "team"`
