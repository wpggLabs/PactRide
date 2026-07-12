# Problem Statement

## Core problem

Modern ride-hailing usually requires drivers and riders to enter a privately owned marketplace. The platform does more than route messages: it controls discovery, rankings, pricing interfaces, identity records, reputation, access to customers, account status, and often payment. The resulting dependency creates a structural imbalance even when the software is convenient.

PactRide is an attempt to separate **ride coordination** from **platform ownership**.

## Stakeholders

### Drivers

Drivers may experience:

- High or unpredictable platform deductions.
- Limited visibility into how a fare was calculated.
- Loss of access through opaque deactivation.
- No portable reputation when moving to another service.
- No durable relationship with repeat riders.
- Algorithmic dispatch without inspectable rules.
- Dependence on one company's application, maps, support, and payment systems.

### Riders

Riders may experience:

- Dynamic pricing with weak transparency.
- No portable trust history across services.
- Limited ability to choose preferred drivers or community policies.
- Centralized collection of sensitive travel histories.
- Service withdrawal when a platform decides a location is unprofitable.
- Lock-in to one application and its dispute process.

### Communities

Local cooperatives, nonprofits, municipalities, campuses, event organizers, and mutual-aid groups may want ride coordination without building an entire proprietary stack. Today they typically must either use a large platform or recreate identity, dispatch, mapping, trust, and client software from scratch.

## Technical problem

The protocol must allow strangers or community members to discover one another without publicly exposing exact travel plans, negotiate privately, agree on terms, verify pickup, exchange trip-state updates, and generate portable evidence of completion—while avoiding a mandatory central server.

That requires solving or containing:

- Sparse local participation.
- Relay disagreement and outages.
- Location privacy.
- Spam and fake identities.
- Conflicting event histories.
- Key loss and rotation.
- Reputation farming and collusion.
- Mobile background restrictions.
- Physical pickup verification.
- Accessibility representation.
- Payment neutrality.
- Disputes that cryptography cannot settle.

## Social problem

The hardest problem is not message transport. It is trust without recreating a single owner.

PactRide therefore treats trust as plural and evidence-based. A client may consider key age, completed ride receipts, repeat counterparties, community attestations, local block lists, and optional external credentials. Different communities may make different policy choices while still using the same ride protocol.

## Opportunity

An open protocol could allow:

- A driver cooperative and a nonprofit rider application to interoperate.
- A neighborhood relay to exchange requests with a broader public relay set.
- A rider to move between apps without abandoning identity and history.
- A driver to use multiple compatible clients without rebuilding reputation.
- Independent developers to improve accessibility, privacy, dispatch, maps, or user experience without permission from a platform owner.
- Communities to experiment with subscriptions, donations, public funding, direct payments, or no-fee coordination without changing the base protocol.

## Success definition

PactRide has not succeeded when one official app is popular. It succeeds when:

1. At least two independently implemented clients complete the same end-to-end ride flow.
2. No required relay, identity provider, map provider, payment provider, or application is controlled by the PactRide maintainers.
3. A participant can export identity and verifiable history to another compatible client.
4. Public discovery does not require publishing exact pickup or destination details.
5. Protocol limitations and residual risks are visible to users and implementers.
6. The specification can continue without its original founder.
