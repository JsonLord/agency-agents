"""In-memory adapter implementing the Nodepad logical interface."""
class MockNodepad:
 def __init__(self,context=None):self.state={'context':context or {},'hypotheses':[],'evidence':[],'research_gaps':[],'experiments':[],'events':[]}
 def context(self):return self.state['context']
 def hypotheses(self):return list(self.state['hypotheses'])
 def evidence(self):return list(self.state['evidence'])
 def submit_evidence(self,p):self.state['evidence'].append(dict(p));return p
 def propose_hypothesis(self,p):self.state['hypotheses'].append(dict(p));return p
 def propose_counter_hypothesis(self,p):return self.propose_hypothesis({'kind':'counter',**p})
 def write_research_gap(self,p):self.state['research_gaps'].append(dict(p));return p
 def submit_experiment_spec(self,p):self.state['experiments'].append({'kind':'spec',**p});return p
 def submit_experiment_result(self,p):self.state['experiments'].append({'kind':'result',**p});return p
 def emit_agent_event(self,p):self.state['events'].append(dict(p));return p
