# Try several shapes

Design for the candidates skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, as one of the build-order step 7 skills. The wording in
the skill sections below is the version to ship. Later sessions tune
it by editing the skill file. This spec stays the record of what we
decided and why.

## Purpose

`try-several-shapes` runs several candidates when the first shape of
a change would stick, picks a base, and folds the strongest pieces
of the others into that base.

`isolate-the-work` creates a checkout. `fan-out` runs a split whose
pieces share no state. `scope-the-edit` still decides the plan and
the proof for the fold, which is the edit that ships.
`set-the-bounds` resolves `worktrees`. This skill reads that value.
It does not revise a layer.

The creed stays in `skills/kobold-codex/SKILL.md`. This skill does
not restate those principles.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. When the first shape would stick,
run several candidates, pick a base, and fold the strongest pieces
of the others into it.

The shape would stick when the change would be hard to undo, or
when more than one structure could hold the work and the rest of
the work will sit on the one that is chosen. A small edit that is
easy to undo stays on `scope-the-edit` and does not grow a second
shape.

Candidates are named before any of them is built. Two is the
minimum. Three is the set when the user names none. Three is the
same bound `fan-out` uses when a request names a kind and not the
pieces. A wider set waits until the user names the extra
candidates. Each candidate says, in one sentence, how it differs.

The candidate sentences, and a checkout `worktrees` allows, are
exploration. They are not the edit that ships. `scope-the-edit`
applies to the fold. A plan is not required before the sentences
are written or before a checkout the key allows is created.

`worktrees` is resolved once for the set. `ask` is one yes, and
the yes names the set. When the value allows a checkout, each
candidate is built in its own checkout through `isolate-the-work`.
The branch name is the work's branch, a hyphen, and a short name
for that candidate. Those checkouts share no files, so `fan-out`
runs that split. This skill names the candidates and reads the
report. When the value does not allow a checkout, the candidates
stay as sentences until the base is picked, and only the base is
built.

The base is the candidate the user names. When the user names
none, the session names the base it would pick, what that base
keeps, and what it gives up, and it stops before the fold. The
shape would stick, so the fold waits for a name. When the fold's
scope is architectural, `write-the-plan` writes the plan and the
fold waits until that plan is approved. The base named in the plan
is the base. When the scope is small or intermediate, the yes that
names the base is the gate. One gate, not two.

The fold takes pieces the base does not already have and that
still belong in it. A piece that fights the base stays out, and
the reply says why. The other candidates are not merged whole.

A checkout for a candidate that is not the base is removed when
`worktrees` allows the removal, unless it still holds work the
fold did not take. The base's checkout stays.
`ship-the-branch` removes that one later. When the key does not
allow the removal, the path is named and the checkout stays.

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
skills/try-several-shapes/SKILL.md
docs/specs/2026-10-03-try-several-shapes-design.md
docs/plans/2026-10-03-remaining-skills.md
```

`isolate-the-work`, `fan-out`, and `ship-the-branch` stay the
skills this one calls. This spec does not restate their
procedures.

## Skill

Frontmatter `name` is `try-several-shapes`. Frontmatter
`description` is one physical line:

```text
Use when the first shape of a change would stick. Run several candidates, pick a base, and fold the strongest pieces of the others into it.
```

The body is the five sections below. Heading text matches.
Paragraphs match, including line breaks. The title is Try several
shapes.

### The moment

Use this skill when the first shape of a change would stick. The
shape would stick when the change would be hard to undo, or when
more than one structure could hold the work and the rest of the
work will sit on the one that is chosen.

Name that moment in the reply, in a sentence, before naming
candidates. A small edit that is easy to undo does not need a
second shape. Say so, and stop. `scope-the-edit` still names the
scope of whatever is about to be edited.

### The candidates

Name at least two candidates before building any of them. Three
is the set when the user names none. Each candidate is one
sentence that says how it differs from the others. A wider set
waits until the user names the extra candidates.

Name the work's branch before any checkout. The branch for a
candidate is that name, a hyphen, and a short name for the
candidate. `isolate-the-work` is the rule for a branch that does
not exist yet, and for the checkout.

Resolve `worktrees` once for the set. `set-the-bounds` is that
rule. When the value allows a checkout, each candidate is built
in its own checkout. When the value is `ask`, one yes covers the
set, and the yes names the set. When the value does not allow a
checkout, leave each candidate as the sentence in the reply, and
build none of them until the base is picked.

When each candidate has its own checkout, the candidates share no
files. `fan-out` runs that split. This skill names the candidates
and reads the report.

The candidate sentences, and a checkout the key allows, are the
exploration. `scope-the-edit` applies to the fold.

### The base

The base is the candidate the user names. When the user names
none, name the base you would pick, what it keeps, and what it
gives up, and stop before the fold.

The fold follows `scope-the-edit`. When that scope is
architectural, `write-the-plan` writes the plan, and the fold
waits until that plan is approved. The base named there is the
base. When the scope is small or intermediate, the yes that names
the base is the gate. A yes for a different candidate does not
carry.

### The fold

Fold into the base the pieces from the other candidates that the
base does not already have and that still belong in it. Leave a
piece out when it fights the base. Say which piece, and why.

The other candidates are not merged whole. The base, after the
fold, is the change.

When a candidate that is not the base has its own checkout,
remove that checkout when `worktrees` allows the removal. A
checkout that still holds work the fold did not take stays. Say
so, and name the path. When the key does not allow the removal,
leave the checkout and name the path. The base's checkout stays.
`ship-the-branch` is the skill that removes that one later.

### The same attempt

A second run reads the candidates again. A base the user already
named stays the base. A fold that is already in the tree stays,
and the reply points at it. A candidate checkout that was removed
stays removed.

## What this skill does not do

It does not become the general split of unrelated work.
`fan-out` does that.

It does not invent a checkout procedure. `isolate-the-work` does
that.

It does not remove the base's checkout. `ship-the-branch` does
that.

It does not fold before the base is named, or before the plan
when the fold is architectural.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, the review skills,
`ship-the-branch`, `run-the-play`, or the catalog.

## Tuning

Edit `skills/try-several-shapes/SKILL.md` when a session shows
that a paragraph is wrong, too thin, or too long. Keep one copy.
When the meaning of a section changes, note the change in a later
spec or in the commit message. This document keeps the 2026-10-03
wording.

## Implementation check

The build is done when all of these are true:

- `skills/try-several-shapes/SKILL.md` carries the frontmatter
  and the five sections above. The heading text matches. The
  paragraphs match this document. The title is Try several
  shapes.
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
