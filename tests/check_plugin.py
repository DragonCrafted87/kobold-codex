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
    "Principles and workflow skills for coding agents on Grok, Claude Code, "
    "Codex, Gemini CLI, Cursor, and any host that reads Agent Skills."
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


SKILLS_MAP = ROOT / "docs/skills.md"
ROOT_PLUGIN = ROOT / "plugin.json"
GEMINI = ROOT / "gemini-extension.json"
AGENT_PLUGINS_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
AGENT_PLUGINS_KEYS = {"$schema", "name", "version", "description", "author", "homepage", "repository", "license", "keywords", "extensions"}


def skill_group(path):
    """The group is frontmatter metadata: a `metadata:` block holding `group:`."""
    lines = path.read_text(encoding="utf-8").splitlines()
    in_meta = False
    for line in lines[1:]:
        if line == "---":
            break
        if line == "metadata:":
            in_meta = True
            continue
        if in_meta and line.startswith("  group:"):
            return line[len("  group:"):].strip()
        if not line.startswith(" "):
            in_meta = False
    fail(f"{path.relative_to(ROOT)} has no metadata group")


def map_groups():
    """docs/skills.md lists the groups as headings, in the order work moves, and links each skill under its group."""
    groups = {}
    current = None
    for line in SKILLS_MAP.read_text(encoding="utf-8").splitlines():
        if line.startswith("### "):
            current = line[4:].strip().lower()
            groups[current] = set()
        elif line.startswith("## "):
            current = None
        elif current:
            groups[current].update(re.findall(r"\(\.\./skills/([a-z0-9-]+)/SKILL\.md\)", line))
    return groups


def check_layout():
    plugin = load_json(PLUGIN)
    skills_root = ROOT / "skills"
    if require(plugin, "skills", "plugin.json") != ["./skills/"]:
        fail('plugin.json skills must be ["./skills/"]: skills sit flat, one folder each')
    groups = map_groups()
    if not groups:
        fail("docs/skills.md lists no group headings")
    for path in sorted(skills_root.rglob("SKILL.md")):
        parts = path.relative_to(skills_root).parts
        if len(parts) != 2:
            fail(f"{path.relative_to(ROOT)} must sit at skills/<name>/SKILL.md")
        folder = parts[0]
        name = skill_name(path)
        if name != folder:
            fail(f"{path.relative_to(ROOT)} name {name!r} does not match its folder")
        group = skill_group(path)
        if group not in groups:
            fail(f"{path.relative_to(ROOT)} group {group!r} is not a heading in docs/skills.md")
        if name not in groups[group]:
            fail(f"docs/skills.md does not link {name} under its group {group}")
    for entry in sorted(p.name for p in skills_root.iterdir() if p.is_dir()):
        if not (skills_root / entry / "SKILL.md").is_file():
            fail(f"skills/{entry} holds no SKILL.md")


def check_other_manifests(version):
    """The Agent Plugins manifest and the Gemini CLI extension manifest agree with plugin.json."""
    plugin = load_json(PLUGIN)
    root = load_json(ROOT_PLUGIN)
    if require(root, "$schema", "plugin.json (root)") != AGENT_PLUGINS_SCHEMA:
        fail("root plugin.json $schema must be the Agent Plugins 1.0.0 schema")
    extra = set(root) - AGENT_PLUGINS_KEYS
    if extra:
        fail(f"root plugin.json has keys outside Agent Plugins 1.0.0: {sorted(extra)}")
    gemini = load_json(GEMINI)
    for label, data in (("plugin.json (root)", root), ("gemini-extension.json", gemini)):
        if require(data, "name", label) != plugin["name"]:
            fail(f"{label} name disagrees with .claude-plugin/plugin.json")
        if parse_version(require(data, "version", label), label) != version:
            fail(f"{label} version disagrees with .claude-plugin/plugin.json")
        if require(data, "description", label) != DESCRIPTION:
            fail(f"{label} description")


EXCLUDED_KEYWORDS = re.compile(r"\b(MUST|SHOULD|MAY|REQUIRED)\b")
KEYWORD_SKILL = ROOT / "skills/spec-the-source/SKILL.md"
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
ADOPT_SKILL = ROOT / "skills/adopt-the-repo/SKILL.md"
CODEX_SKILL = ROOT / "skills/kobold-codex/SKILL.md"
REQUIREMENTS_KEYS = ["source", "path", "tracked", "url", "project", "transport", "mcp-url", "openapi", "token-env"]


def skill_files():
    return sorted((ROOT / "skills").glob("*/SKILL.md"))


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
    if "export-path" in text:
        fail("adopt-the-repo names export-path, which was removed")
    for path in skill_files():
        if "_TRACKER_TOKEN" in path.read_text():
            fail(f"{path.relative_to(ROOT)} derives a token variable; use token-env")


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
    check_other_manifests(version)
    check_requirement_language()
    check_no_project_names()
    check_requirements_keys()
    check_token_hygiene()
    check_single_lookup()
    check_requirements_language()
    check_ahead(version)


if __name__ == "__main__":
    main()
