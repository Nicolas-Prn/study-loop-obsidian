# study-loop-obsidian

A Claude skill that turns Claude into a **demanding Socratic tutor** for
studying a course, with **fully automatic Obsidian note-taking** in the
background.

## The loop

```
explain a concept  →  test you (critically)  →  mastered?
        ↑                                          │
        └──── no: re-explain differently ◄─────────┤
                                                   │ yes
                                                   ▼
                     background sub-agent writes the note  →  next concept
                     (reusing the exact explanations that worked
                      + your mistakes as "pitfall" callouts)
```

- **One concept at a time**, in the order of the course material (PDF,
  slides), with the course's exact formalism, intuitions and concrete
  examples.
- **A test after every concept**: new cases, trick cases, "why?". No "almost
  right", no flattery, justification required. Until it is mastered, you go
  around again from a different angle.
- **Note written once the concept is validated**: the sub-agent waits for you
  to pass the test so the note reuses exactly the explanations, analogies and
  examples that finally made it click, plus your mistakes as "pitfall"
  callouts. A catch-up check makes sure no validated concept is left without
  its note.
- **Zero note-taking friction**: the note is never discussed in the chat; the
  sub-agent writes it straight into your vault (LaTeX, callouts, wikilinks)
  and links it to the notes already there.

## Vault structure (Zettelkasten adapted to Obsidian)

The sub-agent manages the vault's **structure**, not just notes:

```
<vault>/
├── Resources/           # all atomic notes, flat
├── Maps of content/     # MOCs — the only folder with a real tree
│   └── Studies/<Institution>/<Year>/<Term>/COURSE NAME.md
└── Inbox/               # temporary notes, drafts, dashboards
```

- **Empty vault**: it bootstraps this structure from scratch (folders, course
  MOC, a minimal `Inbox/Home.md`).
- **Existing vault**: if the same structure already exists under other names,
  it follows yours; it creates missing branches (new year, term, course) and
  adds new MOC folders to dashboard / `.base` filters.
- **One MOC per course**, with `##` sections following the chapters; every
  new note is added to it — no orphan notes.
- **Properties**: atomic notes get `MOC`, `Source` and `Date`; MOCs get
  `cover` (left empty if no image is available).
- **Strict atomicity**: one note = one small concept, ~15-60 lines
  (`assets/example.md` is already an upper bound). A long note gets split into
  smaller linked notes.
- **Nothing is ever deleted**: removing a note means moving it to
  `<vault>/.trash/`; `.obsidian/` is never touched.

## Language

When the course is taught in a language other than yours, the tutor
**converses and tests you in the course language** (your exam will be in
that language, so you learn the vocabulary from the start), unless you ask
otherwise. You may answer in your own language. Notes are written in the
course language by default.

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

> ⚠️ The sub-agent **writes directly into your vault** and may create folders
> and edit dashboard filters. It never deletes anything (removed notes go to
> `.trash/`) and never modifies `.obsidian/`, but back up / commit your vault
> before the first use.

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
