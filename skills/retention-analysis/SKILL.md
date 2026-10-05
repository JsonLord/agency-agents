---
name: retention-analysis
description: A reusable skill for analyzing and improving customer retention and reducing churn.
version: 1.0.0
---

# Retention Analysis Skill

This skill provides a structured approach to analyzing customer retention, identifying churn reasons, and developing strategies to improve customer longevity. Unlike focusing solely on acquisition, this skill emphasizes understanding why customers leave and how to keep them longer, which is critical for sustainable growth.

## When to Use This Skill

- After acquiring initial customers
- When building financial models and projections
- To assess the viability of the business model through retention metrics
- Before scaling customer acquisition efforts
- To identify opportunities to improve product-market fit

## Core Principles

1. **Retention is cheaper than acquisition** - Keeping existing customers is typically more cost-effective than acquiring new ones
2. **Cohort-based analysis** - Track groups of customers who started at the same time to see how retention changes over time
3. **Understand why customers leave** - Churn is rarely random; there are usually identifiable reasons
4. **Retention is a product problem** - Poor retention often indicates product-market fit issues, not just customer service problems
5. **Segment your analysis** - Different customer segments may have different retention patterns

## Retention Framework

### 1. Retention Rate Calculation

#### Definition
- The percentage of customers who continue to use the product/service over a given time period

#### Calculation
- (Number of customers at end of period - New customers acquired during period) ÷ Number of customers at start of period

#### Cohort Retention
- Track a cohort of customers who signed up in the same week/month
- Measure what percentage of that cohort is still active after 1, 2, 3, etc. months

### 2. Churn Rate Calculation

#### Definition
- The percentage of customers who stop using the product/service over a given time period

#### Calculation
- 1 - Retention rate
- Or: Customers lost during period ÷ Customers at start of period

### 3. Retention Curve Analysis

#### Shape of the Curve
- Steep drop early: Onboarding or first-experience issues
- Gradual decline: Ongoing value or competitive issues
- Plateaus: Strong product-market fit for a segment

#### Key Points
- Day 1, Day 7, Day 30 retention: Critical early retention points
- Monthly, quarterly, annual retention: Longer-term retention

### 4. Churn Analysis Framework

#### 1. Who is churning?
- Customer demographics, firmographics, behavior
- Acquisition channel, campaign, or source
- Customer segment or persona

#### 2. When are they churning?
- Time since signup (days, weeks, months)
- Specific events or triggers
- Usage patterns before churn

#### 3. Why are they churning?
- Product-related: Missing features, bugs, poor performance
- Price-related: Too expensive, not worth the cost
- Competitor-related: Found a better alternative
- Usage-related: Not using enough, lost interest
- Circumstance-related: Business changed, no longer needed

#### 4. What are they doing instead?
- Switching to a competitor
- Going back to a previous solution
- Using a workaround or manual process
- Doing nothing (non-consumption)

### 5. Retention Levers

#### Onboarding & Activation
- Improve first-time user experience
- Increase activation rates (key actions that predict retention)
- Reduce time to value

#### Product Value
- Increase core product value
- Add features that address retention reasons
- Improve performance, reliability, and usability

#### Communication & Engagement
- Improve onboarding and educational emails
- Increase product communication and updates
- Build habits and routines around product use

#### Pricing & Value Alignment
- Ensure pricing matches perceived value
- Offer flexible pricing options
- Provide clear ROI documentation

#### Customer Success & Support
- Improve response times and resolution quality
- Provide proactive customer success outreach
- Build self-service resources and knowledge base

## Retention Analysis Process

### 1. Preparation
- Clearly define what constitutes an "active" or "retained" customer
- Identify hypotheses about retention and churn drivers
- Prepare retention analysis templates

### 2. Data Collection

#### Customer Data
- Signup dates and dates of last activity
- Usage frequency and depth
- Customer attributes (demographics, firmographics, etc.)
- Acquisition source and campaign
- Payment plan and revenue

#### Churn Data
- Exact churn date or date of last activity
- Reason for churn (if collected via survey or interview)
- Final usage patterns

#### Feedback Data
- Exit survey responses
- Customer interviews with churned customers
- Support ticket analysis for churned customers

### 3. Cohort Analysis

#### Cohort Definition
- Define cohorts by signup week or month
- Optionally segment by acquisition channel, customer type, etc.

