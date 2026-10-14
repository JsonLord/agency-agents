# Validation workforce architecture

Agency Agents is the stateless **workforce**: personas apply reusable skills, request semantic capabilities, and return structured artifacts. Nodepad is the **brain/state/truth**: it owns workspace context, hypotheses, evidence, experiments, gaps, audit history, and authoritative qualification.

The canonical active surface is `agents/<division>/`. Preserved upstream personas in `legacy-agents/` are resolvable expertise but are not active divisions. Generated catalogs connect personas, skills, workflows, capabilities, and aliases. Gateways isolate Nodepad, capability routing, delegation, workflow planning, and telemetry from runtime adapters.

## Donor integration boundary

**Agency Agents contains validation methodology and specialist execution. Nodepad remains an independent canonical state/truth service. Donor repository functionality has been adapted into Agency skills, workflows, evaluation helpers and capability providers—not into Nodepad.** Agency has no Nodepad source import, persistent graph, hypothesis database, heartbeat, Gardener, synthesis registry, backup system, or qualification algorithm.

## Hardened production boundary

Production HTTP writes are guarded at the Nodepad gateway itself, not only by orchestration or test harnesses. Agency-generated evidence analysis is a seven-dimension, explicitly non-authoritative vector; Nodepad alone owns canonical confidence and qualification.
