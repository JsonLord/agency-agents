# Nodepad integration

Configure `NODEPAD_BASE_URL`, `NODEPAD_API_KEY`, and `NODEPAD_WORKSPACE_ID`. `gateways.nodepad.client.NodepadClient` maps context, hypotheses, evidence, research tasks/experiments, and heartbeat events to workspace endpoints. `MockNodepad` implements the same logical operations for deterministic local tests. Agency can propose evidence and hypotheses but cannot author authoritative qualification.

## Research boundary

External provider output is research material, not evidence. A specialist interprets it, creates a provenance-bearing evidence candidate and submits it through this gateway. Nodepad alone scores evidence, calculates confidence/qualification, mutates its graph, and promotes or demotes hypotheses. The mock is deterministic test infrastructure, not a production fallback. Stateful production writes fail visibly when Nodepad is unavailable.
