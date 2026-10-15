#!/usr/bin/env python3
import argparse,json
from pathlib import Path
from validation_workforce.evidence_gate import evaluate
from validation_workforce.founder_intelligence.findings import update_findings
p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);p.add_argument('--findings',required=True);a=p.parse_args()
run=json.loads(Path(a.input).read_text()); result=evaluate(run);out=Path(a.output);out.mkdir(parents=True,exist_ok=True)
(out/'metrics.json').write_text(json.dumps(result['metrics'],indent=2)+'\n');(out/'evidence.json').write_text(json.dumps(result,indent=2)+'\n');(out/'report.md').write_text(f"# Analysis {run['id']}\n\nGate: `{result['state']}`\n")
update_findings(a.findings,{'id':'finding-'+run['id'],'hypothesis_id':run['hypothesis_id'],'analysis_run':run['id'],'collection_runs':run.get('collection_runs',[]),'source_provenance':[o['source_url'] for o in run['observations']],'evidence_candidate_ids':[],'nodepad_evidence_ids':[],'status':'criterion_met' if result['state']=='PASS_FOR_NODEPAD_SUBMISSION' else 'insufficient','polarity':'mixed','sample_size':result['metrics']['sample_n'],'independent_source_count':result['metrics']['unique_sources'],'direct_customer':result['metrics']['direct_customer_ratio']>0,'created_at':run.get('created_at'),'updated_at':run.get('created_at')})
print(json.dumps(result,sort_keys=True))
