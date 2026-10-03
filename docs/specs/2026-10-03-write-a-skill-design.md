# Write a skill

Design for the skill-authoring skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, as one of the build-order step 7 skills. The wording in
the skill sections below is the version to ship. Later sessions tune
it by editing the skill file. This spec stays the record of what we
decided and why.

## Purpose

`write-a-skill` authors or revises a skill in this plugin's voice.
The skill has one trigger description, original wording, and a check
that the skill file matches its spec. It ships in the plugin so both
hosts load it.

The catalog's ship rule is the source for the manifest sentence, the
README, and `docs/skills.md`. This skill points at that rule. It
does not copy the sentence into a second home.

`kobold-codex` is the voice. `scope-the-edit` still decides the plan
and the proof. `learn-from-the-session` handles a lesson that
corrects a pinned paragraph without adding a skill, a heading, or a
check.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. One trigger description, original
wording, and a check that the skill file matches its spec. The
skill ships in the plugin.

The description is one physical line. That line is the trigger. A
wrapped description breaks the frontmatter the check reads.

The wording is original. A paragraph taken from another skillset
does not ship. The skill names no Grok tool and no Claude tool. It
adds no hooks. `kobold-codex` stays the voice, and this skill does
not restate those principles.

The spec is the copy the check compares. It lives in `docs/specs/`
in this plugin, named with the date and the skill name, matching
the specs already there. The description sits on one physical line
in the spec. The section bodies that ship are the headings under
the spec's Skill heading.

The skill file is `skills/<name>/SKILL.md`. The title is the skill
name with hyphens written as spaces and the first letter
capitalized, the same rule the playbook titles use. The section
bodies are copied, including line breaks. A rewrap would fail the
check.

`tests/check_plugin.py` gains the pin in the same change. The
plugin version bumps in that change. The manifest description stays
the sentence the catalog's ship rule records. This skill does not
quote that sentence. The root README does not gain a spec link and
does not restate a section body. `docs/skills.md` links the skill
and the spec.

A revision changes the spec and the skill file together. A new
heading is added in both, in the same order, and the check's
heading list gains it in that order. On a second run the spec wins.
When a section differs, the spec's body is copied into the skill
file. A lesson that corrected only the skill file has to land in
the spec first, which is what `learn-from-the-session` already
requires.

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
build order. Its text for this skill stays the brief. Its ship rule
stays the rule this skill points at.

## Where the words live

```text
skills/write-a-skill/SKILL.md
docs/specs/2026-10-03-write-a-skill-design.md
docs/plans/2026-10-03-remaining-skills.md
```

The catalog's ship rule stays the record of the manifest sentence
and of what the README is allowed to contain.

## Skill

Frontmatter `name` is `write-a-skill`. Frontmatter `description`
is one physical line:

```text
Use when authoring or revising a skill in this plugin. Write one trigger description, original wording, and a check that the skill file matches its spec.
```

The body is the five sections below. Heading text matches.
Paragraphs match, including line breaks. The title is Write a
skill.

### The trigger

The description is the trigger. It is one physical line. It says
when the skill applies and what the session does. A second line in
the frontmatter is a broken trigger.

The wording is original. A paragraph taken from another skillset
does not ship. `kobold-codex` is the voice. This skill does not
restate those principles.

The skill names no host tool. It adds no hooks.

### The spec

Write a spec in the directory the project uses for design specs.
In this plugin that directory is `docs/specs/`. Name the file with
the date and the skill name, matching the specs already there.

The spec holds the description on one physical line, and it holds
the section bodies that ship. Those bodies are the headings under
the spec's Skill heading.

### The file

The skill file is `skills/<name>/SKILL.md`. It starts with
frontmatter. `name` is the skill name. `description` is that same
line.

The title is the skill name with hyphens written as spaces and the
first letter capitalized. Copy each section body from the spec,
including line breaks. Do not rewrap a copied line.

### The check

`tests/check_plugin.py` pins those bodies to that spec, the same
way it pins the skills already shipped. Update the check in the
same change that adds the file.

The plugin version bumps in that change. The manifest description
stays the sentence the catalog's ship rule records. The root
README does not gain a link to the spec, and it does not restate a
section body. `docs/skills.md` links the skill and the spec, and
it does not restate a section body.

A revision changes the spec and the skill file together. A new
heading is added in both, in the same order.

### The same skill

A second run reads the spec and the skill file. When the bodies
already match and the check already pins them, leave both files.
When a section differs, copy the spec's body into the skill file.
The spec is the record.

## What this skill does not do

It does not correct a pinned paragraph that adds no skill, no
heading, and no check. `learn-from-the-session` does that, and it
edits the spec and the file together.

It does not quote the manifest sentence. The catalog's ship rule
records it.

It does not put a spec link, or a section body, in the root README.

It does not add hooks.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, the review skills,
`ship-the-branch`, `run-the-play`, or the catalog.

## Tuning

Edit `skills/write-a-skill/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-03 wording.

## Implementation check

The build is done when all of these are true:

- `skills/write-a-skill/SKILL.md` carries the frontmatter and the
  five sections above. The heading text matches. The paragraphs
  match this document. The title is Write a skill.
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
