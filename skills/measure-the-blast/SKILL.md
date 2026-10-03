---
name: measure-the-blast
description: Use before a small diff ships. Name what else could break outside the diff, and prove that claim by running the code that would show the break.
---

# Measure the blast

## The diff

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

## The claim

Name every surface outside the diff that a caller of the changed
code can reach. One line each, with why the diff can reach it.
That list is the safety claim.

When no such surface exists, say so and name the diff. There is
nothing to run.

## The run

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

## Leave the tree

Leave the tree alone. A failure the run produced is evidence.
`debug-the-failure` is the skill that fixes a failure that can be
reproduced. This skill stops at the claim and the runs.

The result stays in the reply. Shipping the diff follows
`ship-the-branch`.

## The same diff

A second run measures the diff as it is now. The new claim
replaces the earlier claim. A surface whose code and whose
command are unchanged can be cited from the earlier result. Name
that result. Run a surface that changed.
