# Model tier routing

Design for sending fast work to a faster model. This spec revises
`set-the-bounds`, `write-the-plan`, `carry-out-the-plan`, `fan-out`,
`try-several-shapes`, `ship-the-branch`, `adopt-the-repo`, and
`write-a-skill`. The wording in the skill
sections below is the version to ship. Later sessions tune it by
editing the skill files. This spec stays the record of what we
decided and why.

## Purpose

A plan holds tasks that need the model running the session, and
tasks that only repeat what the code already shows. Today every
task runs on the session's model. This change gives each plan task
a work kind, hands the fast kinds to a faster model, and keeps the
reasoning on the session's model.

The idea comes from the @cyrilXBT post on cutting a coding agent's
cost, <https://x.com/cyrilXBT/status/2108693524900110515>. That post
scores options by probability and keeps thresholds and retry caps in
harness code. These hosts give a skill neither, so the skills state
rules instead.

`scope-the-edit` still names the scope and decides the plan and the
proof. `set-the-bounds` resolves `subagents`, `model`, and the new
`model-fast`. The other skills read the resolved values. The creed
stays in `skills/kobold-codex/SKILL.md`.

Success for this version is a set of skills that a Grok session and
a Claude Code session can both load, whose section bodies match the
skill sections below.

## Decisions

Route by kind of work, not by size. Each task in a plan names one
kind from a fixed list: `rename-or-move`, `follow-a-pattern`,
`docs-or-config`, `new-logic`, `debugging`, and `design`. The first
three are fast work. The other three stay on the session's model.
The list is fixed in the skill. A session does not add a kind, and
a model does not write the list it picks from.

`docs-or-config` edits prose, comments, or configuration and
changes no code. Production config is not part of that kind. It
stays on the list of work that never goes to the fast model.

The scope in `scope-the-edit` is not the signal. Scope measures how
much plan and proof a change needs. Kind measures how much
reasoning it needs. An intermediate one-line fix with a decision in
it is small in size and still needs the session's model. A rename
across forty files is wide and still mechanical.

A task whose kind is unclear stays on the session's model. The
errors are lopsided. A hard task sent to the fast model costs a
failed check, a takeover, and the time in between. An easy task
kept on the session's model costs only the price difference. A fast
kind needs a clear fit.

A fast task goes to another agent even when the plan orders it
after another task. Parallel work was the only reason to start
another agent before. Cost is now a second reason. `subagents`
still gates both. When the key does not allow another agent, the
task runs in this session.

Under `subagents: ask`, one yes covers the whole plan run. A plan
with a dozen fast tasks would otherwise ask a dozen times, and an
ask nobody reads is no gate. The yes names the plan file, the same
way approval of the plan names it. A later run of the same plan
asks again, because the bounds or the plan may have changed since.
`set-the-bounds` records this as the one place an `ask` covers more
than one action. `fan-out` and `try-several-shapes` keep one yes
per action.

The brief for a fast task names the files to change, the existing
code to copy, the check that ends the task, and only the notes that
task needs. The session's model picks those notes. The worker
returns its diff and the check output. It does not commit, push, or
edit the plan file. This session reads the diff and marks the
checkbox, the same way `carry-out-the-plan` already marks a
checkbox for a task another agent ran. The source post left the
handoff format open. This brief is that format.

Escalate once, then stop. When a fast worker's check fails, the
session's model takes that task over once, starting from the
worker's diff. The diff holds what the worker got right, and the
check output says where it went wrong. Starting from the files
before the diff would pay for the fast work twice. When the
session's check fails too, the run stops the way a failed check
stops it today. A second takeover would hide a plan that is wrong.

A failed run is a command that did not reach a result. It is not a
failed check. After a failed run the session or the worker picks
one move from a fixed list: retry unchanged, install the missing
piece and retry, fix the path and retry, switch to another tool,
hand the task to the session's model, or stop and report. Three
attempts is the limit for one run. A skill cannot hold a counter,
so the limit is a hard rule in the text, and stop and report is the
only move after the third attempt.

Narrow checks run first. Lint and type checks on the changed files
come first, then the tests most relevant to those files, then the
check the plan names. A narrow failure ends the attempt early. The
narrow tests are the session's pick.

