# Kobold Codex: few turns, cited claims

A revision of `kobold-codex`, from research item KCO-2599. The
wording below is the version to ship.

## Research

leanrea (aicodeking, MIT, created 2026-10-17) is one short SKILL.md
that replaced a reverse-engineering tool server of about two hundred
tools with plain command-line tools. Its own benchmark (36 runs on one
Mac, so a small sample) reported 38% less time, 35% lower cost, and 56%
fewer turns than the server, at nearly the same accuracy. Three of its
rules are general: batch independent probes and stop once each question
has evidence; label each claim seen, inferred, or unknown; and prefer a
short routing note and installed tools over a heavy tool server.

`spec-the-source` already uses SEEN, INFERRED, and UNKNOWN for
specs. This change brings the habit to every answer about how
something works, in lower case, so it reads as prose and not as a
spec tag. It lives in `kobold-codex` because it applies to every
investigation skill, and putting it once avoids copying it into each.

The fourth idea, installing through a cross-platform skills CLI,
belongs to KCO-2536 and is taken up there. The wording below is
original.

## Skill: kobold-codex

A new heading before Requirements.

## Few turns, cited claims

A turn costs more than its output. Batch independent probes into one
call, mark where each probe's output starts, and cap each output.
For a question about existing code or a system, aim for a few calls:
one batched survey, one or two targeted reads, then the answer. Stop
when every part of the question has evidence. Do not read again what
this session already read and nothing since has changed.

Use the cheapest tool that answers. A plain command that is already
installed answers before a tool server that has to load, and a slice
of a large file answers before the whole file.

In an answer about how something works, mark each claim as seen,
with the file and line or the output that shows it, or as inferred.
A fact the session looked for and did not find is unknown, not
absent. Reading the code is not watching it run.

## What this change does not do

It does not edit a past spec. It does not change `spec-the-source`'s
tags. It adds no key and no bound, and it names no tool.
