---
name: prove-the-product
description: Use when a repo has no scripted way to drive the app the way a user does. Write a project-local verification skill, prove it once, and re-run it so the map stays honest.
---

# Prove the product

## The drive

A scripted user-level drive performs the actions a user performs
and checks what the user would see. A unit test of a function is
not that drive.

When the repo has no app a user drives, say so and stop. Name the
scripted check the repo already has, and run it when it can be
run.

When the repo already has that drive, name it and stop. When it
does not, write a project-local verification skill that is the
drive. The skill lives in the
project that owns the app. It is not a file under this plugin's
`skills/` directory.

## The skill file

Look for a directory the project that owns the app already uses
for a skill a session loads. That directory is not this plugin's
`skills/` directory. When the project has one, write the skill
there. When it has none, stop and ask where the skill should live.
Leave the tree alone until the user names the directory.

The skill is one directory with one `SKILL.md`. The directory
name is the skill name. Name it for the app and for the drive.
The description is one physical line, and it says when to run
the drive.

Each step is an action a user would take and the result the user
would see. The steps come from a read of the features the app
has. Every feature in that read gets a step. A step needs a
feature.

The edit follows `scope-the-edit`.

## Prove it once

Run the skill once, the way a user would move through it. Record
the command or the actions, and the result.

When a step drives a browser, `browser` is the key. When a step
reaches the network, `shell-network` is the key. `set-the-bounds`
resolves the key. A key that stops the step stops the proof. Say
the key, the value, and the layer.

A failed step stops the proof. The skill file stays, and the
reply names the step and the result. A proof that finishes shows
every step and the result you observed.

## A later pass

A later pass re-reads the features and re-runs the skill. Add a
step for a feature the skill does not cover. Remove a step whose
feature is gone. Re-run after that edit. The map is honest when
every feature has a step, every step has a feature, and the run
matches those steps.

## The same map

A second run reads the features and the skill file again. Each
step is a part under `kobold-codex`. Its inputs are the feature
and whether the last run still describes the app.
