# Agency Agents → Venture Validation Workforce
## Transformation Specification v0.1

**Target repository:** https://github.com/msitarzewski/agency-agents  
**Recommended working fork:** user-owned fork of the repository  
**Primary objective:** reshape Agency Agents from a conventional company-department roster into a validation-first specialist workforce that operates against Nodepad as the durable evidence/hypothesis/brain substrate.  
**Status:** implementation specification  
**Principle:** **Agency Agents owns specialist behavior; Nodepad owns truth and state.**

---

# 1. Vision

Agency Agents should no longer primarily simulate a company organized into departments such as Marketing, Sales, Finance, Product, Engineering, and Project Management.

It should become a **venture-validation workforce** composed of:

- specialist personas,
- reusable skills,
- explicit workflows,
- strict handoff contracts,
- capability requests,
- control/delegation gateways,
- runtime adapters.

The system should be able to receive a validation objective such as:

> “Find whether small design teams experience this pain, formulate competing hypotheses, test willingness to pay, create the cheapest behavioral experiment, and return structured evidence to Nodepad.”

Agency Agents should then select the right specialists and skills, perform work, and submit structured results.

The canonical loop is:

```text
Nodepad hypothesis/evidence state
          ↓
Agency specialist selection
          ↓
skill execution
          ↓
external research / artifact / experiment
          ↓
structured result
          ↓
Nodepad
          ↓
qualification / disqualification / new research gaps
          ↺
```

Agency Agents MUST NOT become a second hypothesis database or duplicate Nodepad’s evidence scoring.

---

# 2. Architectural Boundary

## 2.1 Agency Agents owns

- personas / specialist identities,
- specialist reasoning approaches,
- reusable validation skills,
- reusable workflow definitions,
- delegation metadata,
- capability requirements,
- tool/runtime conversion,
- human-approval requirements for write actions,
- handoff/result schemas,
- specialist routing hints,
- quality bars,
- adversarial review roles.

## 2.2 Nodepad owns

Repository:

https://github.com/JsonLord/nodepad

Nodepad is assumed to evolve according to the separately defined evidence/hypothesis/brain specification.

Nodepad owns:

- evidence records,
- source provenance,
- hypotheses,
- assumptions,
- counter-hypotheses,
- qualification scores,
- confidence,
- contradiction tracking,
- experiment state/results,
- decision history,
- brain knowledge,
- graph relationships,
- continuous heartbeat/research state,
- GitHub-backed workspace recovery.

Agency Agents reads and writes through a Nodepad gateway. It does not reproduce Nodepad’s scoring engine.

## 2.3 External capability layer owns

Examples:

- Reddit research,
- Reddit posting,
- LinkedIn research,
- web search,
- crawling,
- browser automation,
- image generation,
- deployment,
- analytics,
- outbound email.

Agents request semantic capabilities, e.g.:

```yaml
capabilities:
  required:
    - research.web
    - research.reddit
  optional:
    - browser
    - image.generate
```

Agents should not hardcode one vendor unless the capability itself is vendor-specific.

## 2.4 Workflow/orchestration layer

Agency Agents should be usable from:

- Hermes,
- Codex,
- Claude Code,
- OpenCode,
- other supported Agency runtimes,
- later Spynel,
- later Paperclip/n8n,
- direct programmatic/API adapters.

Agency Agents remains a specialist/workforce package rather than becoming the global orchestrator.

---

# 3. Existing Agency Infrastructure to Preserve

Preserve and adapt rather than discard:

- `tools.json` runtime catalog,
- converter infrastructure,
- install scripts,
- lint infrastructure,
- division/catalog validation,
- agent frontmatter compatibility,
- Claude Code support,
- Codex support,
- Gemini CLI support,
- GitHub Copilot support,
- Qwen Code support,
- Cursor support,
- OpenCode support,
- Osaurus support,
- Aider support,
- Antigravity support,
- Kimi support,
- OpenClaw support,
- Windsurf support,
- Hermes support,
- Mistral Vibe support,
- ZCode support,
- DeepSeek Harness support,
- current Hermes lazy router pattern,
- CI guardrails.

The existing runtime ecosystem is an asset. Do not replace it with a new agent framework.

---

# 4. Donor Repositories and Exact Instructions

## 4.1 Foundation — keep and reshape

### Agency Agents

Repository:

https://github.com/msitarzewski/agency-agents

**Action:** KEEP AS FOUNDATION.

Preserve:

- runtime adapters,
- `tools.json`,
- conversion/install system,
- Hermes plugin,
- CI/linting,
- frontmatter conventions where compatible.

Change:

- division taxonomy,
- canonical source layout,
- persona length/responsibilities,
- skill architecture,
- workflows,
- contracts,
- Nodepad gateway,
- capability gateway,
- routing metadata.

---

## 4.2 Actual donor merge/extraction

### Founder Skills

Repository:

https://github.com/SanketSapkal/founder-skills

**Action:** SELECTIVE MERGE / EXTRACT.

Do not preserve Founder Skills as an independent state machine.

Extract/adapt these methods as reusable Agency skills where useful:

- assumption-map,
- pressure-test,
- customer-archetype,
- market-size,
- founder-fit,
- unit-economics,
- regulatory-risk,
- battle-cards,
- pretotype,
- verdict,
- pivot-paths,
- 10x-why-now,
- analogous-cos,
- cold-outreach,
- content-strategy,
- GTM planning concepts,
- objection mapping where present.

Important rewrite:

Founder Skills currently writes its own output artifacts. In Agency Agents, imported skills MUST instead use the common input/result contract and treat Nodepad as state.

Keep methodology. Replace storage semantics.

---

