---
name: isolate-the-work
description: Use when feature work, or the execution of a plan, should sit in its own checkout. Create that checkout when worktrees allows it, and record the path so ship-the-branch can remove it.
---

# Isolate the work

## The work

Isolate feature work, or the execution of a plan, into its own
checkout. The branch is the one the user named. When another skill
in this plugin asks for the checkout, the branch it named is the
branch. When nobody named a branch, keep the branch that is already
checked out, unless that branch is the one a pull request would
merge into. When it is that base, stop and ask which branch the
work belongs on.

A branch that does not exist yet is created as part of the
checkout. Its base is the branch the user named for that. When they
named none, the base is the branch the current checkout would merge
into.

`carry-out-the-plan` runs the plan in the checkout the session is
already in. Continue the rest of this work in the checkout this
skill just made.

## The key

Resolve `worktrees` before creating a checkout. `set-the-bounds` is
that rule. Say the value and the layer that set it.

`ask` stops for a yes that names this checkout. A yes creates it. A
no leaves the work in the current checkout. `deny` leaves the work
in the current checkout. `allow` and `auto` create it. When another
skill names a set of checkouts, each checkout still needs a yes
that names it.

While the user is away, `unattended` still applies.
`set-the-bounds` is that rule.

## The checkout

The checkout is a git worktree for that branch. When the user names
an existing isolated checkout of that branch, that path is the
checkout. When the branch already has a worktree, use that path,
and leave it as the only worktree for the branch.

When the creation fails, stop. Say what failed, and leave the
current checkout as it is.

## The path

Say the path in the reply. The worktree record for that branch is
the record `ship-the-branch` uses when it removes the checkout.

## The same work

A second run uses the checkout that already exists for the branch.
When that path is gone, create it again under the same key. A
checkout that is already there stays there.
