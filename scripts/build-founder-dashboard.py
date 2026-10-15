#!/usr/bin/env python3
import argparse,json,shutil
from datetime import date
from pathlib import Path
from validation_workforce.founder_intelligence import compute_snapshot
p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--workspace',required=True);a=p.parse_args();root=Path(a.workspace); source=json.loads(Path(a.input).read_text()); snapshot={'date':source.get('date',date.today().isoformat()),**compute_snapshot(source),'trajectory':source.get('trajectory','insufficient_data')}; data=root/'dashboard/data';daily=root/'dashboard/daily';data.mkdir(parents=True,exist_ok=True);daily.mkdir(parents=True,exist_ok=True); day=daily/f"{snapshot['date']}.json"
encoded=json.dumps(snapshot,indent=2,sort_keys=True)+'\n'
if day.exists() and day.read_text()!=encoded: raise SystemExit('immutable daily snapshot conflict')
if not day.exists(): day.write_text(encoded); (data/'history.jsonl').open('a').write(json.dumps(snapshot,sort_keys=True)+'\n')
(data/'current.json').write_text(encoded);print(json.dumps(snapshot,sort_keys=True))
