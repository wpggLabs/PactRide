# PactRide Design Principles

These principles constrain protocol decisions. A proposal that violates one should explain why and obtain explicit RFC approval.

## 1. Protocol before platform

PactRide is successful only when independently developed clients can interoperate. A polished official application without independent compatibility is a platform, not a protocol.

## 2. User-held identity

A participant's core identity is controlled by cryptographic keys held by the participant. Applications may help with custody and recovery but must not require a platform-owned account as the only identity.

## 3. Replaceable infrastructure

No relay, map provider, routing engine, notification provider, attestation issuer, moderation service, payment method, or application is mandatory at the base-protocol level.

## 4. Data minimization by default

Public discovery events must disclose the minimum information needed to find potential counterparties. Exact pickup points, destinations, contact details, continuous location, and private negotiation terms belong in encrypted channels.

## 5. Explicit trust, not implied trust

A signature proves control of a key. It does not prove that a person is safe, licensed, truthful, insured, solvent, or physically present. Interfaces and specifications must not blur that distinction.

## 6. Plural trust

Different communities may rely on different attestors, block lists, identity checks, or safety policies. The protocol should transport verifiable evidence without imposing one universal authority or global reputation score.

## 7. Portable evidence

Ride receipts, attestations, ratings, and key-rotation statements should be portable between compatible clients. Evidence must remain inspectable rather than collapsing into an unexplained score.

## 8. Payment neutrality

The protocol may represent agreed terms and settlement evidence, but must not require a native token, central wallet, mandatory processor, or platform commission.

## 9. Progressive resilience

Reliable internet-relay coordination is the first target. Direct channels and nearby-device transports add resilience. Experimental mesh routing must not delay a usable interoperable core.

## 10. Safe failure

When data is missing, signatures conflict, relays disagree, or transport fails, clients should fail visibly and conservatively. They must not silently invent completion, identity, payment, or safety guarantees.

## 11. Local policy remains local

Clients and communities may choose stricter participation rules. Those rules must be described as local policy rather than falsely presented as protocol-wide truth.

## 12. Forkability and succession

The specification, schemas, test vectors, and governance history must be sufficient for the project to continue if the original maintainers disappear.

## 13. No hidden extraction

Compatible clients should disclose fees, paid routing, preferred relays, sponsored ranking, data collection, and third-party services. PactRide should not recreate opaque platform control under a different name.

## 14. Interoperability over feature velocity

Breaking compatibility requires a versioned migration and public rationale. Fast unilateral changes are less valuable than stable shared behavior.

## 15. Claims follow evidence

Security, privacy, reliability, decentralization, and adoption claims must be tied to tests, measurements, or clearly labeled assumptions.
