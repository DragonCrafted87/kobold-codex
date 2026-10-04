---
name: stress-the-change
description: Use when a diff needs several independent reviews. Run separate passes on different angles, merge the findings into one list, and leave the tree alone.
---

# Stress the change

## The diff

Review the change the user named. A named branch, a named range, a
pull request, or a named set of files is that change. Review that
change on its own.

When the user names none, review the current branch against the
branch it would merge into. Include uncommitted work in that
review, and say in the report that it is uncommitted.

Read the request, and the plan when there is one. The request is
what the user asked for. The checks are the ones the plan or the
change named.

## Three passes

Run three passes on that same diff. A pass sees the diff, the
request, the checks, and its own angle. A pass does not see another
pass's findings. A finding from a pass names the file, the line,
what is wrong, and why it matters.

The first pass is the request. A missing piece of the request is a
finding. A change the request did not ask for is a finding.

The second pass is the checks. Run the checks when they can be run.
A failed check is a finding. A check that cannot be run is a
finding, and the finding names the reason. A check that passes
without reaching the behavior it claims is a finding. The other
passes do not run the checks.

The third pass is the changed lines. A defect in a line the diff
adds or changes is a finding. A problem in a line the diff does not
touch stays out of this pass.

When only one model is available, run the three passes one after
another. Each pass starts without the other passes' findings.

Resolve `subagents` before starting another agent. When that key
allows another agent, the three passes may run together. The other
agent returns its findings and does not edit. This session writes
the list. When `subagents` does not allow another agent, run the
three passes one after another in this session.

When `model` is set, a pass in another agent uses that model. When
`model` is absent, the pass uses the model already running the
session. Keep all three passes when `model` is set and when it is
absent.

A pass that does not return leaves the list unfinished. Name the
missing pass and stop. Leave the passes unmerged.

## One list

Merge the finished passes into one list in the reply. A finding
names the file, the line, what is wrong, why it matters, and which
passes raised it. The same file, line, and fault from more than one
pass is one finding. A finding only one pass raised stays on the
list. When one pass calls a line wrong and another pass calls that
line fine, keep the finding and name the passes on each side.

Order the list by file, then by line. When a pass raised nothing,
say so.

A check finding that has no line stays in the list. Name the
command and the reason in place of the line. When some other item
has no line, say what the pass looked at, and leave that item out
of the list.

## Leave the tree

Leave the tree alone. An edit waits until the user asks for one.
`take-the-review` checks this list.

A second run reviews the diff as it is now. The new list replaces
the earlier list.

The list stays in the reply. A request to post it follows
`github-write`. This skill stops at the list.
