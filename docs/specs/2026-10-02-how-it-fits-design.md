# How it fits

Design for the subsystem skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, in the same build step as `debug-the-failure` and
`why-it-is`. The wording in the skill sections below is the version to
ship. Later sessions tune it by editing the skill file. This spec
stays the record of what we decided and why.

## Purpose

`how-it-fits` is the read a session does before changing a subsystem.
The reply names the runtime path, the owner of the behavior, and the
layer the change belongs on.

The read is the work. An edit waits until the user asks for one.
`scope-the-edit` then decides the plan and the proof. This skill does
not restate those scopes, and it does not restate the creed.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The reply names three things, and a read that skips one of them is
not finished. The runtime path is one request, command, or event,
followed from the entry the user named through the behavior and out
to what the caller observes. A fork that this question does not care
about is named and left. The owner is the package, module, or
directory a change to that behavior would land in. A caller that only
invokes the behavior does not own it. When two places both look like
the owner, the reply names both and says which one it would change.

A layer is a boundary the code already has. The usual ones are the
interface a caller uses, the rule behind that interface, the storage,
and the edge that talks to another system. A new rule belongs on the
layer that already decides that kind of rule. When the change needs a
layer the code does not have, the session says so and stops. Adding
that layer is an architectural edit. This skill does not write that
plan. `write-the-plan` is still unshipped, and `scope-the-edit`
already requires the plan once the user asks for the change.

This skill does not edit. That matches the investigation playbook in
the catalog. `debug-the-failure` is the skill that changes code,
because its brief includes the fix.

Nothing in the skill names a Grok tool or a Claude tool. No hooks.

These three investigation skills ship together. The plugin version
becomes `0.4.0` in that change. The manifest description stays the
stable sentence in the catalog's ship rule, and later skills leave
that sentence as it is. The root README stays the introduction and
the install guide. It does not record this decision. `docs/skills.md`
links the skill and this spec, and it does not restate the skill
paragraphs. Install commands stay as they are.

`tests/check_plugin.py` pins the new section bodies to this document
the same way it pins the creed, `scope-the-edit`, and
`set-the-bounds`, and it requires version `0.4.0` and the stable
description.

## Where the words live

```text
skills/how-it-fits/SKILL.md
docs/specs/2026-10-02-how-it-fits-design.md
```

The creed, `scope-the-edit`, and `set-the-bounds` stay. The catalog
keeps the skillset list and the build order. Its text for this skill
stays the brief.

## Skill

Frontmatter `name` is `how-it-fits`. Frontmatter `description` is one
physical line:

```text
Use before changing a subsystem. Name the runtime path, the package that owns the behavior, and the layer the change belongs on.
```

The body is the four sections below. Heading text matches. Paragraphs
match, including line breaks.

### Read first

Read the subsystem this change would touch before editing it. In the
reply, name the runtime path, the owner, and the layer. The read is
the work of this skill. An edit waits until the user asks for one.

### Runtime path

Follow one request, one command, or one event from the entry the user
named, through the place the behavior happens, and out to what the
caller observes. Name the functions or the modules on that path, in
order. When the path forks, follow the fork this question cares about,
and name the forks you left.

### Owner

Name the package, module, or directory that owns the behavior. A
change to that behavior lands there. A caller that only invokes the
behavior does not own it. When two places both look like the owner,
name both, say which one you would change, and say why.

### Layer

Name the layer the change belongs on. A layer is a boundary the code
already has. The usual ones are the interface a caller uses, the rule
behind that interface, the storage, and the edge that talks to another
system. Put a new rule on the layer that already decides that kind of
rule. When the change needs a layer the code does not have, say so and
stop. Adding that layer is an architectural edit.

## What this skill does not do

It does not edit. The user asks for a change before any file is
written.

It does not write the architectural plan. `scope-the-edit` requires
that plan once the user asks for a change that adds a layer or
reshapes the subsystem.

It does not restate the creed. It does not diagnose a failure. That
is `debug-the-failure`. It does not recover why a line was written.
That is `why-it-is`.

It does not change the creed, `scope-the-edit`, `set-the-bounds`, or
the catalog.

## Tuning

Edit `skills/how-it-fits/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-02 wording.

## Implementation check

The build is done when all of these are true:

- `skills/how-it-fits/SKILL.md` carries the frontmatter and the four
  sections above. The heading text matches. The paragraphs match this
  document.
- `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`,
  `skills/set-the-bounds/SKILL.md`, and the three specs those skills
  pin are unchanged. The catalog's skill briefs stay. Its ship rule
  records the stable manifest description and points the skill map
  at `docs/skills.md`.
- `tests/check_plugin.py` fails when a new paragraph, the new
  frontmatter, the version, the manifest description, or a restatement
  of a skill paragraph in the README drifts.
- Plugin version is `0.4.0` in `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and both descriptions match the
  stable sentence in the catalog's ship rule. `debug-the-failure`
  and `why-it-is` ship in that same version.
- The root README keeps the install commands and does not link this
  spec. `docs/skills.md` links this spec and the new skill. The
  README does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.4.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while the skills live under it. The Python
  check is what requires each skill file.
- No tracked file names a hostname, a home directory, or a machine.
