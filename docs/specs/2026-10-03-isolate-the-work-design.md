# Isolate the work

Design for the checkout skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, as one of the build-order step 7 skills. The wording in
the skill sections below is the version to ship. Later sessions tune
it by editing the skill file. This spec stays the record of what we
decided and why.

## Purpose

`isolate-the-work` puts feature work, or the execution of a plan, in
its own checkout when `worktrees` allows it. It records the path so
`ship-the-branch` can remove that checkout.

`set-the-bounds` resolves `worktrees`. This skill reads the resolved
value and creates the checkout. It does not revise a layer.
`carry-out-the-plan` runs a plan in the checkout the session is
already in. This skill is how that checkout gets created first.
`ship-the-branch` removes the isolated checkout for the branch. This
skill does not remove it.

The creed stays in `skills/kobold-codex/SKILL.md`. This skill does
not restate those principles. `scope-the-edit` still decides the
plan and the proof when an edit is asked for.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. Feature work, or the execution of
a plan, lands in a worktree or another isolated checkout when
`worktrees` allows it. The path is recorded so `ship-the-branch` can
remove it.

The checkout this version creates is a git worktree. Git keeps the
path with the branch, and `ship-the-branch` already removes the
isolated checkout for the branch. A second path file would record
the same fact again. This skill does not add one, and it does not
edit `ship-the-branch`. When the user names an existing isolated
checkout of that branch, that path is the checkout. This skill does
not invent a second clone beside the worktree.

The branch is the one the user named. Another skill in this plugin
may ask for the checkout, and the branch it named counts. A current
branch that is the one a pull request would merge into is not a
place feature work lands. The session asks which branch to use. A
branch that does not exist yet is created with the checkout. Its
base is the base the user named, or the branch the current checkout
would merge into.

`ask` stops for a yes that names this checkout. A no, and `deny`,
leave the work in the current checkout. `allow` and `auto` create
it. One checkout per branch. A branch that already has a worktree
keeps that path. While the user is away, `unattended` still
applies. This skill does not loosen it.

This skill does not run the plan and does not ship the branch.

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
skills/isolate-the-work/SKILL.md
docs/specs/2026-10-03-isolate-the-work-design.md
docs/plans/2026-10-03-remaining-skills.md
```

The creed, `scope-the-edit`, `set-the-bounds`, the investigation
skills, the plan skills, the review skills, `ship-the-branch`, and
`run-the-play` stay. The four playbooks stay. The sentences in
`carry-out-the-plan` and `ship-the-branch` that name this skill as
the later checkout skill stay. This skill agrees with them: the plan
runs in the checkout the session is already in, and the ship removes
a checkout it did not create.

## Skill

Frontmatter `name` is `isolate-the-work`. Frontmatter `description`
is one physical line:

```text
Use when feature work, or the execution of a plan, should sit in its own checkout. Create that checkout when worktrees allows it, and record the path so ship-the-branch can remove it.
```

The body is the five sections below. Heading text matches.
Paragraphs match, including line breaks. The title is Isolate the
work.

### The work

Isolate feature work, or the execution of a plan, into its own
checkout. The branch is the one the user named. When another skill
in this plugin asks for the checkout, the branch it named is the
branch. When nobody named a branch, keep the branch that is already
checked out, unless that branch is the one a pull request would
merge into. When it is that base, stop and ask which branch the
work belongs on.

A branch that does not exist yet is created as part of the
checkout. Its base is the branch the user named for that. When they
named none, the base is the branch the current checkout would merge
into.

`carry-out-the-plan` runs the plan in the checkout the session is
already in. Continue the rest of this work in the checkout this
skill just made.

### The key

Resolve `worktrees` before creating a checkout. `set-the-bounds` is
that rule. Say the value and the layer that set it.

`ask` stops for a yes that names this checkout. A yes creates it. A
no leaves the work in the current checkout. `deny` leaves the work
in the current checkout. `allow` and `auto` create it.

While the user is away, `unattended` still applies. This skill does
not loosen it.

### The checkout

The checkout is a git worktree for that branch. When the user names
an existing isolated checkout of that branch, that path is the
checkout. When the branch already has a worktree, use that path,
and leave it as the only worktree for the branch.

When the creation fails, stop. Say what failed, and leave the
current checkout as it is.

### The path

Say the path in the reply. The worktree record for that branch is
the record `ship-the-branch` uses when it removes the checkout.

This skill does not remove the checkout.

### The same work

A second run uses the checkout that already exists for the branch.
When that path is gone, create it again under the same key. A
checkout that is already there stays there.

## What this skill does not do

It does not run the plan. `carry-out-the-plan` does that.

It does not remove the checkout. `ship-the-branch` does that.

It does not write a second file that repeats the worktree path.

It does not resolve a bounds file and it does not revise one.
`set-the-bounds` does that. This skill reads `worktrees` before it
creates a checkout.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, the review skills,
`ship-the-branch`, `run-the-play`, or the catalog.

## Tuning

Edit `skills/isolate-the-work/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-03 wording.

## Implementation check

The build is done when all of these are true:

- `skills/isolate-the-work/SKILL.md` carries the frontmatter and
  the five sections above. The heading text matches. The paragraphs
  match this document. The title is Isolate the work.
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
