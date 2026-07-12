# Public RFC Launch Checklist

PactRide should be announced as a request for criticism and collaboration, not as a functioning ride service.

## Repository readiness

- [x] Clear problem statement.
- [x] Vision, principles, and non-goals.
- [x] Architecture and ride lifecycle diagrams.
- [x] Draft protocol envelope.
- [x] Privacy and threat models.
- [x] Prior-art review.
- [x] Governance and contribution process.
- [x] Machine-readable draft schemas.
- [x] Fictional end-to-end transcript.
- [x] Security reporting policy.
- [ ] Independent review of cryptographic assumptions.
- [ ] Primary-source links completed for all prior-art entries.
- [ ] GitHub Discussions enabled.
- [ ] Repository description and topics configured.
- [ ] Dedicated private security contact configured.

## Messaging requirements

Every announcement should state:

- This is a research RFC, not a live service.
- The general decentralized rideshare idea has prior art.
- The project seeks protocol, privacy, safety, accessibility, and adoption criticism.
- No token or investment is involved.
- Internet relays are primary; Bluetooth is a bounded fallback research track.
- Contributors can participate without committing to build an entire application.

## Audiences

- Nostr protocol developers.
- Mobile and applied cryptography engineers.
- Open mobility and transportation researchers.
- Driver cooperatives.
- Rideshare drivers and riders.
- Accessibility specialists.
- Privacy and abuse researchers.
- Open-source governance practitioners.
- Mapping and routing communities.

## First discussion prompts

1. Can rotating discovery identities preserve portable trust without publicly linking travel requests?
2. Is coarse geohash discovery sufficiently private and useful?
3. What is the minimum bilateral ride receipt?
4. How should clients represent disputes without a global arbiter?
5. Which attestations are useful without creating one mandatory verifier?
6. Which Nostr event/encryption profile should PactRide standardize?
7. What breaks under realistic mobile background restrictions?
8. How can two independent clients prove interoperability early?
9. What accessibility needs are missing from the request schema?
10. What would make a real driver/rider community test this instead of ignoring it?

## Do not announce with

- “Uber killer.”
- “Fully decentralized and unstoppable.”
- “Safe because blockchain/cryptography.”
- “Zero cost forever.”
- “No regulation applies.”
- “Production-ready.”
- “First decentralized rideshare.”

## Evidence to collect after launch

- Number of substantive reviews, not stars alone.
- Security and privacy objections.
- Independent implementation interest.
- Driver/rider workflow corrections.
- Prior projects or standards discovered.
- Maintainer candidates.
- Which issues attract work versus ideological discussion.

## Go/no-go checkpoint

Continue toward test vectors only if external contributors identify concrete value and at least two people outside the founder express serious interest in implementing or reviewing specific components.
