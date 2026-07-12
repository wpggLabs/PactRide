# PactRide Nostr Transport Profile v0.1

## Status

This document defines the initial interoperable Nostr carrier profile for PactRide experiments. It is precise enough for independent implementations and test fixtures, but it is not evidence of production reliability, privacy, or public-road readiness.

PactRide application semantics remain transport-independent. A client may implement another transport if it preserves the same PactRide envelopes, validation, ordering, privacy boundaries, and failure behavior.

## Required Nostr capabilities

A Nostr-based PactRide v0.1 client MUST support:

- **NIP-01** event and relay behavior.
- **NIP-44 version 2** encrypted payloads.
- **NIP-59** seal and gift-wrap handling.
- **NIP-17** private direct-message delivery, including recipient inbox relay discovery through `kind:10050`.
- **NIP-42** relay authentication when an inbox relay requires authenticated access to gift-wrapped events.
- **NIP-65** general read/write relay hints. NIP-65 relay lists do not replace the NIP-17 inbox list.

NIP-13 proof of work, NIP-09 deletion, and NIP-62 vanish requests are optional transport features. They do not erase copies already received by relays or counterparties.

Primary specifications:

- https://github.com/nostr-protocol/nips/blob/master/01.md
- https://github.com/nostr-protocol/nips/blob/master/17.md
- https://github.com/nostr-protocol/nips/blob/master/42.md
- https://github.com/nostr-protocol/nips/blob/master/44.md
- https://github.com/nostr-protocol/nips/blob/master/59.md
- https://github.com/nostr-protocol/nips/blob/master/65.md
- https://github.com/nostr-protocol/nips/blob/master/78.md

## Layering rule

The PactRide envelope is the application object. The Nostr event is only a carrier.

Clients MUST:

1. Parse and verify the outer Nostr event according to the applicable NIP.
2. Recover the PactRide JSON envelope from the carrier content.
3. Validate the complete PactRide envelope, event ID, proof set, payload schema, TTL, causal references, and lifecycle semantics.
4. Deduplicate by PactRide `event_id`, not only by the outer Nostr event ID.

A relay `OK` response proves only that one relay accepted an outer event. It is not rider or driver acceptance, delivery proof, pickup proof, payment confirmation, or a ride-state transition.

## Public discovery carriers

### Ride requests and withdrawals

During v0.1 experiments, public `ride.request` and `ride.withdraw` envelopes use normal Nostr **kind `78`** carriers.

Required tags:

```json
[
  ["t", "pactride"],
  ["p", "0.1"],
  ["type", "ride.request"],
  ["ride", "01JPACTRIDEEXAMPLE"],
  ["g", "dr5x1"]
]
```

Rules:

- `content` MUST be the compact UTF-8 JSON serialization of the complete PactRide envelope.
- Tags are routing hints only. Clients MUST validate the inner envelope and MUST reject a carrier whose tags contradict it.
- Public tags MUST NOT include exact coordinates, exact address, phone number, legal name, contact details, exact destination, price negotiation, or a long-term identity when a rotating discovery key is used.
- The outer Nostr author MUST correspond to the PactRide discovery identity authorized by the inner proof.
- The inner PactRide TTL is authoritative. Relay retention does not extend it.

### Driver availability

`driver.availability` uses addressable Nostr **kind `30078`** during v0.1 experiments so one availability record can replace an earlier record for the same scope.

Required tags include:

```json
[
  ["d", "pactride:driver.availability:<market-or-scope>"],
  ["t", "pactride"],
  ["p", "0.1"],
  ["type", "driver.availability"],
  ["g", "dr5x1"]
]
```

The `d` value identifies the availability scope, not a person-readable profile. Availability MUST remain TTL-bounded inside the PactRide envelope even though the Nostr carrier is addressable.

These carrier kinds are an experimental profile, not a request for global Nostr kind ownership. A stable release requires collision review, migration tests, and either an accepted NIP allocation or a documented continuation strategy.

## Private negotiation and ride-state delivery

All non-public PactRide events use NIP-17 private direct messages.

- The unsigned NIP-17 rumor uses `kind:14`.
- Its `content` is the compact JSON serialization of one complete PactRide envelope.
- The rumor is sealed with `kind:13`, then gift-wrapped separately to each recipient with `kind:1059`.
- The sender SHOULD also create a sender-addressed wrap when encrypted history recovery is enabled.
- Each gift wrap uses a fresh random wrapper key.
- Seal and gift-wrap timestamps SHOULD be independently randomized in the past as required by NIP-17/NIP-59 guidance.
- Clients MUST verify that the seal author matches the rumor author before trusting the inner PactRide envelope.

