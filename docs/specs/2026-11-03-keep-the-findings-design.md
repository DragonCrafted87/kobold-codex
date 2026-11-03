# Keep the findings

A new skill in the investigate group, from research item KCO-2596.
The wording below is the version to ship.

## Research

Falconer is a paid service that stops agents re-reading code. It
saves verified findings outside the session, serves them over a tool
server, has agents retrieve first and search only for what is
unknown, writes findings back, and refreshes them from merged pull
requests. Each finding has five parts: the finding, its evidence,
its scope, its owner, and a review trigger. The code stays the
source of truth.

Open-source options checked when the item was filed (2026-10-22):
Serena (GPL-3.0; its language-server layer is MIT) for symbol
navigation and project memories; codebase-memory-mcp (MIT), a code
knowledge graph; Basic Memory (AGPL-3.0), Markdown notes with a
read-write layer, the closest to Falconer's write-back; code-index-mcp
(MIT); and the Aider repo map idea (Apache-2.0). GitNexus is
noncommercial and not open source.

Most of the value is the convention, and it needs no tool: Markdown
findings in the repository, read first, written back, and rechecked
when their trigger trips. That is this skill. Symbol and graph tools
pair with it through `edit-by-symbol` and the repo map in
`scope-the-edit`, and adding one follows `check-the-licenses`. The
item's repo map file is left out, because the repo map heading
already covers maps a tool builds. Measuring the repeat-read rate is
left for a later review. The wording below is original.

## Skill: keep-the-findings

```text
description: Use before exploring code to answer a question about how it works, after verifying such an answer, and before reviewing or shipping a change. Read the saved findings first, explore only what they leave open, write back each finding verified this session with its evidence, scope, owner, and review trigger, and recheck the findings a change trips.
```

## Read first

Saved findings live in `.kobold/findings/` at the repository root,
one Markdown file per finding. Before reading code to answer how
something works, who owns it, or why it is that way, read the
findings whose scope covers the paths in question. A finding that
answers the question is the answer. Cite its file, and read the code
only for what it leaves open.

A finding is a claim, not the code. When the code it cites changed
since the finding was written, check the claim against the code
before using it.

## A finding

A finding file has five fields, in this order:

- Finding: one or two sentences that state the fact.
- Evidence: the files and lines, the commit, or the run that shows it.
- Scope: the paths it covers.
- Owner: the person, team, or module that decides it.
- Review trigger: the change that would make it untrue, such as an
  edit under a named path or a new version of a dependency.

The file name is a short slug of the finding. One fact goes in one
file. A fact already written in a skill, a spec, or the project's own
docs is linked there, not copied.

## Write back

After this session verifies an answer the findings did not hold,
write it as a finding. Only a claim seen in the code or a run is
written; an inferred or unknown claim stays in the reply. When an
existing finding turned out wrong, correct it in place and name the
change in the reply. Findings are committed with the work, under the
same bounds.

## The triggers

Before reviewing or shipping a change, read the review triggers of
the findings whose scope the change touches. For each one the change
trips, check the finding against the new code. Update it, or remove
it when it no longer holds, in the same change. A tripped finding
left unchecked is named in the reply.

## The same findings

A second run reads the findings again. A finding that already says
what this session verified is left as it is.

## What this change does not do

It does not edit a past spec. It adds no key and no bound. It installs
no tool and names no project, host, or tool.
