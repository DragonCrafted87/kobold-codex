---
name: pick-up-the-work
description: Use when a new session should continue work already in progress. Rebuild a short brief from the branch, the transcript, and the trail.
---

# Pick up the work

## The sources

Read the branch, the transcript, and the trail. The branch is the
one the user named. When they name none, read the current branch.
The transcript is the one the user pointed at. The trail is
`.kobold/trail.md` when that file exists. When the user points at
another log, read that log as the trail.

When a source is missing, say so. When the branch, the transcript,
and the trail are all missing, stop and ask what to read.

## The brief

Write a short brief in the reply. Name the branch. Name the
commits and the uncommitted files that are this work. When a plan
is in progress, name the plan file and the first checkbox still
marked `- [ ]`. When a trail exists, name the last row. Name the
next step.

The brief uses only what those sources say. A gap stays a gap.
Say what you could not find.

## Leave the tree

Leave the tree alone. The brief is the whole product of this
skill. Continuing the work is a separate request.

## The same point

A second run reads the three sources again. The new brief
replaces the earlier brief.
