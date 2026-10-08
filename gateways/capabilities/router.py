import json
from pathlib import Path
class CapabilityRouter:
 def __init__(self,registry=None):self.registry=registry or json.loads((Path(__file__).with_name('registry.json')).read_text())['capabilities']
 def resolve(self,capability_id,approved=False):
  capability=next((c for c in self.registry if c['id']==capability_id),None)
  if not capability:raise KeyError(capability_id)
  if capability['scope']=='write' and capability['approval']=='required' and not approved:raise PermissionError('external write approval required')
  providers=[p for p in capability['providers'] if p['available'] and p['healthy']]
  if not providers:raise RuntimeError(f'no healthy provider for {capability_id}')
  return sorted(providers,key=lambda p:(not p['free'],p['priority'],p['id']))[0]
