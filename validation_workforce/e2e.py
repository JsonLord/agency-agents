"""Deterministic accessibility validation fixture."""
from gateways.nodepad.mock import MockNodepad
from gateways.telemetry.events import Event
from gateways.telemetry.sink import MemorySink
from gateways.capabilities.providers import StaticProvider
from validation_workforce.evaluation import analyze_evidence, analyze_lane, map_assumptions, pressure_test
from validation_workforce.harness import idempotency_key, validate_agent_result, validate_provider_result

def run(fixture):
    node=MockNodepad(fixture["context"]); sink=MemorySink()
    for kind in ("accepted","context_loaded","agent_selected","skill_selected","started"): sink.emit(Event(kind, {"hypothesis":"H1"}))
    support=[e for e in fixture["evidence"] if e["polarity"]=="supporting"]
    contrary=[e for e in fixture["evidence"] if e["polarity"]=="contradicting"]
    for evidence in fixture["evidence"]: node.submit_evidence(evidence); sink.emit(Event("evidence_submitted", evidence))
    lane=analyze_lane(fixture["lane_context"])
    assumptions=map_assumptions(fixture["assumptions"])
    pressure=pressure_test(fixture["hypothesis"]["statement"],fixture["assumptions"])
    external=[]
    for provider_fixture in fixture["provider_results"]:
        provider=StaticProvider(provider_fixture["capability"].split(".")[-1],provider_fixture["items"]); sink.emit(Event("capability_requested",{"capability":provider_fixture["capability"],"provider":provider.id,"query_id":"accessibility-rework","rate_limit_state":"ok"}))
        research=validate_provider_result(provider.search(provider_fixture["query"],limit=10,context={"intent":"disconfirm"}))
        for item in research["items"]:
            candidate={**item,"provider":research["provider"],"query":research["query"],"retrieved_at":research["retrieved_at"],"polarity":item.get("polarity","unknown"),"source_type":item.get("source_type","web")}
            candidate["idempotency_key"]=idempotency_key("fixture","validate-idea",candidate["provider"],candidate["query"],candidate["source_url"],candidate["content"])
            node.submit_evidence(candidate); node.submit_evidence(candidate); external.append(candidate)
    audit=analyze_evidence(fixture["evidence"]+external)
    counter=node.propose_counter_hypothesis({"title":"Counter H1","statement":"Late accessibility rework is too infrequent or inexpensive to motivate payment."})
    gap=node.write_research_gap({"question":"What is the annual rework cost by team size?"})
    experiment=node.submit_experiment_spec({"id":"EXP-1","kind":"experiment","hypothesis_id":"H1","method":"Concierge pretotype automated review","success_criteria":{"paid_pilots":3},"failure_criteria":{"paid_pilots":{"maximum":0}}})
    result={"agent_id":"experiment-designer","status":"completed","summary":"Test willingness to pay; Nodepad alone determines qualification.","artifacts":[experiment],"evidence_ids":[e["id"] for e in fixture["evidence"]],"handoffs":[]}
    validate_agent_result(result)
    sink.emit(Event("artifact_created", experiment)); sink.emit(Event("handoff_created", counter)); sink.emit(Event("completed", result))
    return {"support":len(support),"contradictory":len(contrary),"external_research":len(external),"source_diversity":audit["source_diversity"]["provider_count"],"assumption_map":int(bool(assumptions["assumptions"])),"pressure_test":int(bool(pressure["pre_mortem"])),"counter_hypothesis":int(bool(counter)),"research_gap":int(bool(gap)),"experiment":int(bool(experiment)),"authoritative_qualification":0,"telemetry_events":len(sink.events),"agent_result":result,"nodepad":node,"lane":lane["lane"],"audit":audit}
