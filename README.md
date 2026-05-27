# npx Skills Repo (Version-Controlled)

This repository is a minimal, reproducible setup for:
- executable skill tools using `npx`/`npm exec`
- agent skills consumable via `npx skills add ... --skill ...`

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

## Install This Repo As Agent Skills (`npx skills add`)
If you want a Vercel-style skills workflow:

```powershell
npx --yes skills add . --skill hello-skill-tool
```

List discoverable skills first:

```powershell
npx --yes skills add . --list
```

From any other directory, you can point at this repo path:

```powershell
npx --yes skills add D:\Code\what-i-do\otto --skill hello-skill-tool
```

Remote repo install pattern:

```powershell
npx --yes skills add <owner>/<repo> --skill <name>
```

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
