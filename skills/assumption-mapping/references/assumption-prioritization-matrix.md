# Assumption Prioritization Matrix

## Overview

Not all assumptions are created equal. To focus validation efforts effectively, we need to prioritize assumptions based on their potential impact and current uncertainty. This reference provides a framework for assessing and ranking assumptions using a 2x2 risk matrix.

## The 2x2 Prioritization Matrix

Assumptions are plotted on two axes:

**X-axis: Uncertainty (Low to High)**
- How confident are we that this assumption is true?
- Based on available evidence, data, or validation

**Y-axis: Impact (Low to High)**
- What would be the consequence if this assumption were wrong?
- How much would it affect the venture's success?

## Quadrants and Actions

### Quadrant 1: Low Impact, Low Uncertainty (Bottom Left)
- **Characteristics**: We're confident, and it wouldn't hurt much if wrong
- **Action**: Monitor, minimal validation effort needed
- **Validation**: Light touch, occasional checks

### Quadrant 2: High Impact, Low Uncertainty (Top Left)
- **Characteristics**: We're confident, but it would hurt a lot if wrong
- **Action**: Validate to maintain confidence, but lower priority
- **Validation**: Periodic verification as project progresses

### Quadrant 3: Low Impact, High Uncertainty (Bottom Right)
- **Characteristics**: We're not confident, but it wouldn't hurt much if wrong
- **Action**: Consider if easy/cheap to test, otherwise deprioritize
- **Validation**: Only if resources allow and test is simple

### Quadrant 4: High Impact, High Uncertainty (Top Right) - **PRIORITY**
- **Characteristics**: We're not confident, and it would hurt a lot if wrong
- **Action**: **VALIDATE FIRST** - These are our biggest risks
- **Validation**: Invest significant effort to reduce uncertainty

## Assessing Impact

Impact refers to the consequence of the assumption being false. Consider:

### Business Impact
- Would it invalidate the core business model?
- Would it make the venture economically unviable?
- Would it require a major pivot or restart?

### Customer Impact
- Would it mean no real problem exists?
- Would customers not want or use the solution?
- Would the value proposition collapse?

### Technical Impact
- Would the solution be impossible to build?
- Would it require completely different technology or approach?
- Would timelines or costs increase dramatically?

### Legal/Regulatory Impact
- Would it create compliance barriers?
- Would it prevent market entry or operation?
- Would it require significant redesign or licensing?

## Assessing Uncertainty

Uncertainty refers to our lack of confidence in the assumption. Consider:

### Evidence Level
- **Direct evidence**: We've observed or measured it
- **Indirect evidence**: We have proxy data or analogs
- **Opinion-based**: Based on expert or customer opinion
- **No evidence**: Pure guess or belief

### Source Quality
- **Primary data**: Direct from target customers/users
- **Secondary data**: Reports, studies, published research
- **Expert opinion**: From qualified professionals
- **Anecdotal**: Single examples or stories
- **Opinion**: Personal belief or team consensus

### Time Sensitivity
- Is this likely to change over time?
- Are we basing this on current conditions that may shift?
- Could market, technology, or regulatory changes affect it?

## Prioritization Process

### Step 1: List All Assumptions
- Create a comprehensive list from assumption mapping
- Include assumptions from all domains (D, V, F)

### Step 2: Assess Impact
- For each assumption, ask: "What happens if this is wrong?"
- Assign Impact score: Low (1), Medium (2), High (3)
- Consider business, customer, technical, and legal dimensions

### Step 3: Assess Uncertainty
- For each assumption, ask: "How confident are we?"
- Assign Uncertainty score: Low (1), Medium (2), High (3)
- Consider evidence level, source quality, and time sensitivity

### Step 4: Plot on Matrix
- X-axis = Uncertainty (1=Low to 3=High)
- Y-axis = Impact (1=Low to 3=High)
- Identify which quadrant each assumption falls into

### Step 5: Plan Validation
- **Quadrant 4 (High Impact, High Uncertainty)**: Validate first
- **Quadrant 2 (High Impact, Low Uncertainty)**: Validate periodically
- **Quadrant 3 (Low Impact, High Uncertainty)**: Validate if easy/cheap
- **Quadrant 1 (Low Impact, Low Uncertainty)**: Monitor only

## Output Template

See `templates/assumption-prioritization.md` for a standard output format.

## Quality Gates

- [ ] All assumptions from mapping have been assessed
- [ ] Impact and uncertainty assessments are documented
- [ ] Assumptions are correctly placed in the matrix
- [ ] Validation efforts are focused on Quadrant 4 assumptions
- [ ] The matrix is reviewed and updated as new evidence emerges

## References

See `references/` for:
- assumption-impact-assessment-guide.md
- assumption-uncertainty-assessment.md
- validation-effort-estimation.md

## Dependencies

- No external tools required
- Can be done with sticky notes, spreadsheets, or digital tools
- Works immediately after assumption mapping

## Contributing

Improvements to this skill should:
- Maintain focus on evidence-based prioritization
- Preserve the 2x2 matrix framework
- Include practical guidance for assessing impact and uncertainty
- Be tested with real venture assumptions
---

## Skill Overview

The assumption prioritization matrix skill enables practitioners to systematically rank assumptions by their risk level, ensuring that validation efforts focus on the most critical uncertainties. Unlike gut-feeling or convenience-based prioritization, this method uses explicit criteria to determine which assumptions deserve the most validation resources.

## Key Differentiators

- Uses explicit Impact × Uncertainty framework rather than intuition
- Considers multiple dimensions of impact (business, customer, technical, legal)
- Evaluates uncertainty based on evidence quality and source
- Creates a visual tool for team discussion and alignment
- Focuses validation resources where they matter most

## Common Applications

- Planning validation experiments and customer interviews
- Allocating limited validation resources (time, money, effort)
- Communicating validation priorities to stakeholders and investors
- Building validation roadmaps and milestones
- Conducting pre-mortem analyses to identify killer risks

## Success Indicators

After applying this skill, you should be able to:
- List all assumptions from assumption mapping with source documentation
- Assess impact using multiple dimensions and evidence
- Assess uncertainty based on evidence level and source quality
- Correctly plot assumptions on the 2x2 matrix
- Plan validation efforts that prioritize Quadrant 4 assumptions
- Update the matrix as new evidence reduces uncertainty

## Anti-Patterns to Avoid

- Relying on team intuition or highest-paid-person's-opinion
- Failing to document the reasoning behind impact/uncertainty scores
- Not updating the matrix as evidence accumulates
- Treating all high-uncertainty assumptions as equal priority
- Ignoring low-uncertainty assumptions that could become high-impact
- Creating the matrix but not using it to guide validation efforts

## Next Steps

After completing assumption prioritization, consider:
- Designing validation experiments for Quadrant 4 assumptions
- Creating assumption validation plans with success criteria
- Developing hypothesis framing based on validated assumptions
- Building experiments that test specific high-risk assumptions
- Sharing the prioritization matrix with the venture team and advisors
