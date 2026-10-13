---
name: ship-the-branch
description: Use when the checks pass and the branch should be integrated. Commit the specs, the plans, and the work under their own keys, then push, open a pull request, or merge, and remove the worktree, each as the resolved bounds allow.
---

# Ship the branch

## The branch

Ship the branch the user named. When the user names none, ship the
current branch. When the checkout has no branch, stop, and say so.

When that branch is the branch a pull request would merge into,
stop, and name it.

Run every check the plan or the change named. A check the user
names for this ship is one of those checks. Run them before any
later action in this skill. A failed check stops the ship. A check
that cannot be run stops the ship, and the reply names the reason.
When no check is named, stop and ask which check to run.

Before those checks, run the narrow checks. Those are the project's
lint and type checks on the files the branch changes, then the
tests most relevant to those files. After the named checks, run the
gate. The gate is a filtered test list when the project has a way
to produce one: the tests selected for the changed files or for the
affected area. A project skill, an instruction file, or the
project's test tool can name that way. When none does, the gate is
the full suite. Say which gate ran. A gate that already passed on
the same tree can be cited. Name that run. A narrow check or a gate
that fails stops the ship the same way a failed check does.

When the user is away, `unattended` still decides how far the ship
goes. `set-the-bounds` is that rule.

The reply names each action this run took and each one it skipped.
Name the key that governed it. A ship that stops on the checks does
not commit, push, open a pull request, merge, or remove a checkout.

## Changes made off the tree

Before the commits, name every change this work made outside the
repository: a router or host setting applied live, a script run in
place, a tool or config kept in another folder. Each one is written
into the repository that serves that system or that app, in the
place that repository keeps such files, and it ships with this
branch. When no repository serves it, name it in the reply and ask
where it lives. A value that is a secret is left out and named by
its kind.

## Four commits

Commit the specs under `commit-specs`, then the plans under
`commit-plans`, then the reviews under `commit-reviews`, then the
work under `commit`. Each set is its own
commit. `set-the-bounds` says which files belong in each set and
which value applies. Say the key, the value, and the layer that
set it before the commit.

`ask` stops for a yes that names this commit. A yes makes the
commit, and the ship continues. A no leaves the set unstaged and
stops the ship. `never` leaves the set unstaged, and the ship
continues. `auto` makes the commit. An empty set is skipped.

A second run leaves a finished commit as it is. It commits a set
only when that set is still uncommitted and still allowed. When a
commit fails, stop the ship, and say what failed.

## The remote

Push the branch under `push`, including a force-push under
`force-push`, then open one pull request under `pull-request`,
then merge that pull request under `merge`. Say the key, the
value, and the layer that set it before the action.

`ask` stops for a yes that names this action. A yes does it, and
the ship continues. A no skips it and stops the ship. `never`
skips that action, and the ship continues. `auto` and `open`
proceed.

A push the remote rejects stops the ship. Say what was rejected,
and leave the remote as it is.

When `push` did not update the remote, and the remote does not
have the commits this ship would push, stop before the pull
request. Say that the remote does not have them.

The pull request targets the base the user named. When the user
names none, it targets the branch this one would merge into. When
a pull request for this branch is already open, leave that pull
request as it is, including its title and its body.

Merge the pull request. When none is open, skip the merge and say
so.

When an action fails, stop the ship, and say what failed.

## The worktree

Remove the isolated checkout for this branch when that checkout is
not the primary one. When the user names a checkout, that is the
one. When no separate checkout exists, say so.

Leave the checkout in place when it is the primary one, or when it
still has uncommitted files. Say which of those is true.

When a clean isolated checkout is the one to remove, `worktrees`
is the key. Say the value and the layer that set it. `ask` stops
for a yes that names this removal. A yes removes the checkout. A
no leaves it. `deny` leaves it. `allow` and `auto` remove it.

When the removal goes ahead and the session is standing in that
checkout, return to the primary checkout first. When that return
cannot be done, say so and leave the checkout. When the removal
fails, say what failed, and leave the checkout in place.

## The same branch

A second run reads the bounds again and starts at the first action
in this skill that is not done and that the bounds still allow.
The checks run again. The earlier sections say what a finished
commit, an open pull request, a merged pull request, and a removed
checkout look like on that run.
