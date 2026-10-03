---
name: learn-from-the-session
description: Use after a session that stumbled, or that found a preference worth keeping. Name the lesson and edit the skill, playbook, or bounds file that should carry it.
---

# Learn from the session

## The lesson

After a session that stumbled, or that found a preference worth
keeping, name the lesson in the reply before any edit. The lesson
says what happened and what the next session should do.

One lesson is one edit. A second lesson waits for a second pass.

## The home

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

## The edit

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

## The same lesson

A second run reads the home again. When the home already says
what the lesson says, point at that paragraph and stop. When it
does not, the edit still has to land.
