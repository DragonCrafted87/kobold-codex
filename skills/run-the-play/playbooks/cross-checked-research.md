# Cross-checked research

## When

A research question that needs several sources or angles checked
against each other before an answer. A single-subsystem read is
`how-it-fits` or `why-it-is`. Say that, and stop.

Cross-checked research can use many workers. Prefer a named list of
questions or sources. Prefer a second pass that tries to refute each
claim. Prefer discovery rounds when the set of sources is not known
up front.

## Findings first

`keep-the-findings` reads `.kobold/findings/` before exploring. Cite a
finding that already answers part of the question. Tracker notes are
OPTIONAL and never required.

## The angles

Name the questions, sources, or angles. `fan-out` runs one worker per
named piece when the pieces share no state. Research findings get the
second refutation pass in `fan-out` before they enter the report.
Claims a second pass could not check stay unverified, never refuted.

## Until the set is stable

When sources are found in rounds, `loop-to-the-goal` uses a discovery
goal and the discovery stop (default two empty rounds).

## Handoffs

When a weak claim sends work back to another angle, or a verified
claim feeds a synthesis step, `map-the-handoffs` writes the graph in
the plan. Structured notes on a work item are OPTIONAL.

## Answer

One report. Mark each claim seen, inferred, or unknown under
`kobold-codex`. Prefer verified claims. Name unverified claims and
what was not reached. Leave the tree alone.
