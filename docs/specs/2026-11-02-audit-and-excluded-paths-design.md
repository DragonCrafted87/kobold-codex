# Review the diff: the edit log and excluded paths

A revision of `review-the-diff`. The wording below is the version to
ship.

## Why

A code toolkit can log every agent edit and refuse edits to vendored
or generated paths unless a call names them. A reviewer of that
agent's branch has two cheap checks the diff alone does not give:
the log and the commits agree, and nothing excluded was touched
without being asked for. Both read only what the project already
keeps, so the paragraph applies only where a project has them.

## Skill: review-the-diff

A new paragraph at the end of The request and the checks.

When the change was made by an agent whose edits the project logs,
compare that log with the commits. An edit in the log that no commit
carries, or a changed file the log does not show, is a finding. When
the project marks paths as vendored, generated, or otherwise
excluded from edits, a change to one of them is a finding unless the
request names that path.

## What this change does not do

It does not edit a past spec. It changes no description, key, or
bound. It names no project, host, or tool.
