from .base import StaticProvider
class TrendsProvider(StaticProvider):
    def __init__(self, items=(), health=None): super().__init__("trends", items, health)
