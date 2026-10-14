from .base import StaticProvider
class HackerNewsProvider(StaticProvider):
    def __init__(self, items=(), health=None): super().__init__("hackernews", items, health)
