#!/usr/bin/env python3
"""Pin Kobold Codex to the specs."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = ROOT / "docs/specs/2026-10-01-kobold-codex-design.md"
SKILL = ROOT / "skills/kobold-codex/SKILL.md"
SCOPE_SPEC = ROOT / "docs/specs/2026-10-01-scope-the-edit-design.md"
SCOPE_SKILL = ROOT / "skills/scope-the-edit/SKILL.md"
BOUNDS_SPEC = ROOT / "docs/specs/2026-10-02-set-the-bounds-design.md"
BOUNDS_SKILL = ROOT / "skills/set-the-bounds/SKILL.md"
DEBUG_SPEC = ROOT / "docs/specs/2026-10-02-debug-the-failure-design.md"
DEBUG_SKILL = ROOT / "skills/debug-the-failure/SKILL.md"
FITS_SPEC = ROOT / "docs/specs/2026-10-02-how-it-fits-design.md"
FITS_SKILL = ROOT / "skills/how-it-fits/SKILL.md"
WHY_SPEC = ROOT / "docs/specs/2026-10-02-why-it-is-design.md"
WHY_SKILL = ROOT / "skills/why-it-is/SKILL.md"
PLAN_SPEC = ROOT / "docs/specs/2026-10-02-write-the-plan-design.md"
PLAN_SKILL = ROOT / "skills/write-the-plan/SKILL.md"
CARRY_SPEC = ROOT / "docs/specs/2026-10-02-carry-out-the-plan-design.md"
CARRY_SKILL = ROOT / "skills/carry-out-the-plan/SKILL.md"
REVIEW_SPEC = ROOT / "docs/specs/2026-10-03-review-the-diff-design.md"
REVIEW_SKILL = ROOT / "skills/review-the-diff/SKILL.md"
TAKE_SPEC = ROOT / "docs/specs/2026-10-03-take-the-review-design.md"
TAKE_SKILL = ROOT / "skills/take-the-review/SKILL.md"
STRESS_SPEC = ROOT / "docs/specs/2026-10-03-stress-the-change-design.md"
STRESS_SKILL = ROOT / "skills/stress-the-change/SKILL.md"
SHIP_SPEC = ROOT / "docs/specs/2026-10-03-ship-the-branch-design.md"
SHIP_SKILL = ROOT / "skills/ship-the-branch/SKILL.md"
RUN_SPEC = ROOT / "docs/specs/2026-10-03-run-the-play-design.md"
RUN_SKILL = ROOT / "skills/run-the-play/SKILL.md"
ISOLATE_SPEC = ROOT / "docs/specs/2026-10-03-isolate-the-work-design.md"
ISOLATE_SKILL = ROOT / "skills/isolate-the-work/SKILL.md"
FAN_SPEC = ROOT / "docs/specs/2026-10-03-fan-out-design.md"
FAN_SKILL = ROOT / "skills/fan-out/SKILL.md"
SHAPES_SPEC = ROOT / "docs/specs/2026-10-03-try-several-shapes-design.md"
SHAPES_SKILL = ROOT / "skills/try-several-shapes/SKILL.md"
BLAST_SPEC = ROOT / "docs/specs/2026-10-03-measure-the-blast-design.md"
BLAST_SKILL = ROOT / "skills/measure-the-blast/SKILL.md"
PROVE_SPEC = ROOT / "docs/specs/2026-10-03-prove-the-product-design.md"
PROVE_SKILL = ROOT / "skills/prove-the-product/SKILL.md"
TRAIL_SPEC = ROOT / "docs/specs/2026-10-03-leave-a-trail-design.md"
TRAIL_SKILL = ROOT / "skills/leave-a-trail/SKILL.md"
PICKUP_SPEC = ROOT / "docs/specs/2026-10-03-pick-up-the-work-design.md"
PICKUP_SKILL = ROOT / "skills/pick-up-the-work/SKILL.md"
LEARN_SPEC = ROOT / "docs/specs/2026-10-03-learn-from-the-session-design.md"
LEARN_SKILL = ROOT / "skills/learn-from-the-session/SKILL.md"
AUTHOR_SPEC = ROOT / "docs/specs/2026-10-03-write-a-skill-design.md"
AUTHOR_SKILL = ROOT / "skills/write-a-skill/SKILL.md"
SLOP_SPEC = ROOT / "docs/specs/2026-10-03-cut-the-slop-design.md"
SLOP_SKILL = ROOT / "skills/cut-the-slop/SKILL.md"
DOC_SPEC = ROOT / "docs/specs/2026-10-03-write-the-doc-design.md"
DOC_SKILL = ROOT / "skills/write-the-doc/SKILL.md"
PLAYBOOK_DIR = ROOT / "skills/run-the-play/playbooks"
README = ROOT / "README.md"
GUIDE = ROOT / "docs/skills.md"
PLUGIN = ROOT / ".claude-plugin/plugin.json"
MARKET = ROOT / ".claude-plugin/marketplace.json"

HEADINGS = (
    "Voice",
    "Smallest change",
    "Prove the real artifact",
    "Fix the cause",
    "Re-running converges",
    "Data shape before logic",
    "Redesign instead of bolting on",
    "Remove dead weight first",
    "Build a rerunnable tool",
)

SCOPE_HEADINGS = (
    "Name the scope",
    "Small",
    "Intermediate",
    "Architectural",
    "Real code",
)

BOUNDS_HEADINGS = (
    "Resolve first",
    "Layers",
    "Defaults",
    "Values",
    "Publishing sets",
    "Unattended",
    "Revise a layer",
)

DEBUG_HEADINGS = (
    "Reproduce",
    "One hypothesis",
    "Evidence",
    "The producer",
    "The same failure",
)

FITS_HEADINGS = (
    "Read first",
    "Runtime path",
    "Owner",
    "Layer",
)

WHY_HEADINGS = (
    "The question",
    "Sources",
    "The read",
    "No reason on record",
)

PLAN_HEADINGS = (
    "The document",
    "Where it goes",
    "What the reviewer reads",
    "Tasks",
    "Stop there",
)

CARRY_HEADINGS = (
    "An approved plan",
    "In order",
    "Beside this session",
    "The check",
    "The same plan",
)

REVIEW_HEADINGS = (
    "The diff",
    "The request and the checks",
    "Findings",
    "Leave the tree",
)

TAKE_HEADINGS = (
    "The notes",
    "Against the code",
    "One note at a time",
    "A note that does not hold",
    "The same notes",
)

STRESS_HEADINGS = (
    "The diff",
    "Three passes",
    "One list",
    "Leave the tree",
)

SHIP_HEADINGS = (
    "The branch",
    "Three commits",
    "The remote",
    "The worktree",
    "The same branch",
)

RUN_HEADINGS = (
    "The match",
    "The list",
    "A step left out",
    "Where it stops",
    "The same task",
)

ISOLATE_HEADINGS = (
    "The work",
    "The key",
    "The checkout",
    "The path",
    "The same work",
)

FAN_HEADINGS = (
    "The pieces",
    "The workers",
    "One report",
    "The same split",
)

SHAPES_HEADINGS = (
    "The moment",
    "The candidates",
    "The base",
    "The fold",
    "The same attempt",
)

BLAST_HEADINGS = (
    "The diff",
    "The claim",
    "The run",
    "Leave the tree",
    "The same diff",
)

PROVE_HEADINGS = (
    "The drive",
    "The skill file",
    "Prove it once",
    "A later pass",
    "The same map",
)

TRAIL_HEADINGS = (
    "When it starts",
    "The row",
    "Where it lives",
    "The same run",
)

PICKUP_HEADINGS = (
    "The sources",
    "The brief",
    "Leave the tree",
    "The same point",
)

LEARN_HEADINGS = (
    "The lesson",
    "The home",
    "The edit",
    "The same lesson",
)

AUTHOR_HEADINGS = (
    "The trigger",
    "The spec",
    "The file",
    "The check",
    "The same skill",
)

SLOP_HEADINGS = (
    "The pass",
    "What comes out",
    "A constraint",
    "The same pass",
)

DOC_HEADINGS = (
    "The document",
    "The headings",
    "The sentences",
    "Where it stops",
    "The same document",
)

DESCRIPTION = (
    "Use before writing a reply, a diff, a commit message, or a document. "
    "Kobold Codex is the voice and the engineering principles for "
    "DragonCrafted87's agents on Grok and Claude Code."
)

SCOPE_DESCRIPTION = (
    "Use before changing a file or making a commit. "
    "Name the scope of the edit, then add only the plan and the proof "
    "that scope calls for."
)

BOUNDS_DESCRIPTION = (
    "Use before a commit, a push, a pull request, a merge, a force-push, "
    "an unattended stretch, or a named tool. Resolve the four bounds "
    "layers, and revise one layer when the user wants a change."
)

DEBUG_DESCRIPTION = (
    "Use when a failure can be reproduced. Hold one hypothesis at a time, "
    "check it on the running system, and put the fix at the producer of "
    "the symptom."
)

FITS_DESCRIPTION = (
    "Use before changing a subsystem. Name the runtime path, the package "
    "that owns the behavior, and the layer the change belongs on."
)

WHY_DESCRIPTION = (
    "Use when you need the reason for a behavior or a threshold. Recover "
    "it from the code, the history, the issues, and the docs, and cite "
    "each source."
)

PLAN_DESCRIPTION = (
    "Use when an architectural change needs a written plan, or the user "
    "asks for one. Write what will change, what it touches, what stays "
    "the same, what the checks cover, and the ordered tasks, then stop."
)

CARRY_DESCRIPTION = (
    "Use when a plan has been approved. Run its tasks in order in this "
    "session, send independent tasks to another agent only when subagents "
    "allows it, and finish each task on the check the plan named."
)

REVIEW_DESCRIPTION = (
    "Use before a merge, or when the user asks for a review. Review the "
    "diff against the request and the checks, report each finding with "
    "file and line, and leave the tree alone."
)

TAKE_DESCRIPTION = (
    "Use when review notes are in hand. Check each note against the code, "
    "implement the notes that hold, and for a note that does not hold say "
    "why and leave that code as it is."
)

STRESS_DESCRIPTION = (
    "Use when a diff needs several independent reviews. Run separate "
    "passes on different angles, merge the findings into one list, and "
    "leave the tree alone."
)

SHIP_DESCRIPTION = (
    "Use when the checks pass and the branch should be integrated. "
    "Commit the specs, the plans, and the work under their own keys, "
    "then push, open a pull request, or merge, and remove the worktree, "
    "each as the resolved bounds allow."
)

RUN_DESCRIPTION = (
    "Use when a task should follow a playbook. "
    "Match it to one playbook, copy that playbook's steps into the "
    "working list, record a skip with a reason, and stop where the "
    "resolved bounds say to stop."
)

ISOLATE_DESCRIPTION = (
    "Use when feature work, or the execution of a plan, should sit "
    "in its own checkout. Create that checkout when worktrees allows "
    "it, and record the path so ship-the-branch can remove it."
)

FAN_DESCRIPTION = (
    "Use when work that does not share state should run as parallel "
    "workers. Split it, wait for the workers, and return one report. "
    "subagents has to allow the parallel form."
)

SHAPES_DESCRIPTION = (
    "Use when the first shape of a change would stick. Run several "
    "candidates, pick a base, and fold the strongest pieces of the "
    "others into it."
)

BLAST_DESCRIPTION = (
    "Use before a small diff ships. Name what else could break "
    "outside the diff, and prove that claim by running the code that "
    "would show the break."
)

PROVE_DESCRIPTION = (
    "Use when a repo has no scripted way to drive the app the way a "
    "user does. Write a project-local verification skill, prove it "
    "once, and re-run it so the map stays honest."
)

TRAIL_DESCRIPTION = (
    "Use for a long run or an unattended run. Append one row per "
    "decision, with what, why, evidence, and result, to a log a "
    "reviewer can read afterward."
)

PICKUP_DESCRIPTION = (
    "Use when a new session should continue work already in "
    "progress. Rebuild a short brief from the branch, the "
    "transcript, and the trail."
)

LEARN_DESCRIPTION = (
    "Use after a session that stumbled, or that found a preference "
    "worth keeping. Name the lesson and edit the skill, playbook, "
    "or bounds file that should carry it."
)

AUTHOR_DESCRIPTION = (
    "Use when authoring or revising a skill in this plugin. Write "
    "one trigger description, original wording, and a check that "
    "the skill file matches its spec."
)

SLOP_DESCRIPTION = (
    "Use when prose or a diff needs a pass for narration, stock "
    "phrasing, and comments that restate the code. Encode a real "
    "constraint in the structure, then drop the comment."
)

DOC_DESCRIPTION = (
    "Use when writing or revising a README, a spec, a pull request, "
    "or a commit message. Use the headings the project already uses, "
    "in sentences a new reader can follow."
)

PLUGIN_DESCRIPTION = (
    "Principles and workflow skills for DragonCrafted87's agents on Grok "
    "and Claude Code."
)

INSTALL_LINES = (
    "grok plugin install DragonCrafted87/kobold-codex --trust",
    "grok plugin install . --trust",
    "/plugin marketplace add DragonCrafted87/kobold-codex",
    "/plugin install kobold-codex@kobold-codex",
)

GUIDE_LINKS = (
    "skills/kobold-codex/SKILL.md",
    "docs/specs/2026-10-01-kobold-codex-design.md",
    "skills/scope-the-edit/SKILL.md",
    "docs/specs/2026-10-01-scope-the-edit-design.md",
    "skills/set-the-bounds/SKILL.md",
    "docs/specs/2026-10-02-set-the-bounds-design.md",
    "skills/debug-the-failure/SKILL.md",
    "docs/specs/2026-10-02-debug-the-failure-design.md",
    "skills/how-it-fits/SKILL.md",
    "docs/specs/2026-10-02-how-it-fits-design.md",
    "skills/why-it-is/SKILL.md",
    "docs/specs/2026-10-02-why-it-is-design.md",
    "skills/write-the-plan/SKILL.md",
    "docs/specs/2026-10-02-write-the-plan-design.md",
    "skills/carry-out-the-plan/SKILL.md",
    "docs/specs/2026-10-02-carry-out-the-plan-design.md",
    "skills/review-the-diff/SKILL.md",
    "docs/specs/2026-10-03-review-the-diff-design.md",
    "skills/take-the-review/SKILL.md",
    "docs/specs/2026-10-03-take-the-review-design.md",
    "skills/stress-the-change/SKILL.md",
    "docs/specs/2026-10-03-stress-the-change-design.md",
    "skills/ship-the-branch/SKILL.md",
    "docs/specs/2026-10-03-ship-the-branch-design.md",
    "skills/run-the-play/SKILL.md",
    "docs/specs/2026-10-03-run-the-play-design.md",
    "skills/isolate-the-work/SKILL.md",
    "docs/specs/2026-10-03-isolate-the-work-design.md",
    "skills/fan-out/SKILL.md",
    "docs/specs/2026-10-03-fan-out-design.md",
    "skills/try-several-shapes/SKILL.md",
    "docs/specs/2026-10-03-try-several-shapes-design.md",
    "skills/measure-the-blast/SKILL.md",
    "docs/specs/2026-10-03-measure-the-blast-design.md",
    "skills/prove-the-product/SKILL.md",
    "docs/specs/2026-10-03-prove-the-product-design.md",
    "skills/leave-a-trail/SKILL.md",
    "docs/specs/2026-10-03-leave-a-trail-design.md",
    "skills/pick-up-the-work/SKILL.md",
    "docs/specs/2026-10-03-pick-up-the-work-design.md",
    "skills/learn-from-the-session/SKILL.md",
    "docs/specs/2026-10-03-learn-from-the-session-design.md",
    "skills/write-a-skill/SKILL.md",
    "docs/specs/2026-10-03-write-a-skill-design.md",
    "skills/cut-the-slop/SKILL.md",
    "docs/specs/2026-10-03-cut-the-slop-design.md",
    "skills/write-the-doc/SKILL.md",
    "docs/specs/2026-10-03-write-the-doc-design.md",
)

NEEDLES = (
    "rune" + "wyrm",
    "forge" + "wyrm",
    "hearth" + "wyrm",
    "/home/" + "dragon",
    "dot-" + "files",
)


def fail(message):
    print(message, file=sys.stderr)
    raise SystemExit(1)


def sections(text):
    found = {}
    current = None
    buf = []
    for line in text.splitlines():
        match = re.match(r"^#{1,6} (.+)$", line)
        if match:
            if current is not None:
                found[current] = "\n".join(buf).strip()
            current = match.group(1).strip()
            buf = []
        elif current is not None:
            buf.append(line.rstrip())
    if current is not None:
        found[current] = "\n".join(buf).strip()
    return found


def check_one(path, spec_path, expected_name, description, headings):
    if not path.is_file():
        fail(f"missing {path.relative_to(ROOT)}")
    raw = path.read_text()
    if not raw.startswith("---\n"):
        fail(f"{expected_name} is missing frontmatter")
    end = raw.find("\n---\n", 4)
    if end < 0:
        fail(f"{expected_name} frontmatter does not close")
    front = raw[4:end]
    body = raw[end + 5 :]
    name = re.search(r"^name:\s*(.+)$", front, re.M)
    desc = re.search(r"^description:\s*(.+)$", front, re.M)
    if name is None or name.group(1).strip() != expected_name:
        fail(f"frontmatter name must be {expected_name}")
    if desc is None or desc.group(1).strip() != description:
        fail(f"frontmatter description does not match for {expected_name}")
    skill_sections = sections(body)
    spec_sections = sections(spec_path.read_text())
    readme = README.read_text()
    for heading in headings:
        if heading not in skill_sections:
            fail(f"{expected_name} missing heading {heading}")
        if heading not in spec_sections:
            fail(f"spec missing heading {heading}")
        if skill_sections[heading] != spec_sections[heading]:
            fail(f"section {heading!r} does not match the spec")
        if skill_sections[heading] in readme:
            fail(f"README restates {heading}")


def playbook_title(name):
    words = name.replace("-", " ")
    return words[:1].upper() + words[1:]


def playbook_regions(spec_text):
    lines = spec_text.splitlines()
    found = []
    for index, line in enumerate(lines):
        match = re.match(
            r"^## Playbook: ([a-z][a-z0-9]*(?:-[a-z0-9]+)*)$",
            line,
        )
        if match:
            found.append((match.group(1), index))
    if not found:
        fail("run-the-play spec has no playbook")
    regions = []
    for name, start in found:
        body = []
        for line in lines[start + 1 :]:
            if line.startswith("## ") and not line.startswith("### "):
                break
            body.append(line)
        regions.append((name, body))
    return regions


def region_steps(name, body_lines):
    steps = []
    current = None
    buf = []
    lead = []
    for line in body_lines:
        match = re.match(r"^(#{1,6}) (.+)$", line)
        if match:
            if current is None and "\n".join(lead).strip():
                fail(f"playbook {name} region has text before its steps")
            if current is not None:
                steps.append((current, "\n".join(buf).strip()))
            level = len(match.group(1))
            title = match.group(2).strip()
            if level != 3:
                fail(
                    f"playbook {name} region heading {title!r} "
                    "must be level 3"
                )
            current = title
            buf = []
        elif current is not None:
            buf.append(line.rstrip())
        else:
            lead.append(line.rstrip())
    if current is not None:
        steps.append((current, "\n".join(buf).strip()))
    if not steps:
        fail(f"playbook {name} region has no steps")
    return steps


def heading_items(text):
    items = []
    current = None
    level = None
    buf = []
    for line in text.splitlines():
        match = re.match(r"^(#{1,6}) (.+)$", line)
        if match:
            if current is not None:
                items.append((level, current, "\n".join(buf).strip()))
            level = len(match.group(1))
            current = match.group(2).strip()
            buf = []
        elif current is not None:
            buf.append(line.rstrip())
    if current is not None:
        items.append((level, current, "\n".join(buf).strip()))
    return items


def check_playbook_file(name, steps, readme):
    path = PLAYBOOK_DIR / f"{name}.md"
    if not path.is_file():
        fail(f"missing {path.relative_to(ROOT)}")
    raw = path.read_text()
    if raw.startswith("---"):
        fail(f"{name} playbook starts with frontmatter")
    title = playbook_title(name)
    items = heading_items(raw)
    if not items or items[0][0] != 1 or items[0][1] != title:
        fail(f"{name} playbook title must be {title}")
    before = []
    for line in raw.splitlines():
        if line.startswith("## ") and not line.startswith("### "):
            break
        before.append(line.rstrip())
    kept = []
    removed = False
    for line in before:
        if not removed and line == f"# {title}":
            removed = True
            continue
        kept.append(line)
    if "\n".join(kept).strip():
        fail(f"{name} playbook has text before its steps")
    for level, heading, _body in items[1:]:
        if level != 2:
            fail(f"{name} playbook has an unexpected heading {heading}")
    found = [(heading, body) for level, heading, body in items if level == 2]
    expected = [heading for heading, _body in steps]
    actual = [heading for heading, _body in found]
    if actual != expected:
        fail(f"{name} playbook headings are {actual}, expected {expected}")
    for (heading, body), (_title, spec_body) in zip(found, steps):
        if not body:
            fail(f"{name} playbook section {heading!r} is empty")
        if body != spec_body:
            fail(f"playbook {name} section {heading!r} does not match the spec")
        if body in readme:
            fail(f"README restates {name} {heading}")


def check_playbooks(spec_path):
    regions = playbook_regions(spec_path.read_text())
    readme = README.read_text()
    names = []
    for name, body in regions:
        steps = region_steps(name, body)
        for heading, step_body in steps:
            if not step_body:
                fail(f"playbook {name} section {heading!r} is empty in the spec")
        check_playbook_file(name, steps, readme)
        names.append(name)
    if not PLAYBOOK_DIR.is_dir():
        fail(f"missing {PLAYBOOK_DIR.relative_to(ROOT)}")
    for path in sorted(PLAYBOOK_DIR.glob("*.md")):
        if path.stem not in names:
            fail(f"playbook file {path.name} is not in the spec")


def check_skills():
    check_one(SKILL, SPEC, "kobold-codex", DESCRIPTION, HEADINGS)
    check_one(
        SCOPE_SKILL,
        SCOPE_SPEC,
        "scope-the-edit",
        SCOPE_DESCRIPTION,
        SCOPE_HEADINGS,
    )
    check_one(
        BOUNDS_SKILL,
        BOUNDS_SPEC,
        "set-the-bounds",
        BOUNDS_DESCRIPTION,
        BOUNDS_HEADINGS,
    )
    check_one(
        DEBUG_SKILL,
        DEBUG_SPEC,
        "debug-the-failure",
        DEBUG_DESCRIPTION,
        DEBUG_HEADINGS,
    )
    check_one(
        FITS_SKILL,
        FITS_SPEC,
        "how-it-fits",
        FITS_DESCRIPTION,
        FITS_HEADINGS,
    )
    check_one(
        WHY_SKILL,
        WHY_SPEC,
        "why-it-is",
        WHY_DESCRIPTION,
        WHY_HEADINGS,
    )
    check_one(
        PLAN_SKILL,
        PLAN_SPEC,
        "write-the-plan",
        PLAN_DESCRIPTION,
        PLAN_HEADINGS,
    )
    check_one(
        CARRY_SKILL,
        CARRY_SPEC,
        "carry-out-the-plan",
        CARRY_DESCRIPTION,
        CARRY_HEADINGS,
    )
    check_one(
        REVIEW_SKILL,
        REVIEW_SPEC,
        "review-the-diff",
        REVIEW_DESCRIPTION,
        REVIEW_HEADINGS,
    )
    check_one(
        TAKE_SKILL,
        TAKE_SPEC,
        "take-the-review",
        TAKE_DESCRIPTION,
        TAKE_HEADINGS,
    )
    check_one(
        STRESS_SKILL,
        STRESS_SPEC,
        "stress-the-change",
        STRESS_DESCRIPTION,
        STRESS_HEADINGS,
    )
    check_one(
        SHIP_SKILL,
        SHIP_SPEC,
        "ship-the-branch",
        SHIP_DESCRIPTION,
        SHIP_HEADINGS,
    )
    check_one(
        RUN_SKILL,
        RUN_SPEC,
        "run-the-play",
        RUN_DESCRIPTION,
        RUN_HEADINGS,
    )
    check_one(
        ISOLATE_SKILL,
        ISOLATE_SPEC,
        "isolate-the-work",
        ISOLATE_DESCRIPTION,
        ISOLATE_HEADINGS,
    )
    check_one(
        FAN_SKILL,
        FAN_SPEC,
        "fan-out",
        FAN_DESCRIPTION,
        FAN_HEADINGS,
    )
    check_one(
        SHAPES_SKILL,
        SHAPES_SPEC,
        "try-several-shapes",
        SHAPES_DESCRIPTION,
        SHAPES_HEADINGS,
    )
    check_one(
        BLAST_SKILL,
        BLAST_SPEC,
        "measure-the-blast",
        BLAST_DESCRIPTION,
        BLAST_HEADINGS,
    )
    check_one(
        PROVE_SKILL,
        PROVE_SPEC,
        "prove-the-product",
        PROVE_DESCRIPTION,
        PROVE_HEADINGS,
    )
    check_one(
        TRAIL_SKILL,
        TRAIL_SPEC,
        "leave-a-trail",
        TRAIL_DESCRIPTION,
        TRAIL_HEADINGS,
    )
    check_one(
        PICKUP_SKILL,
        PICKUP_SPEC,
        "pick-up-the-work",
        PICKUP_DESCRIPTION,
        PICKUP_HEADINGS,
    )
    check_one(
        LEARN_SKILL,
        LEARN_SPEC,
        "learn-from-the-session",
        LEARN_DESCRIPTION,
        LEARN_HEADINGS,
    )
    check_one(
        AUTHOR_SKILL,
        AUTHOR_SPEC,
        "write-a-skill",
        AUTHOR_DESCRIPTION,
        AUTHOR_HEADINGS,
    )
    check_one(
        SLOP_SKILL,
        SLOP_SPEC,
        "cut-the-slop",
        SLOP_DESCRIPTION,
        SLOP_HEADINGS,
    )
    check_one(
        DOC_SKILL,
        DOC_SPEC,
        "write-the-doc",
        DOC_DESCRIPTION,
        DOC_HEADINGS,
    )
    check_playbooks(RUN_SPEC)


def check_manifests():
    plugin = json.loads(PLUGIN.read_text())
    market = json.loads(MARKET.read_text())
    if plugin["name"] != "kobold-codex":
        fail("plugin name")
    if plugin["version"] != "0.9.0":
        fail("plugin version")
    if plugin["description"] != PLUGIN_DESCRIPTION:
        fail("plugin description")
    if plugin["license"] != "MIT":
        fail("plugin license")
    if plugin["repository"] != "https://github.com/DragonCrafted87/kobold-codex":
        fail("plugin repository")
    if plugin["author"]["name"] != "Scott Gudeman":
        fail("plugin author")
    if market["name"] != "kobold-codex":
        fail("marketplace name")
    if market["description"] != PLUGIN_DESCRIPTION:
        fail("marketplace description")
    listed = market["plugins"]
    if len(listed) != 1:
        fail("marketplace must list one plugin")
    entry = listed[0]
    if entry["name"] != plugin["name"]:
        fail("marketplace plugin name disagrees with plugin.json")
    if entry["version"] != plugin["version"]:
        fail("marketplace version disagrees with plugin.json")
    if entry["description"] != plugin["description"]:
        fail("marketplace description disagrees with plugin.json")
    if entry["source"] != "./":
        fail("marketplace source must be ./")
    if entry["license"] != "MIT":
        fail("marketplace license")
    readme = README.read_text()
    for line in INSTALL_LINES:
        if line not in readme:
            fail(f"README missing install line: {line}")
    if "docs/skills.md" not in readme:
        fail("README missing link: docs/skills.md")
    if "docs/specs/" in readme:
        fail("README links a spec")
    if not GUIDE.is_file():
        fail("missing docs/skills.md")
    guide = GUIDE.read_text()
    for line in GUIDE_LINKS:
        if line not in guide:
            fail(f"docs/skills.md missing link: {line}")
    if (ROOT / "hooks").exists() or any(ROOT.rglob("hooks.json")):
        fail("hooks are out of scope")


def check_public_text():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue
        text = path.read_text(errors="replace")
        for needle in NEEDLES:
            if needle in text:
                fail(f"{path.relative_to(ROOT)} contains a machine or home path")


def main():
    check_skills()
    check_manifests()
    check_public_text()


if __name__ == "__main__":
    main()
