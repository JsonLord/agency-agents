"""HTTP Nodepad client using only the Python standard library."""
import json, os
from urllib.request import Request, urlopen
class NodepadClient:
 def __init__(self, base_url=None, api_key=None, workspace_id=None):
  self.base=(base_url or os.getenv('NODEPAD_BASE_URL','')).rstrip('/'); self.key=api_key or os.getenv('NODEPAD_API_KEY'); self.workspace=workspace_id or os.getenv('NODEPAD_WORKSPACE_ID','default')
 def _call(self, method, path, payload=None):
  headers={'Content-Type':'application/json'}
  if self.key: headers['Authorization']=f'Bearer {self.key}'
  req=Request(self.base+path, data=None if payload is None else json.dumps(payload).encode(), headers=headers, method=method)
  with urlopen(req,timeout=20) as response:return json.load(response)
 def context(self):return self._call('GET',f'/api/v1/workspaces/{self.workspace}/context')
 def hypotheses(self):return self._call('GET',f'/api/v1/workspaces/{self.workspace}/hypotheses')
 def evidence(self):return self._call('GET',f'/api/v1/workspaces/{self.workspace}/evidence')
 def submit_evidence(self,p):return self._call('POST',f'/api/v1/workspaces/{self.workspace}/evidence',p)
 def propose_hypothesis(self,p):return self._call('POST',f'/api/v1/workspaces/{self.workspace}/hypotheses',p)
 def propose_counter_hypothesis(self,p): p={**p,'kind':'counter'};return self.propose_hypothesis(p)
 def write_research_gap(self,p):return self._call('POST',f'/api/v1/workspaces/{self.workspace}/research/tasks',p)
 def submit_experiment_spec(self,p):return self.write_research_gap({'kind':'experiment_spec',**p})
 def submit_experiment_result(self,p):return self.write_research_gap({'kind':'experiment_result',**p})
 def emit_agent_event(self,p):return self._call('POST',f'/api/v1/workspaces/{self.workspace}/heartbeat',p)
