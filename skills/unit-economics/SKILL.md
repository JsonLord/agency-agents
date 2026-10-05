---
name: unit-economics
description: A reusable skill for analyzing the direct revenues and costs associated with a single unit of a venture's product or service.
version: 1.0.0
---

# Unit Economics Skill

This skill provides a structured approach to analyzing the direct revenues and costs associated with delivering a single unit of a venture's product or service. Unlike high-level financial projections, unit economics focuses on the profitability of each individual transaction or customer, providing insight into the venture's scalability and sustainability.

## When to Use This Skill

- After value proposition and pricing validation
- When developing financial projections and models
- To assess the viability and scalability of the business model
- Before seeking external investment
- To identify areas for cost optimization or revenue enhancement

## Core Principles

1. **Focus on the individual unit** - Analyze revenues and costs per customer, transaction, or product unit
2. **Include all direct costs** - Consider both obvious and hidden costs directly attributable to each unit
3. **Time-bound analysis** - Specify the time period over which revenues and costs are realized
4. **Contribution margin focus** - Understand how much each unit contributes to covering fixed costs and profit
5. **Cohort-based thinking** - Analyze units acquired in the same time period to understand lifetime value

## Unit Economics Framework

### 1. Revenue per Unit

#### Sources of Revenue
- Direct sales price
- Subscription fees
- Transaction fees
- Usage-based charges
- Ancillary revenue (upsells, cross-sells, etc.)

#### Revenue Calculation
- Average revenue per unit (ARPU)
- Revenue per customer per period
- Revenue per transaction
- Adjust for discounts, refunds, and churn

### 2. Costs per Unit

#### Cost of Goods Sold (COGS) / Direct Costs
- **Variable costs**: Costs that scale directly with each unit
  - Materials and supplies
  - Direct labor
  - Transaction fees (payment processing, commissions)
  - Hosting and infrastructure (if usage-based)
  - Customer support (if per-incident)
  - Shipping and fulfillment
- **Semi-variable costs**: Costs that have both fixed and variable components
  - Some aspects of customer support
  - Some software licenses

#### Customer Acquisition Costs (CAC) - Direct
- Sales commissions
- Onboarding costs
- Implementation services (if charged separately)
- Direct marketing costs attributable to acquisition

### 3. Contribution Margin

#### Gross Margin
- Revenue per unit minus direct costs per unit

#### Contribution Margin
- Revenue per unit minus all variable costs per unit
- Shows how much each unit contributes to covering fixed costs

### 4. Lifetime Value (LTV)

#### Definition
- The total net profit attributed to the entire future relationship with a customer

#### Calculation
- Average revenue per period per customer × gross margin % × average customer lifespan
- Or: Sum of discounted future profits from a customer

### 5. Key Ratios

#### LTV:CAC Ratio
- Lifetime value divided by customer acquisition cost
- Indicates the return on investment for acquiring a customer
- Healthy ratio: Typically 3:1 or higher

#### Payback Period
- Time required to recover the customer acquisition cost
- CAC divided by monthly contribution margin per customer

#### Margin per Unit
- Contribution margin expressed as amount or percentage

## Unit Economics Process

### 1. Preparation
- Clearly define what constitutes a "unit" (customer, transaction, product, etc.)
- Identify hypotheses about revenue sources and cost structure
- Prepare unit economics templates

### 2. Revenue Analysis

#### Revenue Streams
- Identify all sources of revenue from a single unit
- Determine pricing for each revenue stream
- Calculate frequency of each revenue stream per unit

#### Revenue Calculation
- For each revenue stream: price × frequency
- Sum all revenue streams for total revenue per unit
- Adjust for known discounts, refunds, or revenue sharing

### 3. Cost Analysis

#### Direct Variable Costs
- List all costs that vary directly with each unit
- Determine cost per unit for each variable cost
- Sum for total variable cost per unit

#### Semi-Variable Costs
- Identify costs with both fixed and variable components
- Estimate the variable portion per unit

#### Acquisition Costs (if including in unit economics)
- Calculate sales and marketing costs attributable to acquiring one unit
- Include onboarding and implementation costs if direct

### 4. Contribution Margin Calculation

