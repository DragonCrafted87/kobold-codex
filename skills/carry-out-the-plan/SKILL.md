---
name: carry-out-the-plan
description: Use when a plan has been approved. Run its tasks in order in this session, send independent tasks to another agent only when subagents allows it, and finish each task on the check the plan named.
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

A task may run beside another when the plan does not order one
before the other, and the two tasks change no file in common.
Resolve `subagents` before starting another agent. When that key
allows another agent, those tasks may run together. The other agent
does the task and returns the result. It leaves the plan file alone.
This session marks the checkbox. When `subagents` does not allow
another agent, run those tasks one after another in this session.

The work stays in the checkout you are already in.

While the user is away, `unattended` still applies.
`set-the-bounds` is that rule. This skill does not loosen it.
`stop-at-plan` does not start a task, because the plan is already
written. `safe-steps` may run a task that reads, edits, runs a
check, or writes a plan or a trail. It does not start another
agent, and it does not publish. `through-publish` and `auto` may
run a task that publishes as far as that task's key allows. A
named tool stays on its own key.

## The check

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

## The same plan

On a second run, read the plan again. Skip each checkbox marked
`- [x]`. Begin at the first checkbox still marked `- [ ]`. The
plan's steps were written so an empty checkbox is a place to
start. Finishing from there reaches the same checks a completed
first run would have reached.

When the files on disk make that step impossible to start, stop and
ask. Leave the checkbox empty.
