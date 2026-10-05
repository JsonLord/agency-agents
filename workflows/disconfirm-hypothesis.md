# Disconfirm Hypothesis Workflow

**Objective**: Actively try to disconfirm a hypothesis to avoid confirmation bias.

## Steps

1. **Hypothesis Framing**
   - Agent: Hypothesis Formulator
   - Output: Hypothesis to disconfirm

2. **Counter-Hypothesis Generation**
   - Agent: Counter-Hypothesis Generator
   - Output: Counter-hypothesis(es)

3. **Experiment Design for Disconfirmation**
   - Agent: Experiment Designer
   - Output: Experiment spec designed to disprove the hypothesis

4. **Experiment Execution**
   - Via capability gateway
   - Output: Experiment results

5. **Evidence Audit**
   - Skill: evidence-audit
   - Output: Audited evidence report

6. **Decision**
   - Agent: Venture Judge
   - Output: Decision to pivot, persevere, or terminate

## Success Criteria

- Counter-hypothesis generated
- Experiment designed to test the negative
- Evidence collected and audited
- Clear decision based on evidence

## Output

- Hypothesis
- Counter-hypothesis(es)
- Experiment spec
- Audited evidence
- Decision

## Next Steps

If hypothesis disconfirmed, pivot or terminate.
If not disconfirmed, proceed to validation workflows.