# 5. Repositories to Mine, Not Merge Wholesale

## 5.1 Startup Skill

Repository:

https://github.com/ferdinandobons/startup-skill

**Action:** STEAL LAYOUT AND QUALITY PATTERNS; DO NOT MERGE WHOLE REPO.

Borrow heavily:

```text
SKILL.md
references/
templates/
verification rules
honesty protocol
research principles
research scaling
research waves
customer interview gate
research verification
output guidelines
```

Use it as the principal inspiration for keeping reusable knowledge out of persona files.

Do NOT import its monolithic startup-design pipeline as the authoritative workflow.

---

## 5.2 Idea Validation Agents

Repository:

https://github.com/MaxKmet/idea-validation-agents

**Action:** STEAL SKILL TAXONOMY AND VALIDATION METHODS.

Borrow concepts from:

- competitor-mapper,
- desire-evaluator,
- distribution-analysis,
- idea-scoring,
- pivot-engine,
- pricing-and-wtp,
- retention-predictor,
- cac-modeler,
- tam-sam-som-builder,
- trend-analysis,
- trend-to-product-mapper,
- user-background-interviewer,
- user-segmentation-profiler,
- weakness-detection,
- decision-memo.

Do not bring its independent memory/state model into Agency Agents.

---

## 5.3 Find Me SaaS

Repository:

https://github.com/Latifox/find-me-saas

**Action:** STEAL VALIDATION-ENGINEERING IDEAS; DO NOT DUPLICATE NODEPAD.

Borrow:

- B2B vs B2C lane distinction,
- score/contract validation mentality,
- pre-mortem,
- devil’s advocate,
- explicit experiment outputs,
- workflow completeness checks,
- portfolio/status UX concepts where relevant.

Do NOT import its canonical scoring or memory state; Nodepad owns those.

---

## 5.4 TweakIdea

Repository:

https://github.com/eph5xx/tweakidea

**Action:** STEAL EVALUATOR PERSONA DESIGN.

Borrow evaluator dimensions/roles such as:

- pain intensity,
- willingness to pay,
- urgency,
- frequency,
- solution gap,
- behavior change,
- mandatory nature,
- incumbent indifference,
- defensibility,
- target clarity,
- scalability.

Convert these primarily into **skeptic/evaluator roles** or skills dispatched against selected Nodepad hypotheses.

Do not copy its model-count architecture.

---

## 5.5 Venture Analyst

Repository:

https://github.com/veyralabsgroup/venture-analyst

**Action:** STEAL PACKAGING PATTERN; OPTIONAL SMALL UTILITIES ONLY.

Borrow:

```text
SKILL.md
scripts/
references/
templates/
```

This is useful for specialist packages that need lightweight executable helpers.

Do not duplicate its research-provider implementations if Nodepad/capability routing already provides the capability.

Agency Agents asks for `research.web`; it should not care whether Nodepad routes to DDGS, HN, Reddit, or another provider.

---

# 6. Repositories Explicitly Not to Merge into Agency Agents

## 6.1 Product Eval

Repository:

https://github.com/sparkline-ventures/product-eval

**Action:** DO NOT MERGE.

Its evidence contracts, confidence, contradiction handling, readiness, calibration, and experiment state belong in Nodepad.

Agency Agents may understand the Nodepad contract, but must not reimplement Product Eval state.

---

## 6.2 Nodepad

Repository:

https://github.com/JsonLord/nodepad

**Action:** EXTERNAL CANONICAL STATE GATEWAY.

Do not merge Nodepad into Agency Agents.

Create an adapter/client boundary.

---

## 6.3 Idea Reality MCP

Repository:

https://github.com/mnemox-ai/idea-reality-mcp

**Action:** EXTERNAL CAPABILITY.

Use through a capability/MCP registry as `research.reality_check`.

---

## 6.4 Reddit research MCP

Repository:

https://github.com/dialog-tools/reddit-research-mcp

**Action:** EXTERNAL CAPABILITY.

Suggested semantic role:

- research.reddit,
- research.community_discovery,
- research.customer_language,
- research.competitor_mentions,
- research.longitudinal_feed.

---

## 6.5 Reddit action MCP

Repository:

https://github.com/jordanburke/reddit-mcp-server

**Action:** EXTERNAL CAPABILITY.

Suggested semantic role:

- social.reddit.publish,
- social.reddit.reply,
- social.reddit.observe.

Write actions require approval.

---

## 6.6 LinkedIn MCP

Repository:

https://github.com/stickerdaniel/linkedin-mcp-server

**Action:** EXTERNAL CAPABILITY.

Suggested semantic role:

- research.linkedin.people,
- research.linkedin.company,
- discovery.leads,
- discovery.decision_makers,
- outreach.linkedin.connect,
- outreach.linkedin.message.

Write actions require approval.

---

# 7. Canonical Repository Layout

Move toward:

