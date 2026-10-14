from .base import StaticProvider
class WebProvider(StaticProvider):
    def __init__(self, items=(), health=None): super().__init__("web", items, health)
