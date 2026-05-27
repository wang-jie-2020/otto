# npx Skills Repo (Version-Controlled)

This repository is a minimal, reproducible setup for skills development and distribution using `npx`/`npm exec`.

## Goals
- Pin tool versions (no `latest` drift)
- Reproducible install (`npm ci` + lockfile)
- Controlled upgrades (PR-based)

## Structure
- `doc/PRD.md`: Product requirements
- `doc/MINIMUM_PRACTICE.md`: Executable baseline guide
- `skills/`: Skills source and assets
- `scripts/doctor.mjs`: Repo policy checks

## Quick Start
1. `npm ci`
2. `npm run doctor`

## Pinned npx Invocation Pattern
Use explicit versions:

```powershell
npx --yes <skill-tool-package>@<x.y.z> <args>
```

Never rely on implicit `latest` for production or CI usage.
