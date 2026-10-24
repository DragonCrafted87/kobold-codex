# Spec the source

A new skill in the investigate group. The wording below is the
version to ship.

## Why

A rewrite or a port of a large codebase needs specs taken from the
source: the rules, the API, the data, and the behavior its tests
pin down. Tools built to reverse-engineer compiled software do not
fit, because the source and its tests are already in hand. The
evidence tags SEEN, INFERRED, and UNKNOWN, and the rule that a
behavior not found is unknown rather than absent, are adapted from
the leanrea skill (MIT). The wording here is original.

The skill was trialed on one slice of a large PHP tracker module.
The trial added: locate symbols by definition, not by path;
reconcile the base schema with migrations; take error shapes from
both code and annotations; look for effects on error paths; and
record license wording when it is not a clean identifier.

Review on the pull request added clean-room mode, the provenance
header, the convention-first output location, and stable requirement
IDs. Clean-room mode lives in this skill, not a sibling, because it
shares the scope, the IDs, the spec format, the checklist, and the
progress file; only the inputs and the citations differ. One skill
also keeps the contamination rule beside the mode it guards.

A second review pass added the `UI` and `PERM` kinds and limited
requirement language to an RFC 2119 subset: SHALL, SHALL NOT,
RECOMMENDED, NOT RECOMMENDED, and OPTIONAL, uppercase only when
normative per RFC 8174. Specs live in target repos, so the skill
carries a one-line search the agent runs on its own output; a script
would need installing in every host. The plugin's check reads this
one skill file and fails when an excluded keyword appears outside
the line that lists them, so the template cannot drift.

A third pass applied the pull request's review notes: source mode
does not run the program or its tests, and, at the owner's
direction, clean-room mode does not read the tests or their output.
The checklist gained a left mark with a reason, and one finishing
rule covers the slice and the module. The progress file records the
revision, license, slice, and output directory, and a changed
revision reopens the checklist. The batching rule taken from leanrea
was dropped. A module without a UI, a store, or HTTP routes marks
those parts left, and its API shape is the surface it has. The
license note follows the source license's own terms. Each evidence
tag is stated as one rule.

## Description

```text
description: Use when a rewrite or a port needs specs from an existing system. Extract one module at a time, in source mode from its code and tests or in clean-room mode from public docs and a running instance only, into domain rules, API shapes, a data model, and behavior cases under stable IDs, with every claim tagged SEEN, INFERRED, or UNKNOWN, a provenance header, a coverage checklist, and a resumable progress file.
```

## Skill: spec-the-source

### Two modes

The skill runs in one of two modes, chosen before the first read and
recorded in every spec.

- Source mode reads the module's source and its tests.
- Clean-room mode never reads the source, the tests, or the tests'
  output. It reads only public documentation, such as archived
  official docs, and observes a running instance from outside: UI
  walkthroughs, API requests and their responses, and the behavior a
  user can see.

Both modes share the scope, the IDs, the spec format, the checklist,
and the progress file. They differ in their inputs and their
citations.

### Contamination

A session that has read the source, in this run or an earlier one,
does not write clean-room specs. Its notes, indexes, and progress
files stay apart from the clean-room output and are not handed to a
clean-room session. A clean-room session that opens a source file,
by accident or not, stops, records it in its progress file, and
hands the work to a fresh session. When a session cannot tell
whether it has read the source, it treats itself as having read it.

### Scope

Extract one module at a time: a plugin, a package, or a bounded
directory or feature area the user names. Before reading, write
down the mode, the module, the source license, and the slice this
run covers, and the source revision. In source mode, code outside the module is read only to
resolve a call the module makes, and it is cited, not specced.

The source is read-only. Write nothing inside it: no build, no
install, no generated index, no formatter. Reach no network beyond
the model the session already uses, except, in clean-room mode, the
public docs and the running instance the user named. Do not read or
use a repo token, a user token, or a secret found in the source or
the docs. In source mode, do not run the program or its tests; a
run can write caches, coverage, or database rows, and the spec comes
from reading. In clean-room mode, do not read the tests or any test
output, logs, or reports. A clean-room session logs in to the instance only with a
test account the user provides for that purpose.

