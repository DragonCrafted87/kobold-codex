---
name: write-a-skill
description: Use when authoring or revising a skill in this plugin. Write one trigger description and original wording, and keep the manifest check current.
---

# Write a skill

## The trigger

The description is the trigger. It is one physical line. It says
when the skill applies and what the session does. A second line in
the frontmatter is a broken trigger.

The wording is original. A paragraph taken from another skillset
does not ship. `kobold-codex` is the voice.

The skill names no host tool. It adds no hooks.

## The spec

Write a spec in the directory the project uses for design specs.
In this plugin that directory is `docs/specs/`. Name the file with
the date and the skill name, matching the specs already there.

The spec holds the description on one physical line, and it holds
the section bodies that ship. Those bodies are the headings under
the spec's Skill heading. A later revision of the skill file does
not rewrite that spec.

## The file

The skill file is `skills/<group>/<name>/SKILL.md`. The group is
the phase of work the skill serves. Use a group that already
exists. A new group is a folder under `skills/` and a path in the
manifest's `skills` list, added in the same change.

The file starts with frontmatter. `name` is the skill name, and it
matches the folder. `description` is that same line.

The title is the skill name with hyphens written as spaces and the
first letter capitalized. Copy each section body from the spec.

## The check

`tests/check_plugin.py` checks the manifests, and it requires a
branch off main to be ahead on version. It reads no skill file.
When a change needs a new check, add it in the same change.

The plugin version bumps in that change. The manifest description
stays the sentence the catalog's ship rule records. The root
README does not gain a link to the spec, and it does not restate a
section body. `docs/skills.md` links the skill and the spec, and
it does not restate a section body.

A revision edits the skill file and writes a new dated spec. The
new spec records the changed sections and why. A past spec never
changes, even when a paragraph it records is out of date. The
newest spec that records a section is the one the skill matches. A
new heading is added to the skill file.

## The same skill

A second run reads the skill file. When it already has the wording
this revision calls for, leave it.
