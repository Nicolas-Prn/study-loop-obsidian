# study-loop-obsidian

A Claude skill that turns Claude into a **demanding Socratic tutor** for
studying a course, with **fully automatic Obsidian note-taking** in the
background.

## The loop

```
explain a concept  →  test you (critically)  →  mastered?
        ↑                                           │
        └──────── no: re-explain differently ◄──────┤
                                                    │ yes
                    background sub-agent ◄──────────┘
             (writes the atomic note into your Obsidian vault,
              links it to your existing notes)
```

- **One concept at a time**, in the order of the course material (PDF,
  slides), with the course's exact formalism, intuitions and concrete
  examples.
- **A test after every concept**: new cases, trick cases, "why?". No "almost
  right", no flattery, justification required. Until it is mastered, you go
  around again from a different angle.
- **Zero note-taking friction**: as soon as a concept is validated, a
  sub-agent drafts an atomic Obsidian note (LaTeX, callouts, wikilinks),
  writes it into your vault, and links it to the notes already there. Your
  mistakes during the test become "pitfall" callouts in the note.

The tutor always talks to you in your own language (e.g. French if you write
in French), and notes are written in the language of the user/course unless
told otherwise.

## Contents

```
study-loop-obsidian/
├── SKILL.md                     # the skill
├── scripts/update_note_list.py  # lists the note titles in the vault
└── assets/example.md            # style reference for notes
```

## Installation

### Claude (desktop / web app)

1. Download `study-loop-obsidian.zip` from the latest
   [release](../../releases/latest) (or zip the `study-loop-obsidian/`
   folder yourself).
2. In Claude: **Settings → Capabilities → Skills → Upload skill**, and pick
   the zip.

### Claude Code

```bash
git clone https://github.com/Nicolas-Prn/study-loop-obsidian.git
mkdir -p ~/.claude/skills
ln -s "$(pwd)/study-loop-obsidian/study-loop-obsidian" ~/.claude/skills/study-loop-obsidian
```

(The symbolic link lets you get updates with a simple `git pull`.)

## Customisation

Open `SKILL.md` and adapt the **"Learner profile"** section: it drives the
choice of concrete examples (DIY, finance, medicine, video games...).

## First use

At the start of a session, give Claude:

- the **path to your Obsidian vault**;
- the location of **`note_list.txt`** (central list of note titles, a single
  file for all your courses);
- the **course folder** containing the PDFs/slides.

Claude needs read/write access to these folders (in the app: connected
folders; in Claude Code: start the session from a parent folder or add
them).

> ⚠️ The sub-agent **writes directly into your vault**. It only adds content
> (never deletes anything, never modifies `.obsidian/`), but back up / commit
> your vault before the first use.

## Graphify (optional)

If Graphify (package `graphifyy`) is installed and a graph of the vault
exists (`<vault>/graphify-out/graph.json`), the sub-agent uses it to find
related notes without opening them one by one. The skill never installs it
itself. Third-party tool, not maintained by Anthropic: test it on a small
subfolder first, building the graph consumes quota.

```bash
uv tool install graphifyy
graphify <test_subfolder> --obsidian --obsidian-dir <test_subfolder>
```

## License

MIT
