# Large audit

## When

An audit across many named files, routes, claims, or questions that
share no state. A one-file review is `review-the-diff` or
`stress-the-change`. Say that, and stop.

A large audit can use many workers. Prefer a named list the user or
the plan already holds. Prefer verifying findings before they enter
the report. Prefer keeping the split in this session unless billing,
approval, tracing, or a later resume already needs a work item.

## Scope

`scope-the-edit` names the scope. An architectural audit still gets a
plan from `write-the-plan` before the fan-out when the change would
stick.

## Findings first

`keep-the-findings` reads `.kobold/findings/` before exploring. Write
back only claims this run verified. A work item's structured notes are
OPTIONAL and never required.

## The split

Name the list of files, claims, or questions. `fan-out` runs one
worker per named piece when the pieces share no state. The ≤3 cap
does not apply to a named list. Audit findings get the second
refutation pass in `fan-out` before they enter the report.
`stress-the-change` is the skill for adversarially reviewing a diff,
not this playbook's whole surface.

When pieces would change the same paths, `isolate-the-work` gives
each colliding piece its own checkout. Read-only audits stay in one
checkout.

## Until the set is stable

When the audit is a search for issues until nothing new appears,
`loop-to-the-goal` runs discovery rounds with the discovery stop
(default two empty rounds).

## Handoffs

When a finding can send work to a fix step or back to another search,
`map-the-handoffs` writes the graph in the plan. Structured notes on a
work item are OPTIONAL.

## Report

One report from `fan-out`. Verified findings first, then unverified,
then what was not reached. Leave the tree alone unless the user asked
for fixes; fixes are a separate request or a later playbook.
