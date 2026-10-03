---
name: try-several-shapes
description: Use when the first shape of a change would stick. Run several candidates, pick a base, and fold the strongest pieces of the others into it.
---

# Try several shapes

## The moment

Use this skill when the first shape of a change would stick. The
shape would stick when the change would be hard to undo, or when
more than one structure could hold the work and the rest of the
work will sit on the one that is chosen.

Name that moment in the reply, in a sentence, before naming
candidates. A small edit that is easy to undo does not need a
second shape. Say so, and stop. `scope-the-edit` still names the
scope of whatever is about to be edited.

## The candidates

Name at least two candidates before building any of them. Three
is the set when the user names none. Each candidate is one
sentence that says how it differs from the others. A wider set
waits until the user names the extra candidates.

Name the work's branch before any checkout. The branch for a
candidate is that name, a hyphen, and a short name for the
candidate. `isolate-the-work` is the rule for a branch that does
not exist yet, and for the checkout.

Resolve `worktrees` once for the set. `set-the-bounds` is that
rule. When the value allows a checkout, each candidate is built
in its own checkout. When the value is `ask`, `isolate-the-work`
asks once per checkout, and the yes names that checkout. When the
value does not allow a checkout, leave each candidate as the
sentence in the reply, and build none of them until the base is
picked.

When each candidate has its own checkout, the candidates share no
files. This skill builds each candidate in its checkout. When
`subagents` allows it, those builds may run together. This skill
reads each result, then picks the base and folds.

The candidate sentences, and a checkout the key allows, are the
exploration. `scope-the-edit` applies to the fold.

## The base

The base is the candidate the user names. When the user names
none, name the base you would pick, what it keeps, and what it
gives up, and stop before the fold.

The fold follows `scope-the-edit`. When that scope is
architectural, `write-the-plan` writes the plan, and the fold
waits until that plan is approved. The base named there is the
base. When the scope is small or intermediate, the yes that names
the base is the gate. A yes for a different candidate does not
carry.

## The fold

Fold into the base the pieces from the other candidates that the
base does not already have and that still belong in it. Leave a
piece out when it fights the base. Say which piece, and why.

The other candidates are not merged whole. The base, after the
fold, is the change.

When a candidate that is not the base has its own checkout,
remove that checkout when `worktrees` allows the removal. A
checkout that still holds work the fold did not take stays. Say
so, and name the path. When the key does not allow the removal,
leave the checkout and name the path. The base's checkout stays.
`ship-the-branch` is the skill that removes that one later.

## The same attempt

A second run reads the candidates again. A base the user already
named stays the base. A fold that is already in the tree stays,
and the reply points at it. A candidate checkout that was removed
stays removed.
