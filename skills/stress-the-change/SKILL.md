---
name: stress-the-change
description: Use when a diff needs several independent reviews. Run separate passes that each try to break it, try to refute every finding, merge what survives into one list, and leave the tree alone.
---

# Stress the change

## The diff

Review the change `review-the-diff` would review. That skill's rule
for a named change, for an unnamed one, and for the request, the
plan, and the checks, is the rule here.

## Three passes

Run three passes on that same diff. A pass sees the diff, the
request, the checks, and its own goal. A pass does not see another
pass's findings. A finding from a pass uses the finding
`review-the-diff` defines, with its evidence and its severity.

Each pass has one goal: to break the change from its side.

The first pass is the request. Its goal is to show what the change
fails to do that the request asked for, does that the request did
not ask for, or does against a project rule for a changed path.
Apply the request findings in `review-the-diff`.

The second pass is the checks. Its goal is to show that a check
fails, cannot run, or passes without reaching the behavior it
claims. Apply the check findings in `review-the-diff`. The other
passes do not run the checks.

The third pass is the changed lines. Its goal is to find the input,
the state, or the caller that makes a changed line do the wrong
thing. Apply the changed-line findings in `review-the-diff`. A pass
does not drop a finding because another pass would also raise it.

Each pass names what it did not reach: a file it could not read, a
path it did not follow, or a check it could not run to a result.
A pass that reached everything says so.

When only one model is available, run the three passes one after
another. Each pass starts without the other passes' findings.

Resolve `subagents` once, before the first pass, reviewer, or
verifier that would start another agent. Under `subagents: ask`,
the yes names this review and covers every agent this run starts.
A later run asks again. When the key allows another agent, the
passes may run together. The other agent returns its findings and
does not edit. This session writes the list. When `subagents` does
not allow another agent, run the passes one after another in this
session.

When `model` is set, a pass in another agent uses that model. When
`model` is absent, the pass uses the model already running the
session. Keep all three passes when `model` is set and when it is
absent. A pass never uses `model-fast`.

A pass that does not return leaves the list unfinished. Name the
missing pass and stop. Leave the passes unmerged.

## Project reviewers

When the `project-review` skill that `review-the-diff` reads lists
reviewers, run each one beside the three passes. A reviewer reads
only the changed files under the paths it covers. A reviewer with
no changed file under its paths does not run, and the list says
so.

A reviewer works like a pass. It sees the diff, the request, the
checks, and its own goal, and not another pass's findings. Its
findings use the finding `review-the-diff` defines. What blocks the
merge for a reviewer is the rule that reviewer names. It names what
it did not reach. The rules for `subagents`, `model`, and a pass
that does not return apply to a reviewer.

With no `project-review` skill, or one that lists no reviewers, no
other reviewer runs.

## One list

Merge the finished passes and reviewers into one list. A finding
follows `review-the-diff`, and it names which passes or reviewers
raised it. The same file, line, and fault from more than one pass
is one finding. A finding only one pass raised stays on the list.
When one pass calls a line wrong and another pass calls that line
fine, keep the finding and name the passes on each side.

Then run The refutation on each finding. The list in the reply
holds the findings that survive, each with its severity and how it
was verified. Name how many findings the refutation dropped.

Put the blocking findings first. Within each severity, order the
list by file, then by line. When a pass or a reviewer raised
nothing, say so.

After the list, name what each pass and reviewer did not reach.
When a verifier did not return, its finding stays on the list
marked unverified. When anything did not return or was not
reached, do not call the review complete.

When the change is someone else's work, write the surviving
findings as the review comments `review-the-diff` defines. Its
summary comment also names the passes and reviewers that ran and
how many findings the refutation dropped.

A finding with no line follows `review-the-diff`.

## The refutation

Send each finding on the merged list to a fresh verifier. The
verifier sees only that finding, the diff, and the request. It
does not see the pass that raised the finding or any other
finding. Its goal is to disprove the finding.

The verifier keeps the finding only when it can cite the file and
line for each part of the claim, under the evidence rule in
`review-the-diff`. A finding it cannot confirm is dropped. To
refute a finding, the verifier cites the code that stops the
fault. A comment that claims the code is safe does not stop it.

A nit gets one verifier. When `project-review` sets a nit cap,
verify the nits in list order until that many are verified. Count
the rest, and verify and list none of them. A finding that would
block the merge gets three verifiers, each with one focus. The
first asks whether the input the finding names can reach the faulty
line. The second asks whether the fault breaks the request or a
check. The third asks whether code already in place stops the
fault. The finding stays when two of the three keep it. It stays
blocking only when two verifiers call it blocking. Otherwise it
stays as a nit. A verifier can lower the severity and never raises
it. When `project-review` gives every finding three verifiers, a
nit gets three under the same tally.

A failed check, and a check that cannot run, go to no verifier.
The run is the evidence.

A verifier uses `model`. When `model` is absent, it uses the model
already running the session. A verifier never uses `model-fast`.

When `subagents` does not allow another agent, verify each finding
in this session, one at a time, from the finding, the diff, and
the request alone. The list says the verification ran in this
session.

## Leave the tree

Leave the tree alone. An edit waits until the user asks for one.
`take-the-review` checks this list.

A second run reviews the diff as it is now. The new list replaces
the earlier list.

The list stays in the reply. A request to post it follows
`review-the-diff`. This skill stops at the list.
