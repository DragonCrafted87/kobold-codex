# Leave a trail

Design for the decision-log skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, as one of the build-order step 7 skills. The wording in
the skill sections below is the version to ship. Later sessions tune
it by editing the skill file. This spec stays the record of what we
decided and why.

## Purpose

`leave-a-trail` appends one row per decision for a long run or an
unattended run. The row carries what, why, evidence, and result. A
reviewer can read the log afterward. The log stays local unless the
reviewer needs it in the branch.

`run-the-play` keeps its working list in the reply.
`carry-out-the-plan` keeps checkboxes in the plan file. The catalog
says a large migration with no narrower playbook uses `multi-phase`
and this log. The `multi-phase` playbook is still a brief. This
skill does not write that playbook.

`set-the-bounds` says `safe-steps` may write the trail. Committing a
copy the reviewer needs follows `commit`. This skill reads those
values. It does not revise a layer.

The creed stays in `skills/kobold-codex/SKILL.md`. This skill does
not restate those principles.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. One row per decision, with what,
why, evidence, and result, in a log a reviewer can read. Local
unless the reviewer needs it in the branch.

The log is one file, `.kobold/trail.md` at the repository root.
Rows append. An earlier row is not rewritten. One file is enough
for a reviewer who wants the run in order. A file per run would
make the same fact live in two places once a copy lands in the
branch.

The run is a section. Its name is the branch, or the plan file,
the user named. When they named neither, the name is the date and
a short name for the work. The row is a heading and three lines:
what was decided, then `Why:`, `Evidence:`, and `Result:`.
Evidence names a command, a file, or a result the session
observed. A decision is a choice that rules out another choice, or
a result the next step depends on. A transcript of every command
is not a row.

The file stays out of git. When the path is not already ignored,
the pattern `.kobold/trail.md` is added to the repository ignore
rules. When the repository has no ignore file, that file is
created with that pattern as its line. This matches the way
`set-the-bounds` keeps `.kobold/bounds.local.yaml` out of git,
without sharing that path. The bounds file and the trail are
different records.

When the reviewer needs the log in the branch, the run's section
is copied into the place the project keeps notes a reviewer will
read. That copy follows `commit`. The local file stays.

`pick-up-the-work` reads this file. This skill does not rebuild
the brief.

Nothing in the skill names a Grok tool or a Claude tool. No hooks.

These eleven step-7 skills ship together. The plugin version becomes
`0.9.0` in that change. The manifest description stays the stable
sentence in the catalog's ship rule.

`tests/check_plugin.py` pins the new section bodies to this document
the same way it pins the earlier skills, and it requires version
`0.9.0` and the stable description.

The root README stays the introduction and the install guide. It
does not record this decision. `docs/skills.md` links the skill and
this spec, and it does not restate the skill paragraphs. Install
commands stay as they are.

The catalog keeps the skillset list, the playbook briefs, and the
build order. Its text for this skill stays the brief. The nine
playbook briefs that are not files yet stay briefs, including
`multi-phase`.

## Where the words live

```text
skills/leave-a-trail/SKILL.md
docs/specs/2026-10-03-leave-a-trail-design.md
docs/plans/2026-10-03-remaining-skills.md
```

The sentence in `run-the-play` that leaves the log to this skill
stays. This skill agrees with it: the working list is not a file.

## Skill

Frontmatter `name` is `leave-a-trail`. Frontmatter `description`
is one physical line:

```text
Use for a long run or an unattended run. Append one row per decision, with what, why, evidence, and result, to a log a reviewer can read afterward.
```

The body is the four sections below. Heading text matches.
Paragraphs match, including line breaks. The title is Leave a
trail.

### When it starts

Start a trail for a long run or an unattended run, and when the
user asks for one. A long run is one that will outlast this
sitting, or one a reviewer will need to read afterward.

A large migration that has no narrower playbook still gets this
log. This skill does not write that playbook.

The working list in `run-the-play` is not this log. The
checkboxes in a plan are not this log.

### The row

Append one row per decision. A decision is a choice that rules
out another choice, or a result the next step depends on.

Open a section for the run when that section is not there yet.
The run is the branch, or the plan file, the user named. When
they named neither, the section name is the date and a short name
for the work.

The row is a heading and three lines. The heading is what was
decided. The lines are `Why:`, `Evidence:`, and `Result:`.
Evidence names a command, a file, or a result you observed. Write
the row when the decision is made.

### Where it lives

The log is `.kobold/trail.md` at the repository root. Append to
that file. A second decision adds a row. It does not rewrite an
earlier row.

The log stays local. When that path is not already ignored, add
the pattern `.kobold/trail.md` to the repository ignore rules.
When the repository has no ignore file, create it with that
pattern as its line.

When the reviewer needs the log in the branch, copy the run's
section into the place the project keeps notes a reviewer will
read. That copy is work, and committing it follows `commit`. The
local file stays.

### The same run

A second run of the same work appends to the same section. An
earlier row stays. A decision that is already the last row, with
the same result, stays as that row. A new decision is a new row.

## What this skill does not do

It does not rebuild the brief a new session needs.
`pick-up-the-work` does that.

It does not write the `multi-phase` playbook. That brief stays a
brief until its own spec.

It does not commit `.kobold/trail.md`. A copy the reviewer needs
is a different file, and `commit` governs that copy.

It does not resolve a bounds file and it does not revise one.
`set-the-bounds` does that.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, the review skills,
`ship-the-branch`, `run-the-play`, or the catalog.

## Tuning

Edit `skills/leave-a-trail/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-03 wording.

## Implementation check

The build is done when all of these are true:

- `skills/leave-a-trail/SKILL.md` carries the frontmatter and the
  four sections above. The heading text matches. The paragraphs
  match this document. The title is Leave a trail.
- The skills already in the plugin, the specs those skills pin, the
  four playbooks, the catalog, and the root README are unchanged.
  The other ten step-7 skills ship in the same change, each from
  its own spec.
- `tests/check_plugin.py` fails when a paragraph, the frontmatter,
  the version, the manifest description, or a restatement of a
  section in the README drifts.
- Plugin version is `0.9.0` in `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and both descriptions match
  the stable sentence in the catalog's ship rule.
- The root README keeps the install commands and does not link this
  spec. `docs/skills.md` links this spec and the skill. The README
  does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.9.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while the skills live under it. The Python
  check is what requires the skill file.
- No tracked file names a hostname, a home directory, or a machine.
