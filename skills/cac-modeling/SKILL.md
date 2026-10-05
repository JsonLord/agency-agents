---
name: cac-modeling
description: A reusable skill for modeling and optimizing customer acquisition costs to ensure profitable and scalable growth.
version: 1.0.0
---

# Customer Acquisition Cost (CAC) Modeling Skill

This skill provides a structured approach to modeling, measuring, and optimizing customer acquisition costs. Unlike guessing or using industry averages, this skill emphasizes calculating actual CAC from venture-specific data, understanding the components that contribute to CAC, and identifying ways to reduce CAC while maintaining or improving customer quality.

## When to Use This Skill

- After developing pricing and distribution strategies
- When building financial models and projections
- To assess the viability of customer acquisition strategies
- Before scaling marketing and sales efforts
- To identify opportunities to reduce acquisition costs

## Core Principles

1. **CAC is not just marketing spend** - Include all costs associated with acquiring a customer
2. **Cohort-based calculation** - Measure CAC for specific groups of customers acquired in a time period
3. **Include fully loaded costs** - Consider both direct and indirect costs attributable to acquisition
4. **Compare to customer lifetime value (LTV)** - Assess viability through LTV:CAC ratio
5. **Continuously measure and optimize** - CAC changes over time; track and improve

## CAC Components Framework

### 1. Direct Marketing Costs
- Advertising spend (PPC, social, display, etc.)
- Content creation and distribution
- Event sponsorships and participation
- Marketing tools and software
- Agency and contractor fees

### 2. Sales Costs
- Salaries and commissions for sales team
- Sales tools and software (CRM, etc.)
- Sales training and enablement
- Travel and entertainment for sales

### 3. Overhead Costs Attributable to Acquisition
- Portion of marketing and sales leadership salaries
- Shared tools and software (marketing automation, analytics)
- Office space and utilities for marketing/sales teams
- General and administrative overhead allocation

### 4. Technology and Platform Costs
- Website and landing page development
- Marketing automation platforms
- Analytics and tracking tools
- Conversion rate optimization tools

### 5. Customer Onboarding and Implementation Costs (if part of acquisition)
- Account setup and configuration
- Training and education
- Implementation services
- Initial support and customer success effort

## CAC Calculation Process

### 1. Preparation
- Clearly define what constitutes a "customer" for CAC purposes
- Identify the time period for measurement (monthly, quarterly, etc.)
- Prepare CAC calculation templates

### 2. Cost Collection

#### Direct Costs
- Gather all marketing and sales invoices and receipts for the period
- Break down costs by category (advertising, sales, tools, etc.)

#### Indirect Costs
- Determine allocation methodology for shared costs
- Calculate the portion attributable to customer acquisition

#### Fully Loaded CAC
- Sum of all direct and indirect costs attributable to acquisition

### 3. Customer Count

#### Paying Customers
- Count only customers who have made a payment
- Include upgrades and expansions from existing customers? (Typically not for CAC)
- Trials and freemium users who convert to paying

#### New Customers
- Focus on newly acquired customers in the period
- Exclude renewals and repeat purchases from existing customers

### 4. CAC Calculation

#### Simple CAC
- Total marketing and sales spend ÷ Number of new customers acquired

#### Fully Loaded CAC
- Total acquisition-related costs ÷ Number of new customers acquired

#### Cohort-Based CAC
- Calculate CAC for specific cohorts (by channel, campaign, time period, etc.)

### 5. CAC Analysis

#### By Channel
- Calculate CAC for each acquisition channel
- Identify most and least expensive channels

#### By Campaign
- Calculate CAC for specific marketing campaigns
- Identify high-performing and underperforming campaigns

#### By Customer Segment
- Calculate CAC for different customer segments
- Identify which segments are most/least expensive to acquire

#### Over Time
- Track CAC trends month-over-month or quarter-over-quarter
- Identify seasonality or trends

## Evidence Collection

- Record all marketing and sales costs with dates and descriptions
- Document cost allocation methodologies for indirect costs
- Capture customer acquisition data with sources and dates
- Note any adjustments made for trials, upgrades, etc.
- Save detailed breakdowns by channel, campaign, and segment

## Output Templates

See `templates/cac-calculation.md` for a standard output format.
See `templates/cac-by-channel.md` for calculating CAC by acquisition channel.
See `templates/ltv-cac-ratio.md` for calculating LTV:CAC ratio.

## Quality Gates

- [ ] All costs associated with customer acquisition are considered
- [ ] Costs are broken down by category (marketing, sales, overhead, technology)
- [ ] Customer count is clearly defined (new paying customers)
- [ ] CAC is calculated for the venture as a whole
- [ ] CAC is calculated by channel, campaign, or segment if relevant
- [ ] CAC is compared to LTV to assess viability

## References

See `references/` for:
- cac-components-guide.md
- cac-calculation-methods.md
- cac-by-channel-analysis.md
- cac-optimization-techniques.md
- ltv-cac-framework.md
- cac-modeling-tools.md

## Dependencies

- No external tools required
- Works best after pricing strategy, distribution analysis, and unit economics
- Can be combined with financial modeling, cohort analysis, and LTV calculation

## Contributing

Improvements to this skill should:
- Maintain focus on fully loaded, customer-specific CAC calculation
- Preserve the emphasis on cohort-based and component-based analysis
- Include techniques for CAC reduction and optimization
- Be tested with real CAC modeling efforts
---

## Skill Overview

The CAC modeling skill enables practitioners to model, measure, and optimize customer acquisition costs to ensure profitable and scalable growth. Unlike using industry averages or guessing, this approach emphasizes calculating actual CAC from venture-specific data, understanding the components that contribute to CAC, and identifying ways to reduce CAC while maintaining or improving customer quality.

## Key Differentiators

- Focuses on fully loaded CAC including direct and indirect costs
- Uses cohort-based calculation for accuracy and comparability
- Breaks down CAC by component, channel, campaign, and customer segment
- Compares CAC to customer lifetime value (LTV) to assess viability
- Provides frameworks for identifying CAC reduction opportunities

## Common Applications

- Calculating actual CAC for a venture
- Assessing the viability of customer acquisition strategies
- Identifying the most and least expensive acquisition channels
- Optimizing marketing and sales spend based on CAC data
- Building investor-ready financial models

## Success Indicators

After applying this skill, you should be able to:
- Identify all costs associated with customer acquisition
- Calculate fully loaded CAC for the venture
- Calculate CAC by acquisition channel, campaign, and customer segment
- Compare CAC to LTV to assess venture viability
- Identify opportunities to reduce CAC while maintaining customer quality

## Anti-Patterns to Avoid

- Focusing only on advertising spend and ignoring other costs
- Including costs not attributable to customer acquisition (e.g., product development)
- Using hypothetical or unverified cost data
- Not defining what constitutes a "customer" clearly
- Failing to adjust for upgrades, expansions, or repeat purchases
- Overlooking indirect costs that contribute to acquisition
- Not comparing CAC to LTV to assess viability

## Next Steps

After completing CAC modeling, consider:
- Building financial models based on CAC and LTV projections
- Testing different acquisition strategies through CAC analysis
- Identifying cost optimization opportunities in marketing and sales
- Determining viable scaling strategies based on LTV:CAC
- Sharing CAC modeling with the venture team and advisors
EOF