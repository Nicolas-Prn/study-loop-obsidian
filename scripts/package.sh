#!/usr/bin/env bash
# Builds one zip per skill in dist/, ready to upload in the Claude app.
# zip follows symlinks by default, so files shared between skills are
# embedded as real files.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
rm -rf "$root/dist"
mkdir -p "$root/dist"

cd "$root/skills"
for skill in */; do
  skill="${skill%/}"
  zip -rq "$root/dist/$skill.zip" "$skill" -x '*.DS_Store' -x '*__pycache__*'
  echo "dist/$skill.zip"
done
