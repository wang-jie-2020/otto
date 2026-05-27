# Release Checklist: v0.1.1

Date: 2026-05-27
Branch: `main`

## 1) Pre-release checks
- [x] `npm ci`
- [x] `npm run doctor`
- [x] `npm run skill:hello:local`
- [x] `git status` is clean before release commit/tag

## 2) Release contents
- [x] Executable sample skill added: `skills/hello-skill-tool`
- [x] Local smoke command added in root `package.json`
- [x] Release/upgrade/rollback SOP added: `doc/RELEASE.md`
- [x] Changelog section prepared: `0.1.1`

## 3) Tagging
- [ ] Create annotated tag:
  - `git tag -a v0.1.1 -m "release: v0.1.1"`
- [ ] Verify tag:
  - `git show v0.1.1 --no-patch`

## 4) Optional publish/push
- [ ] Push commits and tag:
  - `git push origin main`
  - `git push origin v0.1.1`
- [ ] If publishing package externally, announce pinned usage command:
  - `npx --yes otto-hello-skill-tool@0.1.1 --topic "release" --who "team"`
