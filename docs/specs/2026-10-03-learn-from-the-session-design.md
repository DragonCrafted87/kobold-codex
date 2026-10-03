# Learn from the session

Design for the lesson skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, as one of the build-order step 7 skills. The wording in
the skill sections below is the version to ship. Later sessions tune
it by editing the skill file. This spec stays the record of what we
decided and why.

## Purpose

`learn-from-the-session` names a lesson after a session that
stumbled, or that found a preference worth keeping, and edits the
existing skill, playbook, or bounds file that should carry it. A
new personal skill is created when no current file is the right
home.

`set-the-bounds` writes a bounds layer. `write-a-skill` authors or
revises a skill in this plugin when the change adds a skill, a
heading, or a check. This skill names the lesson and makes the
smaller edit. A lesson does not bump the plugin version.

The creed stays in `skills/kobold-codex/SKILL.md`. This skill does
not restate those principles. `scope-the-edit` still decides the
plan and the proof for the edit.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. Name the lesson. Edit the file
that should carry it. Create a personal skill only when no current
file is the home.

One lesson is one edit. The lesson says what happened and what the
next session should do, and it is named in the reply before the
edit. A pile of lessons in one pass would hide which sentence
changed which behavior.

The home is the file that already decides this kind of thing. The
creed and `scope-the-edit` stay as they are. A lesson that belongs
in one of those two is named, and the file stays. Later skills do
not rewrite those two. A bounds value is a key, and
`set-the-bounds` writes the layer. This skill stops at the lesson
and the key, so the plugin does not grow a second writer for
bounds files.

A new skill in this plugin, or a revision that adds a heading or a
check, belongs to `write-a-skill`. The ship rule for a plugin skill
is a spec, a pin, and a version bump. A lesson is none of those.
This skill names that handoff and stops.

A paragraph the check pins is changed in the spec and in the skill
or the playbook, so the two bodies still match. The spec's
decisions stay. The commit message names the lesson. The tuning
note on each shipped spec says the section bodies can be corrected
when a paragraph is wrong. The check is what forces the two copies
to move together. A lesson does not bump the plugin version. The
version moves when a skill ships.

A personal skill is a file outside this plugin and outside the
project's committed plugin skills. The session asks where it
should live. It does not guess a host directory. When the user
names no path, nothing is written. The description is the lesson's
trigger, on one physical line. The body is the procedure. This
plugin's check does not pin that file.

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
build order. Its text for this skill stays the brief.

## Where the words live

```text
skills/learn-from-the-session/SKILL.md
docs/specs/2026-10-03-learn-from-the-session-design.md
docs/plans/2026-10-03-remaining-skills.md
```

`set-the-bounds` stays the writer of a bounds file.
`write-a-skill` stays the procedure for a new plugin skill.

## Skill

Frontmatter `name` is `learn-from-the-session`. Frontmatter
`description` is one physical line:

```text
Use after a session that stumbled, or that found a preference worth keeping. Name the lesson and edit the skill, playbook, or bounds file that should carry it.
```

The body is the four sections below. Heading text matches.
Paragraphs match, including line breaks. The title is Learn from
the session.

### The lesson

After a session that stumbled, or that found a preference worth
keeping, name the lesson in the reply before any edit. The lesson
says what happened and what the next session should do.

One lesson is one edit. A second lesson waits for a second pass.

### The home

The home is the existing file that already decides this kind of
thing. Look at the skills, the playbooks, and the bounds files
that are already loaded.

The creed and `scope-the-edit` stay as they are. When the lesson
belongs in one of those two, name it and stop.

When the lesson is a bounds value, name the key and the value.
`set-the-bounds` writes the layer. This skill stops at the lesson
and the key.

When no current file is the home, ask where a personal skill
should live. When the user names a path, that path is the home.
When they name none, stop, and leave every file as it is.

A new skill in this plugin, or a revision that adds a heading or
a check, belongs to `write-a-skill`. Name that, and stop.

### The edit

Edit the home so the next session meets the lesson. When the
paragraph is pinned to a spec, change the paragraph in the spec
and in the skill or the playbook, so the two bodies still match.
Leave the spec's decisions in place. The commit message names the
lesson.

A personal skill is one file outside this plugin. The description
is the lesson's trigger, on one physical line. The body is the
procedure the next session should follow. This plugin's check
does not pin that file.

The edit follows `scope-the-edit`. A lesson does not bump the
plugin version.

### The same lesson

A second run reads the home again. When the home already says
what the lesson says, point at that paragraph and stop. When it
does not, the edit still has to land.

## What this skill does not do

It does not write a bounds file. `set-the-bounds` does that.

It does not add a skill, a heading, or a check to this plugin.
`write-a-skill` does that.

It does not guess a host directory for a personal skill.

It does not bump the plugin version.

It does not change the creed or `scope-the-edit`. A lesson that
belongs in one of those two is named, and the file stays.

It does not change `set-the-bounds`, the investigation skills, the
plan skills, the review skills, `ship-the-branch`, `run-the-play`,
or the catalog, except for a pinned paragraph whose lesson names
that paragraph.

## Tuning

Edit `skills/learn-from-the-session/SKILL.md` when a session shows
that a paragraph is wrong, too thin, or too long. Keep one copy.
When the meaning of a section changes, note the change in a later
spec or in the commit message. This document keeps the 2026-10-03
wording.

## Implementation check

The build is done when all of these are true:

- `skills/learn-from-the-session/SKILL.md` carries the frontmatter
  and the four sections above. The heading text matches. The
  paragraphs match this document. The title is Learn from the
  session.
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
