from dataclasses import dataclass,field
from datetime import datetime,timezone
VOCABULARY={'accepted','context_loaded','agent_selected','skill_selected','capability_requested','started','artifact_created','evidence_submitted','handoff_created','completed','failed','cancelled'}
@dataclass(frozen=True)
class Event:
 kind:str; payload:dict=field(default_factory=dict); timestamp:str=field(default_factory=lambda:datetime.now(timezone.utc).isoformat())
 def __post_init__(self):
  if self.kind not in VOCABULARY:raise ValueError(f'unknown event: {self.kind}')
