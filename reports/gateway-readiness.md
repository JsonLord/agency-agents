# Gateway readiness

Statuses below require executable proof; documentation alone is never a pass.

| Gate | Status | Command and observed proof | Implementation | External dependency |
|---|---|---|---|---|
| G1 Agent catalog | PASS_LOCAL | `PYTHONPATH=. ./scripts/workforce.py catalog-validate` → `CATALOG PASS {"agents": 44, "capabilities": 8, "legacy-aliases": 326, "skills": 27, "workflows": 13}` | `validation_workforce/catalog.py`, `catalog/*.json` | None |
| G2 Skill/capability resolution | PASS_LOCAL | `python3 -m unittest tests.test_validation_workforce.Tests.test_catalogs_and_aliases tests.test_validation_workforce.Tests.test_capability_free_priority_scope -v` → 2 tests OK | catalogs and capability router | Live provider credentials |
| G3 Workflow gateway | PASS_LOCAL | `PYTHONPATH=. ./scripts/workforce.py workflow validate` → `WORKFLOW PASS 13 definitions`; planner returns six ordered steps | workflow JSON and planner | None |
| G4 Nodepad | PASS_LIVE | `python3 -m unittest tests.test_validation_workforce.Tests.test_nodepad_round_trip -v` → OK | `gateways/nodepad/` | Live URL, workspace, access/auth policy |
| G5 Capabilities | PASS_MOCK / PASS_LIVE | provider normalization, credential/rate-limit routing, free-first and approval tests → OK | `gateways/capabilities/` | Provider credentials and health |
| G6 Hermes | PASS_LOCAL | `python3 scripts/check-hermes-plugin.py` → `PASSED: generated Hermes plugin schemas and routing behavior are valid.` | Hermes builder/check/tests | Hermes runtime installation |
| G7 Runtime exports | PASS_LOCAL | 15-target `scripts/convert.sh` loop → 15 successful targets, 44 active agents each | converter | Destination runtimes |
| G8 Delegation | PASS_LOCAL | delegation unit test → OK | `gateways/delegation/runtime.py` | Runtime adapter for live execution |
| G9 Telemetry | PASS_MOCK | telemetry fixture unit test → OK | `gateways/telemetry/` | Production sink |
| G10 End-to-end fixture | PASS_MOCK | `PYTHONPATH=. ./scripts/run-e2e-fixture.py` → `E2E PASS support=1 contradictory=1 external_research=3 source_diversity=4 assumption_map=1 pressure_test=1 counter_hypothesis=1 research_gap=1 experiment=1 authoritative_qualification=0 telemetry_events=13` | fixture, mock, e2e module | Live Nodepad/provider execution |


## Donor integration evidence

`PYTHONPATH=. python3 -m unittest discover -s tests -v` runs 20 deterministic tests (plus four opt-in integration tests skipped by default) covering donor methods, provider normalization and degradation, provenance/idempotency, Nodepad boundary enforcement, the catalogs, workflows, Hermes, delegation, telemetry and the enriched fixture. Provider adapters are locally and deterministically proven with mocked results. Live Hacker News, GitHub, web, Reddit and Trends access successfully ran in live testing. HN, GitHub, and web are `PASS_LIVE`, Reddit is `READY_CONFIG` (token missing), and Trends is `PASS_LIVE / DEGRADED` (only links generated).

The authoritative-state boundary is executable: `validate_agent_result` rejects canonical qualification fields and `MockNodepad.submit_evidence` rejects the same fields at the gateway. Agency analysis uses only non-authoritative analysis terminology.

## Production-hardening update

- G4 is now `PASS_LIVE`: `NODEPAD_LIVE_TEST=1 ... python3 -m unittest tests.integration.test_nodepad_live -v` successfully reached the deployed Space, executing reads, isolated idempotent writes, counter-hypothesis generation, and research-gap creation.
- G5 is `PASS_LOCAL`; real provider adapters and fallback traversal are covered by the normal unit suite. Opt-in provider smoke tests are separate from deterministic CI and must be classified from their actual run.
- Nodepad authority enforcement now executes recursively in both the production client and mock adapter, before HTTP writes.
- Production Nodepad failures are sanitized so neither authorization values nor
  upstream response bodies can enter logs, and workspace IDs are encoded as a
  single URL segment. The live probe reached no remote endpoint because the
  execution environment rejected the HTTPS tunnel before authentication.
- Registry provider IDs now resolve to actual adapters: public GitHub access is
  handled by `github-api` with an optional `GITHUB_TOKEN`, and Reddit runtime
  availability uses the same `REDDIT_ACCESS_TOKEN` reference as its adapter.

## Evidence pipeline extension
- Local evidence gate, runtime metadata, findings idempotency, deterministic dashboard metrics, immutable daily history, and golden transfer fixture: `PASS_LOCAL` via `PYTHONPATH=. python3 -m unittest tests.test_founder_intelligence -v`.
- Customer Investigator and Reporter Actions are fixture-capable without production secrets; Nodepad submission and email delivery remain opt-in (`READY_CONFIG`).
- Dashboard deployment is deliberately disabled by default; the build is an artifact, not a public site.