The gate before a commit of the work is a filtered test list when
the repo has a way to produce one: the tests selected for the
changed files or for the affected area. The full suite runs only
when no filtered list is available. A good suite's run time tends
toward exponential growth as the project ages, so a full run before
every commit stops being affordable. The filtered list is the
repo's own selection, not the session's, so it is the gate.

The gate sits in `carry-out-the-plan` for commits inside a plan
run, and in `ship-the-branch` for every other commit of the work.
`ship-the-branch` already runs the named checks before its first
commit (`skills/ship-the-branch/SKILL.md`:16-20). A gate that
already passed on the same tree can be cited instead of run again.

How a repo produces its filtered list is a project fact, not a
bound. A bounds key is a permission with a fixed set of values, and
a test command is neither, so `set-the-bounds` stays out of it.
`adopt-the-repo` already turns a fact into a project skill
(`skills/adopt-the-repo/SKILL.md`:86-87), so a source sentence
about selecting tests lands in the project's testing skill with no
new rule. A session finds the way in a project skill, an
instruction file, or the project's test tool. When none of those
names one, the full suite is the gate.

Some work never goes to the fast model, whatever its kind: deleting
a file, a force-push, a migration, and a change to production
config. A mistake there is hard to undo or reaches past the repo.
Those tasks stay in this session. `force-push` keeps its own key as
well.

Note scoring stays out. The source post scores each chunk of the
project notes against the task. These hosts manage context, and a
skill has no score to read. The brief carrying only the notes the
task needs is the stand-in. The session's model picks them, because
a wrong pick derails the worker without a visible error.

`set-the-bounds` gains one key, `model-fast`. It takes a free-form
name, like `model`. When it is absent, the fast model is `model`.
When both are absent, the fast model is the session's model, and
fast work runs in this session, because there is no faster model
to hand it to.

This revises an earlier deferral. The catalog said "A model-per-role
table stays out until the single optional `model` key is not
enough" (`docs/specs/2026-10-02-remaining-skills-design.md`:389).
`set-the-bounds` said "A model-per-role table stays out" and "The
optional `model` key is the menu"
(`docs/specs/2026-10-02-set-the-bounds-design.md`:54-55 and :248).
The creed spec said "no model routing"
(`docs/specs/2026-10-01-kobold-codex-design.md`:100). One `model`
key is no longer enough. Routed work now has two sides, the
reasoning and the fast work, and one name cannot be both. One extra
key covers the second side. A full table stays out. It would need a
role list and a name per role, and nothing yet needs a third model.
The table waits until two keys are not enough.

`carry-out-the-plan` and `try-several-shapes` start other agents
and do not read `model` today. `fan-out` and `stress-the-change`
do. This change fixes that. A task, a piece, or a candidate that is
not fast work and runs in another agent uses `model`, then the
session's model. A candidate in `try-several-shapes` is design
work, so it never uses the fast model. A piece in `fan-out` that is
a task of a fast kind uses the fast model, under the rules for fast
work in `carry-out-the-plan`.

`adopt-the-repo` suggests `model` and `model-fast` in its bounds
table. The names come from the host the session runs on: the
strongest model that host offers for `model`, and a faster, cheaper
one for `model-fast`. The skill text names no host and no model. A
session reads its own host's list, so the same text works on Grok
CLI and on Claude Code. The rows are suggestions. They are written
only on the confirmation The bounds already asks for
(`skills/adopt-the-repo/SKILL.md`:197-201).

The model rows are the one exception to the rule that a key needs a
source sentence (`skills/adopt-the-repo/SKILL.md`:163-164 and
:194-195). A model name is a fact about the host, not about the
repo. A source sentence that names a model is shown beside the
host's suggestion, and the user picks, the same as two sentences
that disagree. An empty tree still gets the model rows (:323-325).
The config repo table does not get them. That repo holds history,
not work.

The model rows suggest the checkout layer,
`.kobold/bounds.local.yaml`, whatever the path. A name one host
offers may not exist on the other, and a team repo can be opened
from either host. The user can name the committed layer instead.

`stress-the-change` and `review-the-diff` stay on the session's
model or `model`. A review pass is the kind of final call a fast
model should not make. Their text does not change.

`scope-the-edit` and `run-the-play` and its playbooks do not
change. The build step in `run-the-play`
already hands an approved plan to `carry-out-the-plan`. Work under
a small or intermediate scope has no plan and no kind, so it stays
in this session.

