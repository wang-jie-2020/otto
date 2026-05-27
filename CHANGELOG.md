# Changelog

All notable changes to this repository should be documented in this file.

## [Unreleased]
- Remove executable sample package files under `skills/hello-skill-tool` (`package.json`, `bin/otto-hello.js`).
- Remove `skill:hello:local` script and executable-tool references from docs.
- Keep `hello-skill-tool` as `SKILL.md`-based agent skill only.
- Add `SKILL.md`-based skill metadata for `npx skills add ... --skill ...` compatibility.
- Update docs with `npx skills add` usage and local-path examples.
- Extend `scripts/doctor.mjs` to validate `skills/*/SKILL.md` frontmatter.

## [0.1.1] - 2026-05-27
- Add first executable sample skill package: `skills/hello-skill-tool`.
- Add local smoke command: `npm run skill:hello:local`.
- Add release/upgrade/rollback SOP: `doc/RELEASE.md`.

## [0.1.0] - 2026-05-27
- Initialize repository baseline for npx-based skills workflow.
- Add PRD and minimum practice docs.
- Add reproducibility policy checks.
