// Vendors pinned browser builds of third-party libraries into assets/js/vendor/.
//
// The site deliberately has no dependency manifest or build step (see the
// "dependency manifests" rule in tools/site_audit.py), so versions are pinned
// here. The script downloads the exact published tarball with `npm pack`,
// copies the minified browser files, and prints their SHA-256 for review.
//
//   node tools/vendor.mjs
import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import { copyFileSync, mkdirSync, mkdtempSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const VENDOR = {
  // GSAP is distributed under the Standard "No Charge" License
  // (https://gsap.com/standard-license), not an open-source licence.
  gsap: { version: "3.15.0", files: ["gsap.min.js", "Flip.min.js"] },
};

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const target = join(root, "assets", "js", "vendor");
mkdirSync(target, { recursive: true });

for (const [name, { version, files }] of Object.entries(VENDOR)) {
  const work = mkdtempSync(join(tmpdir(), `vendor-${name}-`));
  try {
    const tarball = execFileSync("npm", ["pack", `${name}@${version}`, "--silent"], { cwd: work, encoding: "utf8" }).trim();
    execFileSync("tar", ["-xzf", tarball], { cwd: work });
    for (const file of files) {
      const destination = join(target, file);
      copyFileSync(join(work, "package", "dist", file), destination);
      const hash = createHash("sha256").update(readFileSync(destination)).digest("hex");
      console.log(`${name}@${version} ${file} sha256:${hash}`);
    }
  } finally {
    rmSync(work, { recursive: true, force: true });
  }
}