The `carry-out-the-plan` description changes, because the old one
says tasks run in this session and only independent tasks go to
another agent. The other descriptions stay.

`write-a-skill` says to update the check in the same change that
adds a skill file. `tests/check_plugin.py` reads only the manifests
and the version, so that line is stale. It is fixed in this change.

Nothing in the skills names a Grok tool or a Claude tool, or a
model by brand. No hooks.

The release is a minor bump to `1.1.0` in both manifests. The
implementation plan makes that bump, not this spec.
`tests/check_plugin.py` does not change. The manifest description
stays the stable sentence in the catalog's ship rule.

The root README stays the introduction and the install guide. It
does not record this decision. `docs/skills.md` gains one line
under Records that links this spec for the eight skills it revises.
The dated specs for those skills stay the record of what shipped
first.

## Where the words live

```text
skills/set-the-bounds/SKILL.md
skills/write-the-plan/SKILL.md
skills/carry-out-the-plan/SKILL.md
skills/fan-out/SKILL.md
skills/try-several-shapes/SKILL.md
skills/ship-the-branch/SKILL.md
skills/adopt-the-repo/SKILL.md
skills/write-a-skill/SKILL.md
docs/specs/2026-10-11-model-tier-routing-design.md
docs/plans/2026-10-11-model-tier-routing.md
docs/skills.md
```

The creed, `scope-the-edit`, `stress-the-change`, `review-the-diff`,
and `run-the-play` and its playbooks stay. The
sentences in the earlier specs that defer a model table stay as the
record. This spec is the later record that revises them.

## Skill

Each region below is one skill file. The region heading names the
skill. `## Skill: set-the-bounds` is
`skills/set-the-bounds/SKILL.md`. Each `###` section in a region
replaces the `##` section with the same heading in that file, with
the same body. A `###` heading the file does not have yet is a new
`##` section, placed where the region says. A section the region
does not name stays as it is. Heading text matches. Paragraphs
match, including line breaks.

## Skill: set-the-bounds

The frontmatter stays. The three sections below replace the
sections with the same headings.

### Resolve first

Before a commit of the work, a commit of plans, a commit of specs, a
push, a pull request, a merge, a force-push, an unattended stretch, or
a named tool, read the four layers and use the resolved value. Say each
key that governs the action, the value, and the layer that set it.
Reading the repo, editing files, and running the project's own checks
are ordinary work. Those actions have no key.

`ask` stops for a yes that names this action. A yes for a different
action does not carry. `auto`, `open`, and `allow` proceed. `never`
and `deny` stop the action.

One `ask` covers more than one action in one place. Under
`subagents: ask`, a yes that names a plan file covers every agent
`carry-out-the-plan` starts in that run of the plan. A later run
asks again.

### Defaults

| Key | Default | Description |
| --- | --- | --- |
| `commit` | `ask` | Work commit. Changed and untracked files outside the plan directory and the spec directory. |
| `commit-plans` | `never` | Commit of plan files, in the directory `write-the-plan` uses. |
| `commit-specs` | `ask` | Commit of spec files, in the directory the project uses for design specs. |
| `push` | `ask` | Update the remote branch. |
| `pull-request` | `ask` | Open a pull request. |
| `merge` | `never` | Merge the pull request. |
| `force-push` | `never` | Rewrite the remote branch. Also requires `push` to be `ask` or `auto`. |
| `shell-network` | `ask` | A shell command that reaches the network. |
| `browser` | `ask` | Driving a browser. |
| `github-write` | `ask` | Comments, labels, issues, and review submission. |
| `subagents` | `ask` | Starting other agents. |
| `worktrees` | `ask` | An isolated checkout. |
| `unattended` | `stop-at-plan` | How far a session goes while the user is away. |
| `model` | absent | Optional model name for routed work. Absent keeps the session's current model. |
| `model-fast` | absent | Optional model name for fast work. Absent falls back to `model`, then to the session's current model. |

### Values

`commit`, `commit-plans`, `commit-specs`, and `push` are `ask`, `auto`,
or `never`. `pull-request` is `never`, `ask`, `open`, or `auto`.
`merge` and `force-push` are `never` or `ask`. A tool key is `ask`,
`allow`, `auto`, or `deny`. The tool keys in the default set are
`shell-network`, `browser`, `github-write`, `subagents`, and
`worktrees`. A bounds file may add a tool name. `unattended` is
`stop-at-plan`, `safe-steps`, `through-publish`, or `auto`.

