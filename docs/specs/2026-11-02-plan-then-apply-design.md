# Carry out the plan: preview, then apply

A revision of `carry-out-the-plan`. The wording below is the version
to ship.

## Why

A code toolkit can preview a multi-file change, apply the preview as
one step, refuse an apply whose files moved since the preview, refuse
a change that adds new errors, and undo an applied change. A session
that skips the preview, or overrides the error gate to get its change
through, loses what those tools are for. The habit belongs with the
rest of running a task and its check, so it is a heading in
`carry-out-the-plan` rather than a new skill.

## Skill: carry-out-the-plan

A new heading before A failed run.

## A multi-file change

When the workspace's tools can preview a change across files, such
as a rename or a refactor that moves code, preview it first. Read the
preview's diff against the task before applying it. A file in the
preview that the task does not name is a failed check, so change the
request rather than applying it.

Apply the previewed change as one step. When another edit changed
one of its files after the preview, the apply is refused. Preview
again and read the new diff.

When the tools refuse a change because it adds new errors, the
refusal is the check failing. Fix the cause, or narrow the change,
and try again. Do not override the refusal to keep the change. When
the tools keep an undo of applied changes, undo is how a wrong
change comes back out, not a hand edit.

## What this change does not do

It does not edit a past spec. It changes no description, key, or
bound. It names no tool.
