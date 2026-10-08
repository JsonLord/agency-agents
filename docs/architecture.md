# Validation workforce architecture

Agency Agents is the stateless **workforce**: personas apply reusable skills, request semantic capabilities, and return structured artifacts. Nodepad is the **brain/state/truth**: it owns workspace context, hypotheses, evidence, experiments, gaps, audit history, and authoritative qualification.

The canonical active surface is `agents/<division>/`. Preserved upstream personas in `legacy-agents/` are resolvable expertise but are not active divisions. Generated catalogs connect personas, skills, workflows, capabilities, and aliases. Gateways isolate Nodepad, capability routing, delegation, workflow planning, and telemetry from runtime adapters.
