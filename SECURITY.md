# Security Policy

## Current status

PactRide is a pre-implementation research specification. No production deployment is endorsed by this repository.

## Reporting vulnerabilities

Do not publish exploit details involving active users, private keys, exact locations, or deployed experimental systems in a public issue.

Until a dedicated security contact is established, open a minimal public issue titled `Security contact requested` without sensitive details. Maintainers will provide a private reporting channel.

## In scope

- Signature or canonicalization flaws.
- Encryption misuse.
- Key custody, backup, and rotation failures.
- Exact-location or identity leakage.
- Replay and state-machine confusion.
- Pickup-proof bypass.
- Relay metadata or censorship weaknesses.
- BLE tracking, impersonation, or flooding.
- Schema fields that enable unsafe public disclosure.
- Supply-chain risks in future reference implementations.

## Out of scope for a protocol vulnerability claim

These remain serious but cannot be solved solely through protocol patches:

- Physical assault.
- Dishonest ratings.
- Fake external credentials issued by a trusted attestor.
- Failure of emergency services.
- Cash disputes without independent evidence.
- Local clients intentionally implementing discriminatory policies.

Reports about these issues are still useful as threat-model or governance contributions.

## Disclosure process

1. Maintainers acknowledge receipt.
2. Scope and affected documents/implementations are identified.
3. A private fix or specification correction is prepared when necessary.
4. Relevant implementers receive coordinated notice.
5. A public advisory documents impact, affected versions, mitigation, and residual risk.

## Security principles

- Do not invent cryptography.
- Prefer reviewed standards and libraries.
- Keep private keys hardware-backed where possible.
- Use end-to-end encryption on every private transport.
- Treat relays as untrusted.
- Distinguish signed claims from real-world truth.
- Minimize public location data.
- Preserve conflicting evidence rather than silently rewriting history.
- Require reproducible tests for security-sensitive changes.
