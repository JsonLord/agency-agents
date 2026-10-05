# Investigate Hypothesis Workflow

**Objective**: Investigate a specific hypothesis to gather evidence for or against it.

## Steps

1. **Hypothesis Framing**
   - Agent: Hypothesis Formulator
   - Output: Clear, testable hypothesis statement

2. **Assumption Identification**
   - Skill: assumption-mapping
   - Output: Assumptions underlying the hypothesis

3. **Experiment Design**
   - Agent: Experiment Designer
   - Output: Experiment spec with success criteria

4. **Experiment Execution**
   - Via capability gateway (e.g., research.web, research.reddit)
   - Output: Experiment results

5. **Evidence Audit**
   - Skill: evidence-audit
   - Output: Audited evidence report

6. **Hypothesis Update**
   - Agent: Hypothesis Formulator
   - Output: Updated hypothesis (strengthened, weakened, or refined)

## Success Criteria

- Hypothesis is testable and falsifiable
- Experiment designed with clear IV, DV, and controls
- Evidence collected and audited for quality
- Hypothesis updated based on evidence

## Output

- Framed hypothesis
- Experiment spec
- Audited evidence
- Updated hypothesis

## Next Steps

If hypothesis strengthened, consider disconfirm-hypothesis or move to validation.
If weakened, consider disconfirm-hypothesis or pivot.