```text
agency-agents/
│
├── agents/
│   ├── discovery/
│   ├── intelligence/
│   ├── hypothesis/
│   ├── proposition/
│   ├── experimentation/
│   ├── distribution/
│   ├── production/
│   ├── evaluation/
│   └── decision/
│
├── skills/
│   ├── customer-interview/
│   ├── pain-mining/
│   ├── review-mining/
│   ├── social-listening/
│   ├── customer-language/
│   ├── community-discovery/
│   ├── competitor-mapping/
│   ├── substitute-analysis/
│   ├── source-triangulation/
│   ├── assumption-mapping/
│   ├── hypothesis-framing/
│   ├── causal-analysis/
│   ├── counter-hypothesis/
│   ├── hypothesis-falsification/
│   ├── jtbd/
│   ├── value-proposition/
│   ├── positioning/
│   ├── pricing-wtp/
│   ├── offer-design/
│   ├── unit-economics/
│   ├── market-sizing/
│   ├── distribution-analysis/
│   ├── cac-modeling/
│   ├── retention-analysis/
│   ├── experiment-design/
│   ├── pretotype/
│   ├── fake-door/
│   ├── smoke-test/
│   ├── concierge-test/
│   ├── message-test/
│   ├── pricing-test/
│   ├── landing-page-test/
│   ├── cold-outreach/
│   ├── content-test/
│   ├── lead-scoring/
│   ├── evidence-audit/
│   ├── claim-verification/
│   ├── decision-memo/
│   ├── pivot-engine/
│   └── kill-test/
│
├── workflows/
│   ├── validate-idea.yml
│   ├── investigate-hypothesis.yml
│   ├── disconfirm-hypothesis.yml
│   ├── validate-problem.yml
│   ├── validate-value-proposition.yml
│   ├── validate-pricing.yml
│   ├── validate-channel.yml
│   ├── customer-discovery-cycle.yml
│   ├── competitor-pain-mining.yml
│   ├── fake-door-cycle.yml
│   ├── message-test-cycle.yml
│   ├── pivot-cycle.yml
│   └── portfolio-review.yml
│
├── contracts/
│   ├── task-request.schema.json
│   ├── agent-result.schema.json
│   ├── nodepad-context.schema.json
│   ├── evidence-submission.schema.json
│   ├── hypothesis-proposal.schema.json
│   ├── experiment-spec.schema.json
│   ├── experiment-result.schema.json
│   ├── capability-request.schema.json
│   └── delegation-event.schema.json
│
├── gateways/
│   ├── nodepad/
│   ├── capabilities/
│   ├── delegation/
│   ├── workflows/
│   └── telemetry/
│
├── references/
│   ├── evidence-policy.md
│   ├── falsification-policy.md
│   ├── experimentation-policy.md
│   ├── customer-research-policy.md
│   ├── social-research-policy.md
│   ├── ethical-validation-policy.md
│   └── approval-policy.md
│
├── catalog/
│   ├── agents.json
│   ├── skills.json
│   ├── workflows.json
│   ├── legacy-aliases.json
│   └── capabilities.json
│
├── integrations/
│   └── generated runtime outputs
│
├── legacy-agents/
│   └── preserved original source where not migrated
│
├── scripts/
├── tools.json
├── divisions.json
└── README.md
```

The exact folder naming may be adapted to existing converter constraints, but the semantic separation MUST be preserved.

---

# 8. New Validation Divisions

Replace the conventional-company mental model with validation-stage divisions.

Canonical divisions:

1. `discovery`
2. `intelligence`
3. `hypothesis`
4. `proposition`
5. `experimentation`
6. `distribution`
7. `production`
8. `evaluation`
9. `decision`

Update:

- `divisions.json`,
- division checks,
- converter discovery,
- lint scripts,
- Hermes roster generation,
- README catalog,
- any generated app metadata.

If old source files are moved, preserve them under `legacy-agents/` and preserve important legacy aliases.

No destructive loss of original agent text.

---

# 9. Initial Persona Roster

Personas are specialists. They are NOT copies of skills.

## 9.1 Discovery

- Problem Explorer
- Customer Investigator
- Ethnographic Researcher
- Trend Scout
- Community Scout

## 9.2 Intelligence

- Market Intelligence Analyst
- Competitive Intelligence Analyst
- Review Miner
- Lead Researcher
- Signal Analyst

## 9.3 Hypothesis

- Assumption Mapper
- Hypothesis Formulator
- Causal Analyst
- Counter-Hypothesis Generator
- Opportunity Synthesizer

## 9.4 Proposition

- Positioning Strategist
- Value Proposition Designer
- Customer Language Analyst
- Pricing Strategist
- Offer Designer

## 9.5 Experimentation

- Experiment Designer
- Pretotype Designer
- Fake-Door Designer
- Message-Test Designer
- Pricing-Test Designer
- Concierge-Test Designer

## 9.6 Distribution

- Channel Researcher
- Community Activation Specialist
- Outbound Experimenter
- Content Experimenter
- Demand Generation Tester

## 9.7 Production

- Prototype Director
- Landing Page Builder
- Visual Creative
- Demo Producer
- Copy Producer

Production specialists build validation artifacts, not full products by default.

## 9.8 Evaluation

- Evidence Auditor
- Red-Team Analyst
- WTP Skeptic
- Demand Skeptic
- Distribution Skeptic
- Experiment Analyst

## 9.9 Decision

- Venture Judge
- Pivot Strategist
- Kill Agent
- Portfolio Allocator

The coding agent may reuse/migrate existing Agency personas when they are already stronger than creating a new duplicate.

---

# 10. Persona Design

Persona files should become significantly thinner than current Agency files.

A persona defines **who thinks**, not every reusable procedure they know.

Recommended frontmatter:

```yaml
---
id: customer-investigator
name: Customer Investigator
description: Finds behavioral evidence about whether a target customer's problem is real.
division: discovery
color: "#7C3AED"
emoji: "🔎"
vibe: Tries to disprove the founder's story before helping strengthen it.

mission:
  - close customer-evidence gaps
  - distinguish behavior from stated preference
  - return cited evidence and alternative explanations

bias:
  primary: disconfirmation

reads:
  - nodepad.hypotheses
  - nodepad.evidence
  - nodepad.research_gaps

writes:
  - evidence_submission
  - counter_hypothesis
  - research_gap

skills:
  - customer-interview
  - pain-mining
  - customer-language
  - hypothesis-falsification

capabilities:
  required:
    - research.web
  optional:
    - research.reddit
    - research.linkedin

approval:
  read: automatic
  external_write: required

success:
  - closes a material evidence gap
  - produces source-linked evidence
  - distinguishes observation from interpretation

never:
  - fabricate customer evidence
  - qualify a hypothesis itself
  - silently ignore contradictory evidence
---
```

