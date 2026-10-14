---
name: pressure-test
description: Pressure-test a hypothesis.
version: 1.0.0
---

# Pressure Test

## Purpose
Pressure-test a hypothesis while keeping Nodepad authoritative for state, scoring, confidence, and qualification.

## Required inputs
A hypothesis, workspace context, known evidence with provenance, and the workflow intent.

## Method
Write a pre-mortem, strongest counter-case, disconfirming observation and cheapest kill test. Important hypotheses require an intentional disconfirmation pass.

## Outputs
A transient analytical artifact containing observations, limitations, evidence gaps, and a recommended next test.

## Quality gates
Every claim links to an input or source; contradictions remain visible; experiments define success and failure criteria.

## Nodepad boundary
Reads context, hypotheses, evidence, and research gaps. May propose evidence, counter-hypotheses, research gaps, or experiments through the gateway. Never writes qualification, authoritative confidence, canonical scores, or graph state.

## Capabilities
Use semantic research capabilities only when external material is needed. Provider results are research material until interpreted into an evidence candidate.

## Failure conditions
Fail visibly on missing provenance, unavailable required providers, unsupported conclusions, or ambiguous success criteria.

## Anti-patterns
Do not discard negative evidence, count correlated reposts as independent sources, serialize credentials, or become a local canonical store.
