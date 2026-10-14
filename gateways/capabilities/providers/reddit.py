import os
from .base import ProviderHealth, StaticProvider
class RedditProvider(StaticProvider):
    def __init__(self, items=(), health=None): super().__init__("reddit", items, health or ProviderHealth(bool(os.getenv("REDDIT_CLIENT_ID")), "healthy" if os.getenv("REDDIT_CLIENT_ID") else "credentials_missing"))