Retain the current fields required by existing converters where necessary:

- name,
- description,
- color,
- emoji,
- vibe.

The converter/runtime system should tolerate/add the extended metadata.

---

# 11. Persona Body Contract

Recommended persona body:

```markdown
# Persona Name

## Identity
Short specialist perspective.

## Mission
What this specialist is responsible for.

## Default Bias
What failure mode they intentionally counteract.

## Operating Rules
5–12 concise specialist rules.

## Nodepad Interaction
What context to read and what structured results to return.

## Skill Selection
When to apply its assigned reusable skills.

## Handoff Rules
Who/what should receive output next.

## Success Conditions
How useful work is recognized.

## Boundaries
What this persona must not decide or fabricate.
```

Do not repeat large research templates inside every agent.

Reusable methodology belongs in `skills/` or `references/`.

---

# 12. Skill Model

A **skill** answers:

> “How is one expert task performed?”

A skill is reusable by many personas.

Recommended package:

```text
skills/pricing-wtp/
├── SKILL.md
├── references/
│   ├── behavioral-wtp.md
│   └── pricing-methods.md
├── templates/
│   └── pricing-test.yml
└── scripts/
    └── optional helper
```

Not every skill needs all directories.

## 12.1 Skill metadata

Recommended:

```yaml
---
id: pricing-wtp
name: Pricing and Willingness-to-Pay
description: Tests pricing and payment willingness without treating stated preference as purchase evidence.

inputs:
  - hypotheses
  - customer_segments
  - competitor_pricing

outputs:
  - hypothesis_proposals
  - experiment_specs
  - evidence_requests

capabilities:
  optional:
    - research.web
    - browser

quality:
  requires_behavioral_test_for_strong_claim: true
---
```

---

# 13. Persona vs Skill vs Workflow vs Capability vs State

This distinction is mandatory.

## Persona = who thinks

Example:

`Customer Investigator`

## Skill = how to perform one expert task

Example:

`pain-mining`

## Workflow = how multiple tasks/personas compose

Example:

`validate-value-proposition`

## Capability = what external action is possible

Example:

`research.reddit`

## Nodepad = canonical state/truth

Example:

`H31: potentially_qualified, signed evidence score +44, confidence 63`

Never collapse these five layers.

---

# 14. Workflow Model

Workflows are declarative orchestration descriptions.

Example:

```yaml
id: validate-value-proposition
version: 1

objective:
  test whether a proposition resonates with a defined segment strongly enough to justify another validation cycle

inputs:
  - nodepad_workspace
  - hypothesis_id

steps:
  - agent: customer-language-analyst
    skills:
      - customer-language

  - agent: value-proposition-designer
    skills:
      - value-proposition

  - agent: red-team-analyst
    skills:
      - hypothesis-falsification

  - agent: message-test-designer
    skills:
      - message-test

outputs:
  - hypothesis_proposals
  - experiment_spec
  - nodepad_evidence_requests
```

Workflow definitions should not embed provider credentials.

---

# 15. Core Workflows Required in First Pass

Implement at least:

1. `validate-idea`
2. `investigate-hypothesis`
3. `disconfirm-hypothesis`
4. `validate-problem`
5. `validate-value-proposition`
6. `validate-pricing`
7. `validate-channel`
8. `customer-discovery-cycle`
9. `competitor-pain-mining`
10. `fake-door-cycle`
11. `message-test-cycle`
12. `pivot-cycle`
13. `portfolio-review`

Each must pass schema validation.

---

# 16. Shared Contracts

All agent interaction should have machine-readable contracts.

## 16.1 Task request

Minimum fields:

```json
{
  "task_id": "task_123",
  "workspace_id": "venture_7",
  "objective": "Disconfirm H27",
  "actor": "user|agent|workflow",
  "hypothesis_ids": ["H27"],
  "constraints": {},
  "allowed_capabilities": [],
  "approval_policy": {}
}
```

## 16.2 Agent result

Minimum:

```json
{
  "task_id": "task_123",
  "agent_id": "customer-investigator",
  "status": "completed",
  "summary": "...",
  "evidence_submissions": [],
  "hypothesis_proposals": [],
  "counter_hypotheses": [],
  "experiment_specs": [],
  "research_gaps": [],
  "artifacts": [],
  "handoff": []
}
```

## 16.3 Evidence submission

Must distinguish:

- observation,
- interpretation,
- source,
- claim,
- support/contradiction target,
- confidence in extraction,
- provenance.

Agent evidence MUST NOT carry authoritative Nodepad qualification.

## 16.4 Hypothesis proposal

Must include:

- statement,
- hypothesis_type,
- derived_from,
- rationale,
- supporting evidence IDs if any,
- contradicting evidence IDs if any,
- unknowns,
- proposed falsification test.

Nodepad determines qualification.

---

# 17. Nodepad Gateway

Create a Nodepad gateway interface even if the live Nodepad API is not available during this task.

Configuration:

```text
NODEPAD_BASE_URL
NODEPAD_API_KEY
NODEPAD_WORKSPACE_ID
```

Do not require these for repository build/tests.

## 17.1 Required gateway operations

Read:

- workspace context,
- hypotheses,
- hypothesis detail,
- evidence,
- evidence gaps,
- experiments,
- brain context,
- graph neighborhood.

Write:

