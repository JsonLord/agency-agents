import os, unittest
from gateways.nodepad.client import NodepadClient
from validation_workforce.harness import idempotency_key

@unittest.skipUnless(os.getenv("NODEPAD_LIVE_TEST")=="1","set NODEPAD_LIVE_TEST=1")
class NodepadLiveTests(unittest.TestCase):
    def setUp(self):
        if not os.getenv("NODEPAD_API_KEY"): self.skipTest("NODEPAD_API_KEY missing")
        self.client=NodepadClient()
    def test_authenticated_discovery_and_safe_reads(self):
        self.assertEqual(self.client.health().get("status"),"ok")
        self.assertIsInstance(self.client.context(),dict)
        self.assertIsNotNone(self.client.hypotheses())
        self.assertIsNotNone(self.client.evidence())
    def test_isolated_idempotent_evidence_write(self):
        if os.getenv("NODEPAD_LIVE_WRITE")!="1": self.skipTest("set NODEPAD_LIVE_WRITE=1 for isolated write")
        content="Agency Agents idempotency integration marker"
        key=idempotency_key(self.client.workspace,"live-integration","agency-agents-live-test","idempotency probe","https://example.invalid/agency-agents-live-test",content)
        payload={"claim":content,"polarity":"neutral","source":"https://example.invalid/agency-agents-live-test","source_type":"agency_agents_integration_test","actor":"agency-agents-live-test","idempotency_key":key}
        first=self.client.submit_evidence(payload); second=self.client.submit_evidence(payload)
        self.assertIsNotNone(first); self.assertIsNotNone(second)

if __name__=="__main__": unittest.main()
