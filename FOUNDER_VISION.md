# PactRide Founder Vision and Documentation Completion

**Founder-vision status:** complete as of 2026-07-11  
**Project maturity:** pre-implementation research RFC  
**Canonical implementation status:** [`STATUS.md`](STATUS.md)

## Purpose of this document

This document defines what it means for the original PactRide vision to be fully documented.

It does **not** declare PactRide production-ready, technically proven, legally approved, operationally safe, or implemented. It records that the founder's current ride-coordination vision has been translated from an idea into a coherent public body of work with explicit scope, protocol behavior, risks, limits, governance, licensing, and implementation gates.

Future discoveries may improve or replace parts of the proposal through the public RFC process. They do not make the original vision undocumented again.

## Canonical founder vision

PactRide is an open, interoperable protocol for ride coordination. It is intended to let independently developed rider and driver applications discover counterparties, negotiate privately, form bilateral agreements, coordinate ride state, and retain portable evidence without requiring one company to own the coordination layer.

The protocol is designed to support commercial, cooperative, nonprofit, municipal, institutional, and volunteer implementations without requiring one official application, operator, relay, payment processor, identity provider, or per-ride protocol commission.

## Decisions represented in the repository

The founder vision is considered documented because the repository now records decisions and boundaries for every major area below.

### 1. Problem and public-purpose thesis

- The shared ride-coordination language should be separable from any one marketplace operator.
- Drivers and riders should be able to change compatible applications without losing protocol access.
- An open protocol does not eliminate transportation safety, density, insurance, legal, support, or operational requirements.

Canonical documents: [`VISION.md`](VISION.md), [`PROBLEM_STATEMENT.md`](PROBLEM_STATEMENT.md), and [`PRIOR_ART.md`](PRIOR_ART.md).

### 2. Scope and non-goals

- PactRide is a protocol proposal, not a launched transportation company.
- It is not a blockchain, token, DAO, universal identity authority, insurer, emergency service, payment processor, court, or guarantee of safe conduct.
- Optional applications and services may charge transparent fees, but base protocol access does not require a fee payable to PactRide.

Canonical documents: [`PRINCIPLES.md`](PRINCIPLES.md), [`NON_GOALS.md`](NON_GOALS.md), and [`RESPONSIBILITY_BOUNDARIES.md`](RESPONSIBILITY_BOUNDARIES.md).

### 3. Identity and authorization

- Users control cryptographic keys.
- Public discovery may use rotating or temporary identities.
- Long-term identity reliance requires an encrypted, proof-backed binding.
- Signatures establish authorization by keys; they do not prove legal identity, honesty, safety, payment, or physical events by themselves.

Canonical documents: [`IDENTITY.md`](IDENTITY.md), [`PROTOCOL.md`](PROTOCOL.md), and [`THREAT_MODEL.md`](THREAT_MODEL.md).

### 4. Discovery and matching

- Public discovery is coarse, short-lived, signed, and client-validated.
- Exact pickup, destination, contact details, continuous location, and private notes do not belong in public discovery events.
- Relays distribute events; clients decide relevance, ranking, trust, and local policy.
- No canonical dispatcher or global matching authority is required by the protocol.

Canonical documents: [`DISCOVERY_AND_MATCHING.md`](DISCOVERY_AND_MATCHING.md), [`PRIVACY.md`](PRIVACY.md), and the public-event schemas in [`schemas/`](schemas/).

### 5. Private negotiation and agreement

- Offers and counters restate complete proposed terms rather than ambiguous partial changes.
- Agreement exists only when both accepted participants authorize the same terms hash.
- Crossing messages, stale acceptance, and unrelated offer threads must not silently create agreement.
- Exact details are exchanged through encrypted channels under intentional disclosure rules.

Canonical documents: [`PROTOCOL.md`](PROTOCOL.md), [`RIDE_LIFECYCLE.md`](RIDE_LIFECYCLE.md), and [`examples/end-to-end-transcript.md`](examples/end-to-end-transcript.md).

### 6. Ride lifecycle and conflict handling

