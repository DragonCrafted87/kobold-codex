---
name: stress-the-change
description: Use when a diff needs several independent reviews. Run separate passes on different angles, merge the findings into one list, and leave the tree alone.
---

# Stress the change

## The diff

Review the change `review-the-diff` would review. That skill's rule
for a named change, for an unnamed one, and for the request, the
plan, and the checks, is the rule here.

## Three passes

Run three passes on that same diff. A pass sees the diff, the
request, the checks, and its own angle. A pass does not see another
pass's findings. A finding from a pass uses the finding
`review-the-diff` defines.

The first pass is the request. Apply the request findings in
`review-the-diff`.

The second pass is the checks. Apply the check findings in
`review-the-diff`. The other passes do not run the checks.

The third pass is the changed lines. Apply the changed-line
findings in `review-the-diff`. A pass does not drop a finding
because another pass would also raise it.

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
follows `review-the-diff`, and it names which passes raised it.
The same file, line, and fault from more than one pass is one
finding. A finding only one pass raised stays on the list. When
one pass calls a line wrong and another pass calls that line fine,
keep the finding and name the passes on each side.

Order the list by file, then by line. When a pass raised nothing,
say so.

A finding with no line follows `review-the-diff`.

## Leave the tree

Leave the tree alone. An edit waits until the user asks for one.
`take-the-review` checks this list.

A second run reviews the diff as it is now. The new list replaces
the earlier list.

The list stays in the reply. A request to post it follows
`review-the-diff`. This skill stops at the list.
