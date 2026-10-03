# Carry out the plan

Design for the execution skill. The catalog in
`docs/specs/2026-10-02-remaining-skills-design.md` named this skill on
2026-10-02, in the same build step as `write-the-plan`. The wording
in the skill sections below is the version to ship. Later sessions
tune it by editing the skill file. This spec stays the record of what
we decided and why.

## Purpose

`carry-out-the-plan` runs an approved plan, task by task, in the
current session. Each task ends on the check the plan named. A second
run starts at the first unfinished checkbox.

`write-the-plan` writes the file and stops. This skill starts after
the user approves that file. `scope-the-edit` says which reply counts
as the approval. The creed's "Re-running converges" principle stays
in `skills/kobold-codex/SKILL.md`. The checkboxes are how this skill
keeps that promise.

Success for this version is a skill that a Grok session and a Claude
Code session can both load, whose section bodies match the skill
sections below.

## Decisions

The session reads the plan file the user approved. The approval has
to name that file. A yes to an earlier plan, or a yes to the spec,
is a different approval. When no file is named, the session asks
which plan to run and does not start.

Tasks run in the order the plan lists. A task that names an earlier
task waits for that task. A task is done when every checkbox that
belongs to it is `- [x]`. The mark is the one `write-the-plan`
writes. This skill does not invent a second mark.

Independent tasks may run at the same time, through another agent,
when `subagents` allows it. Independent means the plan does not order
one task before the other, and the tasks change no file in common.
The session that is carrying out the plan resolves `subagents` first.
The other agent does the task and returns the result. It leaves the
plan file alone. This session marks the checkbox. When `subagents`
does not allow another agent, those tasks run one after another here.
`fan-out` stays the later skill for a wider split. This skill does
not start a review panel per task. `review-the-diff` is that later
skill.

The work stays in the checkout the session is already in.
`isolate-the-work` is the later skill that puts a plan in a separate
checkout.

A task is finished when the check the plan named has been run and the
result is the one the plan described. The session records the result
it observed. A failed check stops the run. Later checkboxes stay
empty. A task with no check stops the run before that task starts.
The session asks for the check. It does not supply one the plan left
out.

A second run reads the plan again, skips `- [x]`, and begins at the
first `- [ ]`. The plan was written so that empty checkbox is a valid
start. When the files on disk make that step impossible to start, the
session asks, and the checkbox stays empty.

Marking a checkbox is part of finishing the step. Committing the plan
file follows `commit-plans`. A task that commits other files, pushes,
or opens a pull request still follows `set-the-bounds`. The plan does
not raise those keys.

Nothing in the skill names a Grok tool or a Claude tool. No hooks.

These two plan skills ship together. The plugin version becomes
`0.5.0` in that change. The manifest description stays the stable
sentence in the catalog's ship rule, and later skills leave that
sentence as it is. The root README stays the introduction and the
install guide. It does not record this decision. `docs/skills.md`
links the skill and this spec, and it does not restate the skill
paragraphs. Install commands stay as they are.

`tests/check_plugin.py` pins the new section bodies to this document
the same way it pins the creed, `scope-the-edit`, `set-the-bounds`,
and the investigation skills, and it requires version `0.5.0` and
the stable description.

## Where the words live

```text
skills/carry-out-the-plan/SKILL.md
docs/specs/2026-10-02-carry-out-the-plan-design.md
docs/plans/2026-10-02-plan-skills.md
```

The creed, `scope-the-edit`, `set-the-bounds`, and the three
investigation skills stay. The catalog keeps the skillset list and
the build order. Its text for this skill stays the brief.

## Skill

Frontmatter `name` is `carry-out-the-plan`. Frontmatter `description`
is one physical line:

```text
Use when a plan has been approved. Run its tasks in order in this session, send independent tasks to another agent only when subagents allows it, and finish each task on the check the plan named.
```

The body is the five sections below. Heading text matches. Paragraphs
match, including line breaks.

### An approved plan

Start from the plan file the user approved. Read that file before
the first task. The approval has to name this file. When no file is
named, stop and ask which plan to run.

`scope-the-edit` says which reply counts as approval.

### In order

Run the tasks in the order the plan lists. Finish a task before you
start a task that names it as earlier work. A task is done when
every checkbox that belongs to it is `- [x]`.

### Beside this session

A task may run beside another when the plan does not order one
before the other, and the two tasks change no file in common.
Resolve `subagents` before starting another agent. When that key
allows another agent, those tasks may run together. The other agent
does the task and returns the result. It leaves the plan file alone.
This session marks the checkbox. When `subagents` does not allow
another agent, run those tasks one after another in this session.

The work stays in the checkout you are already in.

### The check

A task's check is done when you have run the check the plan names
and the result is the one the plan describes. Record the result you
observed. Mark the checkbox for that step `- [x]`.

When the check fails, stop. Report the task, the check, and the
result. Leave every later checkbox empty.

When a task names no check, stop and ask for the check before
starting the task.

Marking a checkbox is part of finishing that step. Committing the
plan file follows `commit-plans`. A task that commits, pushes, or
opens a pull request still follows `set-the-bounds`.

### The same plan

On a second run, read the plan again. Skip each checkbox marked
`- [x]`. Begin at the first checkbox still marked `- [ ]`. The
plan's steps were written so an empty checkbox is a place to
start. Finishing from there reaches the same checks a completed
first run would have reached.

When the files on disk make that step impossible to start, stop and
ask. Leave the checkbox empty.

## What this skill does not do

It does not write the plan. `write-the-plan` does that, and it stops
with the checkboxes empty.

It does not treat approval of an earlier file as approval of this
one.

It does not open a separate checkout. `isolate-the-work` is the skill
for that.

It does not send a dependent task to another agent, and it does not
start a review panel for each task.

It does not fill in a check the plan left out.

It does not change the creed, `scope-the-edit`, `set-the-bounds`,
the investigation skills, or the catalog.

## Tuning

Edit `skills/carry-out-the-plan/SKILL.md` when a session shows that a
paragraph is wrong, too thin, or too long. Keep one copy. When the
meaning of a section changes, note the change in a later spec or in
the commit message. This document keeps the 2026-10-02 wording.

## Implementation check

The build is done when all of these are true:

- `skills/carry-out-the-plan/SKILL.md` carries the frontmatter and
  the five sections above. The heading text matches. The paragraphs
  match this document.
- `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`,
  `skills/set-the-bounds/SKILL.md`, the three investigation skills,
  and the specs those skills pin are unchanged. The catalog's skill
  briefs stay. Its ship rule records the stable manifest description
  and points the skill map at `docs/skills.md`.
- `tests/check_plugin.py` fails when a new paragraph, the new
  frontmatter, the version, the manifest description, or a restatement
  of a skill paragraph in the README drifts.
- Plugin version is `0.5.0` in `.claude-plugin/plugin.json` and
  `.claude-plugin/marketplace.json`, and both descriptions match the
  stable sentence in the catalog's ship rule. `write-the-plan` ships
  in that same version.
- The root README keeps the install commands and does not link this
  spec. `docs/skills.md` links this spec and the new skill. The
  README does not restate the paragraphs.
- `grok plugin validate` accepts the plugin and reports version
  `0.5.0`. The component line counts the `skills/` directory, so it
  stays `1 skill dir(s)` while the skills live under it. The Python
  check is what requires each skill file.
- No tracked file names a hostname, a home directory, or a machine.
