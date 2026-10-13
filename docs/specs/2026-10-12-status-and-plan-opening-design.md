# Status and plan opening

Design for two revisions. Long work keeps a three-line Status block
that every session reads first and rewrites last. A plan with no
spec opens with three lines that say why the change exists. This
spec revises `carry-out-the-plan`, `leave-a-trail`,
`pick-up-the-work`, `write-the-plan`, `set-the-bounds`, and
`review-the-week`. The wording in the sections
below is the version to ship. Past specs stay as they are. This spec
stays the record of what we decided and why.

## Purpose

A plan's checkboxes say which task is done. The trail says what was
decided. Neither says what is blocking the work right now, and no
skill says to leave the current state when a sitting ends. A long
run with no plan has no status at all.

A plan written without a spec says what will change, but not why.
A reviewer has to reconstruct the why from the tasks.

Success for this version is a Status block that `pick-up-the-work`
reads first, that every session working from a plan rewrites the
moment the status changes, and
that `review-the-week` gathers across repos. And a plan with no spec
that names where it starts, where it ends, and why, before the
tasks.

## Decisions

The Status block is three lines with fixed keys: `Current:`,
`Blocker:`, and `Next:`. One line each. `Blocker: none` when nothing
blocks. It sits under a `## Status` heading.

It is not a kanban file. A separate task list would drift from the
plan's checkboxes, and the trail already keeps the history. The
block lives in what exists. In a plan, it sits at the top, after the
title and before any other heading. With no plan, it sits at the top
of the run's section in `.kobold/trail.md`, before the rows.

The block is rewritten in place. The trail's rows stay append-only.
The block is a claim, and the checkboxes and rows are evidence. When
the block disagrees with the checkboxes, the checkbox wins, and the
session says so and rewrites the block.

Every session that works from a plan rewrites the block when the
status changes, at the moment it changes: a task starts or ends, a
blocker appears or clears, or the next step moves. This is not
limited to long or unattended runs. The rule lives in
`carry-out-the-plan`, beside the rule that marks a checkbox, because
that is the skill that works from a plan. `leave-a-trail` keeps the
block for a run with no plan.

When a plan's Status block changed and `commit-plans` is `auto`,
the whole plan file goes with the next work commit, under `commit`,
as one commit. There is no partial staging. A plan file whose status
changes every sitting would otherwise make a plan commit every
sitting, and splitting one file across two commits is fragile. This
only reduces the number of commits. `commit-plans` still decides
whether a plan file is committed: `ask` still asks, and `never`
leaves it unstaged. When the Status block did not change, the plan
file follows `commit-plans`. `set-the-bounds` names this.

`write-the-plan` writes the block when it writes a plan:
`Current: not started`, `Blocker: none`, and the first task as
`Next:`.

A plan with no spec opens with three lines after the Status block:
`Starting state:` what is true today, `Expected state:` what is true
when the work is done, and `Reason:` why the change is needed. One
sentence each. A plan
that links a spec skips them, because the spec holds the why. Specs
do not gain a question line.

`review-the-week` already opens its reply with a status table from
these blocks. It gains one sentence: a repo with no Status block
gets no row.

No skill is added or renamed. The plugin version becomes `1.5.0`,
the next minor after `1.4.1`. `docs/skills.md` links this spec in
Records.

## Where the words live

```text
skills/leave-a-trail/SKILL.md
skills/pick-up-the-work/SKILL.md
skills/write-the-plan/SKILL.md
skills/set-the-bounds/SKILL.md
skills/review-the-week/SKILL.md
docs/specs/2026-10-12-status-and-plan-opening-design.md
docs/plans/2026-10-12-status-and-plan-opening.md
docs/skills.md
```

## Skill: carry-out-the-plan

In The check, this paragraph is added after the second.

### The check

Rewrite the plan's Status block when the status changes, at the
moment it changes: a task starts or ends, a blocker appears or
clears, or the next step moves. `Current:` names the task and step.
`Blocker:` names what stops the work, or `none`. `Next:` names the
next step. When the block disagrees with the checkboxes, the
checkbox wins. Rewrite the block to match.

## Skill: leave-a-trail

A new section after The row.

### The status

A run with no plan keeps a Status block at the top of the run's
section, before the rows. When the work has a plan, the block is in
the plan, and `carry-out-the-plan` keeps it.

The block is a `## Status` heading and three lines: `Current:`,
`Blocker:`, and `Next:`. `Blocker: none` when nothing blocks.
Rewrite the block in place when the status changes, at the moment
it changes. The rows below it stay append-only.

## Skill: pick-up-the-work

In The sources, this paragraph is added after the first.

### The sources

Read the Status block first, when the plan or the trail has one.
When it disagrees with the plan's checkboxes, the checkbox wins.
Say so in the brief.

In The brief, this sentence is added after "Name the commits and
the uncommitted files that are this work.": "When a Status block
names a blocker, name it."

## Skill: write-the-plan

In What the reviewer reads, these paragraphs are added after the
first.

### What the reviewer reads

A new plan opens with a Status block, after the title: a `## Status`
heading and three lines. `Current: not started`. `Blocker: none`.
`Next:` the first task. `carry-out-the-plan` keeps it current.

When no spec records the change, three lines follow the Status
block: `Starting state:` what is true today, `Expected state:` what
is true when the work is done, and `Reason:` why the change is
needed. One sentence each.
When a spec records the change, link it and skip the three lines.

## Skill: set-the-bounds

In Publishing sets, this paragraph is added after the first.

### Publishing sets

When a plan file's Status block changed and `commit-plans` is
`auto`, the whole plan file stages with the next commit under
`commit`, as one commit. That saves a plan commit. It does not widen
what `commit-plans` allows. When `commit-plans` is `ask`, the plan
file is offered on its own. When it is `never`, the plan file stays
unstaged. Do not stage part of a file. When the Status block did not
change, the plan file follows `commit-plans`.

## Skill: review-the-week

In The report, the first paragraph gains one sentence after "A
blocked row goes first.": "A repo with no Status block gets no row."

## What this change does not do

It does not add a kanban file or a task list.

It does not change a past spec.

It does not add a question line to specs.

It does not make the trail's rows editable.

## Implementation check

- The six skills carry the text above.
- No file under `docs/specs/` changes except this new spec.
- `docs/skills.md` links this spec in Records.
- Plugin version is `1.5.0` in both manifests.
- `python3 tests/check_plugin.py` passes.
