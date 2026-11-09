---
name: fan-out
description: Use when work that does not share state should run as parallel workers, including a named list of many files, claims, or questions. Split it, wait for the workers, verify audit or research findings before they enter the report, and return one report. subagents has to allow the parallel form.
metadata:
  group: build
---

# Fan out

## The pieces

Split work that does not share state. Two pieces share state when
they would change the same file, the same checkout, or the same
record outside the repo. Keep those pieces together.

The pieces are the ones the user named. When another skill in this
plugin asks for the split, the pieces it named are the pieces.
Independent tasks are pieces already separated. Coverage is a set
of areas, each read or run on its own. A race is the same check
run more than once, to see whether the result changes. Exploration
is a set of questions, each read on its own.

A named list of files, claims, or questions is the pieces, one
piece each, when those pieces share no state. There is no small-list
cap on a named list. When the kind of split is named and the pieces
are not, name up to three pieces and run those. A wider unnamed set
waits until the extra pieces are named.

When a piece would change the same file another piece changes,
`isolate-the-work` is the rule for giving that piece its own
checkout. Pieces that only read share no write state and stay in
one checkout.

## The workers

Resolve `subagents` before starting another agent. When that key
allows another agent, the pieces run together. A worker returns
its result. It does not write the report, and it does not change
a file another piece changes. This session writes the report.

When `subagents` does not allow another agent, run the pieces one
after another in this session, and say that the run was serial.

When `model` is set, a worker in another agent uses that model.
When `model` is absent, the worker uses the model already running
the session. A piece that is a task of a fast kind in
`write-the-plan` uses the fast model instead. The rules for fast
work in `carry-out-the-plan` apply to that piece.

While the user is away, `unattended` still applies.
`set-the-bounds` is that rule. When that rule blocks another
agent and still allows the work, run the pieces in this session.

The default split lives only in this session. Workers start here,
report here, and end when the report is written. No durable record
is required.

When a split must be billed, approved, traced, or resumed after
this session, and the session already has a work item in a tracker
the project uses for that work, filing a child work item per piece
is OPTIONAL. The child holds the piece's brief and later its
result. The parent still writes the one report. Filing children is
never required, and a session with no work item, or no tracker,
stays on the in-session split. Do not invent a server API or a
workflow-script runner for the split; use the project's ordinary
way to create a child of the current item when that way is already
in use.

A worker that does not return leaves the report unfinished. Name
the missing piece and stop. Leave the finished pieces unmerged.

## One report

Write one report in the reply, in the order the pieces were named.
Each piece names what it was, the result, and whether it finished.
A piece that found nothing says so.

When the pieces are an audit or research fan-out, and a piece
reports a finding, a second pass tries to refute that finding
before it enters the report. The second pass works like a
refutation under `stress-the-change`: it does not see the other
pieces' findings, and it reads the evidence the first pass cited.
A finding that survives goes in the report as verified. A finding
the second pass could not check stays in the report as unverified,
never as refuted. A finding the second pass refutes is dropped, and
the report names how many were dropped. Edits and ordinary task
splits skip this second pass.

The report stays in the reply. A request to post it follows
`github-write`.

## The same split

A second run splits the work as it stands now. The new report
replaces the earlier report. Each piece is a part under
`kobold-codex`. Its inputs are the ones named for that piece.
