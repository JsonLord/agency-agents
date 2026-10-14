import os
from urllib.parse import quote_plus
from .base import HTTPProvider, ProviderHealth, result
class GitHubProvider(HTTPProvider):
    id="github-api"
    def health(self): return ProviderHealth(True,"available",credential_state="configured" if os.getenv("GITHUB_TOKEN") else "optional_missing")
    def search(self,query,*,limit=10,context=None):
        headers={}; token=os.getenv("GITHUB_TOKEN")
        if token: headers["Authorization"]=f"Bearer {token}"
        kind=(context or {}).get("github_kind","repositories")
        if kind not in {"repositories","issues"}: kind="repositories"
        data,headers_out=self._json(f"https://api.github.com/search/{kind}?q={quote_plus(query)}&per_page={min(limit,50)}",headers)
        items=[]
        for item in data.get("items",[])[:limit]:
            url=item.get("html_url")
            items.append({"source_url":url,"title":item.get("full_name") or item.get("title") or "","content":item.get("description") or item.get("body") or "","author":(item.get("owner") or item.get("user") or {}).get("login"),"published_at":item.get("created_at"),"metadata":{"kind":kind,"stars":item.get("stargazers_count"),"state":item.get("state"),"language":item.get("language")}})
        return result(self.id,query,items,context,self.health())
