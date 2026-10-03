# Write the doc

Design for the document skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, as one of the build-order step 7 skills. The wording in
the skill sections below is the version to ship. Later sessions tune
it by editing the skill file. This spec stays the record of what we
decided and why.

## Purpose

`write-the-doc` writes or revises a README, a spec, a pull request,
or a commit message. It uses the headings the project already uses,
in sentences a new reader can follow.

`ship-the-branch` said commit subjects and pull requests follow the
records this repository already has, and that this skill is the
later one for that prose. `ship-the-branch` does not add a template,
and it leaves an open pull request's title and body alone. This
skill writes the words. The publishing keys and `github-write`
decide what gets posted.

`kobold-codex` is the voice. This skill does not restate it. The
catalog's ship rule stays the rule for this plugin's README.
`scope-the-edit` still decides the plan and the proof for the edit.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. A README, a spec, a pull request,
or a commit message, in the headings the project already uses, in
sentences a new reader can follow.

The document is the one the user named. Another kind of document
counts when the project already has that kind. When the user names
none, the session asks. Guessing a README when they wanted a commit
message would edit the wrong file.

Headings come from an existing file of that kind. A project with no
file of that kind falls back in this order: a spec uses the headings
of the specs already in the spec directory, a commit message uses
the subject shape of recent commits, a pull request uses the
sections of recent pull requests. When no example exists, the
session asks which headings to use and does not invent a house
template. `ship-the-branch` already refused a second template. This
skill agrees.

A rule the project already records for that file still holds. This
plugin's README rule lives in the catalog's ship rule. This skill
does not restate that rule, and it does not move a section body
into a file whose rule keeps section bodies out.

Sentences name a path, a command, or a result. A new reader should
follow them without the session transcript. That is the same bar
`write-the-plan` sets for a plan, applied to these documents.

This skill writes the words and stops. Committing follows `commit`,
`commit-plans`, or `commit-specs`, whichever set the file belongs
to. Opening a pull request follows `pull-request`. Changing a pull
request that is already open follows `github-write`.
`ship-the-branch` integrates the branch and keeps an open pull
request's title and body. Drafting a body before that pull request
exists is this skill. Editing the body after it is open is a
`github-write`.

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
stays the README rule.

## Where the words live

```text
skills/write-the-doc/SKILL.md
docs/specs/2026-10-03-write-the-doc-design.md
docs/plans/2026-10-03-remaining-skills.md
```

The sentence in `ship-the-branch` that leaves commit and pull
request prose to this skill stays. This skill agrees with it: the
ship does not gain a template.

## Skill

Frontmatter `name` is `write-the-doc`. Frontmatter `description`
is one physical line:

```text
Use when writing or revising a README, a spec, a pull request, or a commit message. Use the headings the project already uses, in sentences a new reader can follow.
```

The body is the five sections below. Heading text matches.
Paragraphs match, including line breaks. The title is Write the
doc.

### The document

Write or revise the document the user named. A README, a spec, a
pull request, and a commit message are the documents this skill
writes. When the user names another kind of document the project
already has, write that kind too.

When the user names none, stop and ask which document.

### The headings

Use the headings the project already uses for that kind of
document. Read an existing file of that kind before writing.

When the project has no file of that kind, a spec uses the
headings of the specs in the spec directory. A commit message
uses the subject shape of the repository's recent commits. A pull
request uses the sections of the repository's recent pull
requests. When no example exists, ask which headings to use, and
stop before writing.

A rule the project already records for that file still holds.
This skill does not move a section body into a file whose rule
keeps section bodies out.

### The sentences

Write sentences a new reader can follow without the session
transcript. Name the path, the command, or the result the reader
needs. `kobold-codex` is the voice. This skill does not restate
it.

The edit follows `scope-the-edit`.

### Where it stops

This skill writes the words. Committing them follows `commit`,
`commit-plans`, or `commit-specs`, whichever set the file belongs
to. Opening a pull request follows `pull-request`. Changing a
pull request that is already open follows `github-write`.
`set-the-bounds` resolves the key. `ship-the-branch` is the skill
that integrates the branch, and it keeps an open pull request's
title and body.

### The same document

A second run reads the document again. When it already uses the
project's headings and the sentences still match the work, leave
it. When the work has moved and the document has not, revise the
document.

## What this skill does not do

It does not invent a house template when the project has no
example. It asks which headings to use.

It does not restate a section body into a file whose rule keeps
section bodies out.

It does not open the pull request or make the commit.
`ship-the-branch` and the publishing keys do that.

It does not edit the title or the body of a pull request that is
already open. That write follows `github-write`.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, the review skills,
`ship-the-branch`, `run-the-play`, or the catalog.

## Tuning

Edit `skills/write-the-doc/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-03 wording.

## Implementation check

The build is done when all of these are true:

- `skills/write-the-doc/SKILL.md` carries the frontmatter and the
  five sections above. The heading text matches. The paragraphs
  match this document. The title is Write the doc.
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
