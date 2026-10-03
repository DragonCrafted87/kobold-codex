---
name: leave-a-trail
description: Use for a long run or an unattended run. Append one row per decision, with what, why, evidence, and result, to a log a reviewer can read afterward.
---

# Leave a trail

## When it starts

Start a trail for a long run or an unattended run, and when the
user asks for one. A long run is one that will outlast this
sitting, or one a reviewer will need to read afterward.

A large migration that has no narrower playbook still gets this
log. This skill does not write that playbook.

The working list in `run-the-play` is not this log. The
checkboxes in a plan are not this log.

## The row

Append one row per decision. A decision is a choice that rules
out another choice, or a result the next step depends on.

Open a section for the run when that section is not there yet.
The run is the branch, or the plan file, the user named. When
they named neither, the section name is the date and a short name
for the work.

The row is a heading and three lines. The heading is what was
decided. The lines are `Why:`, `Evidence:`, and `Result:`.
Evidence names a command, a file, or a result you observed. Write
the row when the decision is made.

## Where it lives

The log is `.kobold/trail.md` at the repository root. Append to
that file. A second decision adds a row. It does not rewrite an
earlier row.

The log stays local. When that path is not already ignored, add
the pattern `.kobold/trail.md` to the repository ignore rules.
When the repository has no ignore file, create it with that
pattern as its line.

When the reviewer needs the log in the branch, copy the run's
section into the place the project keeps notes a reviewer will
read. That copy is work, and committing it follows `commit`. The
local file stays.

## The same run

A second run of the same work appends to the same section. An
earlier row stays. A decision that is already the last row, with
the same result, stays as that row. A new decision is a new row.
