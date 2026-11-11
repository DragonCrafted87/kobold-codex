---
name: keep-the-findings
description: Use before exploring code to answer a question about how it works, after verifying such an answer, and before reviewing or shipping a change. Read the saved findings first from `.kobold/findings/`, explore only what they leave open, write back each finding verified this session with its evidence, scope, owner, and review trigger, optionally mirror structured notes on a work item when one already exists, and recheck the findings a change trips.
metadata:
  group: investigate
---

# Keep the findings

## Read first

Saved findings live in `.kobold/findings/` at the repository root,
one Markdown file per finding. That directory is always the place
to read first. Before reading code to answer how something works,
who owns it, or why it is that way, read the findings whose scope
covers the paths in question. When the session already has a work
item with structured notes that hold findings, read those too as a
hint; the files still win when they disagree. A finding that
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
write it as a finding under `.kobold/findings/`. Only a claim seen
in the code or a run is written; an inferred or unknown claim stays
in the reply. When an existing finding turned out wrong, correct it
in place and name the change in the reply. Findings are committed
with the work, under the same bounds.

The local files are the source of truth. A tracker is never
required. When the session already has a work item in a tracker the
project uses for that work, also writing a structured note of the
same five fields on that item is OPTIONAL. Read those notes on a
later session only as a hint; the `.kobold/findings/` files still
win when the two disagree. A session with no work item, or no
tracker, writes only the files.

## The triggers

Before reviewing or shipping a change, read the review triggers of
the findings whose scope the change touches. For each one the change
trips, check the finding against the new code. Update it, or remove
it when it no longer holds, in the same change. A tripped finding
left unchecked is named in the reply.

## The same findings

A second run reads the findings again. A finding that already says
what this session verified is left as it is.
