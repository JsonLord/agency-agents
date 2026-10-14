"""Validation harness for transient Agency outputs."""
import hashlib
from validation_workforce.evaluation.analysis import enforce_boundary

RESEARCH_INTENTS = {"support", "disconfirm", "discriminate", "refresh", "discover"}
SECRET_FIELDS = {
    "api_key", "authorization", "cookie", "cookies", "oauth_token", "password",
    "pat", "secret", "session_token", "token",
}

def idempotency_key(workspace, workflow, provider, query, source_url, content):
    stable = [workspace, workflow, provider, " ".join(query.lower().split()), source_url, hashlib.sha256(content.encode()).hexdigest()]
    return hashlib.sha256("\x1f".join(stable).encode()).hexdigest()

def validate_provider_result(result):
    required = {"provider", "query", "retrieved_at", "items"}
    if required - result.keys() or not isinstance(result["items"], list):
        raise ValueError("malformed provider result")
    if result.get("intent", "discover") not in RESEARCH_INTENTS:
        raise ValueError("unsupported research intent")

    def reject_secrets(value):
        if isinstance(value, dict):
            leaked = SECRET_FIELDS.intersection(key.lower() for key in value)
            if leaked:
                raise ValueError(f"provider result contains secret fields: {sorted(leaked)}")
            for child in value.values():
                reject_secrets(child)
        elif isinstance(value, list):
            for child in value:
                reject_secrets(child)

    reject_secrets(result)
    for item in result["items"]:
        if not item.get("source_url") or "content" not in item:
            raise ValueError("provider item lacks provenance")
    return result

def deduplicate(items):
    seen=set(); output=[]
    for item in items:
        key=item.get("idempotency_key") or (item.get("source_url"), hashlib.sha256(item.get("content", "").encode()).hexdigest())
        if key not in seen: seen.add(key); output.append(item)
    return output

def validate_agent_result(result):
    enforce_boundary(result)
    if not {"agent_id", "status", "summary", "artifacts", "evidence_ids", "handoffs"} <= result.keys(): raise ValueError("incomplete AgentResult")
    for artifact in result["artifacts"]:
        if artifact.get("kind") == "experiment" and not {"success_criteria", "failure_criteria"} <= artifact.keys():
            raise ValueError("experiment requires explicit success and failure criteria")
    return result
