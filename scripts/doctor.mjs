import { readFileSync, existsSync } from "node:fs";

const errors = [];

if (!existsSync("package-lock.json")) {
  errors.push("Missing package-lock.json. Run: npm install --package-lock-only");
}

const pkg = JSON.parse(readFileSync("package.json", "utf8"));
if (!pkg.packageManager || !/^npm@\d+\.\d+\.\d+$/.test(pkg.packageManager)) {
  errors.push("package.json#packageManager must pin an exact npm version (e.g. npm@10.9.7)");
}

const npmrc = existsSync(".npmrc") ? readFileSync(".npmrc", "utf8") : "";
if (!npmrc.includes("save-exact=true")) {
  errors.push(".npmrc must include: save-exact=true");
}

if (errors.length > 0) {
  console.error("[doctor] policy check failed:\n- " + errors.join("\n- "));
  process.exit(1);
}

console.log("[doctor] OK: lockfile + pinned package manager + save-exact policy present");
