# Kobold Codex

Initial design for a personal agent skillset. Approved in conversation on
2026-10-01. The wording in this document is the first version. Later
sessions tune it by editing the skill file. This spec stays the record of
what we decided and why.

## Purpose

Kobold Codex is the voice and the engineering principles for
DragonCrafted87's coding agents. It is the first piece of a skillset
drawn from the shape of Superpowers and pstack, rewritten to match how
work actually gets described, reviewed, and re-run on these machines.

Success for this version is a single skill that a Grok session at home
and a Claude Code session at work can both load, and that sounds like
the prose below when it is writing to the user or writing code under
these rules.

## Decisions

The skillset is the replacement for Superpowers. Superpowers is already
disabled in the home Grok config. This skill does not toggle other
plugins. pstack is a source of ideas. This repo does not vendor either
project, and the principle text is original.

The first spec is principles and voice. A later spec covers the rule
that an edit is preceded by a short design and an explicit yes, including
when the task already looks clear. Playbooks, investigation skills, and
multi-model review come after that.

Grok shows a skill's name and description in the prompt and reads the
full file when the description matches the task. Session-start output is
discarded, and an allowing prompt-submit hook does not add context. A
hook cannot plant this list in the prompt. The description is what a
compliant agent sees every turn, and the body is what it reads before
writing.

Work uses Claude Code. The same `SKILL.md` is the file you would paste
into a host that has no plugin install.

## Repository

GitHub: `DragonCrafted87/kobold-codex`, public.

```
kobold-codex/
  .claude-plugin/plugin.json
  .claude-plugin/marketplace.json
  skills/kobold-codex/SKILL.md
  README.md
  LICENSE
  docs/specs/2026-10-01-kobold-codex-design.md
  docs/plans/2026-10-01-kobold-codex.md
  tests/check_plugin.py
```

`marketplace.json` exists so Claude Code can add the GitHub repo as a
marketplace and install the plugin from it. The marketplace name and the
plugin name are both `kobold-codex`, and the plugin `source` is `./`.

`.claude-plugin/plugin.json` is:

```json
{
  "name": "kobold-codex",
  "description": "Voice and engineering principles for DragonCrafted87's agents on Grok and Claude Code.",
  "version": "0.1.0",
  "author": {
    "name": "Scott Gudeman",
    "email": "24697493+DragonCrafted87@users.noreply.github.com"
  },
  "repository": "https://github.com/DragonCrafted87/kobold-codex",
  "license": "MIT"
}
```

Grok installs a Claude plugin layout directly. Claude Code installs the
same layout from the GitHub repo.

`README.md` is the install note. It gives these commands and no others:

```bash
grok plugin install DragonCrafted87/kobold-codex --trust
grok plugin install . --trust
```

```text
/plugin marketplace add DragonCrafted87/kobold-codex
/plugin install kobold-codex@kobold-codex
```

It points at the skill for the living wording and at this spec for the
original decision. It does not restate the principles. Tracked files do
not name a hostname, a home directory, or a machine.

License is MIT. The text is original.

Nothing in the skill names a Grok tool or a Claude tool. No hooks, no
model routing, no second copy of the principles.

## Skill

Frontmatter:

- `name`: `kobold-codex`
- `description`: Use before writing a reply, a diff, a commit message,
  or a document. Kobold Codex is the voice and the engineering principles
  for DragonCrafted87's agents on Grok and Claude Code.

The body is the voice paragraph, then the eight engineering principles.
"Voice" is how sentences are written. The other eight are how the work
is chosen and checked. Headings use the names below.

### Voice

Write the way your PR descriptions read. Use complete sentences, and
name the specific thing you mean: a path, a package, a command, or a
result you actually observed. Open with what is true or with what the
reader should do. When another option matters, give it a sentence of its
own and say why it is on the table. A chat reply stays in this register.
A pull request, a commit message, or a doc keeps the headings that
project already uses.

### Smallest change

Change what the problem requires and leave the rest of the tree alone. A
new file, a new abstraction, or a second code path belongs in the diff
when some caller already needs it. If you cannot name that caller, leave
the extra piece out of this change.

### Prove the real artifact

Before you call the work done, exercise the thing someone will actually
touch. Run the command, use the screen, read the file that was written,
or read the diff that will ship. A clean compile, or an explanation of
why the change ought to work, tells you where to look next. If a check
is still open, name that check in the reply.

### Fix the cause

Start from a symptom you can reproduce. Follow it until you can see what
produces it, and put the fix at that point. A guard that only stops the
failure from being reported leaves the producer in place, and the next
caller runs into the same behavior.

### Re-running converges

An operation should be safe to run again. A second run that starts from
a finished state stays on that state. A run that stopped halfway is a
valid place to start, and finishing it reaches the same result as a run
that succeeded the first time. Role installers already work this way:
running the role again is how a machine picks up changes.

### Data shape before logic

Before writing branches, name the records you are storing, what type
each one has, and which part of the program owns them. With that
settled, the code that reads and updates those records gets shorter,
because the awkward cases have a place to live in the shape.

### Redesign instead of bolting on

Some requests are a founding assumption the current design never had.
Reshape the surrounding code so the new requirement sits where that
assumption would have sat from the start. Keep a compatibility shim
while a real caller still depends on the old shape, and remove the shim
in the same change when no caller does.

### Remove dead weight first

Before adding the new behavior, look for the unused path, the check that
no longer protects anything, and the stub left from an earlier attempt.
Remove those, then build on the code that remains.

### Build a rerunnable tool

A one-off edit can be done by hand. Work that will happen again, such as
a migration across many call sites, a repeated check, or a sweep of
similar edits, should leave a script or a skill behind. The next person
runs that artifact a second time instead of reconstructing the steps
from the last session.

## What this skill does not do

It does not tell the agent to stop and present a design before editing.
That rule is the next spec.

It does not disable Superpowers. Disabling that plugin is a config
change made at install time, after this skill exists.

It does not guarantee the model will open the file. A model that ignores
skill descriptions will not apply the list. The description is the
available lever on both harnesses without a hook.

## Tuning

Edit `skills/kobold-codex/SKILL.md` when a session shows that a paragraph
is wrong, too thin, or too long. Keep one copy. When the meaning of a
principle changes, note the change in a later spec or in the commit
message. This document keeps the 2026-10-01 wording.

## First implementation check

The first build is done when all of these are true:

- The tree matches the layout above.
- `SKILL.md` carries this voice section and these eight principles, with
  the frontmatter name and description from this spec. The heading text
  matches. The paragraphs match this document.
- `tests/check_plugin.py` fails when a paragraph, the frontmatter, the
  manifest names, or the install commands drift, and when a tracked file
  names a hostname, a home directory, or a machine.
- `grok plugin validate` accepts the plugin.
- The README states the install commands from this spec and does not
  restate the principles.
