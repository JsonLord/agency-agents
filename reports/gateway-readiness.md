# Gateway readiness

Statuses below require executable proof; documentation alone is never a pass.

| Gate | Status | Command and observed proof | Implementation | External dependency |
|---|---|---|---|---|
| G1 Agent catalog | PASS_LOCAL | `PYTHONPATH=. ./scripts/workforce.py catalog-validate` → `CATALOG PASS {"agents": 44, "capabilities": 5, "legacy-aliases": 326, "skills": 20, "workflows": 13}` | `validation_workforce/catalog.py`, `catalog/*.json` | None |
| G2 Skill/capability resolution | PASS_LOCAL | `python3 -m unittest tests.test_validation_workforce.Tests.test_catalogs_and_aliases tests.test_validation_workforce.Tests.test_capability_free_priority_scope -v` → 2 tests OK | catalogs and capability router | Live provider credentials |
| G3 Workflow gateway | PASS_LOCAL | `PYTHONPATH=. ./scripts/workforce.py workflow validate` → `WORKFLOW PASS 13 definitions`; planner returns six ordered steps | workflow JSON and planner | None |
| G4 Nodepad | PASS_MOCK / READY_CONFIG live | `python3 -m unittest tests.test_validation_workforce.Tests.test_nodepad_round_trip -v` → OK | `gateways/nodepad/` | Live URL, workspace, access/auth policy |
| G5 Capabilities | PASS_MOCK | capability routing unit test → OK | `gateways/capabilities/` | Provider credentials and health |
| G6 Hermes | PASS_LOCAL | `python3 scripts/check-hermes-plugin.py` → `PASSED: generated Hermes plugin schemas and routing behavior are valid.` | Hermes builder/check/tests | Hermes runtime installation |
| G7 Runtime exports | PASS_LOCAL | 15-target `scripts/convert.sh` loop → 15 successful targets, 44 active agents each | converter | Destination runtimes |
| G8 Delegation | PASS_LOCAL | delegation unit test → OK | `gateways/delegation/runtime.py` | Runtime adapter for live execution |
| G9 Telemetry | PASS_MOCK | telemetry fixture unit test → OK | `gateways/telemetry/` | Production sink |
| G10 End-to-end fixture | PASS_MOCK | `PYTHONPATH=. ./scripts/run-e2e-fixture.py` → support and contradiction retained, all outputs produced, qualification=0 | fixture, mock, e2e module | Live Nodepad/provider execution |
