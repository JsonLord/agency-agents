#!/usr/bin/env python3
import argparse,json
from validation_workforce.catalog import build,generate,plan,validate
p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='command',required=True)
sub.add_parser('catalog-generate');sub.add_parser('catalog-validate')
w=sub.add_parser('workflow'); ws=w.add_subparsers(dest='action',required=True);ws.add_parser('list');i=ws.add_parser('inspect');i.add_argument('id');ws.add_parser('validate');pl=ws.add_parser('plan');pl.add_argument('id');pl.add_argument('--input',default='{}')
a=p.parse_args()
if a.command.startswith('catalog'):
 counts=generate() if a.command=='catalog-generate' else validate(build());print('CATALOG PASS '+json.dumps(counts,sort_keys=True))
elif a.action=='validate':d=build();validate(d);print(f'WORKFLOW PASS {len(d["workflows"])} definitions')
elif a.action=='list':print('\n'.join(w['id'] for w in build()['workflows']))
elif a.action=='inspect':print(json.dumps(next(w for w in build()['workflows'] if w['id']==a.id),indent=2))
elif a.action=='plan':print(json.dumps(plan(a.id,json.loads(a.input)),indent=2))
