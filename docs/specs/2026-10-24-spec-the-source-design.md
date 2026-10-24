# Spec the source

A new skill in the investigate group. The wording below is the
version to ship.

## Why

A rewrite or a port of a large codebase needs specs taken from the
source: the rules, the API, the data, and the behavior its tests
pin down. Tools built to reverse-engineer compiled software do not
fit, because the source and its tests are already in hand. The
evidence tags SEEN, INFERRED, and UNKNOWN are adapted from the
leanrea skill (MIT). The wording here is original.

The skill was trialed on one slice of a large PHP tracker module.
The trial added: locate symbols by definition, not by path;
reconcile the base schema with migrations; take error shapes from
both code and annotations; look for effects on error paths; and
record license wording when it is not a clean identifier.

## Description

```text
description: Use when a rewrite or a port needs specs from existing source. Extract one module at a time into domain rules, API shapes, a data model, and behavior cases from its tests, tag every claim SEEN, INFERRED, or UNKNOWN, and keep a coverage checklist and a resumable progress file.
```

## Skill: spec-the-source

### Scope

Extract one module at a time: a plugin, a package, or a bounded
directory the user names. Before reading, write down the module's
root, the source license, and the slice this run covers. Code
outside the module is read only to resolve a call the module makes,
and it is cited, not specced.

The source is read-only. Write nothing inside it: no build, no
install, no generated index, no formatter. Keep the index, the
progress file, and the specs in an output directory outside the
source tree. Reach no network beyond the model the session already
uses. Do not read or use a repo token, a user token, or a secret
found in the source.

### Index first

Index before reading. List the files, count them, and locate the
entry points with `rg` or `ctags`: the routes and API handlers, the
domain services, the workflow and permission rules, the schema and
its migrations, and each tier of tests. Locate a symbol by searching
for its definition. A file path that a namespace or a convention
suggests is a guess until a search confirms it.

Read in slices. Open a large file at the lines the index points to,
not whole. Batch independent searches into one command with a
marker between them, and cap each output.

### The coverage checklist

From the index, write a checklist into the progress file: one line
per entry point, per rule-bearing class or module, per schema
object, and per test file. Mark each line done, partial, or not
started. The module is extracted when every line is done or carries
a reason it was left. A line is never dropped to make the list
shorter.

### The progress file

The progress file records the module root, the index counts, the
checklist, the open unknowns, and the next files to read. Update it
after each slice. A new session resumes from it and does not
re-read what it marks done.

### Evidence

Tag every claim in a spec.

- SEEN: read in the source. Cite `file:line` or a line range.
- INFERRED: reasoned from SEEN code. Name the code it rests on.
- UNKNOWN: not found yet. Say what to read to settle it.

A behavior that was not found is UNKNOWN, not absent. A spec states
no behavior the source does not show. Reading code is not running
it, so a claim about runtime order or timing rests on the code path
that produces it.

### The spec

Write one spec per module, or per slice of a module too large for
one. The header records the source module and revision, the source
license as its files state it, and a license note. A spec derived
from source under a copyleft license such as the GPL keeps that
license for a rewrite built from it. When the license wording is
unclear, record the wording and tag the open point UNKNOWN.

The spec has four parts.

- Domain rules: invariants, state transitions and their guards,
  triggers and side effects, computed fields, and permission checks.
- API shapes: each route in an OpenAPI-style block, with method,
  path, parameters, request body, each response and error status
  and its cause, and headers. Errors come from the code and from the
  route's annotations; cite both and say which is which. Look for
  effects on every exit path, including error paths.
- Data model: tables or stores, columns, keys, nullability, and
  defaults. Reconcile the base schema with its migrations before
  calling a shape final; until then, tag the final shape UNKNOWN.
- Behavior cases: each existing test ported to language-neutral
  given, when, then, naming the test it came from. Unit tests give
  the rules; API-level tests confirm status codes and payloads.

The spec names behavior, not the source language's classes. A class
name appears only in a citation.

### Done

A slice is done when its checklist lines are done, each claim in
its spec carries a tag, and its UNKNOWNs are listed in the progress
file. Report the spec paths, the checklist counts, and the open
UNKNOWNs.

## What this change does not do

It names no project, language, or host tool. It adds no hooks. It
does not edit a past spec. The plugin version moves to 2.2.0.
