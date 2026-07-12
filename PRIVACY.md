# Privacy Model

## Objective

PactRide must permit practical discovery without turning public relays into a searchable database of exact travel plans.

Privacy is not a binary property. The protocol separates data into public discovery, encrypted counterparty data, and local-only information.

## Data classification

| Data | Default class | Rationale |
|---|---|---|
| Long-term public key | Private during public discovery; selectively disclosed | Persistent keys make requests linkable |
| Rotating discovery key | Public and temporary | Reduces correlation of public requests |
| Pickup geohash | Public, coarse, expiring | Needed for discovery |
| Destination geohash | Public, coarse, optional | Helps matching but creates movement metadata |
| Exact pickup | Encrypted | High stalking and safety risk |
| Exact destination | Encrypted | Reveals home, work, health, worship, and relationships |
| Fare and settlement terms | Encrypted | Financial privacy |
| Phone number/contact | Encrypted and late disclosure | Prevents harvesting and harassment |
| Continuous GPS | Local/direct only | Not required for public coordination |
| Raw trip history | Local-only by default | Highly sensitive behavioral record |
| Completion receipt | Portable encrypted/local | Needed for reputation and disputes |
| Rating | Selectively disclosed | May reveal relationships and sensitive context |

## Discovery privacy

### Coarse location

Public requests use a geohash or equivalent region identifier whose precision is derived from the location token itself. The numeric precision field was removed from the v0.1 request model so two representations cannot disagree. Clients should subscribe to adjacent cells because cell boundaries can exclude physically nearby drivers.

The appropriate public precision is not yet proven. Urban, suburban, rural, accessibility, and repeated-request cases require simulation before a production default is selected.

### Short expiration

Public discovery events use a positive `ttl_seconds`. Effective expiry is `created_at + ttl_seconds`, so expiry-before-creation cannot be represented. Clients must enforce expiration even if relays retain data.

### Rotating discovery identities

A privacy-preserving client should separate the key used for public ride discovery from the long-term identity used for accepted rides and reputation. The selected counterparty may receive an encrypted `identity.binding` event signed by both keys. That private binding proves key continuity to the recipient but does not hide timing, relay, IP, or geographic correlation.

### Destination minimization

Clients should offer multiple modes:

- Destination zone visible publicly.
- Direction or approximate distance only.
- Destination disclosed only during encrypted negotiation.
- Destination disclosed after pickup.

The rider and driver must understand which mode is active.

## Whole-envelope privacy

Privacy validation applies to the complete public event, not only its `payload`.

The v0.1 public ride-request validator:

- rejects undeclared top-level fields;
- rejects the optional `extensions` container for public ride requests;
- rejects exact coordinates, addresses, contact fields, and legal names in the request payload;
- requires the strict event envelope and strict ride-request payload together.

A client must not treat generic envelope extensibility as permission to publish private data.

## Metadata threats

End-to-end encryption does not hide all metadata. Relays and network observers may infer:

- When a key is active.
- Approximate request region.
- Event volume and timing.
- Which relays a device uses.
- IP address unless privacy networks are used.
- Correlation between public request and encrypted response timing.

Map, routing, notification, analytics, and crash-reporting providers may receive more sensitive metadata than relays. Client documentation must disclose these paths.

## Counterparty risk

Once exact information is disclosed, the counterparty can copy, screenshot, or misuse it. Cryptography cannot retract knowledge. Clients should delay exact disclosure and show the evidence available about the counterparty before the user consents.

## BLE and nearby privacy

Bluetooth broadcasts reveal that a participating device is nearby. Rotating identifiers, authenticated handshakes, minimal advertising payloads, and bounded scan periods reduce correlation but do not eliminate radio observation.

## Logs and telemetry

Reference clients should default to:

- No raw location analytics.
- No centralized trip-history telemetry.
- No private event payloads in logs.
- Redacted crash reports.
- Local, opt-in diagnostic export.
- Short retention for network metadata.

## Backups

Identity and history backups must be encrypted before leaving the device. Backup providers must not receive plaintext private keys or travel history.

## Privacy UX requirements

A compatible client should clearly indicate:

- What is about to be published publicly.
- Which exact details will be revealed to a selected counterparty.
- Which third-party map or notification services are contacted.
- Whether the user is operating under a long-term or rotating discovery key.
- Whether a message is queued, delivered, acknowledged, accepted, or mutually proven.
- When expanding geographic or relay search scope increases exposure.

## Deletion limitations

A deletion request can ask relays and counterparties to remove information, but cannot guarantee deletion from every copy. Clients must not promise global erasure of previously published public events.

## Privacy acceptance tests

1. The whole public-event schema rejects exact coordinates, addresses, contact fields, legal names, undeclared top-level fields, and public extensions.
2. Geohash precision is derived from token length; no separate numeric precision field is accepted.
3. Public events use positive TTL values and expire deterministically from creation time.
4. Exact-location messages fail unless encrypted to an intended recipient.
5. Logs contain no decrypted event payloads.
6. Expired requests disappear from live discovery.
7. A fresh discovery key cannot be linked to a long-term key from public protocol fields alone.
8. An encrypted identity binding requires proofs from both the discovery and long-term keys.
9. A map-provider audit documents every network request containing coordinates.
10. Regression fixtures cover private data placed outside the request payload.