#### Retention Calculation
- For each cohort, calculate what percentage is still active after each time period
- Visualize as a retention curve

#### Cohort Comparison
- Compare retention across cohorts to see trends
- Compare retention across segments to identify high/low performers

### 4. Churn Analysis

#### Timing Analysis
- Plot churn by days/weeks/months since signup
- Identify peaks in churn (e.g., after free trial ends, after first month)

#### Reason Analysis
- Categorize churn reasons from exit surveys and interviews
- Calculate percentage of churn attributable to each reason

#### Usage Analysis
- Compare usage patterns of retained vs. churned customers
- Identify leading indicators of churn (decreasing usage, lack of key features)

#### Segmentation Analysis
- Calculate retention rates by customer segment
- Identify which segments retain best and worst

### 5. Retention Strategy Development

#### Prioritize Levers
- Focus on retention levers that address the biggest churn reasons
- Consider effort, impact, and time to implement

#### Experiment Planning
- Design experiments to test retention improvements
- Define success metrics (retention rate, churn rate, activation rate)

#### Prediction Modeling
- Build simple models to predict churn risk
- Use to target retention interventions

## Evidence Collection

- Record customer signup and activity dates with timestamps
- Capture customer attributes and acquisition source
- Document churn dates and reasons
- Save exit survey responses and interview transcripts
- Record usage metrics and feature adoption
- Note any changes to the product or pricing over time

## Output Templates

See `templates/retention-calculation.md` for calculating retention and churn rates.
See `templates/cohort-retention-chart.md` for visualizing cohort retention.
See `templates/churn-reasons-analysis.md` for analyzing churn reasons.
See `templates/retention-strategy.md` for developing retention strategies.

## Quality Gates

- [ ] Retention and churn rates are calculated correctly
- [ ] Cohort analysis is performed and visualized
- [ ] Churn reasons are identified and categorized
- [ ] Retention analysis is segmented by relevant customer attributes
- [ ] Retention strategies are developed based on analysis

## References

See `references/` for:
- retention-calculation-guide.md
- cohort-analysis-framework.md
- churn-reasons-analysis.md
- retention-levers.md
- retention-analysis-tools.md

## Dependencies

- No external tools required
- Works best after acquiring initial customers and collecting usage data
- Can be combined with unit economics, LTV calculation, and product analytics

## Contributing

Improvements to this skill should:
- Maintain focus on cohort-based retention analysis
- Preserve the emphasis on understanding why customers leave
- Include techniques for identifying and acting on retention levers
- Be tested with real retention analysis efforts
---

## Skill Overview

The retention analysis skill enables practitioners to analyze customer retention, identify churn reasons, and develop strategies to improve customer longevity. Unlike focusing solely on acquisition metrics, this approach emphasizes understanding why customers leave and how to keep them longer, which is critical for sustainable growth and profitability.

## Key Differentiators

- Focuses on cohort-based retention tracking over time
- Analyzes churn reasons to identify root causes
- Segments retention analysis by customer attributes and acquisition source
- Evaluates retention levers across onboarding, product value, communication, pricing, and customer success
- Develops data-driven strategies to improve retention and reduce churn

## Common Applications

- Calculating and tracking retention and churn rates
- Performing cohort analysis to understand retention trends
- Identifying why customers churn through exit surveys and interviews
- Developing retention strategies to improve customer longevity
- Building investor-ready retention metrics and projections

## Success Indicators

After applying this skill, you should be able to:
- Calculate retention and churn rates correctly
- Perform cohort analysis and visualize retention curves
- Identify and categorize churn reasons from customer feedback
- Segment retention analysis by customer attributes and acquisition source
- Develop retention strategies based on analysis of churn reasons and retention levers

## Anti-Patterns to Avoid

- Focusing only on acquisition metrics while ignoring retention
- Not defining what constitutes an "active" or "retained" customer
- Failing to perform cohort-based analysis
- Overlooking the importance of understanding why customers leave
- Not segmenting retention analysis to identify high/low performing groups
- Developing retention strategies without data or analysis

## Next Steps

After completing retention analysis, consider:
- Building financial models based on retention and LTV projections
- Testing retention improvement experiments
- Identifying product improvements based on churn reasons
- Sharing retention analysis with the venture team and advisors
EOF