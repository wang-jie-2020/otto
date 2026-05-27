#!/usr/bin/env node

function getArgValue(args, key, fallback) {
  const index = args.indexOf(`--${key}`);
  if (index === -1 || index + 1 >= args.length) return fallback;
  return args[index + 1];
}

const args = process.argv.slice(2);
const topic = getArgValue(args, "topic", "npx");
const who = getArgValue(args, "who", "team");
const now = new Date().toISOString();

console.log(`[otto-hello] topic=${topic} who=${who} at=${now}`);
console.log("Pinned npx workflow is active.");
