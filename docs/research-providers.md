# Research providers

All research providers implement the same `health()` and `search(query, limit, context)` protocol and normalize results to provider, query, retrieval time, intent, health, and source items. Supported semantic routes cover Hacker News, GitHub, generic web/DDGS, Reddit, and Trends. Provider material is transient research until a specialist creates a provenance-complete evidence candidate and submits it through the Nodepad gateway.

Routing prefers healthy free providers, excludes rate-limited providers, and marks providers with missing credential environment variables unavailable. Fallback metadata enables orchestrators to degrade explicitly; no result is fabricated. Credentials are referenced by environment-variable name and are never serialized.

Research intents are `support`, `disconfirm`, `discriminate`, `refresh`, and `discover`. Important hypotheses should request `disconfirm` or `discriminate` before more confirmation.

## Production adapters versus fixtures

`HackerNewsProvider`, `GitHubProvider`, `WebProvider`, `RedditProvider`, and `TrendsProvider` are network-capable read adapters. Hacker News uses Algolia's public API; GitHub uses public Search with an optional `GITHUB_TOKEN`; web research uses DuckDuckGo's bounded Instant Answer API; Reddit requires `REDDIT_ACCESS_TOKEN`; Trends returns an honest degraded exploration link because automated upstream access is brittle. `StaticProvider` is explicitly reserved for deterministic tests and fixtures.

All adapters normalize provenance and classify network/rate-limit failures without serializing credentials. Opt-in smoke tests use `LIVE_PROVIDER_TESTS=1`; normal CI stays deterministic.
