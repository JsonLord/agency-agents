from urllib.parse import quote_plus
from .base import HTTPProvider, ProviderHealth, result
class WebProvider(HTTPProvider):
    id="ddgs-web"
    def health(self): return ProviderHealth(True,"available")
    def search(self,query,*,limit=10,context=None):
        # DuckDuckGo's public instant-answer JSON API is free and intentionally bounded.
        data,_=self._json(f"https://api.duckduckgo.com/?q={quote_plus(query)}&format=json&no_html=1&no_redirect=1")
        raw=[]
        if data.get("AbstractURL"): raw.append({"FirstURL":data["AbstractURL"],"Text":data.get("AbstractText") or data.get("Heading","")})
        def flatten(values):
            for value in values:
                if "Topics" in value: yield from flatten(value["Topics"])
                elif value.get("FirstURL"): yield value
        raw.extend(flatten(data.get("RelatedTopics",[])))
        items=[{"source_url":x["FirstURL"],"title":x.get("Text","").split(" - ",1)[0],"content":x.get("Text","").strip(),"author":None,"published_at":None,"metadata":{"backend":"duckduckgo-instant-answer"}} for x in raw[:limit]]
        return result(self.id,query,items,context,self.health())
