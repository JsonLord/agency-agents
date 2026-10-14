import os
from urllib.parse import quote_plus
from .base import HTTPProvider, ProviderHealth, result
class RedditProvider(HTTPProvider):
    id="reddit-api"
    def health(self):
        ready=bool(os.getenv("REDDIT_ACCESS_TOKEN")); return ProviderHealth(ready,"available" if ready else "credentials_missing",credential_state="configured" if ready else "missing")
    def search(self,query,*,limit=10,context=None):
        health=self.health()
        if not health.available: raise RuntimeError("credentials_missing")
        data,_=self._json(f"https://oauth.reddit.com/search?q={quote_plus(query)}&limit={min(limit,25)}&restrict_sr=false",{"Authorization":f"Bearer {os.environ['REDDIT_ACCESS_TOKEN']}"})
        items=[]
        for child in data.get("data",{}).get("children",[])[:limit]:
            x=child.get("data",{}); items.append({"source_url":"https://www.reddit.com"+x.get("permalink",""),"title":x.get("title",""),"content":x.get("selftext") or x.get("title", ""),"author":x.get("author"),"published_at":x.get("created_utc"),"metadata":{"subreddit":x.get("subreddit"),"score":x.get("score")}})
        return result(self.id,query,items,context,health)
