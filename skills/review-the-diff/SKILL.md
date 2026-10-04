---
name: review-the-diff
description: Use before a merge, or when the user asks for a review. Review the diff against the request and the checks, report each finding with file and line, and leave the tree alone.
---

# Review the diff

## The diff

Review the change the user named. A named branch, a named range, a
pull request, or a named set of files is that change. Review that
change on its own.

When the user names none, review the current branch against the
branch it would merge into. Include uncommitted work in that
review, and say in the report that it is uncommitted.

Read the diff before you report. Read the request, and the plan
when there is one. The request is what the user asked for.

## The request and the checks

A missing piece of the request is a finding. A change the request
did not ask for is a finding.

Run the checks the plan or the change named, when they can be run.
A failed check is a finding. A check that cannot be run is a
finding, and the finding names the reason. A check that passes
without reaching the behavior it claims is a finding.

A defect in a line the diff adds or changes is a finding when the
request and the checks do not already state it. A problem in a line
the diff does not touch stays out of the findings.

## Findings

A finding names the file, the line, what is wrong, and why it
matters to the request or to a check. A failed check, a check
that cannot be run, and a check that passes without reaching the
behavior stay in the findings when they have no line. Name the
command and the reason in place of the line. When some other item
has no line, say what you looked at, and leave that item out of
the findings.

Report the findings in the reply. When there are none, say that,
and name the diff you reviewed.

After the findings, name anything you considered and left out
because it sits outside the diff. One line each, with the reason.
When you left nothing out, say so.

## Leave the tree

Leave the tree alone. An edit waits until the user asks for one.
`take-the-review` checks a finding and implements it when it holds.

The report stays in the reply. A request to post it follows
`github-write`.

This review is one pass in this session. `stress-the-change` runs
the separate passes. This skill stops at the report. Integrating
the branch follows `ship-the-branch`.
