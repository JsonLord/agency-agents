---
name: experiment-design
description: A reusable skill for designing and structuring experiments to test venture hypotheses and assumptions.
version: 1.0.0
---

# Experiment Design Skill

This skill provides a structured approach to creating rigorous, ethical experiments that generate clear evidence to validate or invalidate venture hypotheses and assumptions. Unlike casual testing or prototyping, this skill emphasizes deliberate experimental design with proper controls, measurement, and interpretation.

## When to Use This Skill

- After hypothesis framing and before validation
- When testing specific assumptions or hypotheses
- To move beyond opinion and gather behavioral evidence
- When resources are limited and learning efficiency is important
- To ensure experiments produce actionable, interpretable results

## Core Principles

1. **Start with hypotheses, not methods** - Begin with what we want to test, not how we want to test it
2. **Design for falsifiability** - Experiments should be capable of disproving the hypothesis
3. **Control for confounding variables** - Isolate the effect of what we're testing
4. **Measure actual behavior, not just intent** - Focus on what people do, not what they say they'll do
5. **Plan for both outcomes** - Prepare for hypothesis confirmation and contradiction
6. **Optimize for learning efficiency** - Maximize insight per unit of time, money, and effort

## Experiment Types

### 1. Discovery Experiments
- **Purpose**: Explore problem spaces and generate hypotheses
- **Examples**: Customer interviews, observational studies, social listening
- **Strengths**: Rich qualitative insights, hypothesis generation
- **Limitations**: Limited generalizability, potential for bias

### 2. Validation Experiments
- **Purpose**: Test specific hypotheses and assumptions
- **Examples**: Landing page tests, concierge tests, prototype experiments
- **Strengths**: Causal inference, behavioral evidence, decision-making support
- **Limitations**: Requires more resources, complex to design properly

### 3. Optimization Experiments
- **Purpose**: Improve existing solutions based on evidence
- **Examples**: A/B tests, conversion rate optimization, feature experiments
- **Strengths**: Continuous improvement, data-driven refinement
- **Limitations**: Requires existing traffic or user base

## Experiment Design Process

### 1. Preparation
- Clearly state the hypothesis or assumption to test
- Review existing evidence and insights
- Identify constraints (time, budget, skills, ethics)
- Prepare experiment design templates

### 2. Experimental Variables

#### Independent Variable (IV)
- What we are manipulating or changing
- The "cause" in our cause-effect relationship
- Should be specific and manipulable
- Examples: "Price point ($10 vs $20 vs $30)", "Landing page version A vs B", "Onboarding flow with vs without tutorial"

#### Dependent Variable (DV)
- What we are measuring as the outcome
- The "effect" in our cause-effect relationship
- Should be observable and measurable
- Examples: "Conversion rate (sign-ups/visitors)", "Task completion time", "Number of features used"

#### Control Variables
- Factors we hold constant to isolate the IV effect
- Should be relevant and controllable
- Examples: "Same target audience", "Same time of day", "Same device type"

#### Confounding Variables
- Factors that could affect both IV and DV
- Should be measured, controlled, or accounted for
- Examples: "Seasonality", "External events", "User experience level"

### 3. Experimental Design

#### Between-Subjects Design
- Different participants experience different IV levels
- Good for testing irreversible changes
- Requires more participants
- Controls for learning and carryover effects

#### Within-Subjects Design
- Same participants experience all IV levels
- Requires fewer participants
- Controls for individual differences
- Risks learning, fatigue, and carryover effects

#### Mixed Design
- Combines between and within-subjects elements
- Useful for complex research questions

#### Factorial Design
- Tests multiple IVs and their interactions
- Efficient for studying multiple factors
- Reveals interaction effects between variables

### 4. Control Groups

#### No Treatment Control
- Participants receive neither the intervention nor a placebo
- Measures baseline behavior
- Appropriate when testing if intervention has any effect

#### Placebo Control
- Participants receive an inert or sham intervention
- Controls for placebo effects and expectations
- Appropriate when psychological effects are possible

#### Active Control
- Participants receive an existing or standard intervention
- Compares new intervention to current best practice
- Appropriate when establishing superiority or non-inferiority

#### Historical Control
- Uses data from previous periods or similar groups
- Useful when concurrent control is impractical
- Requires careful matching and adjustment for differences

### 5. Measurement Plan

#### What to Measure
- Primary outcome: Direct test of the hypothesis
- Secondary outcomes: Additional measures for context and understanding
- Process measures: How the experiment was implemented
- Balancing measures: Check for unintended consequences or side effects

#### How to Measure
- Self-report: Surveys, interviews, questionnaires
- Observation: Direct watching or recording of behavior
- Performance: Task completion, accuracy, speed
- Physiological: Heart rate, skin conductance, eye tracking
- Behavioral: Clicks, visits, purchases, usage patterns
- Archival: Existing records, logs, databases

#### When to Measure
- Baseline: Before intervention begins
- During: Throughout the intervention period
- Post: Immediately after intervention ends
- Follow-up: Some time after intervention ends
- Continuous: Ongoing throughout the experiment period

### 6. Sampling and Participants

