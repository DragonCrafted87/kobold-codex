# Take the review

Design for the review-response skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, in the same build step as `review-the-diff` and
`stress-the-change`. The wording in the skill sections below is the
version to ship. Later sessions tune it by editing the skill file.
This spec stays the record of what we decided and why.

## Purpose

`take-the-review` is how a session handles review notes. It checks
each note against the code before editing. It implements a note that
holds. For a note that does not hold, it says why and leaves that
part of the code as it is.

`review-the-diff` and `stress-the-change` produce findings and stop.
This skill starts when those findings, or notes from somewhere else,
are the work in front of the session. `scope-the-edit` still decides
the plan and the proof for each fix.

The creed stays in `skills/kobold-codex/SKILL.md`. This skill does
not restate those principles.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. Verify, then edit. A note is not
implemented because a reviewer wrote it. It is implemented because
the code at the cited line does the thing the note calls wrong, and
that thing disagrees with the request.

The notes are the ones the user handed over. When the user names
none, the notes are the findings the latest review in this session
reported. When there are none, the session asks which notes to take
and does not edit. Items a review listed as outside the diff are not
findings, so they are not notes unless the user hands them over.

A note the session cannot place on a file and a line is unclear.
The session asks about that note before editing it. Two notes about
the same lines wait until both are clear, because a fix for one
would land on the other's ground. A clear note that shares no lines
with an unclear one proceeds. Holding every note for one unclear
comment was set aside. The notes that share lines are the ones that
can spoil each other.

The request is what the user asked for, and the plan when there is
one. When the request asked for the code the note objects to, the
note does not hold. When no request is on record, the note holds
when the code does the thing the note calls wrong. A note about
code outside the diff the notes came from stays outside the change.
The session says so and leaves that code, unless the user asked to
take that note.

Fixes run one note at a time. The next note is read against the code
after the earlier fix, so a note that the fix already answered does
not get a second edit. The fix is the one the note describes.
`scope-the-edit` chooses the plan and the proof, including a stop
for a written plan when the fix is architectural. The check is the
one that shows the note no longer holds. A failed check stops the
run. Later notes stay untouched. The failed change stays in the
tree, and the report names the note, the change, and the result.
The session does not invent a third shape for that note in the same
run.

A note that does not hold gets a reason and a citation, the file
and the line that were read. That part of the code stays. The reply
states the reason. Praise does not stand in for the reason.

A second run reads the notes again. A fix already in the code is
named and left. A note already declined gets the same reason. A
note not yet checked is checked as on the first run. When the files
make a note impossible to check, the session asks and leaves the
code alone.

Nothing in the skill names a Grok tool or a Claude tool. No hooks.

These three review skills ship together. The plugin version becomes
`0.6.0` in that change. The manifest description stays the stable
sentence in the catalog's ship rule, and later skills leave that
sentence as it is. The root README stays the introduction and the
install guide. It does not record this decision. `docs/skills.md`
links the skill and this spec, and it does not restate the skill
paragraphs. Install commands stay as they are.

`tests/check_plugin.py` pins the new section bodies to this document
the same way it pins the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, and the plan skills, and it requires
version `0.6.0` and the stable description.

## Where the words live

```text
skills/take-the-review/SKILL.md
docs/specs/2026-10-03-take-the-review-design.md
docs/plans/2026-10-03-review-skills.md
```

The creed, `scope-the-edit`, `set-the-bounds`, the three
investigation skills, and the two plan skills stay. The catalog
keeps the skillset list and the build order. Its text for this
skill stays the brief.

## Skill

Frontmatter `name` is `take-the-review`. Frontmatter `description`
is one physical line:

```text
Use when review notes are in hand. Check each note against the code, implement the notes that hold, and for a note that does not hold say why and leave that code as it is.
```

The body is the five sections below. Heading text matches. Paragraphs
match, including line breaks.

### The notes

Start from the notes the user handed you. When the user names none,
use the findings the latest review in this session reported. When
there are none, stop and ask which notes to take.

Read the notes before you edit. A note you cannot place on a file
and a line is unclear. Ask about that note before you edit it. When
two notes are about the same lines, ask before you edit either. A
clear note that shares no lines with an unclear one can proceed.

### Against the code

Read the code at the file and line before you edit. The note holds
when that code does the thing the note calls wrong, and that thing
disagrees with the request. The request is what the user asked for,
and the plan when there is one. When the request asked for the code
the note objects to, the note does not hold. When no request is on
record, the note holds when the code does the thing the note calls
wrong.

When you cannot find the line, say so and leave the code.

The change is the diff the notes came from. When a note is about
code outside that change, and the user did not ask to take that
note, say so, leave that code, and go on to the next note. A note
the user asked to take counts as about the change.

### One note at a time

When the note holds, and it is about the change, make the fix the
note describes. `scope-the-edit` decides the plan and the proof for
that edit. Run the check that shows the note no longer holds.
Record the result you observed.

Finish that note before you start the next. Read the next note
against the code after the fix.

When the check fails, stop. Report the note, the change, and the
result. Leave every later note untouched.

### A note that does not hold

When the note does not hold, say why, and cite the file and line
you read. Leave that part of the code as it is.

Then go on to the next note.

### The same notes

On a second run, read the notes again. When the code already has
the fix, say the note is already there, and leave the code. When
you already said a note does not hold, give that same reason, and
leave the code. A note you have not checked yet is checked the way
the first run checks it.

When the files on disk make a note impossible to check, stop and
ask. Leave the code alone.

## What this skill does not do

It does not write the review. `review-the-diff` and
`stress-the-change` do that, and they leave the tree alone.

It does not implement a note it has not checked against the code.

It does not treat a note about code outside the change as part of
the change, unless the user asked to take that note.

It does not fill a failed check with a second redesign in the same
run. The report ends that note.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, or the catalog.

## Tuning

Edit `skills/take-the-review/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-03 wording.

## Implementation check

The build is done when all of these are true:

- `skills/take-the-review/SKILL.md` carries the frontmatter and the
  five sections above. The heading text matches. The paragraphs
  match this document.
- `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`,
  `skills/set-the-bounds/SKILL.md`, the three investigation skills,
  the two plan skills, and the specs those skills pin are unchanged.
  The catalog's skill briefs stay. Its ship rule records the stable
  manifest description and points the skill map at `docs/skills.md`.
- `tests/check_plugin.py` fails when a new paragraph, the new
  frontmatter, the version, the manifest description, or a
  restatement of a skill paragraph in the README drifts.
- Plugin version is `0.6.0` in `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and both descriptions match the
  stable sentence in the catalog's ship rule. `review-the-diff` and
  `stress-the-change` ship in that same version.
- The root README keeps the install commands and does not link this
  spec. `docs/skills.md` links this spec and the new skill. The
  README does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.6.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while the skills live under it. The Python
  check is what requires each skill file.
- No tracked file names a hostname, a home directory, or a machine.
