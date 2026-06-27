// Minimal dependency-free smoke tests — your "automated quality gate".
// Run with: node tests/smoke.test.js  (exit code 0 = pass, 1 = fail)
const fs = require("fs");
const path = require("path");

const html = fs.readFileSync(
  path.join(__dirname, "..", "site", "index.html"),
  "utf8"
);

let failures = 0;
function check(name, condition) {
  if (condition) {
    console.log(`  ✓ ${name}`);
  } else {
    console.error(`  ✗ ${name}`);
    failures++;
  }
}

console.log("Running smoke tests...");
check("has a <title>", /<title>.*<\/title>/.test(html));
check("declares the lang attribute", /<html lang="en">/.test(html));
check("includes the stylesheet", /styles\.css/.test(html));
check("includes the app script", /app\.js/.test(html));
check("has a viewport meta tag (mobile-ready)", /name="viewport"/.test(html));
check("contains the build placeholder", fs
  .readFileSync(path.join(__dirname, "..", "site", "app.js"), "utf8")
  .includes("__BUILD_NUMBER__"));

if (failures > 0) {
  console.error(`\n${failures} test(s) failed.`);
  process.exit(1);
}
console.log("\nAll tests passed.");