#### Target Population
- Who the hypothesis is about
- Should match the population in the hypothesis statement

#### Sampling Frame
- Available list or method for accessing target population
- Should ideally include all members of target population

#### Sampling Method
- Probability: Random selection from sampling frame
- Non-probability: Convenience, purposive, quota, snowball sampling
- Choose based on resources, goals, and population access

#### Sample Size Considerations
- Statistical power: Ability to detect an effect if one exists
- Effect size: Expected magnitude of the difference
- Variability: Expected spread in the measurements
- Significance level: Probability of false positive (typically 0.05)
- Practical constraints: Time, budget, and access limitations

### 7. Procedure

#### Preparation Phase
- Recruit and screen participants
- Prepare materials and environment
- Obtain informed consent
- Randomize or assign to conditions

#### Intervention Phase
- Administer independent variable levels
- Implement control conditions
- Monitor for adverse events or issues
- Collect process data

#### Measurement Phase
- Administer dependent variable measures
- Collect outcome and process data
- Ensure measurement consistency and reliability

#### Wrap-up Phase
- Debrief participants (when appropriate)
- Collect final data and feedback
- Compensate or thank participants
- Clean and restore environment

### 8. Ethics

#### Informed Consent
- Participants must understand what they're agreeing to
- Must be voluntary and without coercion
- Should include purpose, procedures, risks, and benefits
- Must be obtained before any procedures begin

#### Privacy and Confidentiality
- Protect participant identities and personal data
- Anonymize data when possible
- Securely store and transmit data
- Follow applicable data protection regulations

#### Harm Minimization
- Minimize discomfort, inconvenience, or risk
- Provide alternatives when possible
- Monitor for adverse effects
- Have procedures for handling problems

#### Debriefing
- Explain the true purpose of the study (if deception was used)
- Provide information about results and implications
- Offer resources or referrals when appropriate
- Address any misunderstandings or concerns

## Evidence Collection

- Record hypotheses and assumptions being tested
- Document experimental design choices and rationale
- Capture procedural details and any deviations from plan
- Collect both quantitative and qualitative data
- Label data as primary (directly tests hypothesis) or secondary (contextual)
- Track changes to experimental design over time

## Output Templates

See `templates/experiment-spec.md` for a standard output format.

## Quality Gates

- [ ] Experiment starts with clear hypothesis or assumption
- [ ] Independent and dependent variables are clearly defined
- [ ] Experimental design is appropriate to the research question
- [ ] Control groups are used when necessary to isolate effects
- [ ] Measurement plan specifies what, how, and when to measure
- [ ] Sampling and participant considerations are documented
- [ ] Experiment procedure is detailed and replicable
- [ ] Ethics considerations are addressed (consent, privacy, harm minimization)
- [ ] Success criteria are defined for interpreting results

## References

See `references/` for:
- hypothesis-to-experiment-guide.md
- experimental-design-checklist.md
- sampling-methods-guide.md
- measurement-plan-template.md

## Dependencies

- No external tools required
- Works best after hypothesis framing
- Can be combined with validation planning and assumption mapping

## Contributing

Improvements to this skill should:
- Maintain focus on evidence-based experiment design
- Preserve the core principles of hypothesis-driven experimentation
- Include techniques for proper controls and measurement
- Be tested with real experiment design and execution
---

## Skill Overview

The experiment design skill enables practitioners to structure tests of venture hypotheses and assumptions in a way that produces clear, interpretable evidence. Unlike informal testing or prototyping, this approach applies scientific principles of experimental design to venture validation, ensuring that experiments are capable of supporting or refuting hypotheses with confidence.

## Key Differentiators

- Focuses on starting with hypotheses rather than methods
- Requires clear definition of independent and dependent variables
- Emphasizes proper controls to isolate causal effects
- Distinguishes between measuring behavior and measuring intent
- Provides framework for planning both confirmation and contradiction outcomes

## Common Applications

- Testing desirability hypotheses (customer willingness, problem existence)
- Validating viability assumptions (business model, pricing, channels)
- Evaluating feasibility assumptions (technical, resource, timeline)
- Optimizing existing solutions based on evidence
- Building investor-ready validation evidence

## Success Indicators

After applying this skill, you should be able to:
- Design experiments that start with clear hypotheses or assumptions
- Define independent and dependent variables appropriately
- Select experimental designs that match research questions and constraints
- Implement appropriate control groups to isolate effects
- Create measurement plans that specify what, how, and when to measure
- Address sampling, participant, and ethics considerations adequately
- Define success criteria for interpreting experimental results

## Anti-Patterns to Avoid

- Starting with methods rather than hypotheses
- Failing to define what the experiment is actually testing
- Not using controls when needed to isolate effects
- Measuring only stated intent rather than actual behavior
- Ignoring sampling bias or poor participant representation
- Overlooking ethics considerations like informed consent and privacy
- Designing experiments that cannot produce actionable, interpretable results

## Next Steps

After completing experiment design, consider:
- Executing the designed experiments according to plan
- Collecting and analyzing experimental data
- Interpreting results against success criteria
- Updating hypotheses and assumptions based on evidence
- Sharing experiment designs and results with the venture team
