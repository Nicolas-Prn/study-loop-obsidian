# study-loop-obsidian

A collection of Claude skills for studying a course, all with **fully
automatic Obsidian note-taking** in the background. They install together;
pick the one that matches your goal.

| Skill | Goal | Pace |
|---|---|---|
| [`study-loop-obsidian`](#study-loop-obsidian--deep-understanding) | Understand the course in depth, line by line | Exhaustive: every concept, every definition |
| [`exam-loop-obsidian`](#exam-loop-obsidian--pareto-exam-preparation) | Best grade in the least study time | Pareto: the ~20% of the material that earns ~80% of the points |

Both are demanding: critical tests, no "almost right", no flattery. They
differ in what they cover and how far they go.

You never have to pick the skill yourself: whichever one Claude loads first
asks for your goal at the start of the session (unless your first message
already makes it clear) and hands off to the other one if it fits better.
You can also switch mid-session.

Every session starts with a **session plan** sized to the time you have:
the tutor explains what will be covered, with a time budget per item, and
shows it in the client's progress panel (the **Progress** section in Claude
desktop). Items are ticked off live as you validate them; when you fall
behind, the plan is adjusted out loud so the session still ends on time —
by moving concepts to the next session in `study-loop-obsidian`, by
dropping the lowest-yield item in `exam-loop-obsidian`.

## study-loop-obsidian — deep understanding

A **demanding Socratic tutor** that covers the course concept by concept.

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
- **You do the work**: the tutor never writes to your project, code or repo
  (no scaffolding, no commits) and never offers to; it explains, asks,
  reviews and points you to the right resource.

## exam-loop-obsidian — Pareto exam preparation

A **demanding exam coach** for when the exam is close and the material is
too big to cover in depth.

```
intake: which exam? which latest documents?
        │
        ▼
Pareto plan: Core / If time / Dropped (+ ≥20% of the time for a mock exam)
        │
        ▼
for each item:  diagnose (exam question)  →  already scores? → next item
                        │ no
                        ▼
                teach only the gap  →  exam-style test  →  full marks?
                        ↑                                     │
                        └──────────── no ◄────────────────────┤
                                                              │ yes
                                                              ▼
                              background sub-agent writes lean notes,
                              ticks the item off the plan note → next item
        │
        ▼
mock exam under real conditions  →  targeted fixes  →  final review
```

- **Intake first**: the exam's format, date, grading, allowed material and
  announced scope; the hours you actually have; your target (pass safely or
  maximise); a quick self-assessment per chapter. It asks for the **latest
  version of every course document** (slides, exercise sessions with
  solutions, past exams, announcements) and waits for your confirmation
  before planning.
- **A Pareto plan built on evidence**: each topic is scored by expected
  points per hour of study, weighing teacher announcements first, then past
  exams, exercise sessions, slide emphasis, and page count last. Topics are
  split into **Core**, **If time** and **Dropped** (each dropped topic with
  its estimated cost in points). You validate the plan; it is saved in your
  vault so the next session resumes from it.
- **Diagnose before teaching**: each item opens with an exam question. If
  you already score, nothing is explained and you move on.
- **Exam-level teaching**: the course's exact formalism and notation, the
  method that solves the question type, the classic traps. Derivations only
  if the exam asks for them.
- **Timeboxed**: every item has a time budget; when it is blown, the coach
  says so and re-plans with you.
- **Lean notes**: one note per exam-relevant result, one method note per
  question type, definition notes only for the terms the exam asks or you
  confused (~10-30 lines each), plus a plan note with a checklist and a
  mistake log. They stay compatible with `study-loop-obsidian`, which can
  enrich them later.

## Vault structure (Zettelkasten adapted to Obsidian)

Both skills share the same vault conventions. The sub-agent manages the vault's **structure**, not just notes:

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

Both skills **immerse you in the course language**: explanations, tests,
feedback and the session plan are all in that language from the first
message, whatever language you write in, because your exam will be in it.
You may answer in your own language. Only when you are really lost on a
point does the tutor explain that point in your language, then it switches
back. Notes are written in the course language by default.

## Contents

```
.claude-plugin/                      # Claude Code plugin + marketplace
skills/
├── study-loop-obsidian/
│   ├── SKILL.md                     # the skill
│   ├── scripts/update_note_list.py  # lists the note titles in the vault
│   └── assets/example.md            # style reference for notes
└── exam-loop-obsidian/
    ├── SKILL.md                     # the skill
    ├── references/note-agent.md     # the lean note sub-agent's mission
    ├── scripts/update_note_list.py  # symlink to the shared script
    └── assets/example.md            # symlink to the shared example
scripts/
├── install.sh                       # symlinks every skill into ~/.claude/skills
└── package.sh                       # builds one zip per skill in dist/
```

## Installation

### Claude Code — as a plugin (recommended)

Installs every skill at once:

```
/plugin marketplace add Nicolas-Prn/study-loop-obsidian
/plugin install study-loop@study-loop
```

### Claude Code — from a clone

```bash
git clone https://github.com/Nicolas-Prn/study-loop-obsidian.git
./study-loop-obsidian/scripts/install.sh
```

The script symlinks every skill into `~/.claude/skills`, so a simple
`git pull` updates them all.

### Claude (desktop / web app)

1. Download every `.zip` from the latest
   [release](../../releases/latest) (or build them with
   `scripts/package.sh`, which writes them to `dist/`).
2. In Claude: **Settings → Capabilities → Skills → Upload skill**, once per
   zip.

## Customisation

Open each `SKILL.md` and adapt the **"Learner profile"** section (keep both
in sync): it drives the choice of concrete examples (DIY, finance, medicine,
video games...).

## First use

At the start of a session, give Claude:

- the **path to your Obsidian vault**;
- the location of **`note_list.txt`** (central list of note titles, a single
  file for all your courses);
- the **course folder** containing the PDFs/slides.

For `exam-loop-obsidian`, also have ready: the exam details (date, format,
grading, allowed material), the hours you can study, and the latest course
documents, ideally with exercise solutions and past exams.

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
