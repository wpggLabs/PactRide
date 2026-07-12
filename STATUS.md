# PactRide Project Status

**Last reviewed:** 2026-07-11  
**Founder-vision status:** documented and complete  
**Implementation maturity:** pre-implementation research RFC  
**Public website:** https://wpgglabs.github.io/PactRide/  
**Current maintainer:** `wpggLabs`  
**Maintenance posture:** limited-capacity public research

## Canonical vision

PactRide is an open, interoperable ride-coordination protocol. It is intended to let independently developed rider, driver, cooperative, municipal, nonprofit, and commercial clients communicate without requiring one company to own discovery, identity, reputation, payment, or the rider–driver relationship.

The base protocol has:

- no mandatory platform operator;
- no protocol-level commission or protocol tax;
- no required token, wallet, map provider, payment processor, identity provider, relay, or official client;
- user-held cryptographic identity;
- coarse and short-lived public discovery;
- encrypted exact details and negotiation;
- portable, inspectable evidence instead of one global reputation score;
- replaceable internet relays, with nearby networking limited to verification and resilience;
- explicit safety, legal, privacy, and operational limitations.

Compatible products may charge transparent optional fees for software, hosting, operations, support, payments, or other services. Users and communities must remain able to choose competing implementations and infrastructure.

## Founder-vision documentation completion

The initial founder vision is fully represented in the repository as of 2026-07-11.

This means the public record now contains canonical material for:

- the problem, vision, principles, and non-goals;
- architecture, identities, discovery, negotiation, bilateral agreement, lifecycle, evidence, disputes, and versioning;
- strict schemas, semantic requirements, test vectors, lifecycle scenarios, and implementation guidance;
- privacy, security, threat, failure, accessibility, legal, operational, and responsibility boundaries;
- trust, reputation, moderation, attestations, and revocations;
- relay, Nostr, direct, and nearby-transport roles;
- governance, maintenance, succession, contribution, licensing, trademark, and sustainability policy;
- the non-dependent future relationship between PactRide and CommonPact.

The bounded meaning of completion is defined in [`FOUNDER_VISION.md`](FOUNDER_VISION.md). The CommonPact mapping and extraction rules are defined in [`COMMONPACT_RELATIONSHIP.md`](COMMONPACT_RELATIONSHIP.md).

Documentation completion does not imply implementation completion, independent interoperability, production safety, legal authorization, a functioning marketplace, or a commitment to launch.

## What exists now

### RFC and governance foundation

- Complete initial founder-authored vision, scope, principles, and non-goals.
- Architecture, threat model, privacy model, prior art, governance, contribution process, maintainer policy, maintenance policy, citation metadata, and evidence-gated roadmap.
- Formal documentation of what completion means and how PactRide relates to future CommonPact research.
- Public issues for protocol, privacy, mobile, accessibility, trust, interoperability, legal, pilot, and beginner-friendly contribution work.
- A GitHub Pages discovery site that presents PactRide as a protocol proposal rather than a live transportation service.
- A professional social-preview asset for the website and repository promotion.

### Machine-readable protocol work

- A strict v0.1 event envelope.
- RFC 8785 JSON Canonicalization Scheme and SHA-256 event-ID rules.
- A uniform `proofs[]` representation for single-party and bilateral events.
- Conditional ride scoping so non-ride identity and availability events do not require fake ride IDs.
- Positive TTL-based expiration.
- Privacy-safe public request schemas.
- Strict payload schemas covering every named v0.1 event family.
- An initial Nostr carrier, encryption, inbox-relay, authentication, retry, and capability profile.
- Executable lifecycle scenarios for normal, stale, duplicate, reordered, cancelled, aborted, expired, and disputed flows.
- A protocol-versus-client/operator responsibility matrix and implementer guide.
- Separate ride-aggregate and offer-thread state machines.
- Explicit post-pickup `ride.abort` behavior.
- Encrypted discovery-key to long-term-key binding.
- Normative and regression test vectors.
- GitHub Actions validation for protocol artifacts and public-message alignment.

These items are draft protocol evidence. They are not proof that two independent clients interoperate.

## Current roadmap position

PactRide currently overlaps two roadmap stages:

- **Phase 0 — RFC foundation:** founder-authored documentation deliverables are complete. External review, critical-objection resolution, and maintainer-diversity exit criteria are not complete.
- **Phase 1 — machine-readable protocol core:** canonical event IDs, event-family schemas, an initial Nostr profile, regression vectors, and executable lifecycle scenarios exist; independent encryption, relay-matrix, cross-language, security-review, and two-client conformance evidence remain incomplete.

