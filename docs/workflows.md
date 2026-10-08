# Declarative workflows

The 13 JSON definitions in `workflows/` provide IDs, versions, objectives, typed inputs, ordered dependency edges, agents, skills, capabilities, and expected outputs. Use `scripts/workforce.py workflow list|inspect|validate|plan`. Validation rejects cycles represented by forward/unknown dependencies and missing catalog references.
