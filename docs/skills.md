# Skills

Kobold Codex is a set of skills. A session uses the one whose description matches the task. This page is the map. The spec linked from each skill is the record of the decision that shipped. Later wording lives in the skill file.

## Which skill applies

The skills sit in groups, in the order a piece of work moves.

### Ground

Writing a reply, a diff, a commit message, or a document uses [skills/ground/kobold-codex/SKILL.md](../skills/ground/kobold-codex/SKILL.md). That skill is the voice and the engineering principles.

Changing a file, or making a commit, uses [skills/ground/scope-the-edit/SKILL.md](../skills/ground/scope-the-edit/SKILL.md). The scope of the edit decides the plan and the proof.

A commit, a push, a pull request, a merge, a force-push, an unattended stretch, or a named tool uses [skills/ground/set-the-bounds/SKILL.md](../skills/ground/set-the-bounds/SKILL.md). Resolve the bounds before the action.

### Investigate

A failure that can be run again uses [skills/investigate/debug-the-failure/SKILL.md](../skills/investigate/debug-the-failure/SKILL.md).

Reading a subsystem before changing it uses [skills/investigate/how-it-fits/SKILL.md](../skills/investigate/how-it-fits/SKILL.md).

A behavior or a threshold that needs a reason uses [skills/investigate/why-it-is/SKILL.md](../skills/investigate/why-it-is/SKILL.md).

A rewrite or a port that needs specs from an existing system, from its source or clean-room from docs and a running instance, uses [skills/investigate/spec-the-source/SKILL.md](../skills/investigate/spec-the-source/SKILL.md).

### Plan

An architectural change, or a request for a plan, uses [skills/plan/write-the-plan/SKILL.md](../skills/plan/write-the-plan/SKILL.md).

A task that should follow a playbook uses [skills/plan/run-the-play/SKILL.md](../skills/plan/run-the-play/SKILL.md).

A change whose first shape would stick uses [skills/plan/try-several-shapes/SKILL.md](../skills/plan/try-several-shapes/SKILL.md).

### Build

An approved plan uses [skills/build/carry-out-the-plan/SKILL.md](../skills/build/carry-out-the-plan/SKILL.md).

Feature work, or the execution of a plan, in its own checkout uses [skills/build/isolate-the-work/SKILL.md](../skills/build/isolate-the-work/SKILL.md).

Work that does not share state uses [skills/build/fan-out/SKILL.md](../skills/build/fan-out/SKILL.md).

A repo with no scripted way to drive the app the way a user does uses [skills/build/prove-the-product/SKILL.md](../skills/build/prove-the-product/SKILL.md).

### Review

A review before a merge, or a request to review a diff, uses [skills/review/review-the-diff/SKILL.md](../skills/review/review-the-diff/SKILL.md).

Review notes to check against the code use [skills/review/take-the-review/SKILL.md](../skills/review/take-the-review/SKILL.md).

Several independent passes over one diff use [skills/review/stress-the-change/SKILL.md](../skills/review/stress-the-change/SKILL.md).

A small diff, before it ships, uses [skills/review/measure-the-blast/SKILL.md](../skills/review/measure-the-blast/SKILL.md).

### Ship

Integrating a branch after its checks pass uses [skills/ship/ship-the-branch/SKILL.md](../skills/ship/ship-the-branch/SKILL.md).

### Session

A long run or an unattended run uses [skills/session/leave-a-trail/SKILL.md](../skills/session/leave-a-trail/SKILL.md).

A new session continuing work already in progress uses [skills/session/pick-up-the-work/SKILL.md](../skills/session/pick-up-the-work/SKILL.md).

### Learn

A lesson from a session that stumbled, or from a preference worth keeping, uses [skills/learn/learn-from-the-session/SKILL.md](../skills/learn/learn-from-the-session/SKILL.md).

A weekly pass over the session transcripts since the last review uses [skills/learn/review-the-week/SKILL.md](../skills/learn/review-the-week/SKILL.md).

Authoring or revising a skill in this plugin uses [skills/learn/write-a-skill/SKILL.md](../skills/learn/write-a-skill/SKILL.md).

### Write

A pass over prose or a diff for narration, stock phrasing, and comments that restate the code uses [skills/write/cut-the-slop/SKILL.md](../skills/write/cut-the-slop/SKILL.md).

A README, a spec, a pull request, or a commit message uses [skills/write/write-the-doc/SKILL.md](../skills/write/write-the-doc/SKILL.md).

### Setup

Adding Kobold to a repository uses [skills/setup/adopt-the-repo/SKILL.md](../skills/setup/adopt-the-repo/SKILL.md). The skill converts the repository's instructions into project skills and playbooks, or lays the folder and bounds foundation when the repository has none.

