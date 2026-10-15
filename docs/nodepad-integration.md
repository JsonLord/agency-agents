# Nodepad integration

Configure `NODEPAD_BASE_URL`, `NODEPAD_API_KEY`, and `NODEPAD_WORKSPACE_ID`. `gateways.nodepad.client.NodepadClient` maps context, hypotheses, evidence, research tasks/experiments, and heartbeat events to workspace endpoints. `MockNodepad` implements the same logical operations for deterministic local tests. Agency can propose evidence and hypotheses but cannot author authoritative qualification.

## Research boundary

External provider output is research material, not evidence. A specialist interprets it, creates a provenance-bearing evidence candidate and submits it through this gateway. Nodepad alone scores evidence, calculates confidence/qualification, mutates its graph, and promotes or demotes hypotheses. The mock is deterministic test infrastructure, not a production fallback. Stateful production writes fail visibly when Nodepad is unavailable.

## Production boundary and live verification

`NodepadClient` recursively rejects `qualification`, `qualification_band`, `canonical_score`, and `authoritative_confidence` before any HTTP transport is invoked, including nested artifacts. Writes pass `Idempotency-Key` when an Agency payload contains a deterministic `idempotency_key`. Nodepad remains responsible for enforcing and interpreting idempotency server-side.

The deployed Space can be configured with `NODEPAD_BASE_URL=https://leon4gr45-nodepad-hypotheses.hf.space`. Opt-in tests require `NODEPAD_LIVE_TEST=1`, `NODEPAD_API_KEY`, and an isolated `NODEPAD_WORKSPACE_ID`; writes additionally require `NODEPAD_LIVE_WRITE=1`. The key must never be logged or committed.

Customer evidence candidates reach Nodepad only after the strict local evidence gate and only through the existing API client boundary. GitHub `findings.json` may link accepted Nodepad evidence IDs but cannot promote findings, set qualification/confidence/scores, or become a fallback canonical store.
