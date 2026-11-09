# Large migration

## When

A migration across many named files or modules that should keep
working as each piece lands. A one-file rename or a small move is
`scope-the-edit` and `carry-out-the-plan`. Say that, and stop.

A large migration can use many workers. Prefer a named list. Prefer
isolating only pieces whose writes would collide. Prefer verifying
each piece before folding it into the main branch.

## Plan

`scope-the-edit` names the scope. An architectural migration uses
`write-the-plan`. When steps can branch or send work back,
`map-the-handoffs` writes the graph in the plan. Structured notes on a
work item are OPTIONAL and never required.

## The split

Name the files or modules. `fan-out` runs one worker per named piece
when the pieces share no state. Pieces that would change the same
file use `isolate-the-work` for a per-piece checkout, then fold back.
Disjoint paths stay in one checkout. Per-file checkouts are not the
default for every file.

## Carry out

`carry-out-the-plan` runs the ordered tasks. Preview a multi-file
change before applying it. Each piece's check is the migration check
for that piece: build, type check, or the project's named gate.

## Until green

When the goal is the whole suite or gate green, `loop-to-the-goal`
keeps fixing until the check holds or a stop condition hits.

## Findings

`keep-the-findings` records verified facts about the old and new
shapes under `.kobold/findings/`. Tracker notes are OPTIONAL.

## Report

Name each piece, its check, and whether it folded. Name checkouts
still held. Do not loosen a check to make a piece pass.