- evidence submission,
- hypothesis proposal,
- counter-hypothesis proposal,
- experiment spec,
- experiment result,
- research gap,
- artifact reference,
- agent-run event.

## 17.2 Expected future HTTP shape

Use configurable adapters; do not hardcode if Nodepad’s final route differs.

Reasonable interface expectations:

```text
GET  /api/v1/workspaces/{id}/context
GET  /api/v1/hypotheses/{id}
GET  /api/v1/hypotheses/{id}/evidence
POST /api/v1/evidence
POST /api/v1/hypotheses/proposals
POST /api/v1/experiments
POST /api/v1/agent-events
```

The local Agency interface must remain stable even if the remote URLs are mapped differently.

## 17.3 If live Nodepad is unavailable

DO NOT STOP.

Instead:

1. implement the interface,
2. provide a mock/fixture Nodepad server or adapter,
3. run contract tests,
4. demonstrate read → specialist action → structured write,
5. report the remote gateway as `READY_CONFIG` or `PASS_MOCK`,
6. continue all remaining work.

---

# 18. Capability Gateway

Create a semantic capability registry.

Example:

```yaml
research.reddit:
  providers:
    - dialog-reddit
    - jordan-reddit-read

outreach.reddit:
  providers:
    - jordan-reddit-write

research.linkedin:
  providers:
    - linkedin-local

research.web:
  providers:
    - nodepad-research
    - generic-web

image.generate:
  providers:
    - free-first-image-chain
```

Agent files reference capabilities, not providers.

## 18.1 Provider metadata

Support fields such as:

```yaml
id:
transport:
endpoint:
command:
args:
priority:
cost:
access:
auth_env:
health_probe:
approval:
features:
```

## 18.2 Approval

Default:

- public/read research: automatic where safe,
- social posting: approval required,
- private messages: approval required,
- destructive write: approval required,
- spending paid quota: approval required unless explicitly enabled.

---

# 19. Hermes Gateway

Preserve and expand the existing lazy-router architecture.

Existing Hermes behavior should continue to support conceptually:

- search,
- inspect,
- load,
- delegate.

Extend the generated roster so it understands:

- new validation divisions,
- persona metadata,
- skills,
- capabilities,
- workflows.

Recommended future tool surface:

```text
agency_agents_search
agency_agents_inspect
agency_agents_load
agency_agents_delegate
agency_skills_search
agency_workflows_list
agency_workflow_inspect
agency_workflow_plan
```

Do not require live Hermes availability to complete implementation.

Provide unit/fixture tests for router generation and delegation fallback behavior.

---

# 20. Runtime Export Gateway

`tools.json` remains the source of truth for supported runtimes.

At minimum prove exports for:

- Claude Code,
- Codex,
- OpenCode,
- Hermes.

Do not break the other runtime entries.

Each runtime export should retain enough metadata/instructions to preserve the persona’s:

- identity,
- mission,
- operating rules,
- assigned skills,
- Nodepad interaction rules,
- capability requirements.

If a runtime format cannot directly encode some metadata, render it into the prompt/body or companion generated data without silently discarding it.

---

# 21. Generic Delegation Gateway

Create an internal delegation abstraction independent of Hermes.

Conceptual interface:

```ts
delegate({
  agentId,
  task,
  context,
  workflowId,
  workspaceId
})
```

Hermes can wrap this later.

Spynel can wrap this later.

A future HTTP service can wrap this later.

The core catalog should not depend directly on Hermes internals.

---

# 22. Workflow Control Gateway

Implement library/CLI access to:

- list workflows,
- inspect workflow,
- validate workflow,
- resolve agents/skills,
- generate execution plan.

Actual remote orchestration may remain external.

Recommended CLI examples:

```bash
aa workflows list
aa workflows inspect validate-pricing
aa workflows plan validate-pricing --fixture fixtures/venture.json
```

If the existing `aa` CLI architecture makes another syntax cleaner, adapt while preserving functionality.

---

# 23. Telemetry / Status Gateway

Every delegated task or workflow should be able to emit structured lifecycle events:

```text
accepted
context_loaded
agent_selected
skill_selected
capability_requested
started
artifact_created
evidence_submitted
handoff_created
completed
failed
cancelled
```

Recommended event fields:

```json
{
  "event_id": "...",
  "task_id": "...",
  "workspace_id": "...",
  "agent_id": "...",
  "workflow_id": "...",
  "type": "started",
  "timestamp": "...",
  "summary": "...",
  "metadata": {}
}
```

This is the future connection point for:

- Nodepad graph history,
- Spynel status messages,
- AGTX,
- Paperclip/n8n.

Do not make AGTX or Spynel mandatory runtime dependencies.

---

# 24. Later Spynel Gateway

Reference repository:

https://github.com/JsonLord/spynel

**Action in this pass:** CONTRACT/ADAPTER PREPARATION ONLY unless trivial.

Agency Agents should expose enough control metadata that Spynel can later:

1. select an agent,
2. select a workflow,
3. attach a Nodepad workspace,
4. dispatch a task,
5. follow status events,
6. continue a specialist session.

No Spynel-specific state should enter persona files.

---

# 25. Later AGTX Status Gateway

Reference repository:

https://github.com/fynnfluegge/agtx

**Action in this pass:** TELEMETRY COMPATIBILITY / DOCUMENTATION ONLY.

Provide a clean event/status contract that a later adapter can transform into AGTX state.

Do not block implementation on AGTX connectivity.

---

# 26. Later Paperclip / n8n Gateway

Paperclip reference:

https://github.com/JsonLord/paperclip

n8n workflow repository reference:

https://github.com/JsonLord/n8n_paperclip

**Action in this pass:** DEFINE WORKFLOW CONTROL BOUNDARY.

