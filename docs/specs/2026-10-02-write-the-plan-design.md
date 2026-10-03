# Write the plan

Design for the plan skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, in the same build step as `carry-out-the-plan`. The
wording in the skill sections below is the version to ship. Later
sessions tune it by editing the skill file. This spec stays the
record of what we decided and why.

## Purpose

`write-the-plan` is the document an architectural change stops for.
`scope-the-edit` has already named that scope. This skill writes the
file: what will change, what it touches, what stays the same, what
the checks cover, and the ordered tasks.

The creed stays in `skills/kobold-codex/SKILL.md`. This skill does
not restate those principles. It does not decide the scope. A small
edit and an intermediate edit still follow `scope-the-edit`. When
the user asks for a plan anyway, this skill writes the same document.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. Four things in prose, then the
tasks. A reviewer who was not in the session can read the prose
before the steps. The prose uses the headings the project already
uses for plans. The first plan in a project has no headings to match,
so the skill names four: What will change, What it touches, What
stays the same, and What the checks cover.

The file goes in the directory the project already uses. The session
looks for a plans directory the project's docs name, then for a
directory that already holds plan files, then for `docs/plans/`.
That fallback is the same directory `scope-the-edit` and
`set-the-bounds` already use. One change is one file. The name
carries the date and a short slug. Existing plan files decide the
spelling. A project with no plan files yet uses
`docs/plans/YYYY-MM-DD-name.md`, lowercase words, hyphens.

A second run that finds the four things and the tasks already in
that file leaves the file. A request to change the plan edits the
same file. The skill writes a plan. A design spec stays a separate
request, which `scope-the-edit` already says.

Each task is one change, the files it touches, and one check. The
check is a command, a screen, or a file, plus the result that counts
as done. There is no clock on a task, and there is no rule that a
failing test comes first. `scope-the-edit` already chooses the proof.
When the task changes a function, the plan names a check that reaches
the bar in that skill, and it writes the command and the result in
the task.

The mark is an empty checkbox, `- [ ]`, on the task and on each step
under it. `carry-out-the-plan` reads that mark. One mark means a
second run can see finished work. Each step is written so an empty
checkbox is a valid place to start. The skill stops with every
checkbox empty. The yes that starts the work is the yes
`scope-the-edit` already requires, and it names this plan.

Nothing in the skill names a Grok tool or a Claude tool. No hooks.

These two plan skills ship together. The plugin version becomes
`0.5.0` in that change. The manifest description stays the stable
sentence in the catalog's ship rule, and later skills leave that
sentence as it is. The root README stays the introduction and the
install guide. It does not record this decision. `docs/skills.md`
links the skill and this spec, and it does not restate the skill
paragraphs. Install commands stay as they are.

`tests/check_plugin.py` pins the new section bodies to this document
the same way it pins the creed, `scope-the-edit`, `set-the-bounds`,
and the investigation skills, and it requires version `0.5.0` and
the stable description.

## Where the words live

```text
skills/write-the-plan/SKILL.md
docs/specs/2026-10-02-write-the-plan-design.md
docs/plans/2026-10-02-plan-skills.md
```

The creed, `scope-the-edit`, `set-the-bounds`, and the three
investigation skills stay. The catalog keeps the skillset list and
the build order. Its text for this skill stays the brief. The
`how-it-fits` spec keeps the sentence that this skill was unshipped
on the day that spec was written.

## Skill

Frontmatter `name` is `write-the-plan`. Frontmatter `description`
is one physical line:

```text
Use when an architectural change needs a written plan, or the user asks for one. Write what will change, what it touches, what stays the same, what the checks cover, and the ordered tasks, then stop.
```

The body is the five sections below. Heading text matches. Paragraphs
match, including line breaks.

### The document

Write the plan for an architectural change. `scope-the-edit` has
already named that scope. This skill is the document. When the user
asks for a plan, write this same document for the change they named.

### Where it goes

Look for a plans directory the project's docs name. When they name
none, look for a directory that already holds plan files. When the
project has none, use `docs/plans/`, and create that directory when
it is missing. One change is one file. Name the file with the date
and a short name for the change. When the project already has plan
files, match their names. When it has none, use
`docs/plans/YYYY-MM-DD-name.md`, with the name in lowercase words
separated by hyphens.

When that file already holds the four things below and the tasks,
leave it in place. When the user asks for a change to the plan, edit
that file.

### What the reviewer reads

Say four things, in prose a reviewer can follow without the session
transcript. What will change. Which parts of the system the change
touches. What stays the same. What the checks cover.

When the project already has headings for a plan, use those headings
and put the four things under them. When the project has no plan
yet, head those four things What will change, What it touches, What
stays the same, and What the checks cover.

### Tasks

Under those four things, list the tasks in the order a later session
will run them. A task names the files it changes, the check that
ends it, and the result that counts as done. The check is a command,
a screen, or a file the reviewer can run or read. A task is one
change and that check. When a task needs an earlier task finished,
it names that task.

A task that changes a function names a check that reaches the bar in
`scope-the-edit`. Write the command and the result in the task.

Each task, and each step under it, begins with an empty checkbox,
written `- [ ]`. Write each step so an empty checkbox is a valid
place to start. A later session marks a finished checkbox `- [x]`.

### Stop there

Write the file, then stop. Leave every checkbox empty. The work
starts when the user approves this plan. `scope-the-edit` says which
reply counts as that approval.

## What this skill does not do

It does not decide whether the change is architectural. `scope-the-edit`
already did that.

It does not write a design spec. A spec is a separate request.

It does not start the tasks. Empty checkboxes are the end of this
skill.

It does not set a time limit on a task, and it does not require a
failing test before the change. The check is the one the scope
already calls for.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, or the catalog.

## Tuning

Edit `skills/write-the-plan/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-02 wording.

## Implementation check

The build is done when all of these are true:

- `skills/write-the-plan/SKILL.md` carries the frontmatter and the
  five sections above. The heading text matches. The paragraphs match
  this document.
- `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`,
  `skills/set-the-bounds/SKILL.md`, the three investigation skills,
  and the specs those skills pin are unchanged. The catalog's skill
  briefs stay. Its ship rule records the stable manifest description
  and points the skill map at `docs/skills.md`.
- `tests/check_plugin.py` fails when a new paragraph, the new
  frontmatter, the version, the manifest description, or a restatement
  of a skill paragraph in the README drifts.
- Plugin version is `0.5.0` in `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and both descriptions match the
  stable sentence in the catalog's ship rule. `carry-out-the-plan`
  ships in that same version.
- The root README keeps the install commands and does not link this
  spec. `docs/skills.md` links this spec and the new skill. The
  README does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.5.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while the skills live under it. The Python
  check is what requires each skill file.
- No tracked file names a hostname, a home directory, or a machine.