`auto` on `pull-request` opens one pull request without a fresh ask,
the same as `open`. `auto` on a tool key proceeds, the same as
`allow`. `auto` on `unattended` follows the publishing keys, the same
as `through-publish`.

A setting line is a key, a colon, and a value. Blank lines are skipped.
A line that is not a setting stays in the file and sets nothing. A
value outside the set for a key that has one does not resolve. `model`
and `model-fast` take a name, so that check skips them. Tell the user
the line, and keep the value from the layer behind that file.

## Skill: write-the-plan

The frontmatter stays. The section below replaces Tasks.

### Tasks

Under those four things, list the tasks in the order a later session
will run them. A task names the files it changes, the check that
ends it, and the result that counts as done. The check is a command,
a screen, or a file the reviewer can run or read. A task is one
change and that check. When a task needs an earlier task finished,
it names that task.

Each task names one work kind, on a line of its own under the task,
written `Kind: follow-a-pattern`. The kinds are `rename-or-move`,
`follow-a-pattern`, `docs-or-config`, `new-logic`, `debugging`, and
`design`. `rename-or-move` renames or moves code and changes no
behavior. `follow-a-pattern` repeats a change the code already has,
and the task names the existing code it copies. `docs-or-config`
edits prose, comments, or configuration and changes no code.
`new-logic` adds a decision the code does not have yet. `debugging`
finds the cause of a failure. `design` picks a structure. Use no
other kind.

A fast kind needs a clear fit. When the kind is unclear, or when a
second kind also fits, name the kind of the hardest part of the
task. `carry-out-the-plan` says which kinds go to the fast model.

A task that changes a function names a check that reaches the bar in
`scope-the-edit`. Write the command and the result in the task.

Each task, and each step under it, begins with an empty checkbox,
written `- [ ]`, on a new plan. Write each step so an empty checkbox
is a valid place to start. A later session marks a finished checkbox
`- [x]`. An edit of the plan follows Where it goes.

## Skill: carry-out-the-plan

Frontmatter `name` stays `carry-out-the-plan`. Frontmatter
`description` becomes one physical line:

```text
Use when a plan has been approved. Run its tasks in order, hand fast tasks and independent tasks to another agent only when subagents allows it, and finish each task on the check the plan named.
```

An approved plan, In order, and The same plan stay. Beside this
session and The check are replaced. The fast model and The brief
are new, placed after Beside this session. A failed run is new,
placed after The check.

### Beside this session

Resolve `subagents` once, before the first task that would start
another agent. When the value is `ask`, ask once. The yes names
this plan file, and it covers every agent this run starts for the
plan, fast work included. A later run asks again. `set-the-bounds`
is that rule.

A task may run beside another when the plan does not order one
before the other, and the two tasks change no file in common. When
`subagents` allows another agent, those tasks may run together. The
other agent does the task and returns the result. It leaves the
plan file alone. This session marks the checkbox. When `subagents`
does not allow another agent, run those tasks one after another in
this session.

A task that is not fast work and runs in another agent uses
`model`. When `model` is absent, it uses the model already running
the session.

The work stays in the checkout you are already in.

While the user is away, `unattended` still applies.
`set-the-bounds` is that rule. `stop-at-plan` does not start a
task, because the plan is already written.

### The fast model

A task whose kind is `rename-or-move`, `follow-a-pattern`, or
`docs-or-config` is fast work. `write-the-plan` names the kind. A
task with any other kind, with no kind, or with a kind outside that
list stays on the model running this session.

The fast model is `model-fast`. When `model-fast` is absent, it is
`model`. When both are absent, it is the model running this
session, and fast work runs in this session.

Fast work goes to another agent on the fast model, including a task
the plan orders after another, when `subagents` allows another
agent. When it does not, run the task in this session.
When the other agent cannot start on that model, run the task in
this session, and say so.

Some work never goes to the fast model, whatever its kind: deleting
a file, a force-push, a migration, and a change to production
config. A task that does any of these stays in this session.

### The brief

