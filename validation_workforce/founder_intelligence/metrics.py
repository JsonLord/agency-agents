"""Deterministic dashboard metrics. Narrative models never calculate these numbers."""
def _ratio(a,b): return round(a/b,4) if b else None
def compute_snapshot(data):
 e=data.get('evidence',[]); runs=data.get('runs',[]); experiments=data.get('experiments',[]); customers=data.get('customers',[])
 useful=sum(r.get('category')=='useful_outcome' for r in runs)
 return {'validation':{'gate_passes':sum(x.get('gate_state')=='PASS_FOR_NODEPAD_SUBMISSION' for x in e),'direct_customer_ratio':_ratio(sum(bool(x.get('direct_customer')) for x in e),len(e)),'contradiction_coverage':_ratio(sum(x.get('polarity')=='contradicting' for x in e),len(e))},'customer_pull':{'leads':len(customers),'contactable':sum(bool(x.get('contactable')) for x in customers),'wtp':sum(bool(x.get('wtp')) for x in customers)},'experiments':{'total':len(experiments),'completed':sum(x.get('status')=='completed' for x in experiments)},'operations':{'runs':len(runs),'useful_outputs':useful,'useful_output_rate':_ratio(useful,len(runs))}}
def momentum(components,targets,weights=None):
 weights=weights or {'validation':.3,'customer_pull':.3,'experiment_engine':.2,'execution':.1,'efficiency':.1}
 if any(k not in components or not targets.get(k) for k in weights): return {'status':'insufficient_data','score':None,'components':{}}
 normalized={k:min(1,components[k]/targets[k]) for k in weights}; return {'status':'available','score':round(100*sum(normalized[k]*weights[k] for k in weights),1),'components':normalized,'weights':weights}
def reporter_payload(state):
 empty=lambda: []
 return {'trajectory':state.get('trajectory','insufficient_data'),'executive_summary':state.get('summary',''),'main_bottleneck':state.get('bottleneck'),'largest_opportunity':state.get('opportunity'),'what_changed_today':empty(),'what_changed_seven_days':empty(),'what_accelerated':empty(),'what_slowed':empty(),'what_became_more_true':empty(),'what_became_less_true':empty(),'self_deception_risks':empty(),'workforce_critique':empty(),'recommended_focus':empty(),'founder_actions':empty(),'celebrations':empty(),'decisions':empty(),'concerns':empty(),'opportunity_seeds':empty()}
