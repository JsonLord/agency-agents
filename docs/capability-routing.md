# Capability routing

Five semantic capabilities decouple personas from vendors. Providers declare priority, free status, availability, health, authentication environment reference, fallback, scope, and approval. The router selects a healthy free provider before paid providers and refuses approval-gated writes unless explicitly approved.

Donor integration adds semantic routes for Hacker News, GitHub and Trends. Resolution excludes unhealthy, unavailable, rate-limited, or credential-dependent providers whose environment variable is absent, then prefers free providers by priority. Provider code remains outside personas and returns normalized transient research.

## Runtime fallback

The router returns a resolution path containing requested capability, resolved capability, selected provider, and fallback chain. It excludes unavailable, unhealthy, rate-limited, and credential-blocked providers, prefers free providers, follows semantic fallbacks with depth/cycle protection, and never escalates a read request into write scope.
