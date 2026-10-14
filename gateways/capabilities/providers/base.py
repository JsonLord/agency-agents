"""Common provider protocol and deterministic test adapter."""
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Protocol

@dataclass(frozen=True)
class ProviderHealth:
    available: bool
    status: str
    rate_limited: bool = False
    retry_after: int | None = None

class ResearchProvider(Protocol):
    id: str
    def health(self) -> ProviderHealth: ...
    def search(self, query: str, *, limit: int, context: dict | None = None) -> dict: ...

class StaticProvider:
    def __init__(self, provider_id, items=(), health=None):
        self.id=provider_id; self._items=list(items); self._health=health or ProviderHealth(True, "healthy")
    def health(self): return self._health
    def search(self, query, *, limit=10, context=None):
        if not self._health.available or self._health.rate_limited: raise RuntimeError(self._health.status)
        return {"provider": self.id, "query": query, "intent": (context or {}).get("intent", "discover"),
                "retrieved_at": datetime.now(timezone.utc).isoformat(), "health": asdict(self._health), "items": self._items[:limit]}
