"""Deterministic accessibility validation fixture."""
from gateways.nodepad.mock import MockNodepad
from gateways.telemetry.events import Event
from gateways.telemetry.sink import MemorySink

def run(fixture):
    node=MockNodepad(fixture["context"]); sink=MemorySink()
    for kind in ("accepted","context_loaded","agent_selected","skill_selected","started"): sink.emit(Event(kind, {"hypothesis":"H1"}))
    support=[e for e in fixture["evidence"] if e["polarity"]=="supporting"]
    contrary=[e for e in fixture["evidence"] if e["polarity"]=="contradicting"]
    for evidence in fixture["evidence"]: node.submit_evidence(evidence); sink.emit(Event("evidence_submitted", evidence))
    counter=node.propose_counter_hypothesis({"title":"Counter H1","statement":"Late accessibility rework is too infrequent or inexpensive to motivate payment."})
    gap=node.write_research_gap({"question":"What is the annual rework cost by team size?"})
    experiment=node.submit_experiment_spec({"id":"EXP-1","hypothesis_id":"H1","method":"Concierge automated review","success_criteria":{"paid_pilots":3}})
    result={"agent_id":"experiment-designer","status":"completed","summary":"Test willingness to pay without assigning qualification.","artifacts":[experiment],"evidence_ids":[e["id"] for e in fixture["evidence"]],"handoffs":[],"authoritative_qualification":False}
    sink.emit(Event("artifact_created", experiment)); sink.emit(Event("handoff_created", counter)); sink.emit(Event("completed", result))
    return {"support":len(support),"contradictory":len(contrary),"counter_hypothesis":int(bool(counter)),"research_gap":int(bool(gap)),"experiment":int(bool(experiment)),"authoritative_qualification":int(result["authoritative_qualification"]),"telemetry_events":len(sink.events),"agent_result":result,"nodepad":node}
