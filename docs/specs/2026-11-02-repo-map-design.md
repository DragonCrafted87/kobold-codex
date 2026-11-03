# Scope the edit: the repo map

A revision of `scope-the-edit`. The wording below is the version to
ship.

## Why

A code toolkit can offer a repo map: the workspace's files and key
symbols, ranked by how often they are referenced, cut to a budget,
with vendored and generated paths left out. It pays off at the start
of broad work and wastes context on a one-file fix. The scope named
in `scope-the-edit` already sorts those cases, so the rule for when
to ask for the map sits there.

## Skill: scope-the-edit

A new heading at the end.

## The repo map

When the workspace's tools offer a repo map, a ranked list of the
files and their key symbols, use it to start an architectural change
or work in a repository this session has not read. Ask for it under
a size budget, and read the files it ranks first.

Skip the map for a small edit, and for an intermediate one whose
file is already known. The map does not list vendored or generated
paths. A change that has to touch one names that path itself.

## What this change does not do

It does not edit a past spec. It changes no description, scope, key,
or bound. It names no tool.
