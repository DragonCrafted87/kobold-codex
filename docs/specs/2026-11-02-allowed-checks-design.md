# Ship the branch: allowed checks and their diagnostics

A revision of `ship-the-branch`. The wording below is the version to
ship.

## Why

A sandboxed code toolkit can offer a command tool that runs only a
project's allow-listed commands, such as its test runner and its
linter, and refuses the rest. `ship-the-branch` already runs the
narrow checks and the gate before any commit. It did not say what
those are when only some commands are allowed, or that the
diagnostics they print are read, not just the exit code. The
paragraph names no language or command, so it holds for any project.

## Skill: ship-the-branch

In The branch, a new paragraph after the one on the narrow checks and
the gate.

When the session can run only the commands a project allows, the
narrow checks and the gate are the allowed test and lint commands.
A check that is not allowed is a check that cannot be run. Read the
diagnostics each one reports, warnings included, on the files the
branch changes. A new warning on a changed line is fixed before the
commit, or named in the reply with the reason it stays.

## What this change does not do

It does not edit a past spec. It changes no description, key, or
bound. It names no tool, language, or command.
