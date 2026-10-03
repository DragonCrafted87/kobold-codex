#!/usr/bin/env python3
"""Validate the plugin manifests, and require a version bump off main."""

import json
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


def main():
    version = check_manifests()
    check_ahead(version)


if __name__ == "__main__":
    main()