The brief for a fast task names the files to change, the existing
code to copy, the check that ends the task, and the notes that task
needs. This session picks those notes. A note the task does not
need stays out of the brief.

The worker changes only the files the brief names. It does not
commit, push, or edit the plan file. It returns its diff and the
output of the check.

Read the diff before marking the checkbox. A diff that changes a
file the brief did not name, or that misses a change the brief
asked for, is a failed check.

### The check

Run the narrow checks first. Those are the project's lint and type
checks on the changed files, then the tests most relevant to those
files. A narrow check that fails is a failed check. When the
project has no lint or type check, say so and go on. Then run the
check the plan names.

A task's check is done when you have run the check the plan names
and the result is the one the plan describes. Record the result you
observed. Mark the checkbox for that step `- [x]`.

When a fast worker's check fails, this session takes that task over
once, on its own model, starting from the worker's diff. When that
check fails too, or when a task this session ran fails its check,
stop. Report the task, the check, and the result. Leave every later
checkbox empty.

When a task names no check, stop and ask for the check before
starting the task.

Before each commit of the work, run the gate. The gate is a
filtered test list when the project has a way to produce one: the
tests selected for the changed files or for the affected area. A
project skill, an instruction file, or the project's test tool can
name that way. When none does, the gate is the full suite. Say
which gate ran. When it fails, stop before the commit, and name the
tests that failed.

Marking a checkbox is part of finishing that step. Committing the
plan file follows `commit-plans`. A task that commits, pushes, or
opens a pull request still follows `set-the-bounds`.

### A failed run

A failed run is a command that did not reach a result: a missing
tool or package, a wrong path, or a crash before the check reports.
A check that runs and reports a failure is a failed check, not a
failed run.

After a failed run, pick one move from this list. Retry unchanged.
Install the missing piece, then retry. Fix the path, then retry.
Switch to another tool for the same step. Hand the task to the
model running this session. Stop and report. There is no other
move. An install that reaches the network follows `shell-network`.

Three attempts is the limit for one run. The first run is the first
attempt. After the third failed attempt, the only move is stop and
report. The limit holds for a worker and for this session. A change
of move does not reset the count.

Handing the task over is a fast worker's move. It ends the worker's
attempts, and it is the one takeover The check allows. This session
starts its own count, from the worker's diff.

Stop and report names the run, each attempt and its move, and the
last error output.

## Skill: fan-out

The frontmatter stays. The section below replaces The workers.

### The workers

Resolve `subagents` before starting another agent. When that key
allows another agent, the pieces run together. A worker returns
its result. It does not write the report, and it does not change
a file another piece changes. This session writes the report.

When `subagents` does not allow another agent, run the pieces one
after another in this session, and say that the run was serial.

When `model` is set, a worker in another agent uses that model.
When `model` is absent, the worker uses the model already running
the session. A piece that is a task of a fast kind in
`write-the-plan` uses the fast model instead. The rules for fast
work in `carry-out-the-plan` apply to that piece.

While the user is away, `unattended` still applies.
`set-the-bounds` is that rule. When that rule blocks another
agent and still allows the work, run the pieces in this session.

A worker that does not return leaves the report unfinished. Name
the missing piece and stop. Leave the finished pieces unmerged.

## Skill: try-several-shapes

The frontmatter stays. The section below replaces The candidates.

### The candidates

Name at least two candidates before building any of them. Three
is the set when the user names none. Each candidate is one
sentence that says how it differs from the others. A wider set
waits until the user names the extra candidates.

Name the work's branch before any checkout. The branch for a
candidate is that name, a hyphen, and a short name for the
candidate. `isolate-the-work` is the rule for a branch that does
not exist yet, and for the checkout.

Resolve `worktrees` once for the set. `set-the-bounds` is that
rule. When the value allows a checkout, each candidate is built
in its own checkout. When the value is `ask`, `isolate-the-work`
asks once per checkout, and the yes names that checkout. When the
value does not allow a checkout, leave each candidate as the
sentence in the reply, and build none of them until the base is
picked.

When each candidate has its own checkout, the candidates share no
files. This skill builds each candidate in its checkout. When
`subagents` allows it, those builds may run together. A build in
another agent uses `model`. When `model` is absent, it uses the
model already running the session. A candidate is design work, so
it does not go to the fast model. This skill reads each result,
then picks the base and folds.

