---
name: assumption-mapping
description: A reusable skill for identifying, categorizing, and prioritizing assumptions underlying venture hypotheses.
version: 1.0.0
---

# Assumption Mapping Skill

This skill provides a structured approach to discovering, organizing, and validating assumptions that underlie venture hypotheses, enabling teams to focus validation efforts on the most critical uncertainties.

## When to Use This Skill

- After problem discovery and hypothesis formulation
- Before designing experiments to test hypotheses
- When evaluating the readiness of a hypothesis for validation
- To identify and prioritize risks in a venture
- To create a shared understanding of key uncertainties

## Core Principles

1. **Assumptions are not facts** - Treat everything as uncertain until validated
2. **Separate by domain** - Desirability, viability, feasibility
3. **Prioritize by risk** - Focus on assumptions that are both critical and uncertain
4. **Make assumptions explicit** - Convert implicit beliefs into clear statements
5. **Update continuously** - Revise the map as new evidence emerges

## Assumption Domains

### 1. Desirability (Do customers want it?)
- Problem existence and severity
- Customer willingness to pay
- Solution appeal and resonance
- Market timing and trends
- Customer acquisition potential

### 2. Viability (Can it work as a business?)
- Revenue model sustainability
- Cost structure and profitability
- Channel effectiveness and scalability
- Competitive positioning and defensibility
- Regulatory and legal considerations

### 3. Feasibility (Can we build it?)
- Technical feasibility and complexity
- Resource and skill availability
- Time to develop and launch
- Dependencies and external factors
- Scalability and performance

## Assumption Mapping Process

### 1. Preparation
- Gather the venture hypothesis or idea
- Review existing evidence and insights
- Assemble a diverse team (if possible)
- Prepare assumption statement templates

### 2. Assumption Discovery

#### Brainstorming
- Ask: "What must be true for this to succeed?"
- Use "5 Whys" to drill down to root assumptions
- Consider each domain: desirability, viability, feasibility
- Look for hidden or implicit assumptions

#### Structured Prompts
- Desirability: "Who has this problem? How badly do they want it solved?"
- Viability: "How will we make money? What are the costs?"
- Feasibility: "Can we actually build this? What do we need?"

### 3. Assumption Articulation

#### Assumption Statement Format
"We assume that [specific entity] will [specific behavior/action] because [reason]."

#### Examples
- "We assume that small business owners will pay $50/month for an accessibility auditing tool because they currently face costly late-stage redesigns."
- "We assume that our target customers use Google Chrome as their primary browser because of market share data."
- "We assume that we can develop a minimum viable product in 8 weeks with two developers because of the chosen technology stack."

#### Assumption Components
- **Entity**: Who or what the assumption is about
- **Action**: What they will do or what will happen
- **Basis**: Why we believe this (evidence, analogy, etc.)
- **Certainty**: Our confidence level (optional but useful)

### 4. Assumption Categorization

- Label each assumption by domain (D, V, F)
- Note the source of the assumption (data, opinion, analogy)
- Record the assumption in a central location (spreadsheet, database, etc.)

### 5. Assumption Prioritization

#### Risk Assessment Matrix
- **Impact**: What happens if this assumption is wrong? (Low, Medium, High)
- **Uncertainty**: How confident are we in this assumption? (Low, Medium, High)
- **Risk Level**: Combine impact and uncertainty to prioritize

#### Priority Guidelines
- **High Impact + High Uncertainty** = Top priority (validate first)
- **High Impact + Low Uncertainty** = Monitor but lower validation effort
- **Low Impact + High Uncertainty** = Consider if easy to test
- **Low Impact + Low Uncertainty** = Lowest priority

### 6. Assumption Validation Planning

- For each high-priority assumption, define validation methods
- Determine what evidence would confirm or disprove it
- Estimate effort required for validation
- Sequence validation based on dependencies and resources

## Evidence Collection

- Record assumptions in the exact words formulated
- Note the domain and source of each assumption
- Capture the reasoning or evidence behind each assumption
- Label assumptions as explicit (stated) or implicit (inferred)
- Track changes to assumptions over time

## Output Templates

See `templates/assumption-map.md` for a standard output format.

## Quality Gates

- [ ] Assumptions are specific and testable
- [ ] Each assumption is assigned to a domain
- [ ] Reasoning or source is documented for each assumption
- [ ] Assumptions are prioritized by impact and uncertainty
- [ ] Validation methods are defined for high-priority assumptions
- [ ] Distinction between explicit and implicit assumptions is clear

## References

See `references/` for:
- assumption-interview-guide.txt
- assumption-prioritization-matrix.md
- assumption-validation-methods.md
- assumption-tracking-template.xlsx

## Dependencies

- No external tools required
- Works with sticky notes, digital tools, or spreadsheets
- Can be combined with hypothesis framing and experiment design

## Contributing

Improvements to this skill should:
- Maintain focus on evidence-based assumption discovery
- Preserve the core principles of assumption validation
- Include techniques for assessing assumption criticality
- Be tested with real venture hypotheses
---

## Skill Overview

The assumption mapping skill enables practitioners to systematically uncover and organize the beliefs that underlie venture hypotheses. Unlike informal discussions, assumption mapping creates a shared, explicit representation of what must be true for a venture to succeed, allowing teams to focus validation efforts on the most critical uncertainties.

## Key Differentiators

- Focuses on transforming implicit beliefs into explicit statements
- Separates assumptions by domain (desirability, viability, feasibility)
- Prioritizes assumptions by risk (impact × uncertainty)
- Creates a living document that evolves with evidence
- Enables systematic validation planning

## Common Applications

- Validating problem hypotheses
- Preparing for customer interviews and experiments
- Communicating key risks to stakeholders
- Building investor-ready assumption slides
- Conducting pre-mortem analyses
- Aligning team understanding of uncertainties

## Success Indicators

After applying this skill, you should be able to:
- Identify 10+ assumptions underlying a venture hypothesis
- Categorize assumptions by domain and source
- Prioritize assumptions using a risk matrix
- Define validation methods for top-priority assumptions
- Update the assumption map as new evidence emerges
- Avoid treating assumptions as facts without validation

## Anti-Patterns to Avoid

- Treating assumptions as facts without evidence
- Failing to separate assumptions by domain
- Not updating the map as evidence accumulates
- Overlooking implicit or unconscious assumptions
- Confusing assumptions with observations or data
- Prioritizing based on convenience rather than risk
- Creating assumption maps that are never used for validation

## Next Steps

After completing assumption mapping, consider:
- Framing assumptions into testable hypotheses
- Designing experiments to validate high-priority assumptions
- Creating value propositions based on validated desirability assumptions
- Building financial models based on validated viability assumptions
- Developing technical specifications based on validated feasibility assumptions
- Sharing the assumption map with investors and advisors
