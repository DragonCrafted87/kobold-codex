---
name: carry-out-the-plan
description: Use when a plan has been approved. Run its tasks in order, hand fast tasks and independent tasks to another agent only when subagents allows it, and finish each task on the check the plan named.
---

# Carry out the plan

## An approved plan

Start from the plan file the user approved. Read that file before
the first task. The approval has to name this file. When no file is
named, stop and ask which plan to run.

`scope-the-edit` says which reply counts as approval.

## In order

Run the tasks in the order the plan lists. Finish a task before you
start a task that names it as earlier work. A task is done when
every checkbox that belongs to it is `- [x]`.

## Beside this session

Resolve `subagents` once, before the first task that would start
another agent. When the value is `ask`, ask once. The yes names
this plan file, and it covers every agent this run starts for the
plan, fast work included. A later run asks again. `set-the-bounds`
is that rule.

A task may run beside another when the plan does not order one
before the other, and the two tasks change no file in common. When
`subagents` allows another agent, those tasks may run together. The
other agent does the task and returns the result. It leaves the
plan file alone. This session marks the checkbox. When `subagents`
does not allow another agent, run those tasks one after another in
this session.

A task that is not fast work and runs in another agent uses
`model`. When `model` is absent, it uses the model already running
the session.

The work stays in the checkout you are already in.

While the user is away, `unattended` still applies.
`set-the-bounds` is that rule. `stop-at-plan` does not start a
task, because the plan is already written.

## The fast model

A task whose kind is `rename-or-move`, `follow-a-pattern`, or
`docs-or-config` is fast work. `write-the-plan` names the kind. A
task with any other kind, with no kind, or with a kind outside that
list stays on the model running this session.

The fast model is `model-fast`. When `model-fast` is absent, it is
`model`. When both are absent, it is the model running this
session, and fast work runs in this session.

Fast work goes to another agent on the fast model, including a task
the plan orders after another, when `subagents` allows another
agent. When it does not, run the task in this session.
When the other agent cannot start on that model, run the task in
this session, and say so.

Some work never goes to the fast model, whatever its kind: deleting
a file, a force-push, a migration, and a change to production
config. A task that does any of these stays in this session.

## The brief

The brief for a fast task names the files to change, the existing
code to copy, the check that ends the task, and the notes that task
needs. This session picks those notes. A note the task does not
need stays out of the brief.

The worker changes only the files the brief names. It does not
commit, push, or edit the plan file. It returns its diff and the
output of the check.

Read the diff from the tree yourself before marking the checkbox.
The worker's account of its change is not that diff. A diff that
changes a file the brief did not name, or that misses a change the
brief asked for, is a failed check.

## The check

Run the narrow checks first. Those are the project's lint and type
checks on the changed files, then the tests most relevant to those
files. A narrow check that fails is a failed check. When the
project has no lint or type check, say so and go on. Then run the
check the plan names.

A task's check is done when you have run the check the plan names
and the result is the one the plan describes. Record the result you
observed. Mark the checkbox for that step `- [x]`.

When a fast worker's check fails, this session takes that task over
once, on its own model, starting from the worker's diff. When that
check fails too, or when a task this session ran fails its check,
stop. Report the task, the check, and the result. Leave every later
checkbox empty.

When a task names no check, stop and ask for the check before
starting the task.

Before each commit of the work, run the gate. The gate is a
filtered test list when the project has a way to produce one: the
tests selected for the changed files or for the affected area. A
project skill, an instruction file, or the project's test tool can
name that way. When none does, the gate is the full suite. Say
which gate ran. When it fails, stop before the commit, and name the
tests that failed.

Marking a checkbox is part of finishing that step. Committing the
plan file follows `commit-plans`. A task that commits, pushes, or
opens a pull request still follows `set-the-bounds`.

## A failed run

A failed run is a command that did not reach a result: a missing
tool or package, a wrong path, or a crash before the check reports.
A check that runs and reports a failure is a failed check, not a
failed run.

After a failed run, pick one move from this list. Retry unchanged.
Install the missing piece, then retry. Fix the path, then retry.
Switch to another tool for the same step. Hand the task to the
model running this session. Stop and report. There is no other
move. An install that reaches the network follows `shell-network`.

Three attempts is the limit for one run. The first run is the first
attempt. After the third failed attempt, the only move is stop and
report. The limit holds for a worker and for this session. A change
of move does not reset the count.

Handing the task over is a fast worker's move. It ends the worker's
attempts, and it is the one takeover The check allows. This session
starts its own count, from the worker's diff.

Stop and report names the run, each attempt and its move, and the
last error output.

## The same plan

On a second run, read the plan again. Skip each checkbox marked
`- [x]`. Begin at the first checkbox still marked `- [ ]`. The
plan's steps were written so an empty checkbox is a place to
start. Finishing from there reaches the same checks a completed
first run would have reached.

When the files on disk make that step impossible to start, stop and
ask. Leave the checkbox empty.