The candidate sentences, and a checkout the key allows, are the
exploration. `scope-the-edit` applies to the fold.

## Skill: ship-the-branch

The frontmatter stays. The section below replaces The branch.

### The branch

Ship the branch the user named. When the user names none, ship the
current branch. When the checkout has no branch, stop, and say so.

When that branch is the branch a pull request would merge into,
stop, and name it.

Run every check the plan or the change named. A check the user
names for this ship is one of those checks. Run them before any
later action in this skill. A failed check stops the ship. A check
that cannot be run stops the ship, and the reply names the reason.
When no check is named, stop and ask which check to run.

Before those checks, run the narrow checks. Those are the project's
lint and type checks on the files the branch changes, then the
tests most relevant to those files. After the named checks, run the
gate. The gate is a filtered test list when the project has a way
to produce one: the tests selected for the changed files or for the
affected area. A project skill, an instruction file, or the
project's test tool can name that way. When none does, the gate is
the full suite. Say which gate ran. A gate that already passed on
the same tree can be cited. Name that run. A narrow check or a gate
that fails stops the ship the same way a failed check does.

When the user is away, `unattended` still decides how far the ship
goes. `set-the-bounds` is that rule.

The reply names each action this run took and each one it skipped.
Name the key that governed it. A ship that stops on the checks does
not commit, push, open a pull request, merge, or remove a checkout.

## Skill: adopt-the-repo

The frontmatter stays. The two sections below replace the sections
with the same headings.

### The bounds

After the sources are read, and in the same question set as the
path and the skill root, show a table. The columns are the key,
the suggested value, the file and the sentence that suggested it,
and the value that applies if this repository writes nothing.

Suggest a key only when a sentence is about the action that key
controls. `model` and `model-fast` are the exception below.

A file that forbids commits outright suggests `commit: never`. A
file that says to commit without asking suggests `commit: auto`.
Anything softer, including commits that depend on the branch,
suggests `commit: ask`. The same three values apply to `push`,
`commit-plans`, and `commit-specs`, using the sentences about
those actions.

Always opening a pull request suggests `pull-request: auto`.
Opening one only when asked suggests `pull-request: ask`. Never
opening one suggests `pull-request: never`. A ban on merge
suggests `merge: never`. Merge only when asked suggests
`merge: ask`. A ban on rewriting the remote suggests
`force-push: never`. A rewrite only when asked suggests
`force-push: ask`.

Work that continues through publish while the user is away
suggests `unattended: through-publish`. Stopping at the plan
suggests `unattended: stop-at-plan`. Editing and checking
without publishing suggests `unattended: safe-steps`. A ban on
other agents suggests `subagents: deny`. Permission to start
them without an ask suggests `subagents: allow`. A sentence that
still requires an ask suggests `subagents: ask`. The same three
readings apply to `browser`, `shell-network`, `github-write`,
and `worktrees`.

The suggestions for `model` and `model-fast` come from the host
this session runs on. Name models from the list that host offers.
Suggest the strongest for `model`, and a faster, cheaper one for
`model-fast`. The source column names the host's list. When the
session cannot read that list, the two rows show no suggestion,
and the reply says so. A source sentence that names a model is
shown beside the host's suggestion. Ask which value.

A branch policy the keys cannot express is not a suggestion. It
stays a skill or a playbook, and the reply names the sentence.
Two sentences that suggest different values for one key are both
shown. Ask which value. A key with no sentence, other than the two
model keys, has no suggestion. Its row shows the inherited value.

Ask which layer, with the suggestion from The choice, and which
keys to write. For `model` and `model-fast`, suggest
`.kobold/bounds.local.yaml`, because a name one host offers may
not exist on the other. The user can name the committed layer
instead. Then `set-the-bounds` writes only the keys the user
named, on the layer they named for each, at the project root.
When the user names no keys, write no project bounds file. That
includes a user who keeps the inherited values.

### An empty tree

When the read finds no instruction files and no skills, skip The
move's conversion. Still ask the path, the skill root, the bounds
table, the plans and specs question, and The local repo when a
path will stay out of the project.

Create the skill root, the playbook directory, the plan
directory, and the spec directory. A path the config repo holds
is a real directory inside that repo, and the project path is
the relative symlink The local repo names. A path it does not
hold is a real directory in the project. Apply the hide choice.
Write `.kobold/adopt.yaml`.

