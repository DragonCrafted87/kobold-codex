# Measure the blast

Design for the safety-claim skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, as one of the build-order step 7 skills. The wording in
the skill sections below is the version to ship. Later sessions tune
it by editing the skill file. This spec stays the record of what we
decided and why.

## Purpose

`measure-the-blast` names what else could break outside a small diff,
then proves that claim by running the code that would show the break.

`review-the-diff` leaves a problem outside the diff out of its
findings and names it in one line. `stress-the-change` keeps the
changed-lines pass inside the diff. Both specs leave this proof to
the later skill. This is that skill.

The creed stays in `skills/kobold-codex/SKILL.md`. This skill does
not restate those principles. `scope-the-edit` still decides the
plan and the proof when an edit is asked for. This skill does not
edit.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The catalog brief is the content. Before a small diff ships, name
what else could break outside the diff, and prove the safety claim
by running the code that would show the break.

The occasion in the catalog is a small diff about to ship. The
review specs also point here for a proof outside the lines, without
a size test. This skill accepts the diff the user named. When they
name none, uncommitted work is the diff, and when there is none,
the current branch against the branch it would merge into. The
reply says which diff was measured. A size test that refused every
diff the review skills hand over would leave that handoff with
nowhere to go.

A surface is something outside the diff that a caller of the
changed code can reach. The claim is the list of those surfaces,
one line each, with why the diff can reach it. An empty list is a
finished claim. There is nothing to run.

The proof is a run, not a second paragraph about why the break is
unlikely. Each surface gets the command a caller would run, and
the result. A run that shows the break fails the claim for that
surface. A run that cannot be started stops the skill. Later
surfaces stay unrun, so a blocked proof is not reported as a pass.
The claim holds for the diff only when every named surface was run
and none of them showed the break.

This skill does not file findings, does not fix the break, and
does not ship the diff. `review-the-diff` files findings.
`debug-the-failure` fixes a failure that can be reproduced.
`ship-the-branch` ships.

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
skills/measure-the-blast/SKILL.md
docs/specs/2026-10-03-measure-the-blast-design.md
docs/plans/2026-10-03-remaining-skills.md
```

The sentences in `review-the-diff` and `stress-the-change` that
leave the outside-the-diff proof to this skill stay. This skill
agrees with them: the review stays inside the diff, and this skill
runs the outside surfaces.

## Skill

Frontmatter `name` is `measure-the-blast`. Frontmatter
`description` is one physical line:

```text
Use before a small diff ships. Name what else could break outside the diff, and prove that claim by running the code that would show the break.
```

The body is the five sections below. Heading text matches.
Paragraphs match, including line breaks. The title is Measure the
blast.

### The diff

Prove the safety claim for the diff the user named. A named
branch, a named range, a pull request, or a named set of files is
that diff.

When the user names none, the diff is the uncommitted work. When
there is no uncommitted work, the diff is the current branch
against the branch it would merge into. Say which diff you
measured.

`review-the-diff` reports defects in the lines the diff changes.
This skill starts where that report stops: the surfaces outside
those lines.

### The claim

Name every surface outside the diff that a caller of the changed
code can reach. One line each, with why the diff can reach it.
That list is the safety claim.

When no such surface exists, say so and name the diff. There is
nothing to run.

### The run

For each surface on the claim, run the code a caller of the
changed code would run. Record the command and the result in the
reply.

A run that shows the break means the claim fails for that
surface. Say the surface and the result. A run that cannot be
started stops the skill. Name the surface and the reason. Leave
the later surfaces unrun.

The claim holds for a surface when its run finished and did not
show the break. The claim holds for the diff when it holds for
every surface you named.

### Leave the tree

Leave the tree alone. A failure the run produced is evidence.
`debug-the-failure` is the skill that fixes a failure that can be
reproduced. This skill stops at the claim and the runs.

The result stays in the reply. Shipping the diff follows
`ship-the-branch`.

### The same diff

A second run measures the diff as it is now. The new claim
replaces the earlier claim. A surface whose code and whose
command are unchanged can be cited from the earlier result. Name
that result. Run a surface that changed.

## What this skill does not do

It does not file findings inside the diff. `review-the-diff` and
`stress-the-change` do that.

It does not fix a break the run produced. `debug-the-failure`
does that.

It does not ship the diff. `ship-the-branch` does that.

It does not treat an unrun surface as a pass.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, the plan skills, the review skills,
`ship-the-branch`, `run-the-play`, or the catalog.

## Tuning

Edit `skills/measure-the-blast/SKILL.md` when a session shows that
a paragraph is wrong, too thin, or too long. Keep one copy. When
the meaning of a section changes, note the change in a later spec
or in the commit message. This document keeps the 2026-10-03
wording.

## Implementation check

The build is done when all of these are true:

- `skills/measure-the-blast/SKILL.md` carries the frontmatter and
  the five sections above. The heading text matches. The
  paragraphs match this document. The title is Measure the blast.
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
