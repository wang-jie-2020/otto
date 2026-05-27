# Minimum Practice (Executable)

## 1) Directory Baseline
- `doc/PRD.md`
- `doc/MINIMUM_PRACTICE.md`
- `skills/`
- `scripts/doctor.mjs`
- `package.json`
- `.npmrc`
- `package-lock.json`

## 2) Mandatory Command Set
- Install (reproducible): `npm ci`
- Policy check: `npm run doctor`
- Pinned execution pattern: `npx --yes <tool-package>@<x.y.z> <args>`

## 3) Version Strategy
- Pin package manager in `package.json#packageManager`.
- Require exact dependency versions via `.npmrc: save-exact=true`.
- Never use unversioned `npx <package>` in CI/production.

## 4) Upgrade Strategy (Controlled)
- Upgrade only through PR.
- PR must include:
  - old version -> new version
  - impact scope
  - rollback plan
- Merge only after checks pass.

## 5) Rollback Strategy
- Revert version bump commit OR switch consumers back to previous stable tag/version.
- Re-run `npm ci` and `npm run doctor` after rollback.
