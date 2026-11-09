# Loop to the goal: discovery until stable

A revision of `loop-to-the-goal`, from the ultracode research of
2026-11-09. The wording below is the version to ship.

## Why

Some goals are not a fixed checker exit code but a search whose set
of results has stopped growing: find flaky tests, find callers, find
missing checks. The skill already looped change-then-check. It needed
a stop for "N consecutive rounds added nothing new," with two as the
default.

## Skill: loop-to-the-goal

The description, The goal, The limits, A pass, and The end match the
skill file on this branch.

## What this change does not do

It does not edit a past spec. It adds no key and no bound. It names
no project, host, or tool.
