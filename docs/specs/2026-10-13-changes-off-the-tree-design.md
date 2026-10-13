# Ship the branch: changes made off the tree

A new heading in `ship-the-branch`, from the weekly review of
2026-10-13. The wording below is the version to ship.

## Purpose

In three sessions across two repos, the user had to ask for a
change to be put into git: router settings applied live, a DHCP
change that had to survive a rebuild, and tooling kept outside the
app it served. Each change worked, and none of it was in a
repository.

## Decisions

The rule sits in `ship-the-branch`, before the commits, so it runs
whenever work ships. `scope-the-edit` stays as it is. The plugin
version becomes `2.1.0`, because a heading is added.

## Skill: ship-the-branch

A new heading before Four commits.

## Changes made off the tree

Before the commits, name every change this work made outside the
repository: a router or host setting applied live, a script run in
place, a tool or config kept in another folder. Each one is written
into the repository that serves that system or that app, in the
place that repository keeps such files, and it ships with this
branch. When no repository serves it, name it in the reply and ask
where it lives. A value that is a secret is left out and named by
its kind.

## What this change does not do

It does not commit a secret. It does not edit a past spec.

## Implementation check

- `ship-the-branch` carries the heading above.
- Plugin version is `2.1.0` in both manifests.
- `python3 tests/check_plugin.py` passes.
