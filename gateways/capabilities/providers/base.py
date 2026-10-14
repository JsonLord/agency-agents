"""Common provider protocol and deterministic test adapter."""
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from typing import Protocol
import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

@dataclass(frozen=True)
class ProviderHealth:
    available: bool
    status: str
    rate_limited: bool = False
    retry_after: int | None = None
    credential_state: str = "not_required"
    last_error: str | None = None

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

class HTTPProvider:
    """Small bounded stdlib HTTP base; never includes credentials in results/errors."""
    timeout = 12
    def _json(self, url, headers=None):
        safe_headers={"Accept":"application/json","User-Agent":"agency-agents/validation-workforce",**(headers or {})}
        try:
            with urlopen(Request(url,headers=safe_headers),timeout=self.timeout) as response:
                return json.load(response), dict(response.headers)
        except HTTPError as exc:
            retry=exc.headers.get("Retry-After")
            error=RuntimeError(f"provider_http_error status={exc.code}" + (f" retry_after={retry}" if retry else ""))
            error.status=exc.code; error.retry_after=retry
            raise error from None
        except (URLError, TimeoutError, OSError) as exc:
            raise RuntimeError(f"provider_network_error: {type(exc).__name__}") from None

def result(provider, query, items, context=None, health=None):
    return {"provider":provider,"query":query,"intent":(context or {}).get("intent","discover"),
            "retrieved_at":datetime.now(timezone.utc).isoformat(),"health":asdict(health or ProviderHealth(True,"healthy")),"items":items}