Paperclip/n8n should later be able to:

- trigger an Agency workflow,
- supply workspace/hypothesis IDs,
- receive execution status,
- receive final structured result,
- schedule repeated work.

Do not embed n8n workflow JSON into personas.

---

# 27. Migration of Existing Agents

Do not delete useful existing specialists.

For every current agent:

1. classify it as:
   - migrate,
   - split,
   - reuse unchanged with new metadata,
   - archive as legacy,
   - supersede with alias.

2. record the decision in:

```text
docs/agent-migration-map.md
```

Examples:

- UX Researcher → likely migrate into Discovery/Customer Investigator or remain a supporting specialist.
- Academic Statistician → likely Evaluation/Evidence Auditor or statistical skill support.
- Marketing copy roles → Production/Copy Producer or Proposition/Customer Language Analyst.
- Sales prospecting roles → Intelligence/Lead Researcher or Distribution/Outbound Experimenter.
- Product strategy roles → Hypothesis/Proposition/Decision depending on mission.
- Engineers → only retain where they support prototype/validation artifact production; production-building agents are not the center of this fork.

Preserve old slugs through `catalog/legacy-aliases.json` where reasonable.

---

# 28. No Duplication Rule

The same methodology must not be copied into multiple persona files.

Example:

Wrong:

```text
Customer Investigator contains 300 lines of interview methodology
Ethnographic Researcher contains same 300 lines
Problem Explorer contains same 300 lines
```

Correct:

```text
skills/customer-interview/SKILL.md
references/customer-research-policy.md
```

and agents reference the skill.

---

# 29. Evidence Discipline

Every specialist that produces empirical claims must follow:

1. distinguish observation from interpretation,
2. cite source/provenance,
3. surface contradicting evidence,
4. never turn a generated idea into “customer evidence,”
5. never invent traction,
6. never invent quotes,
7. never invent test results,
8. label synthetic artifacts as synthetic,
9. treat social engagement as weaker than purchase/behavior evidence,
10. submit results to Nodepad rather than self-certifying them.

---

# 30. Falsification Bias

Validation is not persuasion.

Core rule:

> The specialist should make the strongest credible version of a hypothesis or proposition, expose it to reality, attempt to falsify it, and return the resulting evidence.

Important agents must explicitly seek:

- alternative explanations,
- substitutes,
- current workaround sufficiency,
- low urgency,
- low frequency,
- unwillingness to pay,
- channel failure,
- switching costs,
- behavior-change barriers,
- regulatory barriers,
- incumbent advantages,
- indifference.

---

# 31. Artifact-First Validation

Production agents should default to producing the cheapest artifact capable of generating evidence:

- landing page,
- fake door,
- mock workflow,
- clickable prototype,
- screenshot,
- demo video,
- Wizard-of-Oz backend,
- concierge service,
- waitlist,
- pricing page,
- outreach script,
- social content test.

Do not default to building a production backend.

---

# 32. Human Approval and Social Actions

Research can be automated where allowed.

Public posting/outreach should default to approval.

Agents must not:

- impersonate unrelated humans,
- fabricate grassroots support,
- manipulate votes/karma,
- post fake testimonials,
- misrepresent fake-door functionality as already existing,
- invent customer counts or traction.

---

# 33. Catalogs

Generate/maintain machine-readable catalogs.

## `catalog/agents.json`

Include:

- id,
- name,
- division,
- description,
- vibe,
- skills,
- capabilities,
- reads,
- writes,
- approval requirements,
- source path,
- legacy aliases.

## `catalog/skills.json`

Include:

- id,
- description,
- input types,
- output types,
- capability requirements,
- references,
- source path.

## `catalog/workflows.json`

Include:

- id,
- description,
- steps,
- agents,
- skills,
- expected inputs/outputs.

## `catalog/capabilities.json`

Include semantic capability definitions and optional provider mappings.

These catalogs should be generated or validated in CI to avoid drift.

---

# 34. Validation and CI

Add CI/check scripts for:

- every active agent resolves to a known division,
- every assigned skill exists,
- every required capability exists,
- every workflow agent exists,
- every workflow skill exists,
- every contract JSON schema parses,
- every legacy alias resolves,
- no duplicate IDs/slugs,
- no circular workflow dependency unless explicitly allowed,
- runtime converters still pass,
- Hermes plugin generation succeeds,
- catalogs regenerate deterministically,
- no secret-like values are committed in capability config,
- archived agents are not accidentally active,
- Nodepad adapter fixture contract passes.

---

# 35. Control Gateways — Non-Blocking Proof Requirements

“Gateway” in this specification means an integration/control boundary.

A gateway being unavailable MUST NOT stop the coding agent.

Each gateway receives one of these statuses:

```text
PASS_LIVE
PASS_LOCAL
PASS_MOCK
READY_CONFIG
BLOCKED_EXTERNAL
FAILED_INTERNAL
```

Only `FAILED_INTERNAL` is an implementation failure that must be fixed before completion.

`BLOCKED_EXTERNAL` is acceptable only when the external service cannot be reached/configured and the local adapter contract is fully implemented/tested.

Create:

```text
reports/gateway-readiness.md
```

For every gateway include:

- purpose,
- status,
- config variables,
- exact control actions exposed,
- exact test command,
- actual output/proof,
- what external dependency remains,
- how a future controller calls it.

---

# 36. Gateway Proof Matrix

## G1 — Agent Catalog Gateway

Must prove:

- list agents,
- search agents,
- inspect agent,
- resolve legacy alias,
- retrieve skills/capabilities.

Proof via CLI/unit test.

---

## G2 — Skill Catalog Gateway

