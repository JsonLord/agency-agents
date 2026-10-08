from dataclasses import dataclass,asdict
@dataclass(frozen=True)
class Delegation:
 agent_id:str; task:str; context:dict; workflow_id:str|None=None; workspace_id:str|None=None

def delegate(*,agent_id,task,context,workflow_id=None,workspace_id=None,adapter=None):
 request=Delegation(agent_id,task,context,workflow_id,workspace_id)
 return adapter(asdict(request)) if adapter else asdict(request)
