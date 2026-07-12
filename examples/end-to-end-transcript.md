# Example End-to-End Ride Transcript

This fictional transcript demonstrates intended semantics. Hashes, keys, and signatures are shortened and are not cryptographic test vectors. Normative event-ID material is in `../test-vectors/event-id-v0.1.json`.

## Participants

- Rider long-term key: `npub-rider-A`
- Rider rotating discovery key: `npub-discovery-7`
- Driver key: `npub-driver-B`
- Ride ID: `01JPACTRIDEEXAMPLE`

Every event uses the strict envelope. `proofs` signs the event ID computed after omitting `event_id` and `proofs`.

## 1. Public request

The rider publishes one privacy-safe request through three relays:

```json
{
  "protocol": "pactride",
  "version": "0.1",
  "type": "ride.request",
  "event_id": "sha256:req1",
  "actor": "npub-discovery-7",
  "created_at": 1783742400,
  "ttl_seconds": 600,
  "ride_id": "01JPACTRIDEEXAMPLE",
  "previous": [],
  "payload": {
    "pickup": {"geohash": "dr5x1"},
    "destination": {"geohash": "dr5ru"},
    "window": {
      "not_before": 1783742700,
      "duration_seconds": 900
    },
    "party": {
      "seats": 1,
      "wheelchair_accessible_required": false
    },
    "terms_hint": {
      "currency": "USD",
      "maximum": "35.00",
      "negotiable": true
    }
  },
  "proofs": [
    {
      "signer": "npub-discovery-7",
      "algorithm": "schnorr-secp256k1",
      "signature": "sig-discovery-request"
    }
  ]
}
```

The geohash length is the precision. No separate precision integer exists.

The effective expiry is `1783742400 + 600 = 1783743000`.

No exact address, contact information, free-form note, or envelope extension is public.

## 2. Encrypted driver offer

The driver sends an encrypted event:

```json
{
  "protocol": "pactride",
  "version": "0.1",
  "type": "ride.offer",
  "event_id": "sha256:offer1",
  "actor": "npub-driver-B",
  "created_at": 1783742460,
  "ride_id": "01JPACTRIDEEXAMPLE",
  "previous": ["sha256:req1"],
  "payload": {
    "offer_id": "01JOFFER1",
    "pickup_eta_seconds": 480,
    "terms": {
      "amount": "30.00",
      "currency": "USD",
      "settlement_methods": ["cash"]
    },
    "vehicle_summary": {
      "category": "compact-suv",
      "seats_available": 3
    },
    "evidence_refs": ["sha256:community-attestation"]
  },
  "proofs": [
    {
      "signer": "npub-driver-B",
      "algorithm": "schnorr-secp256k1",
      "signature": "sig-driver-offer"
    }
  ]
}
```

The ride aggregate is now `Matching`; this offer thread is `Offered`.

## 3. Encrypted rider counter

The rider counters using the discovery key:

```json
{
  "protocol": "pactride",
  "version": "0.1",
  "type": "ride.counter",
  "event_id": "sha256:counter1",
  "actor": "npub-discovery-7",
  "created_at": 1783742520,
  "ride_id": "01JPACTRIDEEXAMPLE",
  "previous": ["sha256:offer1"],
  "payload": {
    "terms": {
      "amount": "28.00",
      "currency": "USD",
      "settlement_methods": ["cash"],
      "pickup_window": {
        "not_before": 1783742820,
        "duration_seconds": 480
      },
      "cancellation": "no-fee-before-driver-departing"
    },
    "terms_hash": "sha256:terms-H2"
  },
  "proofs": [
    {
      "signer": "npub-discovery-7",
      "algorithm": "schnorr-secp256k1",
      "signature": "sig-discovery-counter"
    }
  ]
}
```

The offer thread is now `Negotiating`.

## 4. Encrypted discovery-to-identity binding

Before the rider switches to a long-term identity, both rider keys prove the binding in one encrypted event:

```json
{
  "protocol": "pactride",
  "version": "0.1",
  "type": "identity.binding",
  "event_id": "sha256:binding1",
  "actor": "npub-discovery-7",
  "created_at": 1783742550,
  "ttl_seconds": 1800,
  "ride_id": "01JPACTRIDEEXAMPLE",
  "previous": ["sha256:req1", "sha256:counter1"],
  "payload": {
    "request_event_id": "sha256:req1",
    "discovery_key": "npub-discovery-7",
    "identity_key": "npub-rider-A",
    "scope": "single-ride",
    "valid_for_seconds": 1800
  },
  "proofs": [
    {
      "signer": "npub-discovery-7",
      "algorithm": "schnorr-secp256k1",
      "signature": "sig-discovery-binding"
    },
    {
      "signer": "npub-rider-A",
      "algorithm": "schnorr-secp256k1",
      "signature": "sig-rider-binding"
    }
  ]
}
```

The driver verifies both proofs. The long-term key is now bound to this request and ride, but the binding remains private.

## 5. Driver accepts H2

```json
{
  "protocol": "pactride",
  "version": "0.1",
  "type": "ride.accept",
  "event_id": "sha256:driver-accept-H2",
  "actor": "npub-driver-B",
  "created_at": 1783742580,
  "ride_id": "01JPACTRIDEEXAMPLE",
  "previous": ["sha256:counter1", "sha256:binding1"],
  "payload": {
    "terms_hash": "sha256:terms-H2",
    "rider": "npub-rider-A",
    "driver": "npub-driver-B"
  },
  "proofs": [
    {
      "signer": "npub-driver-B",
      "algorithm": "schnorr-secp256k1",
      "signature": "sig-driver-H2"
    }
  ]
}
```

