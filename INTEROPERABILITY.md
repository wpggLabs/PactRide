# Interoperability and Conformance

## Definition

A PactRide-compatible implementation is one that exchanges, validates, and interprets protocol events consistently with independent implementations. Compatibility is determined by public tests, not permission from the maintainers.

## Compatibility levels

### Level 0 — Parser

- Parses strict canonical envelopes.
- Recomputes event IDs from the signing object.
- Validates proof arrays, timestamps, TTL, ride scope, and schema version.
- Rejects undeclared top-level fields and unsupported major versions.

### Level 1 — Discovery

- Publishes and consumes whole-envelope privacy-safe ride requests.
- Derives location precision from geohash length.
- Handles neighboring geographic cells.
- Deduplicates events from several relays.
- Withdraws and expires requests correctly using signed creation time plus TTL.

### Level 2 — Negotiation

- Exchanges encrypted offers and counters.
- Verifies discovery-to-identity bindings before accepting a key switch.
- Detects stale acceptances.
- Requires both parties to accept identical terms.
- Treats `Declined` and `Expired` as offer-thread outcomes, not ambiguous global states.

### Level 3 — Ride lifecycle

- Implements pickup challenge and bilateral proof arrays.
- Applies separate ride-aggregate and offer-thread transition rules.
- Supports pre-pickup cancellation and post-pickup abort.
- Distinguishes unilateral completion claims from bilateral receipts.
- Exports portable ride evidence.

### Level 4 — Trust evidence

- Imports and verifies attestations, revocations, receipts, and ratings.
- Shows provenance and local policy.
- Does not present a local score as protocol-wide truth.

### Level 5 — Resilient transport

- Supports several relay operators.
- Preserves behavior under duplicate, delayed, and reordered delivery.
- Supports at least one optional direct or nearby transport without altering protocol semantics.

## Conformance artifacts

Start with `IMPLEMENTATION_GUIDE.md`, `NOSTR_PROFILE.md`, `schemas/protocol-event-types.schema.json`, `test-vectors/protocol-event-types-v0.1.json`, `test-vectors/lifecycle-v0.1.json`, and `examples/end-to-end-transcript.md`.

The repository should provide:

- Strict JSON schemas.
- Whole-envelope public-event schemas.
- Canonical serialization and event-ID vectors.
- Valid and invalid proof vectors.
- Encryption test vectors.
- State-machine fixtures.
- Multi-relay duplicate/reorder scenarios.
- Privacy lint rules.
- Import/export examples.
- End-to-end transcripts.

## Version negotiation

- Major versions indicate breaking semantic changes.
- Minor versions add optional capabilities within declared extension points.
- Events advertise protocol and schema versions.
- Clients should declare supported capabilities during encrypted negotiation.
- Unknown top-level fields are invalid in v0.1.
- Compatible private extensions belong in the namespaced `extensions` object.
- Public discovery extensions require an accepted RFC and schema revision.

## Capability document

```json
{
  "protocol": "pactride",
  "versions": ["0.1"],
  "capabilities": [
    "envelope.strict",
    "event-id.jcs-sha256",
    "proofs.explicit-array",
    "discovery.geohash-derived-precision",
    "negotiation.identity-binding",
    "pickup.qr",
    "receipt.bilateral",
    "lifecycle.abort",
    "attestation.basic"
  ],
  "limits": {
    "max_event_bytes": 16384,
    "max_negotiation_rounds": 8
  }
}
```

## Independence test

Before a stable release, the full ride transcript must be completed by two clients that do not share core protocol code. Shared cryptographic libraries are acceptable; shared state-machine implementation is not sufficient evidence of independent interpretation.

Both clients must independently:

- Reproduce the canonical event-ID vectors.
- Reject every invalid review case.
- Produce identical signer-set decisions for bilateral events.
- Produce identical aggregate and offer-thread states under reordering.

## No official-client privilege

Reference clients must not use undocumented fields, private relay behavior, hidden allowlists, or proprietary ranking to obtain protocol advantages.

## Fork compatibility

A fork may truthfully claim compatibility when it passes the applicable public conformance level. Trademark or governance disagreement must not be used to block technical interoperability claims.

## Compatibility failures

When a client encounters unsupported behavior it should:

- Preserve the original signed event when safe.
- Explain the unsupported capability.
- Avoid destructive conversion.
- Offer safe downgrade only when confidentiality and semantics remain intact.
- Never infer agreement from data it cannot validate.