Private PactRide events include offers, counters, identity bindings, acceptances, declines, cancellations after a private thread exists, exact locations, ride execution events, receipts, disputes, and private trust evidence.

## Inbox relay discovery

Recipients advertise private-message inbox relays with NIP-17 `kind:10050`.

- Clients MUST publish gift wraps only to relays listed by the recipient.
- If no valid `kind:10050` list is available, the recipient is not considered reachable for NIP-17 delivery.
- Clients SHOULD guide users toward one to three inbox relays.
- General NIP-65 read/write relay metadata MAY help locate public material but MUST NOT be treated as an inbox declaration.

## Authentication and metadata protection

Clients MUST implement NIP-42 challenge handling for relays that require authentication.

For private inbox relays, clients SHOULD prefer relays that:

- require authentication before serving `kind:1059` events;
- serve gift wraps only to the `p`-tagged recipient;
- publish retention and deletion behavior;
- enforce event-size and connection limits;
- do not claim that transport authentication verifies a real-world rider or driver identity.

Authentication is connection-scoped relay access. It is not a PactRide credential or attestation.

## Publication and retry profile

### Public discovery

A client SHOULD publish a request to at least two configured public relays when available. It records transport acceptance per relay and continues discovery if one relay fails.

### Private events

A client publishes one gift wrap per recipient per listed inbox relay. It SHOULD:

- retry with bounded exponential backoff;
- stop retrying after the inner event expires or becomes causally obsolete;
- preserve the same inner PactRide `event_id` across retries;
- generate a new outer gift wrap for a retry only when required by the transport implementation;
- treat duplicate delivery as normal and harmless after inner-event deduplication.

### Delivery states shown to users

Clients SHOULD distinguish:

- **Queued:** stored locally for an attempted send.
- **Relay accepted:** at least one relay returned a successful `OK` for the carrier.
- **Counterparty activity observed:** a valid later PactRide event causally references the sent event.
- **Failed or expired:** no valid route remains before the event becomes obsolete.

The word **delivered** SHOULD NOT be shown solely because a relay accepted the event.

## Capability declaration

During encrypted negotiation, clients exchange a capability object containing at least:

```json
{
  "protocol": "pactride",
  "versions": ["0.1"],
  "transport": {
    "name": "nostr",
    "public_carriers": [78, 30078],
    "private_profile": "nip17+nip44-v2+nip59",
    "nip42": true
  },
  "limits": {
    "max_inner_event_bytes": 16384,
    "max_negotiation_rounds": 8
  }
}
```

Clients MUST fail closed when they cannot agree on the PactRide major version, encryption profile, or required payload limits. Unsupported optional capabilities must not be inferred.

## Size and abuse limits

- The compact inner PactRide envelope MUST NOT exceed 16,384 UTF-8 bytes in v0.1.
- Clients MUST reject oversized payloads before expensive decryption or schema work when possible.
- Public relays and clients SHOULD rate-limit discovery by connection, coarse region, and local policy.
- Gift-wrap spam cannot safely rely on wrapper-key reputation. Inbox relays may require NIP-42 authentication, proof of work, payment, allowlists, or other disclosed policy.
- A paid or restricted relay remains optional infrastructure and must not become a protocol requirement.

## Failure behavior

Clients MUST preserve accepted PactRide state locally and MUST NOT infer state from one relay's current contents.

- Missing relay history does not cancel a ride.
- Relay ordering does not determine causal ordering.
- Conflicting valid events are preserved and resolved under the PactRide lifecycle rules.
- Expired discovery events may remain retrievable but are invalid for live matching.
- Transport failure must remain visibly distinct from counterparty rejection.

## Conformance requirements

A Nostr transport implementation is conformant only when it demonstrates:

1. Correct kind `78` request/withdraw carriers and kind `30078` availability replacement.
2. Tag-to-inner-envelope consistency checks.
3. NIP-17 inbox discovery and per-recipient gift wrapping.
4. NIP-44 v2 encryption and NIP-59 unwrap validation.
5. NIP-42 challenge handling.
6. Multi-relay publication, retry, duplicate delivery, reordering, and outage tests.
7. PactRide inner-event validation after transport decoding.
8. Clear separation between relay acceptance and protocol agreement.

The initial profile closes the documentation ambiguity. Issue-level implementation, relay-matrix, privacy, and cross-client evidence remain required before the profile is considered proven.
