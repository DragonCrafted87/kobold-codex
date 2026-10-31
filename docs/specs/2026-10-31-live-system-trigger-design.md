# Set the bounds: the live system trigger

A lesson from the weekly review of 2026-10-31. It revises
`set-the-bounds`. The wording below is the version to ship.

## The lesson

Four sessions across two repos deployed new code, applied manifests
to a running cluster, ran a database migration, or took a backup
with `set-the-bounds` unloaded, and one of them loaded no skill at
all. The description named only git actions, an unattended stretch,
and a named tool, so a change to a live system did not trigger it.
The next session resolves the bounds before any deploy, apply,
migration, backup, or restore, even when the user asked for it by
name.

## Skill: set-the-bounds

The description becomes:

```text
description: Use before a commit, a push, a pull request, a merge, a force-push, an unattended stretch, a named tool, or a change to a live system such as a deploy, a migration, a backup, or a restore. Resolve the four bounds layers, and revise one layer when the user wants a change.
```

In Resolve first, the first sentence becomes the paragraph below.
The rest of the section stays.

### Resolve first

Before a commit of the work, a commit of plans, a commit of specs, a
push, a pull request, a merge, a force-push, an unattended stretch,
a named tool, or a change to a live system, read the four layers and
use the resolved value. A deploy, an apply to a running cluster, a
database migration, a backup, and a restore change a live system.
They resolve the bounds even when the user asked for the change by
name, and the tool that makes the change is the named tool.

## What this change does not do

It adds no key and changes no default. It does not edit a past spec.