### Where the specs go

The specs go in the repo the rewrite will live in. Look there first
for an existing spec convention: a `specs/` or `docs/specs/`
directory, a requirements file, or a project instruction that names
one. Follow its location, its file naming, and its format. When the
repo has none, use `specs/<module>/` at its root, in Markdown, with
the progress file beside the specs. Say which convention was found,
or that the default was used. The index and any scratch output stay
out of the source tree.

### Requirement IDs

Every requirement gets a stable ID of the form
`<MODULE>-<KIND>-<NNN>`. MODULE is a short uppercase name for the
module. NNN is a zero-padded number, counted per module and kind.
KIND is one of these.

- `RULE`: a domain rule, such as an invariant, a state transition,
  a trigger, or a computed field.
- `API`: one operation on the module's surface, such as an HTTP
  route, a command, an event, or an exported call, with its inputs,
  outputs, and errors.
- `DATA`: one table, store, or record shape.
- `UI`: a screen, a flow, or a behavior a user sees.
- `PERM`: a permission or access rule: who can see or do what.
- `CASE`: a behavior case in given, when, then.

When the target repo already has an ID scheme, follow it instead.

An ID is never renumbered or reused. A requirement found to be wrong
is marked withdrawn and keeps its ID; a new one gets the next free
number. The progress file records the next free number for each
kind. The IDs let the specs be imported into a requirements manager
later.

### Requirement language

Specs use the requirement keywords of RFC 2119, limited to this
set: SHALL, SHALL NOT, RECOMMENDED, NOT RECOMMENDED, and OPTIONAL.
A keyword is uppercase only when it is normative, as RFC 8174
clarifies; the same word in lowercase is plain English. Every
`RULE`, `API`, `DATA`, `UI`, and `PERM` requirement carries exactly
one keyword. A `CASE` stays given, when, then, with no keyword.

The other RFC 2119 keywords are not used. This line lists them so
they can be found: MUST, MUST NOT, REQUIRED, SHOULD, SHOULD NOT, MAY.

Before reporting a slice, search the specs for them and fix each
hit:

```sh
rg -nw -e MUST -e SHOULD -e MAY -e REQUIRED <spec-dir>
```

### Index first

Index before reading. In source mode, list the files, count them,
and locate the entry points with the search on hand, such as `rg` or
`ctags`: the surface the module exposes (routes, commands, events,
or exported calls), the domain logic, the permission rules, any
store and its migrations, and each tier of tests. A missing search
program does not stop the index; use what the host has. Locate a
symbol by searching for its definition. A file path that a namespace
or a convention suggests is a guess until a search confirms it. Read
in slices. Open a large file at the lines the index points to, not
whole.

In clean-room mode, the index is the docs' table of contents, the
published API reference, and the screens and menus of the running
instance.

### The coverage checklist

From the index, write a checklist into the progress file: one line
per entry point or screen, per area that holds rules, per data
object, and, in source mode, per test file, or in clean-room mode,
per documented example. Add one line per spec part. Mark each line
done, partial, not started, or left; a left line carries its reason
on the same line. A slice is finished, and so is the module, when
every line in its scope is done or left. A line is never dropped to
make the list shorter.

### The progress file

The progress file records the mode, the module, the source revision
(or, in clean-room mode, the doc capture dates and the instance
version), the source license, the slice, the output directory, the
index counts, the checklist, the next free ID for each kind, the
open unknowns, and the next inputs to read. Update it after each
slice. A new session resumes from it and does not re-read what it
marks done. When the revision or the instance version differs from
the one recorded, mark the affected checklist lines not started and
read them again. A clean-room session resumes only from a clean-room
progress file.

### Evidence

Tag every claim in a spec.

- SEEN cites what was read or observed. In source mode, that is
  `file:line` or a line range. In clean-room mode, it is the doc URL
  with its section, the observed request and response, or the UI
  steps and what the screen showed.