## Records

- [skills/ground/kobold-codex/SKILL.md](../skills/ground/kobold-codex/SKILL.md) is recorded in [docs/specs/2026-10-01-kobold-codex-design.md](specs/2026-10-01-kobold-codex-design.md).
- [skills/ground/scope-the-edit/SKILL.md](../skills/ground/scope-the-edit/SKILL.md) is recorded in [docs/specs/2026-10-01-scope-the-edit-design.md](specs/2026-10-01-scope-the-edit-design.md).
- [skills/ground/set-the-bounds/SKILL.md](../skills/ground/set-the-bounds/SKILL.md) is recorded in [docs/specs/2026-10-02-set-the-bounds-design.md](specs/2026-10-02-set-the-bounds-design.md).
- [skills/investigate/debug-the-failure/SKILL.md](../skills/investigate/debug-the-failure/SKILL.md) is recorded in [docs/specs/2026-10-02-debug-the-failure-design.md](specs/2026-10-02-debug-the-failure-design.md).
- [skills/investigate/how-it-fits/SKILL.md](../skills/investigate/how-it-fits/SKILL.md) is recorded in [docs/specs/2026-10-02-how-it-fits-design.md](specs/2026-10-02-how-it-fits-design.md).
- [skills/investigate/why-it-is/SKILL.md](../skills/investigate/why-it-is/SKILL.md) is recorded in [docs/specs/2026-10-02-why-it-is-design.md](specs/2026-10-02-why-it-is-design.md).
- [skills/plan/write-the-plan/SKILL.md](../skills/plan/write-the-plan/SKILL.md) is recorded in [docs/specs/2026-10-02-write-the-plan-design.md](specs/2026-10-02-write-the-plan-design.md).
- [skills/build/carry-out-the-plan/SKILL.md](../skills/build/carry-out-the-plan/SKILL.md) is recorded in [docs/specs/2026-10-02-carry-out-the-plan-design.md](specs/2026-10-02-carry-out-the-plan-design.md).
- [skills/review/review-the-diff/SKILL.md](../skills/review/review-the-diff/SKILL.md) is recorded in [docs/specs/2026-10-03-review-the-diff-design.md](specs/2026-10-03-review-the-diff-design.md).
- [skills/review/take-the-review/SKILL.md](../skills/review/take-the-review/SKILL.md) is recorded in [docs/specs/2026-10-03-take-the-review-design.md](specs/2026-10-03-take-the-review-design.md).
- [skills/review/stress-the-change/SKILL.md](../skills/review/stress-the-change/SKILL.md) is recorded in [docs/specs/2026-10-03-stress-the-change-design.md](specs/2026-10-03-stress-the-change-design.md).
- [skills/ship/ship-the-branch/SKILL.md](../skills/ship/ship-the-branch/SKILL.md) is recorded in [docs/specs/2026-10-03-ship-the-branch-design.md](specs/2026-10-03-ship-the-branch-design.md).
- [skills/plan/run-the-play/SKILL.md](../skills/plan/run-the-play/SKILL.md) is recorded in [docs/specs/2026-10-03-run-the-play-design.md](specs/2026-10-03-run-the-play-design.md).
- [skills/build/isolate-the-work/SKILL.md](../skills/build/isolate-the-work/SKILL.md) is recorded in [docs/specs/2026-10-03-isolate-the-work-design.md](specs/2026-10-03-isolate-the-work-design.md).
- [skills/build/fan-out/SKILL.md](../skills/build/fan-out/SKILL.md) is recorded in [docs/specs/2026-10-03-fan-out-design.md](specs/2026-10-03-fan-out-design.md).
- [skills/plan/try-several-shapes/SKILL.md](../skills/plan/try-several-shapes/SKILL.md) is recorded in [docs/specs/2026-10-03-try-several-shapes-design.md](specs/2026-10-03-try-several-shapes-design.md).
- [skills/review/measure-the-blast/SKILL.md](../skills/review/measure-the-blast/SKILL.md) is recorded in [docs/specs/2026-10-03-measure-the-blast-design.md](specs/2026-10-03-measure-the-blast-design.md).
- [skills/build/prove-the-product/SKILL.md](../skills/build/prove-the-product/SKILL.md) is recorded in [docs/specs/2026-10-03-prove-the-product-design.md](specs/2026-10-03-prove-the-product-design.md).
- [skills/session/leave-a-trail/SKILL.md](../skills/session/leave-a-trail/SKILL.md) is recorded in [docs/specs/2026-10-03-leave-a-trail-design.md](specs/2026-10-03-leave-a-trail-design.md).
- [skills/session/pick-up-the-work/SKILL.md](../skills/session/pick-up-the-work/SKILL.md) is recorded in [docs/specs/2026-10-03-pick-up-the-work-design.md](specs/2026-10-03-pick-up-the-work-design.md).
- [skills/learn/learn-from-the-session/SKILL.md](../skills/learn/learn-from-the-session/SKILL.md) is recorded in [docs/specs/2026-10-03-learn-from-the-session-design.md](specs/2026-10-03-learn-from-the-session-design.md).
- [skills/learn/write-a-skill/SKILL.md](../skills/learn/write-a-skill/SKILL.md) is recorded in [docs/specs/2026-10-03-write-a-skill-design.md](specs/2026-10-03-write-a-skill-design.md).
- [skills/write/cut-the-slop/SKILL.md](../skills/write/cut-the-slop/SKILL.md) is recorded in [docs/specs/2026-10-03-cut-the-slop-design.md](specs/2026-10-03-cut-the-slop-design.md).
- [skills/write/write-the-doc/SKILL.md](../skills/write/write-the-doc/SKILL.md) is recorded in [docs/specs/2026-10-03-write-the-doc-design.md](specs/2026-10-03-write-the-doc-design.md).
- [skills/setup/adopt-the-repo/SKILL.md](../skills/setup/adopt-the-repo/SKILL.md) is recorded in [docs/specs/2026-10-04-adopt-the-repo-design.md](specs/2026-10-04-adopt-the-repo-design.md).
- The model tier routing revision of `set-the-bounds`, `write-the-plan`, `carry-out-the-plan`, `fan-out`, `try-several-shapes`, `ship-the-branch`, `adopt-the-repo`, and `write-a-skill` is recorded in [docs/specs/2026-10-11-model-tier-routing-design.md](specs/2026-10-11-model-tier-routing-design.md).
- The adversarial review revision of `stress-the-change`, `review-the-diff`, `take-the-review`, `carry-out-the-plan`, `set-the-bounds`, and `adopt-the-repo` is recorded in [docs/specs/2026-10-11-adversarial-review-design.md](specs/2026-10-11-adversarial-review-design.md).
- The surgical changes revision of `kobold-codex` and `review-the-diff` is recorded in [docs/specs/2026-10-11-surgical-changes-design.md](specs/2026-10-11-surgical-changes-design.md).
- [skills/learn/review-the-week/SKILL.md](../skills/learn/review-the-week/SKILL.md) is recorded in [docs/specs/2026-10-12-review-the-week-design.md](specs/2026-10-12-review-the-week-design.md). The same spec records the `commit-reviews` key and the `commit-plans` default in `set-the-bounds`, `adopt-the-repo`, and `ship-the-branch`.
- The past specs and review window revision of `write-a-skill`, `learn-from-the-session`, `set-the-bounds`, and `review-the-week` is recorded in [docs/specs/2026-10-12-past-specs-and-review-window-design.md](specs/2026-10-12-past-specs-and-review-window-design.md).
- The status and plan opening revision of `carry-out-the-plan`, `leave-a-trail`, `pick-up-the-work`, `write-the-plan`, `set-the-bounds`, and `review-the-week` is recorded in [docs/specs/2026-10-12-status-and-plan-opening-design.md](specs/2026-10-12-status-and-plan-opening-design.md).
- The isolate-the-work trigger lesson is recorded in [docs/specs/2026-10-13-isolate-the-work-trigger-design.md](specs/2026-10-13-isolate-the-work-trigger-design.md).
- The carry-out-the-plan noted-bug lesson is recorded in [docs/specs/2026-10-13-carry-out-the-plan-noted-bug-design.md](specs/2026-10-13-carry-out-the-plan-noted-bug-design.md).
- The changes-off-the-tree heading in `ship-the-branch` is recorded in [docs/specs/2026-10-13-changes-off-the-tree-design.md](specs/2026-10-13-changes-off-the-tree-design.md).
- [skills/investigate/spec-the-source/SKILL.md](../skills/investigate/spec-the-source/SKILL.md) is recorded in [docs/specs/2026-10-24-spec-the-source-design.md](specs/2026-10-24-spec-the-source-design.md).
- The tracker requirements and one source of truth revision of `kobold-codex`, `adopt-the-repo`, `set-the-bounds`, `spec-the-source`, `ship-the-branch`, `write-the-plan`, `review-the-diff`, and `write-a-skill` is recorded in [docs/specs/2026-10-31-tracker-requirements-design.md](specs/2026-10-31-tracker-requirements-design.md).
