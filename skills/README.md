# skills/

Put skill implementations and metadata under this directory.

Recommended approach:
- Keep each skill in its own folder.
- Add `SKILL.md` in every skill folder for `npx skills add` compatibility.
- Use YAML frontmatter in `SKILL.md` with at least `name` and `description`.
- Track version changes via Git tags and changelog.
- During personal development/experiments, focus only on one skill folder and avoid unrelated cross-repo refactors.

Consumer path:
- Install as agent skills:
  - `npx --yes skills add <repo-or-path> --list`
  - `npx --yes skills add <repo-or-path> --skill <name>`

Included example:
- `skills/hello-skill-tool`: agent skill with standard `SKILL.md`.
