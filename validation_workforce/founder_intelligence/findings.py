import json
from pathlib import Path
def update_findings(path,item):
 path=Path(path); data=json.loads(path.read_text()) if path.exists() else {'findings':[]}; by={x['id']:x for x in data['findings']}; by[item['id']]={**by.get(item['id'],{}),**item}; data['findings']=sorted(by.values(),key=lambda x:x['id']); path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(data,indent=2,sort_keys=True)+'\n'); return data
