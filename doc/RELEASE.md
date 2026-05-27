# Release / Upgrade / Rollback SOP

## 1) Scope
This document defines the operational process for:
- release
- dependency/tool upgrades
- rollback

All actions are PR-based and version-controlled.

## 2) Preconditions
- Working branch is up to date with `main`.
- `npm ci` passes.
- `npm run doctor` passes.
- Local skill command check passes:
  - `npm run skill:hello:local`

## 3) Release Process
1. Prepare changes on a feature branch.
2. Update `CHANGELOG.md`.
3. Open PR with:
   - summary
   - version impact
   - rollback plan
4. Merge PR after review and CI green.
5. Create and push a Git tag for the release version.
6. Announce pinned consumer command:
   - `npx --yes <tool>@<x.y.z> <args>`

## 4) Upgrade Process (Controlled)
1. Create a dedicated upgrade branch.
2. Bump exact versions only (no implicit `latest`).
3. Run:
   - `npm ci`
   - `npm run doctor`
   - skill smoke checks
4. Open PR including:
   - old version -> new version
   - risk assessment
   - rollback instruction
5. Merge only after review and passing checks.

## 5) Rollback Process
1. Identify last known good version/tag.
2. Revert the upgrade commit, or pin consumers back to previous version.
3. Run:
   - `npm ci`
   - `npm run doctor`
   - local skill smoke checks
4. Open emergency rollback PR.
5. Merge and retag/reannounce if needed.

## 6) Checklist
- [ ] No unpinned `npx <package>` usage in CI/prod paths.
- [ ] Lockfile present and committed.
- [ ] `doctor` check passing.
- [ ] Changelog updated.
- [ ] Rollback plan included in PR.