PactRide has not entered independent client simulation, mobile reference implementation, community pilot, or production hardening.

## Maintenance and stewardship

PactRide is maintained as a limited-capacity public research project. It does not promise continuous development, response times, release dates, or a production launch.

The founder maintains the completed initial vision, repository, website, and public record but is not attempting to build or operate a production ride network alone. Major implementation should resume only when there are committed technical maintainers, funded research, or a credible bounded pilot partner.

See [`MAINTAINERS.md`](MAINTAINERS.md) for current authority and succession, and [`MAINTENANCE.md`](MAINTENANCE.md) for inactivity, archival, and restart policy.

## What is not implemented or proven

- No rider application.
- No driver application.
- No production relay network.
- No two-client interoperability demonstration.
- An initial Nostr profile exists, but no independent relay/client implementation has proven it interoperable or reliable.
- No mobile background-delivery or BLE reliability evidence.
- No production identity verification or credential network.
- No emergency response, insurance, payment protection, or dispute-resolution service.
- No proof that the design is safe for public-road transportation.
- No official compatibility certification program.
- No funded implementation team or committed pilot operator.

## Immediate gates

1. Obtain substantive external review of the complete founder-vision RFC and record critical objections publicly.
2. Implement the initial Nostr profile in two independent clients and publish the relay/encryption test matrix.
3. Expand executable state fixtures with cryptographically complete events and cross-language results.
4. Implement event-ID, envelope, event-family, and lifecycle validation independently in at least two languages.
5. Demonstrate two independently written command-line clients completing one ride transcript.
6. Model location correlation and Sybil/reputation farming with reproducible simulations.
7. Complete mobile delivery and nearby-network measurements before making reliability claims.
8. Recruit at least one additional sustained technical maintainer or institutional research partner before treating implementation as active.
9. Obtain appropriate legal and operational review before any real transportation pilot, trademark certification program, regulated payment activity, or safety-related commercial commitment.

## Future protocol-family research

CommonPact remains a possible later extraction, not a current dependency or stable specification. PactRide is authoritative and self-contained until a reusable core is proven in another substantially different domain.

See [`COMMONPACT_RELATIONSHIP.md`](COMMONPACT_RELATIONSHIP.md) for the candidate core mapping, profile boundaries, extraction criteria, compatibility rules, and safety-preservation requirements.

## Licensing status

- The current specification repository is licensed under the standard **Apache License 2.0** in the root [`LICENSE`](LICENSE) file.
- Apache-2.0 applies to the protocol documents, schemas, test vectors, website, automation, and code in this repository unless a file contains another explicit notice.
- Commercial and independent implementations are permitted subject to the license conditions.
- Apache-2.0 does not require payment, revenue sharing, or publication of modifications.
- Existing Apache-2.0 releases remain available under the rights already granted.
- Future official applications or hosted products may be placed in separate repositories with separately published software-license terms after appropriate rights and legal review; this does not restrict independent protocol implementations.
- The PactRide name and any future certification marks remain governed separately from the repository license.

See [`LICENSE`](LICENSE), [`LICENSING.md`](LICENSING.md), [`MONETIZATION.md`](MONETIZATION.md), [`CONTRIBUTOR_POLICY.md`](CONTRIBUTOR_POLICY.md), and [`TRADEMARK.md`](TRADEMARK.md).

## Claim discipline

Until the missing evidence exists, public material must describe PactRide as:

- a protocol proposal;
- a research RFC;
- founder-vision documented;
- pre-implementation;
- limited-capacity;
- open to independent review.

It must not describe PactRide as a launched rideshare network, production-safe service, verified identity system, guaranteed zero-fee marketplace, completed decentralized replacement for existing platforms, actively staffed product team, or independently proven standard.

## Synchronization rule

[`STATUS.md`](STATUS.md) is the canonical implementation-status summary. Changes that affect project maturity, founder-vision completion, licensing, lifecycle semantics, maintenance posture, stewardship, CommonPact dependency claims, or public claims must update this file, [`README.md`](README.md), and [`docs/index.html`](docs/index.html) together.

Changes to the bounded definition of founder-vision completion must also update [`FOUNDER_VISION.md`](FOUNDER_VISION.md). Changes to the PactRide/CommonPact relationship must also update [`COMMONPACT_RELATIONSHIP.md`](COMMONPACT_RELATIONSHIP.md).