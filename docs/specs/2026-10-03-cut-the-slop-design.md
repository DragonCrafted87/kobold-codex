# Cut the slop

Design for the prose-and-comment pass. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, as one of the build-order step 7 skills. The wording in
the skill sections below is the version to ship. Later sessions tune
it by editing the skill file. This spec stays the record of what we
decided and why.

## Purpose

`cut-the-slop` takes one pass over prose or a diff and removes
narration, stock phrasing, and comments that restate the code. A
comment that carries a real constraint is encoded in the structure,
and then the comment is dropped.

`kobold-codex` is the voice. This skill does not restate it.
`scope-the-edit` still decides the plan and the proof for the edit.
The pass keeps outward behavior.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. One pass. Remove narration, stock
phrasing, and comments that restate the code. Encode a real
constraint in the structure, then drop the comment.

The pass is the prose or the diff the user named. When they name
none, it is the uncommitted diff. When there is no uncommitted
diff, the session asks which text. The pass does not wander into
files the user did not include.

Narration is a sentence that retells the next line or the next
step. Stock phrasing is a sentence that could sit on any other
change and names nothing in this one. A banned-word list was set
aside. A list would go stale, and it would flag a concrete
sentence that happens to share a word with the list.

A comment that restates the code comes out. A comment that names a
constraint the code does not enforce stays until that constraint
is in the structure. The structure is a name, a type, a check, or
the shape of the data. That list is the creed's data-shape
principle applied to a comment, without restating the principle.
When the constraint cannot move without changing outward behavior,
the comment stays, and the reply says why.

The pass does not change outward behavior. A spot that would
change it stays. The reply names the spot. `scope-the-edit` still
classifies the edit. A comment-only deletion is the small scope
that skill already describes. Moving a constraint into a function
is whatever scope that edit actually is.

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
skills/cut-the-slop/SKILL.md
docs/specs/2026-10-03-cut-the-slop-design.md
docs/plans/2026-10-03-remaining-skills.md
```

The creed stays the voice. This skill names the three things the
pass removes and the place a constraint goes.

## Skill

Frontmatter `name` is `cut-the-slop`. Frontmatter `description` is
one physical line:

```text
Use when prose or a diff needs a pass for narration, stock phrasing, and comments that restate the code. Encode a real constraint in the structure, then drop the comment.
```

The body is the four sections below. Heading text matches.
Paragraphs match, including line breaks. The title is Cut the
slop.

### The pass

Take one pass over the prose or the diff the user named. When
they name none, the pass is the uncommitted diff. When there is
no uncommitted diff, stop and ask which prose or which diff.

The pass covers that text and nothing past it. `kobold-codex` is
the voice for the prose that remains.

### What comes out

Narration comes out. Narration is a sentence that retells the
next line or the next step. Stock phrasing comes out. Stock
phrasing is a sentence that could sit on any other change and
names nothing in this one. A comment that restates the code comes
out.

A comment that names a constraint stays for the next section.

### A constraint

When a comment carries a constraint the code does not enforce,
put that constraint in the structure, then drop the comment. The
structure is a name, a type, a check, or the shape of the data.

When the constraint cannot move into the structure without
changing outward behavior, leave the comment and say why.

The pass does not change outward behavior. A spot that would
change it stays, and the reply names the spot.

The edit follows `scope-the-edit`. When the edit changes a
function, the check is the one that skill names.

### The same pass

A second run reads the same prose or the same diff. A sentence
that is already gone stays gone. A constraint that already lives
in the structure stays there. The reply points at the file.

## What this skill does not do

It does not keep a list of banned words.

It does not change outward behavior in order to drop a comment.

It does not pass over text the user did not name, once a target
is named.

It does not restate the creed. `kobold-codex` is the voice.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, the review skills,
`ship-the-branch`, `run-the-play`, or the catalog.

## Tuning

Edit `skills/cut-the-slop/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-03 wording.

## Implementation check

The build is done when all of these are true:

- `skills/cut-the-slop/SKILL.md` carries the frontmatter and the
  four sections above. The heading text matches. The paragraphs
  match this document. The title is Cut the slop.
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
