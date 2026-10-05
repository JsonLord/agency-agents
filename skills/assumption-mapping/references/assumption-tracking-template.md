# Assumption Tracking Template

## Overview

Effective assumption management requires systematic tracking of assumptions from discovery through validation to resolution. This template provides a structured format for recording assumptions, their assessments, validation plans, and outcomes.

## Assumption Tracking Template

| ID | Assumption Statement | Domain | Source | Impact (1-3) | Uncertainty (1-3) | Risk Quadrant | Validation Method | Success Criteria | Evidence Collected | Current Status | Resolution | Date Updated |
|----|----------------------|--------|--------|--------------|-------------------|---------------|-------------------|------------------|--------------------|----------------|------------|--------------|
| A1 | We assume that [specific entity] will [specific behavior/action] because [reason]. | D/V/F | [Data/Opinion/Analogy/etc.] | [1/2/3] | [1/2/3] | [Q1/Q2/Q3/Q4] | [Method description] | [What would confirm/disconfirm] | [Summary of evidence] | [To Test/Testing/Validated/Invalidated] | [Supported/Refuted/Updated] | [YYYY-MM-DD] |

## Instructions for Use

### 1. Assumption Statement
- Use the format: "We assume that [entity] will [action] because [reason]."
- Make assumptions specific, testable, and domain-appropriate
- Include the reasoning or basis for the assumption

### 2. Domain
- Mark as D (Desirability), V (Viability), or F (Feasibility)
- Some assumptions may span multiple domains - pick the primary one

### 3. Source
- Document where the assumption came from:
  - Data: Direct measurement, observation, or metrics
  - Opinion: Expert opinion, team consensus, or stakeholder input
  - Analogy: Based on similar situations, products, or markets
  - Theory: Based on conceptual models or frameworks
  - Hypothesis: Derived from another assumption or hypothesis
  - Observation: Directly witnessed or experienced
  - Interview: From customer or stakeholder interviews
  - Research: From published studies, reports, or analysis

### 4. Impact Assessment
- Score 1-3 where:
  - 1 = Low: Minimal impact on venture if wrong
  - 2 = Medium: Moderate impact, may require adjustment
  - 3 = High: Major impact, could invalidate venture or require pivot
- Consider business, customer, technical, and legal dimensions

### 5. Uncertainty Assessment
- Score 1-3 where:
  - 1 = Low: High confidence, strong supporting evidence
  - 2 = Medium: Moderate confidence, mixed or limited evidence
  - 3 = High: Low confidence, little or no supporting evidence
- Consider evidence level, source quality, and time sensitivity

### 6. Risk Quadrant
- Determine quadrant based on Impact and Uncertainty scores:
  - Q1: Low Impact, Low Uncertainty (Bottom Left)
  - Q2: High Impact, Low Uncertainty (Top Left)
  - Q3: Low Impact, High Uncertainty (Bottom Right)
  - Q4: High Impact, High Uncertainty (Top Right) - Priority for validation

### 7. Validation Method
- Describe the method(s) used to test the assumption
- Reference specific techniques from assumption-validation-methods.md
- Include enough detail for replication

### 8. Success Criteria
- Define what evidence would confirm the assumption
- Define what evidence would invalidate the assumption
- Specify any thresholds or criteria for decision-making

### 9. Evidence Collected
- Summarize the evidence gathered through validation efforts
- Include both supporting and contradictory evidence
- Note the quality and quantity of evidence
- Label assumptions as explicit (stated) or implicit (inferred)

### 10. Current Status
- Mark the current state of the assumption:
  - To Test: Validation planned but not started
  - Testing: Validation currently in progress
  - Validated: Sufficient evidence supports the assumption
  - Invalidated: Sufficient evidence refutes the assumption
  - Updated: Assumption has been revised based on evidence

### 11. Resolution
- For validated/invalidated assumptions:
  - Supported: Evidence confirms the assumption
  - Refuted: Evidence contradicts the assumption
  - Updated: Assumption has been modified based on new evidence

### 12. Date Updated
- Record the date when the assumption was last reviewed or updated
- Use YYYY-MM-DD format for consistency

