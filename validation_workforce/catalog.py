"""Deterministic catalog generation and cross-reference validation."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {"id", "name", "description", "division", "skills", "capabilities", "reads", "writes", "approval", "bias", "aliases"}


def _scalar(value: str):
    value = value.strip().strip("'\"")
    return value


def frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"missing frontmatter: {path}")
    lines = text.split("---\n", 2)[1].splitlines()
    result: dict = {}
    key = None
    for line in lines:
        if line.startswith("  - ") and key:
            result.setdefault(key, []).append(_scalar(line[4:]))
        elif line.startswith("  ") and ":" in line and key:
            subkey, value = line.strip().split(":", 1)
            if not isinstance(result.get(key), dict):
                result[key] = {}
            result[key][subkey] = _scalar(value)
        elif ":" in line:
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip()
            result[key] = [] if not value else ([] if value == "[]" else _scalar(value))
    return result


def build(root: Path = ROOT) -> dict[str, object]:
    divisions = set(json.loads((root / "divisions.json").read_text())["divisions"])
    agents = []
    for path in sorted((root / "agents").glob("*/*.md")):
        if path.name == "README.md":
            continue
        item = frontmatter(path)
        item["source"] = str(path.relative_to(root))
        agents.append(item)
    skills = []
    for path in sorted((root / "skills").glob("*/SKILL.md")):
        item = frontmatter(path); item["id"] = item.get("id", item.get("name", path.parent.name)); item["source"] = str(path.relative_to(root)); skills.append(item)
    workflows = [json.loads(p.read_text()) for p in sorted((root / "workflows").glob("*.json"))]
    capabilities = json.loads((root / "gateways/capabilities/registry.json").read_text())["capabilities"]
    aliases = {}
    for item in agents:
        aliases[f'{item["division"]}/{item["id"]}'] = item["source"]
    for path in sorted((root / "legacy-agents").rglob("*.md")):
        if path.name != "README.md":
            aliases[str(path.relative_to(root / "legacy-agents").with_suffix(""))] = str(path.relative_to(root))
    return {"agents": agents, "skills": skills, "workflows": workflows, "capabilities": capabilities, "legacy-aliases": aliases, "divisions": divisions}


def _unique(items, label):
    ids = [x["id"] for x in items]
    if len(ids) != len(set(ids)): raise ValueError(f"duplicate {label} IDs")
    return set(ids)


def validate(data: dict) -> dict[str, int]:
    agents, skills, workflows, capabilities = data["agents"], data["skills"], data["workflows"], data["capabilities"]
    agent_ids = _unique(agents, "agent"); skill_ids = _unique(skills, "skill"); workflow_ids = _unique(workflows, "workflow"); capability_ids = _unique(capabilities, "capability")
    for a in agents:
        missing = REQUIRED - a.keys()
        if missing: raise ValueError(f'{a.get("id")}: missing metadata {sorted(missing)}')
        if a["division"] not in data["divisions"]: raise ValueError(f'{a["id"]}: unknown division')
        if set(a["skills"]) - skill_ids: raise ValueError(f'{a["id"]}: missing skills {set(a["skills"])-skill_ids}')
        if set(a["capabilities"]) - capability_ids: raise ValueError(f'{a["id"]}: missing capabilities')
        if "qualification" in a["writes"]: raise ValueError("Agency may not author qualification")
    for w in workflows:
        seen = set()
        for step in w["steps"]:
            if step["id"] in seen: raise ValueError(f'{w["id"]}: duplicate step')
            if step["agent_id"] not in agent_ids: raise ValueError(f'{w["id"]}: missing agent')
            if set(step["skill_ids"]) - skill_ids: raise ValueError(f'{w["id"]}: missing skill')
            if set(step.get("capabilities", [])) - capability_ids: raise ValueError(f'{w["id"]}: missing capability')
            if set(step["depends_on"]) - seen: raise ValueError(f'{w["id"]}: malformed dependency or cycle')
            seen.add(step["id"])
    for alias, target in data["legacy-aliases"].items():
        if not (ROOT / target).is_file(): raise ValueError(f"broken alias {alias}: {target}")
    return {"agents":len(agents),"skills":len(skills),"workflows":len(workflows),"capabilities":len(capabilities),"legacy-aliases":len(data["legacy-aliases"])}


def generate(root: Path = ROOT) -> dict[str, int]:
    data = build(root); counts = validate(data); out = root / "catalog"; out.mkdir(exist_ok=True)
    for name in ("agents", "skills", "workflows", "capabilities", "legacy-aliases"):
        (out/f"{name}.json").write_text(json.dumps(data[name], indent=2, sort_keys=True)+"\n")
    return counts


def plan(workflow_id: str, inputs: dict, root: Path = ROOT):
    data=build(root); validate(data)
    workflow=next((w for w in data["workflows"] if w["id"]==workflow_id),None)
    if not workflow: raise ValueError(f"unknown workflow: {workflow_id}")
    for key,spec in workflow["inputs"].items():
        if spec.get("required") and key not in inputs: raise ValueError(f"missing input: {key}")
    return {"workflow_id":workflow_id,"inputs":inputs,"steps":workflow["steps"]}
