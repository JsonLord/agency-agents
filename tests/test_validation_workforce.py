import copy,importlib.util,json,tempfile,unittest
from pathlib import Path
from urllib.error import HTTPError
from jsonschema import Draft7Validator
from gateways.capabilities.router import CapabilityRouter
from gateways.delegation.runtime import delegate
from gateways.nodepad.mock import MockNodepad
from gateways.telemetry.events import Event,VOCABULARY
from gateways.telemetry.sink import MemorySink
from validation_workforce.catalog import ROOT,build,plan,validate
from validation_workforce.e2e import run
from validation_workforce.evaluation import analyze_evidence,analyze_lane,map_assumptions,pressure_test
from validation_workforce.evaluation.analysis import enforce_boundary
from validation_workforce.harness import deduplicate,idempotency_key,validate_agent_result,validate_provider_result
from gateways.capabilities.providers import StaticProvider,ProviderHealth,RedditProvider,HackerNewsProvider,GitHubProvider,WebProvider
from gateways.nodepad.client import NodepadClient

class Tests(unittest.TestCase):
 def test_catalogs_and_aliases(self):
  data=build();counts=validate(data);self.assertEqual((counts['agents'],counts['workflows'],counts['capabilities'],counts['legacy-aliases']),(44,13,8,326));self.assertGreaterEqual(counts['skills'],27)
  self.assertTrue(all((ROOT/path).is_file() for path in data['legacy-aliases'].values()))
 def test_missing_references_rejected(self):
  data=build();data['agents'][0]['skills'].append('missing')
  with self.assertRaises(ValueError):validate(data)
 def test_capability_free_priority_scope(self):
  router=CapabilityRouter([{'id':'x','scope':'read','approval':'none','providers':[{'id':'paid','priority':1,'free':False,'available':True,'healthy':True},{'id':'free','priority':9,'free':True,'available':True,'healthy':True}]}]);self.assertEqual(router.resolve('x')['id'],'free')
  with self.assertRaises(PermissionError):CapabilityRouter().resolve('artifact.generate')
  self.assertEqual(CapabilityRouter().resolve('artifact.generate',approved=True)['id'],'local-template')
 def test_workflow_validation_and_plan(self):
  steps=plan('validate-idea',{'hypothesis':'H1'})['steps'];self.assertEqual(len(steps),7)
  by_id={x['id']:x for x in steps};self.assertEqual(by_id['step-2']['depends_on'],['step-1']);self.assertEqual(by_id['step-intelligence']['depends_on'],['step-1'])
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
  result=run(json.loads(Path('tests/fixtures-accessibility.json').read_text()));self.assertEqual([result[x] for x in ('support','contradictory','counter_hypothesis','research_gap','experiment','authoritative_qualification')],[1,1,1,1,1,0]);self.assertEqual(result['external_research'],3);self.assertGreaterEqual(result['source_diversity'],3);self.assertEqual(len(result['nodepad'].state['evidence']),5);Draft7Validator(json.loads(Path('contracts/agent-result.json').read_text())).validate(result['agent_result'])
 def test_product_eval_methods_preserve_contradictions(self):
  evidence=[{'id':'a','polarity':'supporting','provider':'web','source_url':'a','source_type':'report'},{'id':'b','polarity':'contradicting','provider':'github','source_url':'b','source_type':'behavior'}]
  result=analyze_evidence(evidence);self.assertEqual(result['contradiction_flags'],['b']);self.assertEqual(result['source_diversity']['provider_count'],2);self.assertNotIn('qualification',result)
  with self.assertRaises(ValueError):enforce_boundary({'qualification':'validated'})
  with self.assertRaises(ValueError):enforce_boundary({'artifacts':[{'canonical_score':0.9}]})
 def test_lanes_assumptions_pressure_and_harness(self):
  self.assertEqual(analyze_lane({'buyer_role':'CTO','budget':True,'procurement':True})['lane'],'b2b');self.assertEqual(analyze_lane({'habit':True,'frequency':'daily','identity_value':True})['lane'],'b2c')
  assumptions=[{'statement':'cheap','impact':2,'uncertainty':2},{'statement':'killer','impact':5,'uncertainty':5}]
  self.assertEqual(map_assumptions(assumptions)['kill_assumption']['statement'],'killer');self.assertIn('pre_mortem',pressure_test('H',assumptions))
  with self.assertRaises(ValueError):validate_agent_result({'qualification_band':'strong'})
 def test_provider_normalization_health_and_deduplication(self):
  item={'source_url':'https://example.test/1','content':'x','metadata':{}}
  result=StaticProvider('github',[item]).search('q',limit=1,context={'intent':'disconfirm'});validate_provider_result(result);self.assertEqual(result['intent'],'disconfirm')
  unavailable=StaticProvider('github',[],ProviderHealth(False,'rate_limited',True,60))
  with self.assertRaises(RuntimeError):unavailable.search('q',limit=1)
  key=idempotency_key('w','flow','github',' Q ','u','x');self.assertEqual(key,idempotency_key('w','flow','github','q','u','x'));self.assertEqual(len(deduplicate([{**item,'idempotency_key':key},{**item,'idempotency_key':key}])),1)
  self.assertFalse(RedditProvider().health().available)
  with self.assertRaisesRegex(ValueError,'unsupported research intent'):
   validate_provider_result({'provider':'web','query':'q','retrieved_at':'now','intent':'confirm-again','items':[]})
  with self.assertRaisesRegex(ValueError,'secret fields'):
   validate_provider_result({'provider':'web','query':'q','retrieved_at':'now','items':[{'source_url':'u','content':'x','metadata':{'authorization':'secret'}}]})
 def test_router_credentials_rate_limit_and_fallback(self):
  registry=[{'id':'x','scope':'read','approval':'none','providers':[{'id':'limited','priority':1,'free':True,'available':True,'healthy':True,'rate_limited':True},{'id':'credentialed','priority':2,'free':True,'available':True,'healthy':True,'auth_env':'ABSENT_TEST_TOKEN'},{'id':'fallback','priority':3,'free':True,'available':True,'healthy':True}]}]
  self.assertEqual(CapabilityRouter(registry).resolve('x')['id'],'fallback')
 def test_router_semantic_fallback_and_cycles(self):
  registry=[{'id':'a','scope':'read','approval':'none','fallback':'b','providers':[{'id':'bad','free':True,'available':False}]},{'id':'b','scope':'read','approval':'none','providers':[{'id':'ok','free':True,'priority':1}]}]
  result=CapabilityRouter(registry).resolve_path('a');self.assertEqual((result['provider'],result['fallback_chain']),('ok',['a','b']))
  registry[1]['providers']=[];registry[1]['fallback']='a'
  with self.assertRaisesRegex(RuntimeError,'cycle'):CapabilityRouter(registry).resolve_path('a')
 def test_nodepad_http_boundary_headers_and_paths(self):
  calls=[]
  def transport(method,url,headers,body):calls.append((method,url,headers,json.loads(body) if body else None));return {'ok':True}
  client=NodepadClient('https://nodepad.test','secret','workspace',transport=transport)
  client.submit_evidence({'claim':'x','idempotency_key':'stable'})
  self.assertEqual(calls[0][0:2],('POST','https://nodepad.test/api/v1/workspaces/workspace/evidence'));self.assertEqual(calls[0][2]['Authorization'],'Bearer secret');self.assertEqual(calls[0][2]['Idempotency-Key'],'stable')
  with self.assertRaises(ValueError):client.submit_evidence({'nested':{'qualification_band':'strong'}})
  self.assertEqual(len(calls),1)
  encoded=NodepadClient('https://nodepad.test',workspace_id='team/alpha',transport=transport);encoded.context()
  self.assertEqual(calls[-1][1],'https://nodepad.test/api/v1/workspaces/team%2Falpha/context')
 def test_nodepad_http_errors_are_sanitized(self):
  client=NodepadClient('https://nodepad.test','top-secret','workspace')
  def fail(*_args,**_kwargs):raise HTTPError('https://nodepad.test',403,'Bearer top-secret',{},None)
  import gateways.nodepad.client as module
  original=module.urlopen;module.urlopen=fail
  try:
   with self.assertRaisesRegex(RuntimeError,r'nodepad_http_error status=403') as raised:client.context()
   self.assertNotIn('top-secret',str(raised.exception))
  finally:module.urlopen=original
 def test_default_registry_maps_to_real_provider_ids(self):
  resolved=CapabilityRouter().resolve_path('research.github')
  self.assertEqual(resolved['provider'],'github-api')
 def test_lane_mixed_and_quality_vector(self):
  lane=analyze_lane({'budget':True,'habit':True});self.assertEqual(lane['lane'],'mixed');self.assertIn('budget',lane['signals']['b2b']);self.assertIn('habit',lane['signals']['b2c']);self.assertIn('roi_threshold',lane['checks']);self.assertIn('retention',lane['checks'])
  empty=analyze_evidence([]);self.assertEqual(empty['analysis_quality'],0);self.assertEqual(set(empty['quality_dimensions']),{'directness','recency','source_independence','behavioral_strength','segment_relevance','contradiction_coverage','triangulation'})
 def test_live_provider_normalizers_with_mocked_transport(self):
  hn=HackerNewsProvider();hn._json=lambda *_:({'hits':[{'objectID':'1','title':'T','url':'https://example.test/hn','author':'a','created_at':'now'}]}, {})
  gh=GitHubProvider();gh._json=lambda *_:({'items':[{'html_url':'https://example.test/repo','full_name':'o/r','description':'d','owner':{'login':'o'}}]}, {})
  web=WebProvider();web._json=lambda *_:({'RelatedTopics':[{'FirstURL':'https://example.test/web','Text':'Title - snippet'}]}, {})
  for provider in (hn,gh,web):
   result=validate_provider_result(provider.search('q',limit=1));self.assertEqual(len(result['items']),1);self.assertTrue(result['items'][0]['source_url'].startswith('https://'))
  hn._json=lambda *_:(_ for _ in ()).throw(RuntimeError('provider_network_error: TimeoutError'))
  with self.assertRaisesRegex(RuntimeError,'TimeoutError'):hn.search('q',limit=1)
if __name__=='__main__':unittest.main()
