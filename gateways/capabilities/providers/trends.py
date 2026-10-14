from urllib.parse import quote_plus
from .base import HTTPProvider, ProviderHealth, result
class TrendsProvider(HTTPProvider):
    id="trends-public"
    def health(self): return ProviderHealth(True,"degraded",last_error="upstream may throttle automated requests")
    def search(self,query,*,limit=10,context=None):
        url=f"https://trends.google.com/trends/explore?q={quote_plus(query)}"
        return result(self.id,query,[{"source_url":url,"title":f"Google Trends: {query}","content":"Interactive trend exploration; values must be retrieved and interpreted by the caller.","author":None,"published_at":None,"metadata":{"mode":"explore_link","degraded":True}}],context,self.health())
