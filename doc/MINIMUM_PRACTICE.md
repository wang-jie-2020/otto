# Minimum Practice (Executable)

## 1) Directory Baseline
- `doc/PRD.md`
- `doc/MINIMUM_PRACTICE.md`
- `doc/RELEASE.md`
- `skills/`
- `scripts/doctor.mjs`
- `package.json`
- `.npmrc`
- `package-lock.json`

## 2) Mandatory Command Set
- Install (reproducible): `npm ci`
- Policy check: `npm run doctor`
- Skill discovery check: `npx --yes skills add . --list`
- Skill install pattern: `npx --yes skills add <repo-or-path> --skill <name>`

## 3) Version Strategy
- Pin package manager in `package.json#packageManager`.
- Require exact dependency versions via `.npmrc: save-exact=true`.
- Keep each `skills/<name>/SKILL.md` with YAML frontmatter (`name`, `description`).
- Prefer pinning skills CLI in automation/CI: `npx --yes skills@<x.y.z> ...`.
- Avoid unversioned tool invocation in CI/production.

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
- Re-run `npx --yes skills add . --list` to confirm skills are discoverable.
- Follow detailed SOP in `doc/RELEASE.md`.

## 6) Personal Experiment Rule
- For personal skill writing and testing, scope changes to one skill folder (for example `skills/article-writing/`).
- Do not require repository-wide alignment during experiments.
- Only expand change scope beyond the target skill folder when preparing a release/PR that needs shared docs or policy updates.
