#!/usr/bin/env python3
"""Validate the plugin manifests and skill layout, and require a version bump off main."""

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / ".claude-plugin/plugin.json"
MARKET = ROOT / ".claude-plugin/marketplace.json"
DESCRIPTION = (
    "Principles and workflow skills for DragonCrafted87's agents on Grok "
    "and Claude Code."
)
REPOSITORY = "https://github.com/DragonCrafted87/kobold-codex"
BASE_BRANCHES = {"main", "master"}


def fail(message):
    print(message, file=sys.stderr)
    raise SystemExit(1)


def load_json(path):
    if not path.is_file():
        fail(f"missing {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text())
    except json.JSONDecodeError as error:
        fail(f"{path.relative_to(ROOT)} is not valid JSON: {error}")


def require(obj, key, label):
    if not isinstance(obj, dict) or key not in obj:
        fail(f"{label} missing {key}")
    return obj[key]


def parse_version(value, label):
    if not isinstance(value, str):
        fail(f"{label} version is not a string")
    parts = value.split(".")
    if len(parts) != 3 or any(not part.isdigit() for part in parts):
        fail(f"{label} version must be major.minor.patch, got {value}")
    return tuple(int(part) for part in parts)


def branch_name():
    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        fail(result.stderr.strip() or "cannot read the current branch")
    return result.stdout.strip()


def version_on_main():
    seen = None
    for ref in ("origin/main", "main"):
        result = subprocess.run(
            ["git", "show", f"{ref}:.claude-plugin/plugin.json"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            seen = result.stderr.strip()
            continue
        try:
            payload = json.loads(result.stdout)
        except json.JSONDecodeError as error:
            fail(f"{ref} plugin.json is not valid JSON: {error}")
        return parse_version(require(payload, "version", ref), ref)
    fail(seen or "cannot read plugin.json on main")


def check_manifests():
    plugin = load_json(PLUGIN)
    market = load_json(MARKET)
    name = require(plugin, "name", "plugin.json")
    version = parse_version(require(plugin, "version", "plugin.json"), "plugin.json")
    description = require(plugin, "description", "plugin.json")
    if name != "kobold-codex":
        fail("plugin name")
    if description != DESCRIPTION:
        fail("plugin description")
    if require(plugin, "license", "plugin.json") != "MIT":
        fail("plugin license")
    if require(plugin, "repository", "plugin.json") != REPOSITORY:
        fail("plugin repository")
    author = require(plugin, "author", "plugin.json")
    if require(author, "name", "plugin.json author") != "Scott Gudeman":
        fail("plugin author")

    if require(market, "name", "marketplace.json") != "kobold-codex":
        fail("marketplace name")
    if require(market, "description", "marketplace.json") != DESCRIPTION:
        fail("marketplace description")
    listed = require(market, "plugins", "marketplace.json")
    if not isinstance(listed, list) or len(listed) != 1:
        fail("marketplace must list one plugin")
    entry = listed[0]
    if require(entry, "name", "marketplace plugin") != name:
        fail("marketplace plugin name disagrees with plugin.json")
    entry_version = parse_version(
        require(entry, "version", "marketplace plugin"),
        "marketplace plugin",
    )
    if entry_version != version:
        fail("marketplace version disagrees with plugin.json")
    if require(entry, "description", "marketplace plugin") != description:
        fail("marketplace description disagrees with plugin.json")
    if require(entry, "source", "marketplace plugin") != "./":
        fail("marketplace source must be ./")
    if require(entry, "license", "marketplace plugin") != "MIT":
        fail("marketplace license")
    return version


def check_ahead(version):
    if branch_name() in BASE_BRANCHES:
        return
    base = version_on_main()
    if version <= base:
        current = ".".join(str(part) for part in version)
        main = ".".join(str(part) for part in base)
        fail(f"version {current} is not ahead of main {main}")


def skill_name(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        fail(f"{path.relative_to(ROOT)} has no frontmatter")
    for line in lines[1:]:
        if line == "---":
            break
        if line.startswith("name:"):
            return line[len("name:"):].strip()
    fail(f"{path.relative_to(ROOT)} has no name")


def check_layout():
    plugin = load_json(PLUGIN)
    skills_root = ROOT / "skills"
    listed = require(plugin, "skills", "plugin.json")
    if not isinstance(listed, list):
        fail("plugin.json skills must be a list")
    listed_groups = set()
    for entry in listed:
        if not isinstance(entry, str) or not entry.startswith("./skills/"):
            fail(f"plugin.json skills entry {entry!r} must start with ./skills/")
        group = entry[len("./skills/"):].strip("/")
        if not group or "/" in group:
            fail(f"plugin.json skills entry {entry!r} must name one group")
        if not (skills_root / group).is_dir():
            fail(f"plugin.json lists {entry} but it does not exist")
        listed_groups.add(group)
    seen = {}
    groups = set()
    for path in sorted(skills_root.rglob("SKILL.md")):
        parts = path.relative_to(skills_root).parts
        if len(parts) != 3:
            fail(f"{path.relative_to(ROOT)} must sit at skills/<group>/<name>/SKILL.md")
        group, folder, _ = parts
        name = skill_name(path)
        if name != folder:
            fail(f"{path.relative_to(ROOT)} name {name!r} does not match its folder")
        if name in seen:
            fail(f"skill {name} is in both {seen[name]} and {group}")
        seen[name] = group
        groups.add(group)
    for entry in sorted(p.name for p in skills_root.iterdir() if p.is_dir()):
        if entry not in groups:
            fail(f"skills/{entry} holds no skill")
        if entry not in listed_groups:
            fail(f"skills/{entry} is missing from the plugin.json skills key")
    for group in sorted(listed_groups - groups):
        fail(f"plugin.json lists skills/{group} but it holds no skill")


EXCLUDED_KEYWORDS = re.compile(r"\b(MUST|SHOULD|MAY|REQUIRED)\b")
KEYWORD_SKILL = ROOT / "skills/investigate/spec-the-source/SKILL.md"
KEYWORD_LIST_MARKER = "This line lists them so"


def check_requirement_language():
    """spec-the-source uses only its RFC 2119 subset, outside the line that lists the rest."""
    lines = KEYWORD_SKILL.read_text().splitlines()
    for number, line in enumerate(lines, 1):
        previous = lines[number - 2] if number > 1 else ""
        if KEYWORD_LIST_MARKER in previous or KEYWORD_LIST_MARKER in line:
            continue
        if line.lstrip().startswith("rg -nw"):
            continue
        if EXCLUDED_KEYWORDS.search(line):
            fail(f"{KEYWORD_SKILL.relative_to(ROOT)}:{number} uses an excluded RFC 2119 keyword")


PROJECT_NAMES = re.compile(r"forgeledger|stealthdragonland|\bFL-\d", re.IGNORECASE)
TOKEN_PRINT = re.compile(r"\b(echo|printf|print|cat)\b[^\n]*\$\{?\w*TOKEN", re.IGNORECASE)
ADOPT_SKILL = ROOT / "skills/setup/adopt-the-repo/SKILL.md"
CODEX_SKILL = ROOT / "skills/ground/kobold-codex/SKILL.md"
REQUIREMENTS_KEYS = ["source", "path", "tracked", "url", "project", "transport", "mcp-url", "openapi"]


def skill_files():
    return sorted((ROOT / "skills").glob("*/*/SKILL.md"))


def check_no_project_names():
    """Skills stay generic: no project, host, or tracker item names."""
    for path in skill_files():
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if PROJECT_NAMES.search(line):
                fail(f"{path.relative_to(ROOT)}:{number} names a project or host")


def check_requirements_keys():
    """adopt-the-repo records the requirements key and every key under it, and no export path."""
    text = ADOPT_SKILL.read_text()
    if "`requirements`" not in text:
        fail("adopt-the-repo does not name the requirements key")
    for key in REQUIREMENTS_KEYS:
        if f"`{key}`" not in text:
            fail(f"adopt-the-repo does not name the requirements key {key}")
    for removed in ("export-path", "token-env"):
        if removed in text:
            fail(f"adopt-the-repo names {removed}, which was removed")
    if "_TRACKER_TOKEN" not in CODEX_SKILL.read_text():
        fail("kobold-codex does not state the vault-name token rule")


def check_token_hygiene():
    """No skill tells a session to print a token."""
    for path in skill_files():
        for number, line in enumerate(path.read_text().splitlines(), 1):
            if TOKEN_PRINT.search(line):
                fail(f"{path.relative_to(ROOT)}:{number} prints a token")


def check_single_lookup():
    """The tracker lookup order lives once, in kobold-codex."""
    for path in skill_files():
        if path != CODEX_SKILL and "operationId" in path.read_text():
            fail(f"{path.relative_to(ROOT)} repeats the tracker lookup; link kobold-codex instead")


def check_requirements_language():
    """The Requirements heading in kobold-codex uses the RFC 2119 subset too."""
    text = CODEX_SKILL.read_text()
    section = text.split("## Requirements", 1)[-1].split("\n## ", 1)[0]
    if EXCLUDED_KEYWORDS.search(section):
        fail("kobold-codex Requirements uses an excluded RFC 2119 keyword")


def main():
    version = check_manifests()
    check_layout()
    check_requirement_language()
    check_no_project_names()
    check_requirements_keys()
    check_token_hygiene()
    check_single_lookup()
    check_requirements_language()
    check_ahead(version)


if __name__ == "__main__":
    main()
