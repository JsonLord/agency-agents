"""Pure evaluation helpers; none of these functions mutate canonical state."""
from collections import Counter

FORBIDDEN = {
    "authoritative_confidence",
    "canonical_score",
    "qualification",
    "qualification_band",
}

def analyze_lane(context):
    business_signals = [k for k in ("buyer_role", "budget", "procurement") if context.get(k)]
    consumer_signals = [k for k in ("habit", "frequency", "identity_value") if context.get(k)]
    business,consumer=len(business_signals),len(consumer_signals)
    lane = "b2b" if business > consumer else "b2c" if consumer > business else "mixed"
    b2b=["buyer_user_split", "budget_owner", "switching_cost", "sales_cycle", "roi_threshold"]
    b2c=["frequency", "urgency", "habit", "willingness_to_pay", "retention"]
    checks=b2b if lane=="b2b" else b2c if lane=="b2c" else list(dict.fromkeys(b2b+b2c))
    return {"lane": lane,"signals":{"b2b":business_signals,"b2c":consumer_signals}, "checks": checks, "analytical_only": True}

def map_assumptions(items):
    ranked = [{**item, "priority": item["impact"] * item["uncertainty"]} for item in items]
    ranked.sort(key=lambda x: (-x["priority"], x["statement"]))
    return {"assumptions": ranked, "kill_assumption": ranked[0] if ranked else None}

def pressure_test(hypothesis, assumptions):
    kill = map_assumptions(assumptions)["kill_assumption"]
    return {"hypothesis": hypothesis,
            "pre_mortem": "The venture failed because the highest-impact uncertain assumption was false.",
            "devils_advocate": f"What observable result would refute: {hypothesis}?",
            "kill_assumption": kill,
            "recommended_test": "Run the cheapest behavior-based discriminating test."}

def analyze_evidence(evidence):
    polarities = Counter(item.get("polarity", "unknown") for item in evidence)
    sources = {(item.get("provider") or item.get("source_type", "unknown"), item.get("source_url")) for item in evidence}
    providers = {provider for provider, _ in sources}
    flags = [item.get("id", item.get("source_url")) for item in evidence if item.get("polarity") == "contradicting"]
    direct = sum(item.get("source_type") in {"behavior", "experiment", "interview"} for item in evidence)
    count=max(1,len(evidence)); nowish=sum(bool(x.get("observed_at") or x.get("published_at")) for x in evidence)
    behavioral=sum(x.get("source_type") in {"behavior","experiment"} for x in evidence)
    segment=sum(bool(x.get("segment") or x.get("metadata",{}).get("segment")) for x in evidence)
    dimensions={"directness":direct/count,"recency":nowish/count,"source_independence":min(1,len(providers)/count),"behavioral_strength":behavioral/count,"segment_relevance":segment/count,"contradiction_coverage":sum(polarities[x] for x in ("contradicting","contradiction"))/count,"triangulation":min(1,len(providers)/2)}
    dimensions={k:round(v,3) for k,v in dimensions.items()}; quality=round(sum(dimensions.values())/len(dimensions),3) if evidence else 0.0
    warnings = []
    if len(providers) < 2: warnings.append("single-source concentration")
    if not flags: warnings.append("no contradictory evidence sampled")
    return {"analysis_quality": quality,"quality_dimensions":dimensions, "source_diversity": {"provider_count": len(providers), "source_count": len(sources)},
            "contradiction_flags": flags, "calibration_notes": warnings,
            "evidence_gaps": ["seek behavioral evidence"] if direct == 0 else [], "polarity_counts": dict(polarities)}

def enforce_boundary(payload):
    """Reject canonical Nodepad fields anywhere in an Agency-authored payload.

    Checking recursively is intentional: artifacts and handoffs are still Agency
    output and must not become a back door for writing Nodepad decisions.
    """
    violations = set()

    def visit(value):
        if isinstance(value, dict):
            violations.update(FORBIDDEN.intersection(value))
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(payload)
    if violations:
        raise ValueError(
            f"Agency may not author canonical fields: {sorted(violations)}"
        )
    return payload
