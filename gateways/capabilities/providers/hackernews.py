from urllib.parse import quote_plus
from .base import HTTPProvider, ProviderHealth, result
class HackerNewsProvider(HTTPProvider):
    id="hackernews-public"
    def health(self): return ProviderHealth(True,"available")
    def search(self,query,*,limit=10,context=None):
        data,_=self._json(f"https://hn.algolia.com/api/v1/search?query={quote_plus(query)}&hitsPerPage={min(limit,50)}")
        items=[]
        for hit in data.get("hits",[])[:limit]:
            object_id=str(hit.get("objectID","")); url=hit.get("url") or f"https://news.ycombinator.com/item?id={object_id}"
            items.append({"source_url":url,"title":hit.get("title") or hit.get("story_title") or "", "content":hit.get("story_text") or hit.get("comment_text") or hit.get("title") or "","author":hit.get("author"),"published_at":hit.get("created_at"),"metadata":{"item_id":object_id,"item_type":"story" if hit.get("title") else "comment","points":hit.get("points")}})
        return result(self.id,query,items,context,self.health())
