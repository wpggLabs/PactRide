# PactRide v0.1 Semantic Validation

JSON Schema validates document shape. A conforming PactRide validator MUST also apply the rules below in this order.

## 1. Select the correct schema

- All events: `event-envelope.schema.json`.
- Public `ride.request`: `public-ride-request-event.schema.json`, not the payload schema alone.
- Validate the full decrypted event before state processing.

## 2. Reject legacy contradictory representations

The following fields from earlier drafts are invalid in v0.1:

- Top-level `signature`.
- Top-level `signatures`.
- Top-level `expires_at`.
- `pickup.precision` or `destination.precision`.
- Ride windows using `earliest` and `latest`.

Use:

- `proofs[]` for one or more signatures.
- `ttl_seconds` for effective expiry.
- Geohash string length for precision.
- `not_before` plus `duration_seconds` for windows.

## 3. Recompute the event ID

1. Copy the event.
2. Remove `event_id`.
3. Remove `proofs`.
4. Canonicalize the remainder with RFC 8785 JCS.
5. SHA-256 hash the UTF-8 canonical bytes.
6. Encode as lowercase hexadecimal and prefix `sha256:`.
7. Reject if the result does not equal the supplied `event_id`.

No placeholder is inserted for omitted fields.

## 4. Verify proofs

- Reject duplicate `signer` values.
- Verify every proof over the raw 32-byte event digest.
- Require exactly one proof from the primary `actor`.
- Reject unsupported algorithms visibly.
- Do not accept a signature over the printable event-ID string when the profile requires the raw digest.

For `pickup.proof` and `ride.completed.receipt`:

- Read rider and driver keys from the accepted terms referenced by the event.
- Require exactly those two signers.
- Require both proofs to cover the same event ID.

For `identity.binding`:

- Require the exact discovery and identity keys named in the payload.
- Require one proof from each.
- Verify the referenced public request and ride ID.
- Enforce the declared binding scope and lifetime.

## 5. Enforce ride scope

Ride-scoped types require `ride_id` as enumerated in `PROTOCOL.md` and the envelope schema.

Non-ride-scoped events remain valid without `ride_id`, including:

- `driver.availability`
- `identity.attestation`
- `vehicle.attestation`
- `credential.revocation`
- `key.rotation`
- `moderation.warning`

Never manufacture a placeholder ride ID.

## 6. Enforce expiry safely

For an event with `ttl_seconds`:

```text
effective_expiry = created_at + ttl_seconds
```

- `ttl_seconds` must be positive.
- Addition must be overflow-safe.
- Reject the event for live processing when current time is later than effective expiry plus the permitted clock-skew window.
- Archival storage does not revive an expired event.

## 7. Enforce public privacy across the envelope

For public `ride.request`:

- Reject all undeclared top-level fields.
- Reject `extensions` entirely in v0.1.
- Reject exact coordinates, addresses, phone numbers, legal names, contact fields, and free-form personal notes anywhere in the public event.
- Do not treat payload-only validation as sufficient.

Encrypted private events may contain exact details when their event type and local disclosure policy permit them.

## 8. Derive location precision

- Precision equals the geohash string length.
- Do not accept a separate precision value.
- Neighbor-cell matching and UI disclosure must use the derived length.

## 9. Derive time ranges

For public and negotiated windows:

```text
not_after = not_before + duration_seconds
```

- `duration_seconds` must be positive.
- Addition must be overflow-safe.
- A reversed interval cannot be represented.

## 10. Apply causal and lifecycle rules

- Validate every `previous` reference before applying a transition.
- Do not order conflicting states solely by arrival time.
- Apply separate ride-aggregate and offer-thread rules from `RIDE_LIFECYCLE.md`.
- `ride.cancel` is pre-pickup.
- `ride.abort` is post-pickup.
- One offer becoming `Declined` does not terminate other offer threads.
- Request expiry terminates all unaccepted threads.

## 11. Preserve evidence without overstating it

- A unilateral completion claim is not a bilateral receipt.
- An abort is not proof of fault.
- A relay acknowledgement is not ride acceptance.
- Cryptographic signatures prove key participation, not real-world identity, payment, safety, or truth.

## Conformance expectation

Two independent validators MUST make the same decision for every case in `../test-vectors/review-cases-v0.1.json` before claiming PactRide v0.1 envelope compatibility.
