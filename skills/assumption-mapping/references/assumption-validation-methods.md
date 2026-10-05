# Assumption Validation Methods

## Overview

Once assumptions have been identified and prioritized, we need to select appropriate methods to validate or invalidate them. This reference provides a toolkit of validation techniques organized by assumption type and domain, helping teams choose the most effective and efficient approach for each assumption.

## Validation Methods by Domain

### 1. Desirability Assumptions

#### Customer Problem & Pain
- **Customer Interviews**: Open-ended discovery of problem experiences
- **Problem Interviews**: Focused on specific problem scenarios
- **Diary Studies**: Tracking problem occurrence over time
- **Observational Research**: Watching problem context in natural settings
- **Social Listening**: Monitoring online discussions about problems
- **Review Mining**: Analyzing customer reviews and feedback

#### Customer Desire & Willingness to Pay
- **Price Sensitivity Tests**: Van Westendorp, Gabor-Granger, conjoint analysis
- **Purchase Intent Surveys**: Measuring stated likelihood to buy
- **Pre-order Campaigns**: Measuring actual purchase commitment
- **Landing Page Tests**: Measuring sign-ups or click-throughs
- **Fake Door Tests**: Measuring interest through action (not just words)
- **Conjoint Analysis**: Understanding trade-offs between features and price

#### Solution Appeal & Resonance
- **Concept Testing**: Presenting solution concepts for feedback
- **Preference Testing**: Comparing different solution approaches
- **Message Testing**: Testing different value propositions and messaging
- **Prototype Feedback**: Getting reactions to low-fidelity prototypes
- **A/B Testing**: Comparing different solution variants

### 2. Viability Assumptions

#### Revenue Model & Pricing
- **Price Experiments**: Actual pricing tests with real customers
- **Revenue Projections**: Financial modeling based on assumptions
- **Competitive Pricing Analysis**: Benchmarking against similar offerings
- **Subscription Model Tests**: Testing different pricing tiers and structures
- **Value-based Pricing**: Aligning price with quantified customer value

#### Cost Structure & Profitability
- **Cost Estimation**: Bottom-up costing of resources and expenses
- **Benchmarking**: Comparing to similar businesses or industry averages
- **Supplier Quotes**: Getting actual pricing for materials/services
- **Resource Planning**: Detailed planning of personnel and equipment needs
- **Break-even Analysis**: Calculating volume needed to cover costs

#### Channel Effectiveness & Scalability
- **Channel Tests**: Small-scale experiments in different acquisition channels
- **CAC Measurement**: Tracking actual customer acquisition costs
- **Channel Partner Interviews**: Understanding partner economics and motivations
- **Conversion Funnel Analysis**: Measuring drop-off at each stage
- **LTV:CAC Ratio**: Comparing lifetime value to acquisition cost

#### Competitive Positioning & Defensibility
- **Competitive Analysis**: Systematic evaluation of competitors
- **Differentiation Testing**: Measuring perceived uniqueness and value
- **IP Landscape Analysis**: Understanding patents, trademarks, and protections
- **Switching Cost Analysis**: Understanding barriers to customer switching
- **Moat Assessment**: Evaluating sustainable competitive advantages

#### Regulatory & Legal Considerations
- **Regulatory Research**: Investigating applicable laws and regulations
- **Compliance Consulting**: Getting expert advice on requirements
- **Licensing Investigation**: Understanding needed permits and approvals
- **Liability Assessment**: Evaluating potential legal risks and exposures
- **Industry Standard Review**: Understanding required certifications or standards

### 3. Feasibility Assumptions

#### Technical Feasibility & Complexity
- **Proof of Concept**: Building minimal working versions of core technology
- **Technical Spikes**: Time-boxed exploration of specific technical questions
- **Architecture Review**: Expert evaluation of technical approach
- **Prototyping**: Building working models to test technical approaches
- **Technology Benchmarks**: Measuring performance against requirements

#### Resource & Skill Availability
- **Skills Inventory**: Mapping team capabilities against needs
- **Hiring Feasibility**: Assessing difficulty and cost of hiring needed skills
- **Training Assessment**: Evaluating time and cost to upskill team
- **Outsourcing Evaluation**: Assessing viability of external resources
- **Partnership Exploration**: Investigating potential collaborations

#### Time to Develop & Launch
- **Project Planning**: Detailed breakdown of tasks and dependencies
- **Reference Class Forecasting**: Comparing to similar projects
- **Buffer Analysis**: Adding contingency time for unknowns
- **Milestone Tracking**: Setting and monitoring intermediate goals
- **Resource Leveling**: Adjusting schedule based on resource constraints

#### Dependencies & External Factors
- **Dependency Mapping**: Identifying and documenting all dependencies
- **Supplier Reliability**: Assessing track record and capacity of suppliers
- **Platform Risk Analysis**: Evaluating risks of building on third-party platforms
- **Integration Testing**: Testing connections with external systems
- **Contingency Planning**: Developing backup plans for dependency failures

#### Scalability & Performance
- **Load Testing**: Testing system behavior under expected and peak loads
- **Performance Benchmarks**: Measuring speed, throughput, and response times
- **Architecture Review**: Evaluating design for scalability bottlenecks
- **Technology Selection**: Choosing technologies with appropriate scaling characteristics
- **Pilot Testing**: Running small-scale versions to identify scaling issues