Must prove:

- list skills,
- inspect skill,
- resolve skill dependencies,
- identify personas that can use skill.

---

## G3 — Workflow Gateway

Must prove:

- list workflows,
- inspect workflow,
- validate workflow,
- generate a deterministic execution plan from a fixture.

Actual agent execution is optional in this first gateway proof.

---

## G4 — Nodepad Gateway

Must prove:

```text
fixture context
→ read hypothesis H1
→ run one specialist result transformation
→ submit evidence/hypothesis proposal through adapter
→ fixture Nodepad store records write
```

If live Nodepad is available, additionally test live read-only connectivity.

Do not require live writes for acceptance.

---

## G5 — Capability Gateway

Must prove:

- semantic capability lookup,
- provider resolution,
- free-first ordering,
- approval gating,
- graceful unavailable-provider handling.

Use fixture providers if external providers are unavailable.

---

## G6 — Hermes Gateway

Must prove:

- build plugin,
- search new validation roster,
- inspect a specialist,
- load specialist context,
- exercise delegation fallback or mocked lifecycle.

If Hermes is installed, optionally perform a live smoke test.

Do not stop if Hermes is absent.

---

## G7 — Runtime Export Gateway

Must prove valid generated output for at least:

- Claude Code,
- Codex,
- OpenCode,
- Hermes.

Also run existing converter checks across all supported runtimes.

---

## G8 — Generic Delegation Gateway

Must prove:

```text
agent ID + task + fixture context
→ resolved persona
→ resolved skills
→ delegation request object
→ structured result object
```

No cloud model is required for contract proof.

---

## G9 — Telemetry Gateway

Must prove structured events are emitted for a fixture run:

```text
accepted
agent_selected
started
completed
```

and can be consumed by a simple test sink.

---

## G10 — Future Orchestrator Gateway

Must demonstrate that a future controller can provide:

```json
{
  "workflow_id": "validate-pricing",
  "workspace_id": "venture_7",
  "hypothesis_ids": ["H17"]
}
```

and receive:

- execution plan,
- task IDs,
- status events,
- structured result.

This can be fixture-based.

---

# 37. Implementation Gates — Report but Do Not Stop

The coding agent should report progress at these gates but must continue automatically.

## Gate A — Baseline

Report:

- branch,
- starting commit,
- current tests/lint/converter status,
- repository inventory.

Continue.

## Gate B — Architecture

Report:

- new layout,
- catalogs,
- new divisions,
- migration strategy.

Continue.

## Gate C — Skills

Report:

- extracted Founder Skills,
- newly normalized skills,
- donor attribution.

Continue.

## Gate D — Personas

Report:

- active roster,
- migrated original agents,
- archived/legacy agents,
- aliases.

Continue.

## Gate E — Workflows and Contracts

Report:

- workflow count,
- schema validation status,
- sample execution plans.

Continue.

## Gate F — Nodepad/Capability Boundaries

Report:

- adapter interfaces,
- mock/live status,
- control proof.

Continue.

## Gate G — Runtime/Hermes

Report:

- converter results,
- Hermes plugin build,
- router proof.

Continue.

## Gate H — Final Validation

Report:

- all tests,
- build/lint,
- gateway-readiness report,
- remaining external-only work.

Do not ask the user to approve between gates.

---

# 38. Minimum End-to-End Fixture

Create a realistic fixture such as:

```text
Venture:
AI-assisted accessibility review for small product teams

Hypothesis H1:
Small product teams experience enough costly late accessibility rework
to pay for earlier automated review.

Evidence:
E1 — 3 community complaints about late fixes
E2 — competitor review mentioning expensive remediation
E3 — one contradictory source saying accessibility is rarely prioritized
```

Run:

```text
Nodepad fixture
→ Customer Investigator
→ pain-mining / falsification
→ Counter-Hypothesis Generator
→ Experiment Designer
→ structured Agency result
→ Nodepad fixture write
```

Expected result should include:

- supporting evidence,
- contradictory evidence,
- counter-hypothesis,
- research gap,
- proposed experiment,
- no self-assigned qualification.

---

# 39. Deliverables

The implementation is not complete until it produces all applicable items below.

## Architecture

- [ ] validation-stage divisions
- [ ] canonical `agents/` structure
- [ ] central `skills/`
- [ ] `workflows/`
- [ ] `contracts/`
- [ ] `gateways/`
- [ ] `catalog/`
- [ ] `references/`
- [ ] legacy preservation strategy

## Skills

- [ ] Founder Skills donor extraction documented
- [ ] at least 20 normalized reusable validation skills
- [ ] no donor-specific state assumptions left in imported skill contracts
- [ ] references/templates separated where useful

## Personas

- [ ] core validation roster implemented
- [ ] personas reduced to role-specific behavior
- [ ] skills referenced rather than duplicated
- [ ] Nodepad read/write semantics present
- [ ] falsification bias where appropriate
- [ ] success/boundary rules present

## Workflows

- [ ] 13 required workflows
- [ ] workflow schema
- [ ] workflow validator
- [ ] fixture execution-plan generation

## Contracts

- [ ] task request
- [ ] agent result
- [ ] Nodepad context
- [ ] evidence submission
- [ ] hypothesis proposal
- [ ] experiment spec
- [ ] experiment result
- [ ] capability request
- [ ] delegation event

## Gateways

- [ ] Nodepad adapter
- [ ] capability registry
- [ ] generic delegation abstraction
- [ ] workflow control
- [ ] telemetry sink
- [ ] Hermes adapter/plugin compatibility
- [ ] runtime export compatibility

## Compatibility

