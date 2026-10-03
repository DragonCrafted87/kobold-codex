---
name: fan-out
description: Use when work that does not share state should run as parallel workers. Split it, wait for the workers, and return one report. subagents has to allow the parallel form.
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

When the kind of split is named and the pieces are not, name up to
three pieces and run those. A wider set waits until the extra
pieces are named.

`carry-out-the-plan` splits tasks inside one plan.
`stress-the-change` runs the three review passes.
`try-several-shapes` runs the candidates for one change. This
skill is the split those three do not already cover.

## The workers

Resolve `subagents` before starting another agent. When that key
allows another agent, the pieces run together. A worker returns
its result. It does not write the report, and it does not change
a file another piece changes. This session writes the report.

When `subagents` does not allow another agent, run the pieces one
after another in this session, and say that the run was serial.

When `model` is set, a worker in another agent uses that model.
When `model` is absent, the worker uses the model already running
the session.

While the user is away, `unattended` still applies. A named tool
stays on its own key. `set-the-bounds` is that rule.

A worker that does not return leaves the report unfinished. Name
the missing piece and stop. Leave the finished pieces unmerged.

## One report

Write one report in the reply, in the order the pieces were named.
Each piece names what it was, the result, and whether it finished.
A piece that found nothing says so.

The report stays in the reply. A request to post it follows
`github-write`.

## The same split

A second run splits the work as it stands now. The new report
replaces the earlier report. A piece whose result is already
recorded, and whose inputs are unchanged, can be cited from that
record. Name the record. Run a piece whose inputs changed.
