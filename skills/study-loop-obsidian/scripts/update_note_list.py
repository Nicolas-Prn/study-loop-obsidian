#!/usr/bin/env python3
"""
Scans an Obsidian vault and generates the up-to-date list of all existing
note titles (without the .md extension), so that the agent knows which notes
it can create [[...]] wikilinks to, without ever pointing to a note that does
not exist.

Usage:
    python3 update_note_list.py <path_to_obsidian_vault> [output_path]

If output_path is omitted, writes to ./note_list.txt (current directory).
"""

import os
import sys


def generate_list(vault_dir: str, output_path: str) -> int:
    if not os.path.isdir(vault_dir):
        print(f"Error: folder '{vault_dir}' not found.")
        return 1

    titles = []
    for root, dirs, files in os.walk(vault_dir):
        # Skip Obsidian's hidden config folder
        if ".obsidian" in dirs:
            dirs.remove(".obsidian")
        # Also skip any hidden folder (.git, .trash, etc.)
        dirs[:] = [d for d in dirs if not d.startswith(".")]

        for file_name in files:
            if file_name.endswith(".md"):
                title = file_name[:-3]  # strip the .md extension
                titles.append(title)

    titles.sort(key=str.lower)

    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for title in titles:
            f.write(title + "\n")

    print(f"OK: {len(titles)} notes found. List written to {os.path.abspath(output_path)}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 update_note_list.py <path_to_obsidian_vault> [output_path]")
        sys.exit(1)

    vault = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else "note_list.txt"
    sys.exit(generate_list(vault, output))
