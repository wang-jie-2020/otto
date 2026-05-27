# skills/

Put skill implementations and metadata under this directory.

Recommended approach:
- Keep each skill in its own folder.
- Add `SKILL.md` in every skill folder for `npx skills add` compatibility.
- Use YAML frontmatter in `SKILL.md` with at least `name` and `description`.
- Track version changes via Git tags and changelog.

Consumer paths:
- Install as agent skills:
  - `npx --yes skills add <repo-or-path> --list`
  - `npx --yes skills add <repo-or-path> --skill <name>`
- Invoke executable tools:
  - `npx --yes <package>@<x.y.z> <args>`
  - `npm exec --yes --package=./skills/<tool-folder> -- <bin> <args>`

Included example:
- `skills/hello-skill-tool`: executable package with `otto-hello` command and agent `SKILL.md`.
