---
name: spec-the-source
description: Use when a rewrite or a port needs specs from an existing system. Extract one module at a time, in source mode from its code and tests or in clean-room mode from public docs and a running instance only, into domain rules, API shapes, a data model, and behavior cases under stable IDs, with every claim tagged SEEN, INFERRED, or UNKNOWN, a provenance header, a coverage checklist, and a resumable progress file.
---

# Spec the source

## Two modes

The skill runs in one of two modes, chosen before the first read and
recorded in every spec.

- Source mode reads the module's source and its tests.
- Clean-room mode never reads the source. It reads only public
  documentation, such as archived official docs, and observes a
  running instance from outside: UI walkthroughs, API requests and
  their responses, and the behavior a user can see.

Both modes share the scope, the IDs, the spec format, the checklist,
and the progress file. They differ in their inputs and their
citations.

## Contamination

A session that has read the source, in this run or an earlier one,
does not write clean-room specs. Its notes, indexes, and progress
files stay apart from the clean-room output and are not handed to a
clean-room session. A clean-room session that opens a source file,
by accident or not, stops, records it in its progress file, and
hands the work to a fresh session. When a session cannot tell
whether it has read the source, it treats itself as having read it.

## Scope

Extract one module at a time: a plugin, a package, or a bounded
directory or feature area the user names. Before reading, write
down the mode, the module, the source license, and the slice this
run covers. In source mode, code outside the module is read only to
resolve a call the module makes, and it is cited, not specced.

The source is read-only. Write nothing inside it: no build, no
install, no generated index, no formatter. Reach no network beyond
the model the session already uses, except, in clean-room mode, the
public docs and the running instance the user named. Do not read or
use a repo token, a user token, or a secret found in the source or
the docs. A clean-room session logs in to the instance only with a
test account the user provides for that purpose.

## Where the specs go

The specs go in the repo the rewrite will live in. Look there first
for an existing spec convention: a `specs/` or `docs/specs/`
directory, a requirements file, or a project instruction that names
one. Follow its location, its file naming, and its format. When the
repo has none, use `specs/<module>/` at its root, in Markdown, with
the progress file beside the specs. Say which convention was found,
or that the default was used. The index and any scratch output stay
out of the source tree.

## Requirement IDs

Every requirement gets a stable ID of the form
`<MODULE>-<KIND>-<NNN>`. MODULE is a short uppercase name for the
module. NNN is a zero-padded number, counted per module and kind.
KIND is one of these.

- `RULE`: a domain rule, such as an invariant, a state transition,
  a trigger, or a computed field.
- `API`: one route or operation, with its request, responses, and
  errors.
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

## Requirement language

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

## Index first

Index before reading. In source mode, list the files, count them,
and locate the entry points with `rg` or `ctags`: the routes and API
handlers, the domain services, the workflow and permission rules,
the schema and its migrations, and each tier of tests. Locate a
symbol by searching for its definition. A file path that a namespace
or a convention suggests is a guess until a search confirms it. Read
in slices. Open a large file at the lines the index points to, not
whole. Batch independent searches into one command with a marker
between them, and cap each output.

In clean-room mode, the index is the docs' table of contents, the
published API reference, and the screens and menus of the running
instance.

## The coverage checklist

From the index, write a checklist into the progress file: one line
per entry point or screen, per rule-bearing area, per data object,
and per test file or documented example. Mark each line done,
partial, or not started. The module is extracted when every line is
done or carries a reason it was left. A line is never dropped to
make the list shorter.

## The progress file

The progress file records the mode, the module, the index counts,
the checklist, the next free ID for each kind, the open unknowns,
and the next inputs to read. Update it after each slice. A new
session resumes from it and does not re-read what it marks done. A
clean-room session resumes only from a clean-room progress file.

## Evidence

Tag every claim in a spec.

- SEEN: read or observed. In source mode, cite `file:line` or a line
  range. In clean-room mode, cite the doc URL with its section, or
  the observed request and response, or the UI steps and what the
  screen showed.
- INFERRED: reasoned from SEEN evidence. Name what it rests on.
- UNKNOWN: not found yet. Say what to read or try to settle it.

A behavior that was not found is UNKNOWN, not absent. A spec states
no behavior the evidence does not show. Reading code is not running
it, and a doc is not the behavior it describes. When a doc and an
observation disagree, record both and tag the conflict.

## The spec

Write one spec per module, or per slice of a module too large for
one. The header records the provenance: the mode, the inputs used
(source revision and paths, or doc URLs with their capture dates and
the instance's version), the source license as its files or docs
state it, and a license note.

In source mode, the license note says a spec derived from source
under a copyleft license such as the GPL keeps that license for a
rewrite built from it. In clean-room mode, the note says the spec
was written without reading the source. When the license wording is
unclear, record the wording and tag the open point UNKNOWN. Every
header ends with one line saying that the license notes are not
legal advice.

The spec has these parts, each requirement under its ID.

- Domain rules: invariants, state transitions and their guards,
  triggers and side effects, computed fields, and permission checks.
- API shapes: each route in an OpenAPI-style block, with method,
  path, parameters, request body, each response and error status
  and its cause, and headers. Look for effects on every exit path,
  including error paths. In source mode, errors come from the code
  and from the route's annotations; cite both and say which is
  which.
- Data model: tables or stores, columns, keys, nullability, and
  defaults. In source mode, reconcile the base schema with its
  migrations before calling a shape final; until then, tag the
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

## The template

A spec looks like this. The values are an example.

```markdown
---
mode: source
inputs: <source revision and paths, or doc URLs, capture dates, and instance version>
source-license: <the license as the source states it>
license-note: <copyleft carry-over in source mode, or "written without reading the source">
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

## Done

A slice is done when its checklist lines are done, each requirement
has an ID and each claim a tag, and its UNKNOWNs are listed in the
progress file. Report the mode, the spec paths, the convention
followed, the checklist counts, and the open UNKNOWNs.