## Example Entries

| ID | Assumption Statement | Domain | Source | Impact (1-3) | Uncertainty (1-3) | Risk Quadrant | Validation Method | Success Criteria | Evidence Collected | Current Status | Resolution | Date Updated |
|----|----------------------|--------|--------|--------------|-------------------|---------------|-------------------|------------------|--------------------|----------------|------------|--------------|
| A1 | We assume that small business owners will pay $50/month for an accessibility auditing tool because they currently face costly late-stage redesigns. | D | Interview | 3 | 3 | Q4 | Price sensitivity test (Van Westendorp) | 40%+ willing to pay >=$40/month | 35% willing to pay >=$40/month | Invalidated | Refuted | 2026-09-15 |
| A2 | We assume that our target customers use Google Chrome as their primary browser because of market share data. | F | Research | 1 | 1 | Q1 | Analytics review | Chrome usage >=60% of target segment | Chrome usage 68% of target segment | Validated | Supported | 2026-09-10 |
| A3 | We assume that we can develop a minimum viable product in 8 weeks with two developers because of the chosen technology stack. | F | Technical spike | 3 | 2 | Q4 | Development timeline tracking | MVP feature complete in <=8 weeks | MVP feature complete in 10 weeks | Invalidated | Refuted | 2026-09-20 |

## Output Templates

See `templates/assumption-tracking-log.md` for a standard output format.

## Quality Gates

- [ ] All assumptions from assumption mapping are recorded
- [ ] Each assumption has domain, source, impact, and uncertainty assessments
- [ ] Risk quadrants are correctly calculated
- [ ] Validation methods are specified for all assumptions
- [ ] Success criteria are defined for validation efforts
- [ ] Current status and resolution are regularly updated

## References

See `references/` for:
- assumption-tracking-best-practices.md
- assumption-tracking-tools.md

## Dependencies

- No external tools required
- Can be implemented as a spreadsheet, database, or digital tool
- Works with both qualitative and quantitative assumption tracking

## Contributing

Improvements to this skill should:
- Maintain focus on systematic assumption management
- Preserve the structured tracking template format
- Include practical guidance for assumption lifecycle management
- Be tested with real assumption tracking campaigns
---

## Skill Overview

The assumption tracking template skill provides practitioners with a systematic format for recording, assessing, validating, and resolving assumptions throughout the venture validation process. Unlike ad-hoc notes or informal discussions, this approach creates a living document that tracks assumptions from initial identification through final resolution, enabling teams to manage uncertainty effectively and make evidence-based decisions.

## Key Differentiators

- Provides a structured format for recording all key assumption attributes
- Includes both assessment (impact/uncertainty) and tracking (status/resolution) dimensions
- Enables prioritization based on risk quadrant analysis
- Supports evidence-based validation planning and outcome tracking
- Creates a shared, updatable record of venture uncertainties

## Common Applications

- Recording outcomes of assumption mapping sessions
- Tracking validation progress for prioritized assumptions
- Communicating assumption status to stakeholders and investors
- Building validation dashboards and progress reports
- Conducting assumption reviews and retrospectives

## Success Indicators

After applying this skill, you should be able to:
- Record all assumptions from assumption mapping in the tracking template
- Assess impact and uncertainty using standardized scales
- Calculate risk quadrants correctly for prioritization
- Specify appropriate validation methods for each assumption
- Define clear success criteria for validation efforts
- Update assumption status and resolution as evidence emerges
- Maintain a current, accurate record of venture uncertainties

## Anti-Patterns to Avoid

- Recording assumptions without making them specific and testable
- Failing to assess impact or uncertainty for assumptions
- Not updating the template as assumptions are validated or invalidated
- Using validation methods that don't actually test the assumption
- Not defining what evidence would count as validation or invalidation
- Creating the template but not using it to guide validation efforts

## Next Steps

After completing assumption tracking setup, consider:
- Populating the template with assumptions from assumption mapping
- Planning validation efforts based on risk quadrant analysis
- Executing validation methods and recording results
- Updating assumption status as evidence is collected
- Sharing the assumption tracking template with the venture team
