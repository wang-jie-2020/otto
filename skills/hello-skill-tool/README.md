# otto-hello-skill-tool

Minimal executable example for this repository.

## Local run (from repo root)

```powershell
npm exec --yes --package=./skills/hello-skill-tool -- otto-hello --topic "version-control" --who "team"
```

## Pinned run (after publish)

```powershell
npx --yes otto-hello-skill-tool@0.1.0 --topic "release" --who "team"
```