- The ride aggregate and individual offer threads are separate.
- Cancellation applies before pickup verification; abort applies after pickup verification or ride start.
- One-sided completion is a claim.
- Only matching bilateral proofs over one event create a portable completion receipt.
- Conflicting valid evidence is preserved and may produce a disputed state rather than being erased or resolved by relay arrival order.

Canonical documents: [`RIDE_LIFECYCLE.md`](RIDE_LIFECYCLE.md), [`PROTOCOL.md`](PROTOCOL.md), and the executable scenarios in [`test-vectors/lifecycle-v0.1.json`](test-vectors/lifecycle-v0.1.json).

### 7. Trust, reputation, and moderation

- PactRide uses inspectable evidence rather than one mandatory global reputation score.
- Attestations, credentials, warnings, ratings, revocations, key history, and bilateral receipts remain distinguishable by provenance and confidence.
- Clients and communities evaluate evidence under visible local policy.
- The base protocol does not create a universal "verified safe" status.

Canonical documents: [`TRUST_AND_REPUTATION.md`](TRUST_AND_REPUTATION.md), [`IDENTITY.md`](IDENTITY.md), and [`RESPONSIBILITY_BOUNDARIES.md`](RESPONSIBILITY_BOUNDARIES.md).

### 8. Transport and resilience

- Application semantics are transport-independent.
- The first concrete internet profile uses Nostr-compatible relays and encrypted private messaging.
- Delivery acknowledgement is not agreement or proof of a ride-state transition.
- Multi-relay publication, deduplication, retry, expiry, and local validation are required concepts.
- Bluetooth and nearby networking are limited initial tools for pickup verification and degraded connectivity, not a claim of reliable citywide phone mesh dispatch.

Canonical documents: [`TRANSPORTS.md`](TRANSPORTS.md), [`NOSTR_PROFILE.md`](NOSTR_PROFILE.md), [`RELAY_NETWORK.md`](RELAY_NETWORK.md), and [`OFFLINE_MESH.md`](OFFLINE_MESH.md).

### 9. Interoperability and implementation

- The protocol has deterministic event IDs, strict envelopes, event-family schemas, proof rules, semantic validation requirements, test vectors, and lifecycle fixtures.
- Compatibility depends on independent implementations producing the same results.
- The specification does not treat its own reference validator as sufficient interoperability evidence.

Canonical documents: [`INTEROPERABILITY.md`](INTEROPERABILITY.md), [`IMPLEMENTATION_GUIDE.md`](IMPLEMENTATION_GUIDE.md), [`schemas/`](schemas/), [`test-vectors/`](test-vectors/), and [`scripts/validate_protocol_artifacts.py`](scripts/validate_protocol_artifacts.py).

### 10. Safety, privacy, legal, and operational limits

- The protocol cannot guarantee physical safety, lawful operation, insurance coverage, emergency response, payment finality, credential truth, dispute enforcement, or market liquidity.
- Those responsibilities belong to clients, operators, communities, external providers, participants, and applicable authorities according to the documented boundary matrix.
- No real-world pilot should proceed without named operational responsibility and appropriate professional review.

Canonical documents: [`SECURITY.md`](SECURITY.md), [`PRIVACY.md`](PRIVACY.md), [`THREAT_MODEL.md`](THREAT_MODEL.md), [`FAILURE_MODES.md`](FAILURE_MODES.md), [`LEGAL_REVIEW_CHECKLIST.md`](LEGAL_REVIEW_CHECKLIST.md), and [`RESPONSIBILITY_BOUNDARIES.md`](RESPONSIBILITY_BOUNDARIES.md).

### 11. Economics, licensing, and official status

- The specification repository is available under Apache License 2.0.
- Apache-2.0 does not require royalties, revenue sharing, permission for independent implementations, or publication of modifications.
- The PactRide name, logo, endorsement, and any future certification marks are separate from the copyright license.
- Future official applications or hosted products may use a different published software-license model in separate repositories, but that does not retroactively restrict the open specification or independent clean-room implementations.
- Sustainable revenue should come from optional software, services, support, infrastructure, audits, integrations, certification, partnerships, grants, or sponsorships—not a hidden protocol toll.