#### Gross Margin
- Revenue per unit minus direct costs per unit

#### Contribution Margin
- Revenue per unit minus all variable costs per unit

### 5. Lifetime Value Calculation

#### Customer Lifespan
- Estimate average customer retention period
- Use cohort analysis if available

#### Revenue and Margin Projection
- Project monthly/annual revenue per customer
- Apply gross margin to get profit per period
- Discount future profits to present value

### 6. Ratio Analysis

#### LTV:CAC
- Divide LTV by CAC

#### Payback Period
- Divide CAC by monthly contribution margin per customer

#### Margin Percentage
- Divide contribution margin by revenue per unit

## Evidence Collection

- Record revenue sources with pricing and frequency
- Document cost items with amounts and variability classification
- Capture assumptions about customer lifespan and retention
- Note sources for all data (customer interviews, pricing tests, vendor quotes, etc.)
- Record calculations step by step for transparency

## Output Templates

See `templates/unit-economics-canvas.md` for a standard output format.
See `templates/ltv-cac-calculation.md` for calculating LTV and CAC ratios.

## Quality Gates

- [ ] Unit of analysis is clearly defined and appropriate
- [ ] All direct revenue streams from the unit are identified
- [ ] All direct variable costs are identified and quantified
- [ ] Revenue and cost calculations are documented step by step
- [ ] Contribution margin is calculated correctly
- [ ] LTV and CAC are calculated if relevant to the unit
- [ ] Key ratios are calculated and interpreted

## References

See `references/` for:
- unit-definition-guide.md
- revenue-analysis-framework.md
- cost-analysis-framework.md
- ltv-calculation-methods.md
- cac-calculation-methods.md
- unit-economics-tools.md

## Dependencies

- No external tools required
- Works best after pricing strategy and value proposition validation
- Can be combined with financial modeling, cohort analysis, and pricing testing

## Contributing

Improvements to this skill should:
- Maintain focus on per-unit analysis of revenues and costs
- Preserve the emphasis on direct, attributable costs
- Include techniques for calculating LTV and CAC
- Be tested with real unit economics analysis
---

## Skill Overview

The unit economics skill enables practitioners to analyze the direct revenues and costs associated with delivering a single unit of a venture's product or service. Unlike aggregate financial projections, this approach focuses on the profitability of each individual transaction or customer, providing critical insight into the venture's scalability, sustainability, and potential for profitability.

## Key Differentiators

- Focuses on the individual unit (customer, transaction, product) rather than aggregate totals
- Identifies and quantifies all direct costs attributable to each unit
- Calculates contribution margin to understand unit profitability
- Computes lifetime value (LTV) and customer acquisition cost (CAC) when appropriate
- Calculates key ratios (LTV:CAC, payback period) to assess venture viability

## Common Applications

- Assessing the viability of a pricing strategy
- Determining whether a venture can be profitable at scale
- Identifying opportunities to reduce costs or increase revenue per unit
- Informing decisions about sales and marketing spend
- Building investor-ready financial models

## Success Indicators

After applying this skill, you should be able to:
- Define the appropriate unit of analysis for the venture
- Identify all revenue streams associated with a single unit
- Identify all direct costs associated with delivering a single unit
- Calculate revenue per unit, cost per unit, and contribution margin
- Calculate lifetime value (LTV) and customer acquisition cost (CAC) if applicable
- Compute key ratios such as LTV:CAC and payback period
- Interpret unit economics to assess venture viability and scalability

## Anti-Patterns to Avoid

- Focusing only on revenue and ignoring costs
- Including fixed costs that are not attributable to individual units
- Using hypothetical or unverified pricing and cost data
- Not defining what constitutes a "unit" clearly
- Failing to adjust for discounts, refunds, or revenue sharing
- Overlooking semi-variable costs that have a per-unit component
- Calculating LTV without considering customer retention and churn
- Ignoring the time value of money in LTC calculations

## Next Steps

After completing unit economics analysis, consider:
- Building financial models based on unit economics projections
- Testing different pricing strategies through unit economics
- Identifying cost optimization opportunities
- Determining viable customer acquisition strategies based on LTV:CAC
- Sharing unit economics with the venture team and advisors
EOF