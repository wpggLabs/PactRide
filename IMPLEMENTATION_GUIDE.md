# PactRide Implementer Guide

## Start here

PactRide is a protocol proposal, not a ready-made rideshare backend. A first implementation should prove deterministic interoperability before building a polished rider or driver application.

Read in this order:

1. [`RESPONSIBILITY_BOUNDARIES.md`](RESPONSIBILITY_BOUNDARIES.md) — what the protocol does and does not own.
2. [`PROTOCOL.md`](PROTOCOL.md) — application envelope, proofs, payload semantics, and validation.
3. [`NOSTR_PROFILE.md`](NOSTR_PROFILE.md) — initial public and encrypted carrier profile.
4. [`RIDE_LIFECYCLE.md`](RIDE_LIFECYCLE.md) — aggregate and offer-thread transitions.
5. [`schemas/protocol-event-types.schema.json`](schemas/protocol-event-types.schema.json) — payload coverage for every v0.1 event family.
6. [`test-vectors/`](test-vectors/) — canonical IDs, regression cases, event-family fixtures, and executable lifecycle scenarios.
7. [`examples/end-to-end-transcript.md`](examples/end-to-end-transcript.md) — one complete fictional request-to-receipt flow.
8. [`INTEROPERABILITY.md`](INTEROPERABILITY.md) — conformance levels and independence requirements.

## Minimum client layers

A minimal client needs separate modules for:

- key generation, storage, proof creation, and verification;
- RFC 8785 canonicalization and event-ID calculation;
- strict envelope and event-family payload validation;
- public-request privacy validation;
- Nostr carrier encoding, encryption, inbox discovery, retry, and deduplication;
- ride aggregate plus independent offer-thread state;
- encrypted local storage and exportable evidence;
- user-visible distinction between claims, bilateral proof, transport status, and external-service status.

Do not combine relay delivery state with ride state. Do not let UI convenience bypass semantic validation.

## Recommended implementation sequence

### Step 1 — Level 0 parser

- Parse the strict envelope.
- Recompute event IDs from the signing object.
- Verify every proof and exact signer sets.
- Validate all valid and invalid fixtures.
- Reject unsupported major versions and undeclared top-level fields.

### Step 2 — Public discovery

- Encode and decode the Nostr public carriers.
- Validate routing tags against the inner PactRide event.
- Enforce TTL and public privacy rules locally.
- Deduplicate one inner event received from several relays.

### Step 3 — Encrypted negotiation

- Implement NIP-17/NIP-44-v2/NIP-59 delivery.
- Resolve recipient inbox relays.
- Exchange full offers and counters, never ambiguous diffs.
- Verify the rotating discovery-key to long-term-key binding.
- Require two intentional accepts over the same current terms hash.

### Step 4 — Ride lifecycle

- Run every scenario in `test-vectors/lifecycle-v0.1.json`.
- Keep aggregate ride state separate from offer-thread state.
- Reject stale, reordered, impossible, and post-pickup cancellation transitions.
- Preserve conflicting valid claims and surface disputes.

### Step 5 — Independent transcript

- Complete `examples/end-to-end-transcript.md` with another implementation written in a different language.
- Export a bilateral receipt from one client and verify it in the other.
- Demonstrate behavior under duplicate delivery and one relay outage.

## Definition of a useful first implementation

A command-line implementation is useful when it can:

1. create an identity;
2. publish and discover a privacy-safe request;
3. exchange an encrypted offer and counter;
4. bind a discovery key to a long-term identity privately;
5. double-accept identical terms;
6. create a bilateral pickup proof;
7. record normal completion or abnormal termination;
8. export and independently verify the resulting evidence;
9. reproduce every conformance vector without shared protocol code.

A mobile UI, payment integration, public relay deployment, or real ride pilot is not required for this milestone.

## Security rules for implementers

- Never log private keys, decrypted exact locations, contact details, or raw private messages.
- Treat every relay, map provider, notification service, counterparty, and imported attestation as a separate trust boundary.
- Apply byte-size limits before expensive parsing or decryption.
- Use established cryptographic libraries; do not invent encryption or signature primitives.
- Preserve original signed events when converting or displaying them.
- Fail closed on unknown major versions, malformed proofs, mismatched carrier tags, or unsupported encryption profiles.
- Do not describe a passing test suite as proof of transportation safety.
