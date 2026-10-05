# Validate Pricing Workflow

**Objective**: Validate that customers are willing to pay the proposed price.

## Steps

1. **Pricing Strategy Development**
   - Agent: Pricing Strategist
   - Output: Pricing strategy and price points

2. **Willingness to Pay Testing**
   - Skill: pricing-wtp
   - Output: WTP data and price sensitivity

3. **Price Experiment Design**
   - Agent: Pricing-Test Designer
   - Output: Price test experiment spec

4. **Price Experiment Execution**
   - Via capability gateway (e.g., fake-door, landing page)
   - Output: Price test results

5. **Evidence Audit**
   - Skill: evidence-audit
   - Output: Audited price test evidence

6. **Pricing Decision**
   - Agent: Pricing Strategist
   - Output: Final pricing decision

## Success Criteria

- WTP established with acceptable range
- Price test shows conversion at target price
- Audited evidence supports pricing decision

## Output

- Pricing strategy
- WTP data
- Price test spec and results
- Audited evidence
- Final pricing decision

## Next Steps

Proceed to validate-channel or fake-door-cycle.