This remains unilateral acceptance.

## 6. Rider accepts H2 and reveals exact pickup privately

```json
{
  "protocol": "pactride",
  "version": "0.1",
  "type": "ride.accept",
  "event_id": "sha256:rider-accept-H2",
  "actor": "npub-rider-A",
  "created_at": 1783742600,
  "ride_id": "01JPACTRIDEEXAMPLE",
  "previous": ["sha256:driver-accept-H2", "sha256:binding1"],
  "payload": {
    "terms_hash": "sha256:terms-H2",
    "rider": "npub-rider-A",
    "driver": "npub-driver-B",
    "exact_pickup": {
      "latitude": 40.000001,
      "longitude": -73.000001,
      "instructions": "fictional encrypted test location"
    }
  },
  "proofs": [
    {
      "signer": "npub-rider-A",
      "algorithm": "schnorr-secp256k1",
      "signature": "sig-rider-H2"
    }
  ]
}
```

The ride aggregate becomes `Accepted` because both parties signed the same terms hash and participant set.

## 7. Driver arrival

```json
{
  "protocol": "pactride",
  "version": "0.1",
  "type": "driver.arrived",
  "event_id": "sha256:arrived1",
  "actor": "npub-driver-B",
  "created_at": 1783743250,
  "ride_id": "01JPACTRIDEEXAMPLE",
  "previous": ["sha256:rider-accept-H2"],
  "payload": {"arrival_zone": "dr5x1"},
  "proofs": [
    {
      "signer": "npub-driver-B",
      "algorithm": "schnorr-secp256k1",
      "signature": "sig-driver-arrived"
    }
  ]
}
```

This is a signed arrival claim, not physical proof.

## 8. Bilateral pickup proof

The rider displays `RIVER-ORANGE-42`, derived from a random challenge. Both clients sign one identical event:

```json
{
  "protocol": "pactride",
  "version": "0.1",
  "type": "pickup.proof",
  "event_id": "sha256:pickup-proof",
  "actor": "npub-rider-A",
  "created_at": 1783743300,
  "ride_id": "01JPACTRIDEEXAMPLE",
  "previous": ["sha256:arrived1"],
  "payload": {
    "challenge_hash": "sha256:pickup-nonce",
    "rider": "npub-rider-A",
    "driver": "npub-driver-B",
    "verified_at": 1783743300,
    "methods": ["qr", "ble-proximity"]
  },
  "proofs": [
    {
      "signer": "npub-rider-A",
      "algorithm": "schnorr-secp256k1",
      "signature": "sig-rider-pickup"
    },
    {
      "signer": "npub-driver-B",
      "algorithm": "schnorr-secp256k1",
      "signature": "sig-driver-pickup"
    }
  ]
}
```

The signer set exactly matches the rider and driver frozen in accepted terms.

## 9. Ride start

A valid `ride.started` references `sha256:pickup-proof`. The ride aggregate becomes `InProgress`.

## 10A. Normal completion path

The driver first emits `ride.completed.claim`. The rider client displays “completion awaiting rider confirmation.”

Both then sign one identical receipt:

```json
{
  "protocol": "pactride",
  "version": "0.1",
  "type": "ride.completed.receipt",
  "event_id": "sha256:receipt1",
  "actor": "npub-driver-B",
  "created_at": 1783745100,
  "ride_id": "01JPACTRIDEEXAMPLE",
  "previous": ["sha256:completion-claim1"],
  "payload": {
    "rider": "npub-rider-A",
    "driver": "npub-driver-B",
    "accepted_terms_hash": "sha256:terms-H2",
    "pickup_proof_hash": "sha256:pickup-proof",
    "started_at": 1783743310,
    "completed_at": 1783745100,
    "completion_zone": "dr5ru",
    "settlement": {
      "status": "declared-complete",
      "method": "cash",
      "amount": "28.00"
    }
  },
  "proofs": [
    {
      "signer": "npub-rider-A",
      "algorithm": "schnorr-secp256k1",
      "signature": "sig-rider-completion"
    },
    {
      "signer": "npub-driver-B",
      "algorithm": "schnorr-secp256k1",
      "signature": "sig-driver-completion"
    }
  ]
}
```

The receipt proves agreement between keys. It does not independently prove payment or physical route.

## 10B. Abnormal termination path

If the ride ends after pickup without bilateral completion, a participant emits:

```json
{
  "protocol": "pactride",
  "version": "0.1",
  "type": "ride.abort",
  "event_id": "sha256:abort1",
  "actor": "npub-rider-A",
  "created_at": 1783744000,
  "ride_id": "01JPACTRIDEEXAMPLE",
  "previous": ["sha256:ride-start1"],
  "payload": {
    "last_recognized_state": "InProgress",
    "reason": "counterparty_requested_stop",
    "external_help_requested": false
  },
  "proofs": [
    {
      "signer": "npub-rider-A",
      "algorithm": "schnorr-secp256k1",
      "signature": "sig-rider-abort"
    }
  ]
}
```

The aggregate becomes `Aborted`. If the driver later submits a conflicting completion claim, it becomes `Disputed`.

## 11. Receipt-backed ratings

After normal completion, each participant may issue a structured rating referencing `sha256:receipt1`. Clients verify the relationship without a central rating database.
