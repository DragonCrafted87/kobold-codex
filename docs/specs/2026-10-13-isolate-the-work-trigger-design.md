# Isolate the work: the trigger

A lesson from the weekly review of 2026-10-13. It revises
`isolate-the-work`. The wording below is the version to ship.

## The lesson

In eight sessions across two repos, the user had to ask for a
separate checkout before `isolate-the-work` loaded. Most were fixes
meant for a pull request, made while the main checkout held other
work or another agent. `worktrees` was already `auto`. The
description named only feature work and plans, so a fix did not
trigger it. The next session isolates a pull-request fix, and any
work started beside other work in progress, before the first edit.

## Skill: isolate-the-work

The description becomes:

```text
description: Use when feature work, a fix meant for a pull request, or the execution of a plan should sit in its own checkout, and always when the current checkout holds other work in progress or another agent. Create that checkout when worktrees allows it, and record the path so ship-the-branch can remove it.
```

In The work, this paragraph replaces the first two sentences.

### The work

Isolate feature work, a fix meant for a pull request, or the
execution of a plan, into its own checkout. Do this before the
first edit, without waiting for the user to ask. When the current
checkout already holds uncommitted work, another branch's work in
progress, or another agent, the new work always gets its own
checkout.

## What this change does not do

It does not change the `worktrees` key or its default. It does not
edit a past spec. It does not bump the plugin version.