On the full path, create `AGENTS.md` at the repository root. Its
body is the pointer, unless the user supplies a why sentence, in
which case the why comes first and the pointer follows. Do not
invent a product purpose. On the shadow path, create no
instruction file.

The bounds table on an empty tree has no file sentences. Every
row other than `model` and `model-fast` shows the inherited value
and no suggestion. The two model rows show the host's suggestions.
Writing still waits for keys the user names.

## Skill: write-a-skill

The frontmatter stays. The section below replaces The check.

### The check

`tests/check_plugin.py` checks the manifests, and it requires a
branch off main to be ahead on version. It reads no skill file.
When a change needs a new check, add it in the same change.

The plugin version bumps in that change. The manifest description
stays the sentence the catalog's ship rule records. The root
README does not gain a link to the spec, and it does not restate a
section body. `docs/skills.md` links the skill and the spec, and
it does not restate a section body.

A revision edits the skill file. The dated spec stays the record
of the decision that shipped. A new heading is added to the skill
file.

## What this skill does not do

It does not add a third model key or a model-per-role table. Two
names, `model` and `model-fast`, cover routed work.

It does not route by scope. `scope-the-edit` still names the scope,
and the scope still decides the plan and the proof.

It does not score notes, options, or confidence. The kinds and the
moves are fixed lists, and the rules pick from them.

It does not send a review pass, a candidate, or an unclear task to
the fast model.

It does not let a worker commit, push, mark a checkbox, or edit the
plan file.

It does not ask for each handoff under `subagents: ask`. One yes
covers a plan run.

It does not run the full suite before a commit when the repo can
produce a filtered test list.

It does not put a test command in a bounds file. How a repo selects
its tests is a project fact.

It does not name a model in skill text. `adopt-the-repo` reads the
names from the host, and writes them only on the user's
confirmation.

It does not change `stress-the-change`, `review-the-diff`,
`scope-the-edit`, `run-the-play` or its playbooks, the creed, or the
catalog.

It does not bump the version. The implementation plan does that.

## Tuning

Edit the skill files when a session shows that a paragraph is
wrong, too thin, or too long. Keep one copy. When a session shows a
kind that keeps landing on the wrong model, change the kind list in
`write-the-plan` and the fast kinds in `carry-out-the-plan` in the
same change. When a commit passes the filtered gate and a later
full run fails on a test the list left out, fix the way the repo
selects tests, in the project's own skill. When the meaning of a
section changes, note the change in a later spec or in the commit
message. This document keeps the 2026-10-11 wording.

## Implementation check

The build is done when all of these are true:

- Each skill file in Where the words live carries the sections its
  region above names. The heading text matches. The paragraphs
  match this document. The sections a region does not name are
  unchanged.
- `skills/carry-out-the-plan/SKILL.md` carries the new description
  on one physical line, and its sections run An approved plan, In
  order, Beside this session, The fast model, The brief, The check,
  A failed run, The same plan.
- `skills/adopt-the-repo/SKILL.md` names no model. Its `model` and
  `model-fast` rows come from the host's list at run time.
- No skill file names a Grok tool, a Claude tool, or a model by
  brand. The repo has no `hooks/` directory and no `hooks.json`.
- `skills/kobold-codex/SKILL.md`, `skills/scope-the-edit/SKILL.md`,
  `skills/stress-the-change/SKILL.md`,
  `skills/review-the-diff/SKILL.md`, `skills/run-the-play/` and its
  playbooks, the earlier specs, and the catalog are unchanged.
- Plugin version is `1.1.0` in `.claude-plugin/plugin.json` and in
  the plugin entry in `.claude-plugin/marketplace.json`, and both
  descriptions match the stable sentence in the catalog's ship
  rule.
- `python3 tests/check_plugin.py` exits 0 on the branch, with
  `1.1.0` ahead of `1.0.0` on `main`.
- The root README keeps the install commands and does not link this
  spec. `docs/skills.md` links this spec under Records. The README
  does not restate the paragraphs.
- `grok plugin validate .` accepts the plugin and reports version
  `1.1.0`. When `grok` is not on the path, say so and leave that
  check open.
- No tracked file names a hostname, a home directory, or a machine.
