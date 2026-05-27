# otto-hello-skill-tool

Minimal executable + agent-skill example for this repository.

## Agent skill install (`npx skills add`)

```powershell
npx --yes skills add . --skill hello-skill-tool
```

Check discoverability:

```powershell
npx --yes skills add . --list
```

## Executable local run (from repo root)

```powershell
npm exec --yes --package=./skills/hello-skill-tool -- otto-hello --topic "version-control" --who "team"
```

## Executable pinned run (after publish)

```powershell
npx --yes otto-hello-skill-tool@0.1.0 --topic "release" --who "team"
```
