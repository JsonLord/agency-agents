#!/usr/bin/env python3
import json
from pathlib import Path
def reject(pairs):
 out={}
 for key,value in pairs:
  if key in out:raise ValueError(f'duplicate JSON key: {key}')
  out[key]=value
 return out
files=sorted(Path('contracts').glob('*.json'))
schemas=[json.loads(p.read_text(),object_pairs_hook=reject) for p in files]
try:
 from jsonschema import Draft7Validator
except ImportError as exc:raise SystemExit('jsonschema is required: pip install jsonschema') from exc
for path,schema in zip(files,schemas):
 try:Draft7Validator.check_schema(schema)
 except Exception as exc:raise SystemExit(f'{path}: {exc}')
try:json.loads('{"x":1,"x":2}',object_pairs_hook=reject)
except ValueError:pass
else:raise SystemExit('duplicate key check failed')
print(f'SCHEMA PASS {len(files)} contracts parsed and meta-schema validated; duplicate keys rejected')
