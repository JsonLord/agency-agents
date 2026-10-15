"""Deterministic, non-authoritative customer evidence gate."""
from __future__ import annotations
from collections import Counter
FORBIDDEN={"qualification","qualification_band","canonical_score","authoritative_confidence"}

def _forbidden(value):
    if isinstance(value,dict):
        return any(k in FORBIDDEN or _forbidden(v) for k,v in value.items())
    return isinstance(value,list) and any(_forbidden(v) for v in value)

def evaluate(run:dict)->dict:
    if _forbidden(run): raise ValueError("Agency payload contains canonical Nodepad field")
    observations=run.get("observations",[]); unique={o.get("dedupe_key") or o.get("source_url") for o in observations if o.get("dedupe_key") or o.get("source_url")}
    counts=Counter(o.get("polarity","neutral") for o in observations)
    sources={o.get("source_url") for o in observations if o.get("source_url")}; threads={o.get("thread_id") for o in observations if o.get("thread_id")}; communities={o.get("community") for o in observations if o.get("community")}
    direct=sum(bool(o.get("direct_customer")) for o in observations); matches=sum(bool(o.get("segment_match")) for o in observations)
    required=bool(run.get("hypothesis_id") and run.get("criterion") and run.get("analysis_file"))
    provenance=all(o.get("source_url") and o.get("collected_at") and o.get("observation") is not None and o.get("inference") is not None for o in observations)
    duplicate_rate=0 if not observations else round(1-len(unique)/len(observations),4)
    metrics={"supporting_n":counts["supporting"],"contradicting_n":counts["contradicting"],"neutral_n":counts["neutral"],"sample_n":len(observations),"unique_sources":len(sources),"unique_threads":len(threads),"unique_communities":len(communities),"duplicate_rate":duplicate_rate,"segment_match_rate":round(matches/len(observations),4) if observations else 0,"source_diversity":len({o.get('source_type') for o in observations if o.get('source_type')}),"direct_customer_ratio":round(direct/len(observations),4) if observations else 0,"recency":run.get("recency"),"contradiction_coverage":round(counts['contradicting']/len(observations),4) if observations else 0}
    if not required or not provenance or duplicate_rate>=run.get("max_duplicate_rate",.25): state="DATA_QUALITY_FAILURE"
    elif len(unique)<run.get("minimum_sample",3) or not counts["contradicting"]: state="INSUFFICIENT"
    else: state="PASS_FOR_NODEPAD_SUBMISSION"
    return {"state":state,"metrics":metrics,"hypothesis_id":run.get("hypothesis_id"),"criterion":run.get("criterion")}
