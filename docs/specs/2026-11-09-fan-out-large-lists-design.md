# Fan out: large named lists and verify-before-report

A revision of `fan-out`, from the 2026-11-09 multi-agent orchestration research.
The wording below is the version to ship.

## Why

A large audit, migration, or research task often has a named list of
many files, claims, or questions that share no state. The skill
capped unnamed splits at three pieces and had no rule for verifying
findings before they entered the report. Dynamic-workflow practice
fans out one worker per named item and adversarially checks findings
before reporting. That habit belongs here, without naming a host
runtime.

## Skill: fan-out

The description becomes:

```text
description: Use when work that does not share state should run as parallel workers, including a named list of many files, claims, or questions. Split it, wait for the workers, verify audit or research findings before they enter the report, and return one report. subagents has to allow the parallel form.
```

### The pieces

(as in the skill file)

### The workers

(as in the skill file, including the in-session default and the
OPTIONAL child work items when a tracker work item already exists)

### One report

(as in the skill file, including the audit/research second pass that
follows `stress-the-change`'s refutation shape)

## What this change does not do

It does not edit a past spec. It adds no key and no bound. It does
not require a tracker or child work items. It does not rename
`stress-the-change`. It names no project, host, or tool.
