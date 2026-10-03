# Why it is

Design for the reason skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, in the same build step as `debug-the-failure` and
`how-it-fits`. The wording in the skill sections below is the version
to ship. Later sessions tune it by editing the skill file. This spec
stays the record of what we decided and why.

## Purpose

`why-it-is` recovers why a behavior or a threshold exists. The session
reads the code, the history, the issues, and the docs, and returns a
short read that cites those sources.

The read is the work. An edit waits until the user asks for one. A
reason the sources do not state stays out of the read. This skill does
not restate the creed, and it does not restate `scope-the-edit`.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The sources are the four the catalog names, in that order: the code
that sets the behavior and the code that reads it, the history of the
line, the issues and review notes that mention it, and the docs the
repository keeps. History means the commits that introduced or changed
the line. An issue means a tracked report in the project. Docs mean
the documents the repository already has. A source the session could
not open is recorded as unopened, with the reason.

The reply quotes the line and names the file, then states the reason
with a citation for each source it used. A citation is the file and
the line, the commit, the issue, or the document. A statement with no
citation is a guess. A guess stays out of the reason. A guess that is
mentioned is labeled as a guess. When the sources disagree, the read
reports each side with its citations and leaves the disagreement in
place.

When none of the four sources states a reason, that is the answer.
The session names what it opened. A story that would make the line
sensible stays out.

This skill does not edit. That matches the investigation playbook in
the catalog. `debug-the-failure` is the skill that changes code.

Nothing in the skill names a Grok tool or a Claude tool. No hooks.
The skill does not become a tour of one version-control command.

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
skills/why-it-is/SKILL.md
docs/specs/2026-10-02-why-it-is-design.md
```

The creed, `scope-the-edit`, and `set-the-bounds` stay. The catalog
keeps the skillset list and the build order. Its text for this skill
stays the brief.

## Skill

Frontmatter `name` is `why-it-is`. Frontmatter `description` is one
physical line:

```text
Use when you need the reason for a behavior or a threshold. Recover it from the code, the history, the issues, and the docs, and cite each source.
```

The body is the four sections below. Heading text matches. Paragraphs
match, including line breaks.

### The question

Name the behavior or the threshold you were asked about. A threshold
is a number, a limit, a timeout, a flag, or a special case. Quote the
line that sets it, and name the file. The question is why that line
exists.

### Sources

Read the code that sets the behavior and the code that reads it, the
history of that line, the issues and review notes that mention it, and
the docs the repository keeps. Record a source you could not open as
unopened, with the reason.

History means the commits that introduced or changed the line. An
issue means a tracked report in the project. Docs mean the documents
the repository already has.

### The read

Answer with a short read. State the reason, then cite each source you
used. A citation is the file and the line, the commit, the issue, or
the document. A statement with no citation is a guess. Keep a guess
out of the reason. If you mention a guess, label it as a guess.

When the sources disagree, report each side with its citations. Leave
the disagreement in the read.

### No reason on record

When the code, the history, the issues, and the docs do not state a
reason, say that. Name what you opened. A story that would make the
line sensible stays out of the read.

The read is the work of this skill. An edit waits until the user asks
for one.

## What this skill does not do

It does not edit. The user asks for a change before any file is
written.

It does not invent a reason the sources do not state.

It does not restate the creed. It does not diagnose a failure. That
is `debug-the-failure`. It does not map a subsystem. That is
`how-it-fits`.

It does not change the creed, `scope-the-edit`, `set-the-bounds`, or
the catalog.

## Tuning

Edit `skills/why-it-is/SKILL.md` when a session shows that a paragraph
is wrong, too thin, or too long. Keep one copy. When the meaning of a
section changes, note the change in a later spec or in the commit
message. This document keeps the 2026-10-02 wording.

## Implementation check

The build is done when all of these are true:

- `skills/why-it-is/SKILL.md` carries the frontmatter and the four
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
  and `how-it-fits` ship in that same version.
- The root README keeps the install commands and does not link this
  spec. `docs/skills.md` links this spec and the new skill. The
  README does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.4.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while the skills live under it. The Python
  check is what requires each skill file.
- No tracked file names a hostname, a home directory, or a machine.
