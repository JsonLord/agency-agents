"""Semantic capability resolution with free-first fallback traversal."""
import json, os
from pathlib import Path

class CapabilityRouter:
    def __init__(self,registry=None,health=None,max_depth=8):
        self.registry=registry or json.loads((Path(__file__).with_name("registry.json")).read_text())["capabilities"]
        self.health=health or {}; self.max_depth=max_depth
    def _capability(self,identifier):
        return next((c for c in self.registry if c["id"]==identifier),None)
    def _usable(self,provider):
        runtime=self.health.get(provider["id"])
        if runtime is not None:
            if hasattr(runtime,"health"): runtime=runtime.health()
            available=getattr(runtime,"available",runtime.get("available",True) if isinstance(runtime,dict) else True)
            limited=getattr(runtime,"rate_limited",runtime.get("rate_limited",False) if isinstance(runtime,dict) else False)
            if not available or limited:return False
        return provider.get("available",True) and provider.get("healthy",True) and not provider.get("rate_limited",False) and (not provider.get("auth_env") or bool(os.getenv(provider["auth_env"])))
    def resolve(self,capability_id,approved=False): return self.resolve_path(capability_id,approved=approved)["provider_config"]
    def resolve_path(self,capability_id,approved=False):
        requested=capability_id; chain=[]; visited=set()
        for _ in range(self.max_depth):
            if capability_id in visited: raise RuntimeError(f"capability fallback cycle: {' -> '.join(chain+[capability_id])}")
            visited.add(capability_id); chain.append(capability_id)
            capability=self._capability(capability_id)
            if not capability: raise KeyError(capability_id)
            if capability.get("scope")=="write" and capability.get("approval")=="required" and not approved: raise PermissionError("external write approval required")
            providers=sorted((p for p in capability.get("providers",[]) if self._usable(p)),key=lambda p:(not p.get("free",False),p.get("priority",100),p["id"]))
            if providers:
                provider=providers[0]
                return {"requested_capability":requested,"resolved_capability":capability_id,"provider":provider["id"],"provider_config":provider,"fallback_chain":chain}
            fallbacks=[]
            if capability.get("fallback"): fallbacks.append(capability["fallback"])
            fallbacks += [p["fallback"] for p in capability.get("providers",[]) if p.get("fallback","").startswith("research.")]
            fallback=next((x for x in fallbacks if x not in visited),None)
            if not fallback:
                if fallbacks: fallback=fallbacks[0]  # allow next iteration to report a cycle
                else: raise RuntimeError(f"fallback exhausted for {requested}: {' -> '.join(chain)}")
            next_cap=self._capability(fallback)
            if next_cap and capability.get("scope")=="read" and next_cap.get("scope")!="read": raise PermissionError("fallback may not escalate scope")
            capability_id=fallback
        raise RuntimeError(f"fallback depth exceeded for {requested}")
