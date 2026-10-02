---
name: scope-the-edit
description: Use before changing a file or making a commit. Name the scope of the edit, then add only the plan and the proof that scope calls for.
---

# Scope the edit

## Name the scope

Before editing, name the scope in the reply. The scopes are small,
intermediate, and architectural. Name the scope once, before the first
edit of a change. A commit of work already under that scope is part of
the same change. A settings change, or any other edit whose destination
is already known and that does not change behavior, is small. A bug
fix is intermediate. A change inside a function that has a decision is
intermediate, including a one-line fix. A new subsystem, or a change
that reshapes how the pieces fit together, is architectural. When two
scopes both fit, use the larger one.

## Small

Do the edit in the same turn. The edit is the whole task. The check is
the file that was written.

## Intermediate

Say what is wrong, what will change, and which check will show the
fix. The original repro, an existing command, or a run of the system
can be that check. Carry out the edit and the check in the same turn.
When two checks would change the work, stop and ask which one to run.

## Architectural

Write a plan the reviewer can read. Say what will change, which parts
of the system it touches, what the tests will cover, and what stays
the same. Write the plan where the project keeps plans. When the
project has nowhere for it, use docs/plans/. Stop after the plan.
Implementation starts after an explicit yes to that plan. A yes names
this plan. "Yes", "do it", or the choice the plan just offered counts.
Approval of an earlier piece of work does not carry forward. Once the
conversation has that yes, do the work.

## Real code

When the edit changes a function in C, C++, C#, Python, Java, or
another language in that class, the check follows the code. A
non-trivial function has a decision in it, and the check reaches each
branch. A complex algorithm is one whose decision combines several
conditions, or whose result depends on interacting decisions. Aim at
MC/DC for that algorithm: each condition can change the outcome on its
own. Say whether the check reached branch coverage or MC/DC. Exercise
the system. Use a mock when the dependency cannot be run, such as
hardware or a paid external service. When a branch cannot be reached
from the system boundary, cover that branch with a focused test. Add a
test when no existing run reaches the bar.