- [ ] existing tool catalog retained
- [ ] existing converters pass or intentional changes documented
- [ ] Hermes lazy loading remains
- [ ] legacy agent content preserved
- [ ] legacy aliases documented

## Documentation

- [ ] README rewritten for validation-workforce vision
- [ ] `docs/architecture.md`
- [ ] `docs/personas-vs-skills.md`
- [ ] `docs/nodepad-integration.md`
- [ ] `docs/capability-routing.md`
- [ ] `docs/workflows.md`
- [ ] `docs/agent-migration-map.md`
- [ ] `docs/donor-attribution.md`
- [ ] `reports/gateway-readiness.md`

## Proof

- [ ] end-to-end fixture passes
- [ ] catalogs validate
- [ ] workflows validate
- [ ] contracts validate
- [ ] Hermes plugin builds
- [ ] Claude export works
- [ ] Codex export works
- [ ] OpenCode export works
- [ ] capability resolution fixture works
- [ ] Nodepad mock round trip works
- [ ] telemetry fixture works

---

# 40. Donor Attribution Document

Create:

```text
docs/donor-attribution.md
```

For each donor record:

- repository URL,
- license,
- files/methods reviewed,
- files actually copied or adapted,
- conceptual patterns reused,
- significant rewrites,
- attribution requirements.

Do not casually copy incompatible-license material.

Prefer reimplementation of methodology when license compatibility is uncertain.

---

# 41. Safe Implementation Rules

1. Work on a dedicated branch.
2. Record starting commit.
3. Run baseline tests before changes.
4. Do not force-push.
5. Preserve original agent content before moving/restructuring.
6. Do not delete runtime adapters.
7. Do not collapse Nodepad state into Agency files.
8. Do not hardcode secrets.
9. Do not require paid providers.
10. Do not make a live remote service a prerequisite for tests.
11. Use fixture/mock gateways where remote systems are unavailable.
12. Continue through non-blocking gates automatically.
13. Fix regressions introduced by this work.
14. Do not spend excessive effort on unrelated pre-existing failures.
15. Keep commits logically grouped if possible.

---

# 42. Acceptance Criteria

The transformed repository should answer these questions positively:

### Can I ask for the right specialist?

Yes:

```text
search "disprove willingness to pay"
→ WTP Skeptic / Pricing Strategist / Experiment Designer
```

### Can personas share methods without duplicated prompts?

Yes:

```text
skills/pricing-wtp
skills/hypothesis-falsification
```

### Can a workflow compose agents?

Yes:

```text
validate-pricing
```

### Can an external controller inspect and dispatch?

Yes, proven through catalog/delegation/workflow gateway fixtures.

### Can Nodepad remain source of truth?

Yes, Agency writes proposals/evidence/results through an adapter and does not self-qualify.

### Can Hermes control the workforce later?

Yes, the lazy router still builds and can search/load/delegate the validation roster.

### Can Codex/OpenCode/Claude consume the same personas?

Yes, converter proof exists.

### Can MCP/provider implementations change without rewriting agents?

Yes, capabilities are semantic and provider-routed.

### Can unavailable remote gateways be completed later without redesign?

Yes, each boundary has a stable local contract and a recorded proof fixture.

### Can the original Agency knowledge be recovered?

Yes, migrated/archived originals and legacy alias mapping remain in git.

---

# 43. Desired Final Identity of the Repository

The repository should no longer be best described as:

> “A company of AI employees.”

It should be closer to:

> **A portable venture-validation workforce: specialist personas, reusable skills, adversarial workflows, and runtime adapters that gather evidence, design tests, challenge hypotheses, and operate against an external evidence graph.**

Or more compactly:

> **Agency Agents = the workforce. Nodepad = the brain.**

---

# 44. Final Agent Report Format

At completion, the coding agent must report:

## A. Starting state

- branch
- starting SHA
- baseline failures

## B. Architecture implemented

- final directory layout
- active divisions
- catalog design
- contracts

## C. Donors

For every donor:

- URL
- merge/steal decision
- what was used
- what was intentionally not used

## D. Persona migration

- migrated
- newly created
- split
- archived
- aliases

## E. Skills

- total normalized skills
- Founder Skills adaptations
- new validation-native skills

## F. Workflows

- total workflows
- validation results
- example plan

## G. Gateways

Include the entire gateway proof matrix with statuses:

- G1 Agent Catalog
- G2 Skills
- G3 Workflows
- G4 Nodepad
- G5 Capabilities
- G6 Hermes
- G7 Runtime Exports
- G8 Delegation
- G9 Telemetry
- G10 Future Orchestrator

## H. Tests

- lint
- conversion checks
- plugin build
- schema tests
- fixture tests

## I. End-to-end proof

Show one fixture path from:

```text
Nodepad context
→ specialist selection
→ skill execution
→ adversarial/counter-hypothesis work
→ experiment proposal
→ structured Nodepad submission
```

## J. Deferred external work

Only list genuinely external/environment-dependent items.

Do not list core architecture as deferred.

## K. Commits

Provide resulting commit SHA(s).

---

# 45. Definition of Done

Done means the repository is no longer just a reorganized prompt collection.

It must demonstrably provide:

```text
specialists
    +
reusable skills
    +
validation workflows
    +
machine-readable contracts
    +
Nodepad boundary
    +
semantic capability routing
    +
runtime exports
    +
delegation/control gateways
    +
non-blocking integration proof
```

The central behavioral test is:

> A future orchestrator should be able to select a venture workspace and hypothesis in Nodepad, ask Agency Agents to investigate or challenge it, receive status while the work runs, and receive structured evidence/hypothesis/experiment results without either system needing to understand the other’s internal implementation.

That future control path must be proven locally even where the live external gateway is not yet connected.