- INFERRED names the SEEN evidence it rests on. A claim about order
  or timing is INFERRED from the code path, or the sequence of
  observations, that produces it.
- UNKNOWN is a behavior that was not found. It names the files, docs,
  or observations already checked, and it never becomes "absent".

A spec states no behavior without one of these tags. When a doc and
an observation disagree, record both and tag the conflict.

### The spec

Write one spec per module, or per slice of a module too large for
one. The header records the provenance: the mode, the inputs used
(source revision and paths, or doc URLs with their capture dates and
the instance's version), the source license as its files or docs
state it, and a license note.

In source mode, the license note says a rewrite built from the spec
follows the terms the source files state, including the share-alike
scope those terms name and any notice they require. In clean-room
mode, the note says the spec was written without reading the source
or its tests. When the license wording is unclear, the note stays
UNKNOWN and the rewrite waits on it. Every
header ends with one line saying that the license notes are not
legal advice.

The spec has these parts, each requirement under its ID. A part the
module does not have, such as a UI or a store, is one checklist line
marked left with the reason, not an invented section.

- Domain rules: invariants, state transitions and their guards,
  triggers and side effects, computed fields, and permission checks.
- API shapes: the surface that exists. An HTTP route is an
  OpenAPI-style block, with method, path, parameters, request body,
  each response and error status and its cause, and headers. A
  command, an event, or an exported call lists its inputs, outputs,
  and errors. Look for effects on every exit path,
  including error paths. In source mode, errors come from the code
  and from any annotations on it; cite both and say which is
  which.
- Data model: tables or stores, columns, keys, nullability, and
  defaults. In source mode, when the store has migrations, reconcile
  the base schema with them before calling a shape final; until then, tag the
  final shape UNKNOWN. In clean-room mode, the model is what the API
  and the UI expose.
- Screens and flows (`UI`): what a user sees and does, step by step.
- Permissions (`PERM`): who can see or do each thing, and what
  happens to someone who cannot.
- Behavior cases: given, when, then, in language-neutral terms. In
  source mode, port each existing test and name the test it came
  from. In clean-room mode, write each case from an observation or a
  documented example and cite it.

The spec names behavior, not the source language's classes. A class
name appears only in a source-mode citation.

### The template

A spec looks like this. The values are an example.

```markdown
---
mode: source
inputs: <source revision and paths, or doc URLs, capture dates, and instance version>
source-license: <the license as the source states it>
license-note: <the source license's terms for a rewrite in source mode, or "written without reading the source or its tests">
requirement-language: RFC 2119 keywords as clarified by RFC 8174, limited to SHALL, SHALL NOT, RECOMMENDED, NOT RECOMMENDED, and OPTIONAL; uppercase only when normative.
caveat: The license notes are not legal advice.
---

# ORDERS: order lifecycle

ORDERS-RULE-001. An order SHALL NOT move from cancelled to any other
state. SEEN src/orders/state.ext:41-48

ORDERS-API-001. `DELETE /orders/{id}` SHALL answer 404 when the order
does not exist. SEEN src/orders/routes.ext:120

ORDERS-DATA-001. An order record SHALL hold a non-null status.
SEEN schema/orders.sql:12

ORDERS-UI-001. It is RECOMMENDED that the order page show the cancel
button only while cancelling is allowed. INFERRED from ORDERS-RULE-001

ORDERS-PERM-001. Only the order's owner or an admin SHALL cancel it.
SEEN src/orders/policy.ext:22-30

ORDERS-CASE-001 (from test_cancel_twice, tests/orders.ext:88)
  Given a cancelled order
  When the owner cancels it again
  Then the request is refused and the order stays cancelled
```

### Done

A slice is done when every checklist line in its scope is done or
left, each requirement
has an ID and each claim a tag, and its UNKNOWNs are listed in the
progress file. Report the mode, the spec paths, the convention
followed, the checklist counts, and the open UNKNOWNs.

## What this change does not do

It names no project, language, or host tool. It adds no hooks. It
does not edit a past spec. The plugin version moves to 2.2.0.
