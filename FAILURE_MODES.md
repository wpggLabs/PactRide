# Failure Modes

PactRide should be designed around how it can fail, not only around ideal message flows.

## Technical failures

### Empty local market

**Failure:** riders see no drivers and drivers see no riders.

**Impact:** users abandon the network before density forms.

**Mitigation:** start within existing communities; support scheduled rides, favorites, and direct relationships; expose search reach honestly.

### Relay fragmentation

**Failure:** rider and driver use relay sets with no overlap.

**Mitigation:** regional defaults, relay recommendation documents, multi-relay publishing, community bridges, and reach diagnostics.

### Relay censorship

**Failure:** one relay suppresses users, regions, or event types.

**Mitigation:** replaceable relay sets, cross-relay comparison, self-hosting, and no relay-authoritative ordering.

### Key loss

**Failure:** user loses identity and portable history.

**Mitigation:** encrypted backups, multi-device authorization, rotation, and clearly labeled community recovery attestations.

### Key compromise

**Failure:** attacker signs valid-looking events.

**Mitigation:** revocation, rotation, compromise timestamps, hardware-backed keys, and rapid community warnings.

### Public location leakage

**Failure:** requests expose homes, destinations, routines, or vulnerable users.

**Mitigation:** coarse geographies, short expiration, rotating discovery keys, private destination modes, and schema linting.

### Background suspension

**Failure:** mobile OS stops relay sockets, BLE scans, or direct connections.

**Mitigation:** platform-supported push, visible delivery state, encrypted queues, bounded retry, and no always-on mesh promises.

### State divergence

**Failure:** devices disagree because messages arrive late, duplicated, crossed, or reordered.

**Mitigation:** causal references, immutable terms hashes, bilateral acceptance, deterministic state rules, and conflict preservation.

### Map or route provider outage

**Failure:** app cannot calculate ETA or route.

**Mitigation:** provider abstraction, external-navigation fallback, cached maps, multiple routing providers, and protocol independence from route estimates.

### Notification failure

**Failure:** user misses an offer or arrival message.

**Mitigation:** in-app polling, several transport paths, expiration, visible notification health, and no silent automatic acceptance.

## Security and abuse failures

### Sybil saturation

Fake keys dominate discovery or ratings. Mitigations are layered but imperfect: rate limits, proof-of-work, attestations, key age, graph diversity, and community policy.

### Reputation capture

A vendor creates a dominant proprietary score and becomes a new gatekeeper. Mitigation: portable raw evidence, transparent local evaluation, and no canonical score.

### Attestor capture

One verifier becomes mandatory. Mitigation: multiple issuers, scoped claims, expiry, revocation, and user-selectable trust policy.

### Harassment after disclosure

A counterparty misuses exact locations or contact details. Mitigation: delayed disclosure, in-protocol communication, blocks, evidence preservation, and minimal data sharing. Residual risk remains.

### False safety confidence

Users interpret cryptographic signatures as guarantees of physical safety. Mitigation: precise language, layered evidence display, and no “verified safe” badge.

## Governance failures

### Founder bottleneck

All decisions depend on the original founder.

Mitigation: public RFCs, additional maintainers, documented succession, open licenses, and independent implementations.

### Corporate capture

A well-funded company dominates maintainers, default relays, or client distribution.

Mitigation: conflict disclosure, no paid voting, no canonical relay, independent conformance, and diversified maintainers.

### Ideological capture

The project prioritizes decentralization slogans over usability, safety, accessibility, or evidence.

Mitigation: principles, measurable phase gates, driver/rider review, and explicit stop conditions.

### Token distraction

Speculation redirects effort from protocol and community problems.

Mitigation: no native token and payment neutrality in the base protocol.

### Standards stagnation

Documentation grows but no independent implementation appears.

Mitigation: early parsers, test vectors, command-line clients, and roadmap exit criteria.

## Operational failures

### No incident owner

A community launches but nobody handles abuse, compromised keys, or relay outages.

Mitigation: require pilot-specific operating responsibility and public escalation procedures. The base protocol cannot provide operations by itself.

### Cost denial

Participants assume open source means free infrastructure.

Mitigation: document relay, map, support, security, and verification costs; allow transparent plural funding models.

### App-store dependency

Mobile distribution is blocked or delayed.

Mitigation: web/PWA and sideloadable builds where possible, reproducible releases, multiple clients, and no protocol dependency on one store.

## Adoption failures

### Too broad a launch

A global launch creates empty local markets.

Mitigation: begin with existing driver/rider groups and repeat/scheduled rides.

### No reason to switch

Lower fees alone may not overcome reliability and trust gaps.

Mitigation: portable favorite-driver relationships, community ownership, transparent pricing, privacy, and interoperability.

### Driver-only interest

Drivers join but riders do not.

Mitigation: solve rider reliability, safety, usability, and support—not only driver economics.

### Rider-only interest

Requests exist without dependable driver supply.

Mitigation: recruit communities with existing driver density and schedule predictable routes.

## Stop-and-reassess triggers

- Public requests require exact coordinates to match effectively.
- Users routinely misunderstand signed claims as verification.
- One relay or client becomes technically mandatory.
- Independent implementation remains impossible.
- Abuse controls require centralized surveillance.
- A pilot community cannot assign operational responsibility.
- Contributors repeatedly prioritize tokens or proprietary extensions over conformance.
