# Research providers

All research providers implement the same `health()` and `search(query, limit, context)` protocol and normalize results to provider, query, retrieval time, intent, health, and source items. Supported semantic routes cover Hacker News, GitHub, generic web/DDGS, Reddit, and Trends. Provider material is transient research until a specialist creates a provenance-complete evidence candidate and submits it through the Nodepad gateway.

Routing prefers healthy free providers, excludes rate-limited providers, and marks providers with missing credential environment variables unavailable. Fallback metadata enables orchestrators to degrade explicitly; no result is fabricated. Credentials are referenced by environment-variable name and are never serialized.

Research intents are `support`, `disconfirm`, `discriminate`, `refresh`, and `discover`. Important hypotheses should request `disconfirm` or `discriminate` before more confirmation.
