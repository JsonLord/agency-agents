import os, unittest
from gateways.capabilities.providers import HackerNewsProvider,GitHubProvider,WebProvider,RedditProvider,TrendsProvider
from validation_workforce.harness import validate_provider_result

@unittest.skipUnless(os.getenv("LIVE_PROVIDER_TESTS")=="1","set LIVE_PROVIDER_TESTS=1")
class ProviderLiveTests(unittest.TestCase):
    def test_public_providers(self):
        for provider in (HackerNewsProvider(),GitHubProvider(),WebProvider(),TrendsProvider()):
            result=validate_provider_result(provider.search("accessibility automation",limit=2));self.assertLessEqual(len(result["items"]),2)
    def test_reddit_classification(self):
        provider=RedditProvider()
        if not os.getenv("REDDIT_ACCESS_TOKEN"): self.assertEqual(provider.health().status,"credentials_missing")
        else: validate_provider_result(provider.search("accessibility automation",limit=1))

if __name__=="__main__": unittest.main()
