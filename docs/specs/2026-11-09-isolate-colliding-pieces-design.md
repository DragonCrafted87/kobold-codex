# Isolate the work: colliding parallel pieces

A revision of `isolate-the-work`, from the ultracode research of
2026-11-09. The wording below is the version to ship.

## Why

A fan-out that edits overlapping paths needs isolation or the
workers fight. Per-file checkouts for every migration file would be
wasteful. The rule is: isolate only when writes would collide, then
fold back.

## Skill: isolate-the-work

The description and the new heading Parallel pieces that collide
match the skill file on this branch.

## What this change does not do

It does not edit a past spec. It does not make per-file checkouts
the default for every migration. It adds no key and no bound. It
names no project, host, or tool.