Canonical documents: [`LICENSE`](LICENSE), [`LICENSING.md`](LICENSING.md), [`MONETIZATION.md`](MONETIZATION.md), and [`TRADEMARK.md`](TRADEMARK.md).

### 12. Governance, maintenance, and succession

- Protocol decisions are public and reviewable.
- The founder currently maintains the repository but is not intended to remain a permanent global gatekeeper.
- Maintainer admission, conflicts, inactivity, archival, restart, and succession are documented.
- The project may remain in limited-capacity maintenance until credible contributors, research support, or pilot partners appear.

Canonical documents: [`GOVERNANCE.md`](GOVERNANCE.md), [`MAINTAINERS.md`](MAINTAINERS.md), [`MAINTENANCE.md`](MAINTENANCE.md), [`CONTRIBUTING.md`](CONTRIBUTING.md), and [`CONTRIBUTOR_POLICY.md`](CONTRIBUTOR_POLICY.md).

## Meaning of "100% documented"

For PactRide, **100% documented** means:

1. Every major part of the founder's current vision has a canonical repository location.
2. Core terms, lifecycle behavior, privacy boundaries, responsibility boundaries, economic intent, and governance do not depend on private notes or prior chat history.
3. The proposal includes machine-readable artifacts sufficient for independent implementers to identify ambiguities and attempt conformance.
4. Claims are separated from evidence, and aspirations are separated from implemented facts.
5. Known unresolved questions are recorded as research, implementation, review, or operational gates rather than omitted from the public record.
6. A future maintainer can understand the intended project without requiring the founder to restate the vision privately.

It does **not** mean:

- every possible ride type or jurisdiction is specified;
- the protocol is frozen permanently;
- every design decision is correct;
- independent interoperability has been demonstrated;
- production clients or infrastructure exist;
- the protocol is safe or lawful for real transportation deployment;
- contributors, funding, users, or operators are guaranteed to appear.

## What remains after documentation completion

The remaining work is evidence and execution, not missing founder vision:

1. Independent technical and security review.
2. Cryptographically complete cross-language conformance fixtures.
3. Two independent validators and command-line clients.
4. Relay, encryption, retry, duplicate, reordering, and outage measurements.
5. Privacy, Sybil, moderation, and reputation simulations.
6. Mobile background-delivery and nearby-network measurements.
7. Accessibility and usability review.
8. Legal, insurance, payment, emergency, and operational design by accountable domain participants.
9. Maintainer and partner recruitment.
10. Any carefully bounded pilot justified by prior evidence.

These gates are tracked in [`STATUS.md`](STATUS.md), [`ROADMAP.md`](ROADMAP.md), and public issues.

## Relationship to CommonPact

PactRide is complete as a self-contained ride-coordination proposal. It does not depend on CommonPact.

CommonPact is a planned later effort to test whether reusable concepts—identity, discovery, private negotiation, bilateral agreement, lifecycle events, and portable evidence—can form a domain-neutral coordination core. The relationship and extraction rules are documented in [`COMMONPACT_RELATIONSHIP.md`](COMMONPACT_RELATIONSHIP.md).

A future CommonPact specification must be derived from multiple coherent profiles. It must not erase or weaken transportation-specific privacy, accessibility, safety, legal, or operational requirements in PactRide.

## Change discipline after completion

After this completion point:

- Corrections, clarifications, evidence, test vectors, and implementation feedback may update the RFC through normal review.
- New protocol scope must identify the concrete failure it solves and follow the RFC process.
- CommonPact work must not be inserted into PactRide as speculative generic abstraction unless it improves the ride profile directly.
- Public claims must continue to match [`STATUS.md`](STATUS.md).
- A formal protocol release remains gated by independent implementation and review evidence.

## Completion statement

As of 2026-07-11, the repository contains the complete initial founder vision for PactRide as a public, pre-implementation ride-coordination RFC.

PactRide can now remain in documentation maintenance while independent contributors, researchers, organizations, or funders determine whether the proposal progresses into interoperable software, a bounded experiment, a standards effort, or an archived public design record.