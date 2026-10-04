---
name: write-the-plan
description: Use when an architectural change needs a written plan, or the user asks for one. Write what will change, what it touches, what stays the same, what the checks cover, and the ordered tasks, then stop.
---

# Write the plan

## The document

Write the plan for an architectural change. `scope-the-edit` has
already named that scope. This skill is the document. When the user
asks for a plan, write this same document for the change they named.

## Where it goes

Look for a plans directory the project's docs name. When they name
none, look for a directory that already holds plan files. When the
project has none, use `docs/plans/`, and create that directory when
it is missing. One change is one file. Name the file with the date
and a short name for the change. When the project already has plan
files, match their names. When it has none, use
`docs/plans/YYYY-MM-DD-name.md`, with the name in lowercase words
separated by hyphens.

When that file already holds the four things below and the tasks,
leave it in place. When the user asks for a change to the plan, edit
that file. Leave each `- [x]` mark. A new step, or a step whose text
changed, begins with `- [ ]`.

## What the reviewer reads

Say four things, in prose a reviewer can follow without the session
transcript. What will change. Which parts of the system the change
touches. What stays the same. What the checks cover.

When the project already has headings for a plan, use those headings
and put the four things under them. When the project has no plan
yet, head those four things What will change, What it touches, What
stays the same, and What the checks cover.

## Tasks

Under those four things, list the tasks in the order a later session
will run them. A task names the files it changes, the check that
ends it, and the result that counts as done. The check is a command,
a screen, or a file the reviewer can run or read. A task is one
change and that check. When a task needs an earlier task finished,
it names that task.

A task that changes a function names a check that reaches the bar in
`scope-the-edit`. Write the command and the result in the task.

Each task, and each step under it, begins with an empty checkbox,
written `- [ ]`, on a new plan. Write each step so an empty checkbox
is a valid place to start. A later session marks a finished checkbox
`- [x]`. An edit of the plan follows Where it goes.

## Stop there

Write the file, then stop. Leave every checkbox empty when the plan
has not been approved. An edit keeps the marks from Where it goes.
The work starts when the user approves this plan. `scope-the-edit`
says which reply counts as that approval.
