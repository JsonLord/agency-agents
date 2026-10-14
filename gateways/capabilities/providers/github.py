from .base import StaticProvider
class GitHubProvider(StaticProvider):
    def __init__(self, items=(), health=None): super().__init__("github", items, health)
