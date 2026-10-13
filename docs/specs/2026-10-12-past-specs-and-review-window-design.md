# Past specs and the review window

Design for two small revisions. Past specs never change, and the
newest spec records a change. The weekly review gains a bounds key
for its first window. This spec revises `write-a-skill`,
`learn-from-the-session`, `set-the-bounds`, and `review-the-week`.
The wording in the sections below is the version to ship. This spec
stays the record of what we decided and why.

## Purpose

Two skills said a pinned paragraph changes in the spec and in the
skill together. That rewrites a dated record. A reviewer can no
longer see what shipped on that date. The rule now: the skill
changes, a new dated spec records the change, and every past spec
stays as it was.

`review-the-week` read seven days in a repo with no report. Seven
days is a guide. Some repos want a longer first window, or all of
their history.

## Decisions

A past spec never changes. The newest spec that records a section
is the one the skill matches. This holds for `write-a-skill`
revisions and for `learn-from-the-session` lessons alike. A lesson
that changes a pinned paragraph now writes a small dated spec. It
still does not bump the plugin version.

`review-window` is a bounds key. Its default is `7`. Its value is a
positive whole number of days, or `all`. `all` reads every session
the host still keeps. The key applies only when a repo has no
report yet. Once a report exists, its start time is the window. A
window the user names for one run overrides the key.

The plugin version becomes `1.4.1`. This branch builds on
`review-the-week`, which ships `1.4.0`. Both changes revise skills
and a key that `1.4.0` introduced or already had, and `1.5.0` is
kept for the Status block and the plan opening lines.

## Where the words live

```text
skills/write-a-skill/SKILL.md
skills/learn-from-the-session/SKILL.md
skills/set-the-bounds/SKILL.md
skills/review-the-week/SKILL.md
docs/specs/2026-10-12-past-specs-and-review-window-design.md
docs/plans/2026-10-12-past-specs-and-review-window.md
docs/skills.md
```

## Skill: write-a-skill

In The check, this paragraph replaces the one that starts "A
revision edits the skill file."

### The check

A revision edits the skill file and writes a new dated spec. The
new spec records the changed sections and why. A past spec never
changes, even when a paragraph it records is out of date. The
newest spec that records a section is the one the skill matches. A
new heading is added to the skill file.

## Skill: learn-from-the-session

In The edit, this paragraph replaces the first one.

### The edit

Edit the home so the next session meets the lesson. When the
paragraph is pinned to a spec, change it in the skill or the
playbook, and write a new dated spec that records the new
paragraph and the lesson. A past spec does not change. The commit
message names the lesson.

## Skill: set-the-bounds

In Defaults, a row before `unattended`:

```text
| `review-window` | `7` | Days the weekly review reads in a repo with no report yet. |
```

In Values, after the sentence on `unattended`:

```text
`review-window` is a positive whole number of days, or `all`.
```

## Skill: review-the-week

In The window, this paragraph replaces the second one.

### The window

run reads sessions written after that time. A repo with no report
reads the window `review-window` sets: a number of days, or every
session the host still keeps when it is `all`. A window the user
names for this run overrides the bound.

## What this change does not do

It does not edit a past spec, including the specs these paragraphs
first shipped in.

It does not change the window once a repo has a report.

## Implementation check

- The four skills carry the text above.
- No file under `docs/specs/` changes except this new spec.
- `docs/skills.md` links this spec in Records.
- Plugin version is `1.4.1` in both manifests.
- `python3 tests/check_plugin.py` passes.
