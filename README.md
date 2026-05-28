# npx Skills Repo (Version-Controlled)

This repository is a minimal, reproducible setup for agent skills consumable via `npx skills add ... --skill ...`.

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
3. `npx --yes skills add . --list`

## Personal Skill Development Rule
- For personal skill authoring and experiments, work inside one target skill folder only (for example `skills/article-writing/`).
- Do not couple the implementation to repository-wide changes unless explicitly needed for publishing or validation.
- Keep edits scoped to files under the target skill folder whenever possible.

## Install This Repo As Agent Skills (`npx skills add`)
Install from current directory:

```powershell
npx --yes skills add . --skill hello-skill-tool
```

List discoverable skills first:

```powershell
npx --yes skills add . --list
```

From any other directory, point to local repo path:

```powershell
npx --yes skills add D:\Code\what-i-do\otto --skill hello-skill-tool
```

Remote repo install pattern:

```powershell
npx --yes skills add <owner>/<repo> --skill <name>
npx --yes skills@1.5.7 add wang-jie-2020/otto --skill article-writing
```
