#!/usr/bin/env bash
# Symlinks every skill of this repository into ~/.claude/skills, so that
# `git pull` updates them all.
set -euo pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
target="${CLAUDE_SKILLS_DIR:-$HOME/.claude/skills}"
mkdir -p "$target"

for skill in "$root"/skills/*/; do
  skill="${skill%/}"
  ln -sfn "$skill" "$target/$(basename "$skill")"
  echo "$target/$(basename "$skill") -> $skill"
done
