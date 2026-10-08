import copy,importlib.util,json,tempfile,unittest
from pathlib import Path
from jsonschema import Draft7Validator
from gateways.capabilities.router import CapabilityRouter
from gateways.delegation.runtime import delegate
from gateways.nodepad.mock import MockNodepad
from gateways.telemetry.events import Event,VOCABULARY
from gateways.telemetry.sink import MemorySink
from validation_workforce.catalog import ROOT,build,plan,validate
from validation_workforce.e2e import run

class Tests(unittest.TestCase):
 def test_catalogs_and_aliases(self):
  data=build();self.assertEqual(validate(data),{'agents':44,'skills':20,'workflows':13,'capabilities':5,'legacy-aliases':326})
  self.assertTrue(all((ROOT/path).is_file() for path in data['legacy-aliases'].values()))
 def test_missing_references_rejected(self):
  data=build();data['agents'][0]['skills'].append('missing')
  with self.assertRaises(ValueError):validate(data)
 def test_capability_free_priority_scope(self):
  router=CapabilityRouter([{'id':'x','scope':'read','approval':'none','providers':[{'id':'paid','priority':1,'free':False,'available':True,'healthy':True},{'id':'free','priority':9,'free':True,'available':True,'healthy':True}]}]);self.assertEqual(router.resolve('x')['id'],'free')
  with self.assertRaises(PermissionError):CapabilityRouter().resolve('artifact.generate')
  self.assertEqual(CapabilityRouter().resolve('artifact.generate',approved=True)['id'],'local-template')
 def test_workflow_validation_and_plan(self):self.assertEqual(len(plan('validate-idea',{'hypothesis':'H1'})['steps']),6)
 def test_contracts_and_duplicate_keys(self):
  for path in Path('contracts').glob('*.json'):Draft7Validator.check_schema(json.loads(path.read_text()))
  def reject(pairs):
   d={}
   for k,v in pairs:
    if k in d:raise ValueError(k)
    d[k]=v
   return d
  with self.assertRaises(ValueError):json.loads('{"x":1,"x":2}',object_pairs_hook=reject)
 def test_nodepad_round_trip(self):
  n=MockNodepad({'x':1});n.submit_evidence({'id':'E1'});n.propose_counter_hypothesis({'statement':'not H1'});n.submit_experiment_spec({'id':'X'});self.assertEqual((n.context()['x'],len(n.evidence()),len(n.hypotheses()),len(n.state['experiments'])),(1,1,1,1))
 def test_delegation_runtime_independent(self):self.assertEqual(delegate(agent_id='a',task='t',context={})['agent_id'],'a')
 def test_telemetry_fixture(self):
  sink=MemorySink()
  for kind in VOCABULARY:sink.emit(Event(kind))
  self.assertEqual(len(sink.events),len(VOCABULARY))
 def test_hermes_roster(self):
  spec=importlib.util.spec_from_file_location('builder','scripts/build-hermes-plugin.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);agents={a['slug']:a['division'] for a in m.collect_agents(ROOT)}
  self.assertEqual(len(agents),44);self.assertEqual({x:agents[x] for x in ['customer-investigator','hypothesis-formulator','experiment-designer','red-team-analyst','venture-judge']},{'customer-investigator':'discovery','hypothesis-formulator':'hypothesis','experiment-designer':'experimentation','red-team-analyst':'evaluation','venture-judge':'decision'})
 def test_e2e(self):
  result=run(json.loads(Path('tests/fixtures-accessibility.json').read_text()));self.assertEqual([result[x] for x in ('support','contradictory','counter_hypothesis','research_gap','experiment','authoritative_qualification')],[1,1,1,1,1,0]);Draft7Validator(json.loads(Path('contracts/agent-result.json').read_text())).validate(result['agent_result'])
if __name__=='__main__':unittest.main()