## Choosing the Right Method

### Criteria for Method Selection

1. **Validity**: Does the method actually test the assumption?
2. **Reliability**: Will it produce consistent results under similar conditions?
3. **Efficiency**: What is the cost (time, money, effort) per unit of learning?
4. **Ethics**: Does it respect participants and follow ethical guidelines?
5. **Actionability**: Will results clearly inform next steps?

### Validation Method Decision Tree

1. **Is the assumption about customer behavior or desires?**
   - Yes → Consider interviews, experiments, tests, or observation
   - No → Continue to next question

2. **Is the assumption about business model or economics?**
   - Yes → Consider financial modeling, tests, or benchmarking
   - No → Continue to next question

3. **Is the assumption about technical feasibility or resources?**
   - Yes → Consider prototyping, spikes, or expert consultation
   - No → Continue to next question

4. **Can we test with actual behavior rather than stated intent?**
   - Yes → Prioritize methods that measure actions (purchases, usage, etc.)
   - No → Consider surveys, interviews, or expert opinion

5. **Is the assumption time-sensitive or likely to change?**
   - Yes → Favor faster, lighter-weight methods
   - No → Can invest in more rigorous or comprehensive methods

## Hybrid Validation Approaches

### Triangulation
- Use multiple methods to validate the same assumption
- Combine qualitative and quantitative approaches
- Use different sources or populations for confirmation

### Sequential Validation
- Start with low-cost, fast methods to reduce uncertainty
- Follow up with higher-cost methods for remaining uncertainty
- Stop validation when confidence reaches acceptable threshold

### Continuous Validation
- Build validation into ongoing operations and customer interactions
- Use metrics and analytics to monitor assumptions over time
- Update assumptions as new data becomes available

## Evidence Standards

### Levels of Evidence

**Level 1: Strongest**
- Randomized controlled experiments
- Actual purchasing behavior
- Direct observation of behavior
- Quantitative data with statistical significance

**Level 2: Strong**
- Quasi-experimental designs
- Consistent qualitative patterns across multiple sources
- Pre-post measurements with controls
- Expert validation with clear methodology

**Level 3: Moderate**
- Single-method qualitative or quantitative studies
- Expert opinion with clear reasoning
- Case studies or examples
- Correlational data with controls for confounding factors

**Level 4: Weakest**
- Anecdotal evidence
- Unsupported expert opinion
- Theoretical reasoning without empirical support
- Logical deduction without empirical testing

## Output Templates

See `templates/assumption-validation-plan.md` for a standard output format.

## Quality Gates

- [ ] Each high-priority assumption has at least one validation method
- [ ] Methods are appropriate to the assumption domain and type
- [ ] Validity, reliability, and efficiency considerations are documented
- [ ] Evidence standards are specified for each validation method
- [ ] Validation efforts are sequenced to maximize learning efficiency

## References

See `references/` for:
- validation-method-selection-guide.md
- evidence-standards-framework.md
- validation-effort-estimation.md

## Dependencies

- No external tools required
- Can be combined with experiment design and hypothesis framing
- Works with both qualitative and quantitative approaches

## Contributing

Improvements to this skill should:
- Maintain focus on evidence-based validation
- Preserve the domain-organized method toolkit
- Include practical guidance for choosing validation methods
- Be tested with real assumption validation campaigns
---

## Skill Overview

The assumption validation methods skill provides practitioners with a comprehensive toolkit for testing the assumptions that underlie venture hypotheses. Unlike random or intuition-based validation efforts, this approach matches specific validation techniques to assumption types and domains, ensuring that teams use the most effective and efficient methods to reduce uncertainty.

## Key Differentiators

- Organizes validation methods by assumption domain (desirability, viability, feasibility)
- Provides specific techniques for different assumption types within each domain
- Includes criteria for selecting the most appropriate validation method
- Distinguishes between methods that test behavior vs. opinion
- Provides evidence standards for evaluating validation results

## Common Applications

- Planning validation experiments for prioritized assumptions
- Selecting appropriate methods for customer interviews and tests
- Designing mixed-methods validation approaches
- Determining when to use quantitative vs. qualitative methods
- Building validation roadmaps with appropriate method selection

## Success Indicators

After applying this skill, you should be able to:
- List validation methods appropriate for each assumption domain
- Select validation methods based on validity, reliability, and efficiency
- Design validation plans that match methods to assumption types
- Specify evidence standards for different validation approaches
- Sequence validation efforts to maximize learning per unit of effort

## Anti-Patterns to Avoid

- Using the same validation method for all assumptions regardless of type
- Failing to consider whether a method actually tests the assumption
- Ignoring the cost-efficiency trade-off of validation methods
- Not specifying what evidence would count as validation or invalidation
- Using validation methods that cannot produce actionable results

## Next Steps

After completing assumption validation methods selection, consider:
- Creating detailed validation plans for each high-priority assumption
- Designing experiments that implement the chosen validation methods
- Building hypothesis frames based on validated assumptions
- Developing success criteria and decision rules for validation outcomes
- Sharing the validation method selection with the venture team
