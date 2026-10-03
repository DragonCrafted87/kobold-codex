# Prove the product

Design for the user-level drive skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, as one of the build-order step 7 skills. The wording in
the skill sections below is the version to ship. Later sessions tune
it by editing the skill file. This spec stays the record of what we
decided and why.

## Purpose

`prove-the-product` writes a project-local verification skill when a
repo has no scripted way to drive the app the way a user does, proves
that skill once, and re-runs it on a later pass so the map of
features stays honest.

The creed's proof principle stays in `skills/kobold-codex/SKILL.md`.
This skill does not restate it. `scope-the-edit` still decides the
plan and the proof for the edit that writes the skill.
`set-the-bounds` resolves `browser` and `shell-network` when a step
needs them. This skill reads those values. It does not revise a
layer.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. When a repo has no scripted way
to drive the app the way a user does, write a project-local
verification skill and prove it once. A later pass re-reads the
features and re-runs that skill.

A scripted user-level drive performs the actions a user performs
and checks what the user would see. A unit test of a function is
not that drive. When the repo already has the drive, this skill
names it and stops. A second skill beside a drive that already
works would split the map.

The skill is project-local. It is not a skill in this plugin, and
it does not bump this plugin's version. The session looks for a
directory the project already uses for a skill a session loads.
When the project has none, the session asks where the file should
live and does not guess a host directory. The two hosts do not
share one path, and a guessed path would be wrong on one of them.

The file is one `SKILL.md` in a directory named for the skill. The
name comes from the app and the drive. The description is one
physical line and says when to run the drive. Each step is a user
action and the result the user would see, taken from a read of the
features the app has. Every feature in that read gets a step. A
step needs a feature.

The first proof is one run of those steps. A step that drives a
browser uses `browser`. A step that reaches the network uses
`shell-network`. A key that stops the step stops the proof. A
failed step stops the proof. The skill file stays, and the reply
names the step and the result, so the next edit has a failure to
start from.

A later pass re-reads the features and re-runs the skill. A
feature with no step is added. A step whose feature is gone is
removed. The run after that edit is what makes the map honest. A
map that was edited and not re-run is not done.

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
skills/prove-the-product/SKILL.md
docs/specs/2026-10-03-prove-the-product-design.md
docs/plans/2026-10-03-remaining-skills.md
```

The verification skill this procedure writes lives in the project
that owns the app. It is not a file under this plugin's `skills/`
directory.

## Skill

Frontmatter `name` is `prove-the-product`. Frontmatter
`description` is one physical line:

```text
Use when a repo has no scripted way to drive the app the way a user does. Write a project-local verification skill, prove it once, and re-run it so the map stays honest.
```

The body is the five sections below. Heading text matches.
Paragraphs match, including line breaks. The title is Prove the
product.

### The drive

A scripted user-level drive performs the actions a user performs
and checks what the user would see. A unit test of a function is
not that drive.

When the repo already has that drive, name it and stop. Do not
write a second one. When it does not, write a project-local
verification skill that is the drive.

### The skill file

Look for a directory the project already uses for a skill a
session loads. When the project has one, write the skill there.
When it has none, stop and ask where the skill should live.
Leave the tree alone until the user names the directory.

The skill is one directory with one `SKILL.md`. The directory
name is the skill name. Name it for the app and for the drive.
The description is one physical line, and it says when to run
the drive.

Each step is an action a user would take and the result the user
would see. The steps come from a read of the features the app
has. Every feature in that read gets a step. A step needs a
feature.

The edit follows `scope-the-edit`.

### Prove it once

Run the skill once, the way a user would move through it. Record
the command or the actions, and the result.

When a step drives a browser, `browser` is the key. When a step
reaches the network, `shell-network` is the key. `set-the-bounds`
resolves the key. This skill does not loosen it. A key that stops
the step stops the proof. Say the key, the value, and the layer.

A failed step stops the proof. The skill file stays, and the
reply names the step and the result. A proof that finishes shows
every step and the result you observed.

### A later pass

A later pass re-reads the features and re-runs the skill. Add a
step for a feature the skill does not cover. Remove a step whose
feature is gone. Re-run after that edit. The map is honest when
every feature has a step, every step has a feature, and the run
matches those steps.

### The same map

A second run reads the features and the skill file again. A step
that already matches a feature, and whose last run still
describes the app, can be cited. Name that run. Run a step that
is new or whose feature changed.

## What this skill does not do

It does not add a skill to this plugin. `write-a-skill` does that.

It does not guess a host directory when the project has no skill
directory.

It does not replace a user-level drive the repo already has.

It does not treat a unit test as that drive.

It does not call the map honest until the edited skill has been
run.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, the review skills,
`ship-the-branch`, `run-the-play`, or the catalog.

## Tuning

Edit `skills/prove-the-product/SKILL.md` when a session shows that
a paragraph is wrong, too thin, or too long. Keep one copy. When
the meaning of a section changes, note the change in a later spec
or in the commit message. This document keeps the 2026-10-03
wording.

## Implementation check

The build is done when all of these are true:

- `skills/prove-the-product/SKILL.md` carries the frontmatter and
  the five sections above. The heading text matches. The
  paragraphs match this document. The title is Prove the product.
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
