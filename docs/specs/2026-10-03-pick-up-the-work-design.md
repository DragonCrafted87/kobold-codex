# Pick up the work

Design for the resume-brief skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, as one of the build-order step 7 skills. The wording in
the skill sections below is the version to ship. Later sessions tune
it by editing the skill file. This spec stays the record of what we
decided and why.

## Purpose

`pick-up-the-work` rebuilds a short brief of where the work stands
from the branch, the transcript, and the trail, so a new session can
continue.

The catalog's `pickup` playbook is still a brief. It says this skill
rebuilds the brief. This skill does not write that playbook, and it
does not continue the work. The next request does.

`leave-a-trail` owns the log. This skill reads it.

The creed stays in `skills/kobold-codex/SKILL.md`. This skill does
not restate those principles. The brief is a read. An edit waits
for a separate request.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. A short brief from the branch,
the transcript, and the trail.

The branch is the one the user named, or the current branch. The
transcript is the one the user pointed at. This skill does not
search a host's session store for a transcript the user did not
point at. The two hosts do not share one store. The trail is
`.kobold/trail.md` when that file exists. Another log the user
points at is the trail for that run.

A missing source is named. The brief is built from the sources
that are there. When all three are missing, the session stops and
asks what to read. A brief with no source would be invented
history.

The brief names the branch, the commits and uncommitted files that
are the work, the plan file and the first empty checkbox when a
plan is in progress, the last trail row when a trail exists, and
the next step. A gap stays a gap.

The brief lives in the reply. It is not a commit and not a plan
file. Continuing the work is a separate request, so this skill
can be used at the start of a session without starting the edit.

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
build order. Its text for this skill stays the brief. The `pickup`
and `pause` briefs stay briefs.

## Where the words live

```text
skills/pick-up-the-work/SKILL.md
docs/specs/2026-10-03-pick-up-the-work-design.md
docs/plans/2026-10-03-remaining-skills.md
```

`leave-a-trail` stays the writer of `.kobold/trail.md`. This skill
reads that file and does not append a row.

## Skill

Frontmatter `name` is `pick-up-the-work`. Frontmatter `description`
is one physical line:

```text
Use when a new session should continue work already in progress. Rebuild a short brief from the branch, the transcript, and the trail.
```

The body is the four sections below. Heading text matches.
Paragraphs match, including line breaks. The title is Pick up the
work.

### The sources

Read the branch, the transcript, and the trail. The branch is the
one the user named. When they name none, read the current branch.
The transcript is the one the user pointed at. The trail is
`.kobold/trail.md` when that file exists. When the user points at
another log, read that log as the trail.

When a source is missing, say so. When the branch, the transcript,
and the trail are all missing, stop and ask what to read.

### The brief

Write a short brief in the reply. Name the branch. Name the
commits and the uncommitted files that are this work. When a plan
is in progress, name the plan file and the first checkbox still
marked `- [ ]`. When a trail exists, name the last row. Name the
next step.

The brief uses only what those sources say. A gap stays a gap.
Say what you could not find.

### Leave the tree

Leave the tree alone. The brief is the whole product of this
skill. Continuing the work is a separate request.

### The same point

A second run reads the three sources again. The new brief
replaces the earlier brief.

## What this skill does not do

It does not append a trail row. `leave-a-trail` does that.

It does not write the `pickup` playbook. That brief stays a brief
until its own spec.

It does not continue the work. The next request does.

It does not search a host session store the user did not point at.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, the review skills,
`ship-the-branch`, `run-the-play`, or the catalog.

## Tuning

Edit `skills/pick-up-the-work/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-03 wording.

## Implementation check

The build is done when all of these are true:

- `skills/pick-up-the-work/SKILL.md` carries the frontmatter and
  the four sections above. The heading text matches. The paragraphs
  match this document. The title is Pick up the work.
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
