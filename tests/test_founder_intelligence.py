import importlib.util,json,subprocess,tempfile,unittest
from pathlib import Path
from jsonschema import Draft7Validator
from validation_workforce.catalog import ROOT,build,validate
from validation_workforce.evidence_gate import evaluate
from validation_workforce.founder_intelligence import compute_snapshot,momentum,reporter_payload,update_findings
from validation_workforce.founder_intelligence.theme import derive
class FounderIntelligenceTests(unittest.TestCase):
 def fixture(self): return json.loads(Path('tests/fixtures/company/analysis-run.json').read_text())
 def test_roster_reporter_and_skill(self):
  data=build();counts=validate(data);self.assertEqual(counts['agents'],45);self.assertEqual(counts['legacy-aliases'],327);self.assertIn('founder-intelligence-reporter',{x['id'] for x in data['agents']});self.assertIn('founder-intelligence-reporting',{x['id'] for x in data['skills']})
 def test_persona_boundaries(self):
  scout=Path('agents/discovery/community-scout.md').read_text(); investigator=Path('agents/discovery/customer-investigator.md').read_text();self.assertIn('Collection-only',scout);self.assertNotIn('evidence_submission',scout.split('---',2)[1]);self.assertIn('pandas',investigator);self.assertIn('research gap',investigator)
 def test_evidence_gate_pass_insufficient_quality_and_boundary(self):
  run=self.fixture();result=evaluate(run);self.assertEqual(result['state'],'PASS_FOR_NODEPAD_SUBMISSION');self.assertEqual(result['metrics']['contradicting_n'],1);self.assertEqual(result['metrics']['unique_sources'],3)
  short={**run,'observations':run['observations'][:2]};self.assertEqual(evaluate(short)['state'],'INSUFFICIENT')
  bad={**run,'observations':run['observations']+[run['observations'][0]]};self.assertEqual(evaluate(bad)['state'],'DATA_QUALITY_FAILURE')
  with self.assertRaises(ValueError):evaluate({**run,'artifact':{'authoritative_confidence':.9}})
 def test_findings_idempotent(self):
  with tempfile.TemporaryDirectory() as d:
   p=Path(d)/'findings.json'; item={'id':'F1','status':'candidate'};update_findings(p,item);update_findings(p,item);self.assertEqual(len(json.loads(p.read_text())['findings']),1)
 def test_metrics_momentum_and_report_shape(self):
  data=json.loads(Path('tests/fixtures/company/operating-data.json').read_text());snap=compute_snapshot(data);self.assertEqual(snap['operations']['useful_output_rate'],.5)
  self.assertEqual(momentum({}, {})['status'],'insufficient_data');self.assertEqual(momentum({'validation':1,'customer_pull':1,'experiment_engine':1,'execution':1,'efficiency':1},{k:1 for k in ['validation','customer_pull','experiment_engine','execution','efficiency']})['score'],100)
  report=reporter_payload({});Draft7Validator(json.loads(Path('contracts/founder-reporter.json').read_text())).validate(report);self.assertEqual([len(report[x]) for x in ('founder_actions','celebrations','decisions')],[0,0,0])
 def test_runtime_references_and_no_continuous_jules(self):
  back={x['id'] for x in json.loads(Path('runtime/backends.json').read_text())['backends']}; schedules=json.loads(Path('runtime/schedules.json').read_text())['bindings'];self.assertTrue(all(x['primary'] in back and (not x.get('fallback') or x['fallback'] in back) for x in schedules)); reporter=next(x for x in schedules if x['agent']=='founder-intelligence-reporter');self.assertEqual(reporter['primary'],'github-actions');self.assertEqual(reporter['frontend'],'jules')
 def test_dashboard_history_immutable_and_private(self):
  with tempfile.TemporaryDirectory() as d:
   subprocess.run(['python3','scripts/build-founder-dashboard.py','--input','tests/fixtures/company/operating-data.json','--workspace',d],check=True,capture_output=True,text=True);subprocess.run(['python3','scripts/build-founder-dashboard.py','--input','tests/fixtures/company/operating-data.json','--workspace',d],check=True,capture_output=True,text=True);self.assertEqual(len((Path(d)/'dashboard/data/history.jsonl').read_text().splitlines()),1)
  self.assertFalse(Path('.github/workflows/pages.yml').exists()); html=Path('templates/founder-dashboard/index.html').read_text();self.assertIn('Founder attention',html);self.assertIn('Longitudinal',html)
 def test_theme_bridge(self):
  with tempfile.TemporaryDirectory() as d:
   files=derive('templates/company-workspace/DESIGN.md',d);self.assertTrue(all(x.exists() for x in files));self.assertIn('Derived from DESIGN.md',files[0].read_text())
 def test_hermes_roster_45(self):
  spec=importlib.util.spec_from_file_location('builder','scripts/build-hermes-plugin.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);self.assertEqual(len(m.collect_agents(ROOT)),45)
 def test_golden_transfer_local(self):
  with tempfile.TemporaryDirectory() as d:
   root=Path(d); findings=root/'findings.json'; out=root/'analysis';subprocess.run(['python3','scripts/analyze-customer-collection.py','--input','tests/fixtures/company/analysis-run.json','--output',str(out),'--findings',str(findings)],env={'PYTHONPATH':'.','PATH':'/usr/bin:/bin'},check=True,capture_output=True,text=True);self.assertEqual(json.loads((out/'evidence.json').read_text())['state'],'PASS_FOR_NODEPAD_SUBMISSION');self.assertEqual(json.loads(findings.read_text())['findings'][0]['status'],'criterion_met')
if __name__=='__main__':unittest.main()
