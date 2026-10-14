"""Production Nodepad HTTP boundary. Secrets are never serialized or logged."""
import json, os
from urllib.request import Request, urlopen
from validation_workforce.evaluation.analysis import enforce_boundary

class NodepadClient:
    def __init__(self,base_url=None,api_key=None,workspace_id=None,transport=None,timeout=20):
        self.base=(base_url or os.getenv("NODEPAD_BASE_URL","")).rstrip("/"); self.key=api_key or os.getenv("NODEPAD_API_KEY"); self.workspace=workspace_id or os.getenv("NODEPAD_WORKSPACE_ID","default"); self.transport=transport; self.timeout=timeout
    def _call(self,method,path,payload=None,idempotency_key=None):
        headers={"Accept":"application/json","Content-Type":"application/json"}
        if self.key: headers["Authorization"]=f"Bearer {self.key}"
        if idempotency_key: headers["Idempotency-Key"]=idempotency_key
        body=None if payload is None else json.dumps(payload).encode()
        if self.transport:return self.transport(method,self.base+path,headers,body)
        with urlopen(Request(self.base+path,data=body,headers=headers,method=method),timeout=self.timeout) as response:return json.load(response)
    def _write(self,path,payload):
        enforce_boundary(payload)
        return self._call("POST",path,payload,payload.get("idempotency_key"))
    def health(self):return self._call("GET","/health")
    def api_docs(self):return self._call("GET","/api-docs")
    def context(self):return self._call("GET",f"/api/v1/workspaces/{self.workspace}/context")
    def hypotheses(self):return self._call("GET",f"/api/v1/workspaces/{self.workspace}/hypotheses")
    def evidence(self):return self._call("GET",f"/api/v1/workspaces/{self.workspace}/evidence")
    def submit_evidence(self,p):return self._write(f"/api/v1/workspaces/{self.workspace}/evidence",p)
    def propose_hypothesis(self,p):return self._write(f"/api/v1/workspaces/{self.workspace}/hypotheses",p)
    def propose_counter_hypothesis(self,p):return self.propose_hypothesis({**p,"kind":"counter"})
    def write_research_gap(self,p):return self._write(f"/api/v1/workspaces/{self.workspace}/research/tasks",p)
    def submit_experiment_spec(self,p):return self.write_research_gap({"kind":"experiment_spec",**p})
    def submit_experiment_result(self,p):return self.write_research_gap({"kind":"experiment_result",**p})
    def emit_agent_event(self,p):return self._write(f"/api/v1/workspaces/{self.workspace}/heartbeat",p)
