# Prior Art and Lessons

PactRide is not the first attempt to make ride coordination open, cooperative, decentralized, or zero-commission. This document exists to prevent reinvention and overclaiming.

## Freeport

Repository: `ptrinh/freeport`

Relevant ideas:

- Nostr-based public intents.
- Client-side matching.
- Geohash-scoped markets.
- Encrypted bilateral negotiation.
- Double acceptance of terms.
- Replaceable relays.
- Rideshare as one vertical in a general peer-to-peer marketplace.

Lessons:

- This is the closest architectural starting point.
- Public intent plus encrypted negotiation is viable as a protocol shape.
- Reputation, anti-Sybil defenses, and full ride execution remain incomplete.
- PactRide should collaborate with or extend prior work rather than falsely claim the general concept is new.

## Namma Yatri

Repository: `nammayatri/nammayatri`

Relevant ideas:

- Open-source production ride-hailing stack.
- Driver-oriented zero-commission or subscription economics.
- Large operational backend covering dispatch, routing, payments, support, and local deployments.

Lessons:

- Open source and low-commission operations can exist at meaningful scale.
- Production transportation requires far more than request/offer messaging.
- Namma Yatri remains an operated service architecture rather than a permissionless peer protocol.
- Its complexity is evidence that PactRide should define a minimal protocol instead of cloning an entire production stack.

## Bitchat

Repository: `permissionlesstech/bitchat`

Relevant ideas:

- BLE mesh for nearby communication.
- Nostr for internet-distance communication.
- Common transport routing.
- Encrypted store-and-forward.
- Controlled flooding, TTL, deduplication, and opportunistic couriers.

Lessons:

- Hybrid transport is more realistic than Bluetooth-only networking.
- Store-and-forward can improve resilience but does not guarantee real-time delivery.
- Ride events must remain much smaller and more safety-sensitive than ordinary chat.

## Nairobi2

Repository: `f321x/nairobi2` (archived)

Relevant ideas:

- Nostr ride requests.
- Open mapping and routing.
- Reverse-auction style driver offers.
- No required central account.

Lessons:

- Demonstrates the recurring appeal of a Nostr ride client.
- Archived prototypes reinforce that adoption, maintenance, trust, and safety matter more than a basic demo.

## Runabout

Repository: `sector01tech/Runabout`

Relevant ideas:

- Nostr ride requests.
- Private messaging.
- Ratings.
- OpenStreetMap tracking.
- Optional Lightning settlement.

Lessons:

- Event schemas and user flows are useful prior art.
- Code quality and maintenance must be independently evaluated.
- Exact public coordinates and premature payment integration create avoidable risk.

## LibreTaxi

Repository: `ro31337/libretaxi`

Relevant ideas:

- Open-source ride coordination through Telegram.
- Lightweight deployment.
- Human-readable request and response flows.

Lessons:

- A simple communication layer can attract attention and users.
- Dependency on a central messaging platform limits protocol independence.
- Local liquidity and community operations remain unsolved by open-source code alone.

## Arcade City / Bullrun

Relevant ideas:

- Peer-to-peer driver communities.
- Nostr and Lightning experiments.
- Driver/rider direct relationships.

Lessons:

- Community governance and moderation can become concentrated even without conventional platform ownership.
- Escrow, payment finality, and dispute handling are difficult.
- Ideological decentralization does not automatically produce safe or reliable operations.

## DRIFE and blockchain ride projects

Relevant ideas:

- Decentralized identity.
- Token incentives.
- Driver-owned or community-oriented narratives.

Lessons:

- Tokens frequently distract from local liquidity, dispatch, safety, and trust.
- Blockchain consensus is unnecessary for bilateral ride-state agreement.
- PactRide should remain payment-neutral and chain-optional at most.

## Driver cooperatives

Examples include local driver-owned ride services and cooperative dispatch projects.

Lessons:

- Ownership structure matters.
- Cooperatives still need technology, customer acquisition, support, governance, and capital.
- PactRide could become shared infrastructure for cooperatives without prescribing one cooperative model.

## Open mobility standards

Relevant standards and ecosystems to examine:

- Nostr event and relay protocols.
- DID and Verifiable Credentials.
- Mobility Data Specification.
- General Transit Feed Specification.
- TOMP-API and MaaS interoperability work.
- OpenStreetMap, OSRM, Valhalla, and GraphHopper.
- Matrix and ActivityPub federation lessons.

These standards solve adjacent problems; PactRide should reuse mature components rather than invent new cryptography or mapping formats.

## Repeated failure patterns

1. Building an app before defining interoperability.
2. Assuming open source creates local market liquidity.
3. Treating signatures as real-world identity.
4. Publishing exact locations for easy matching.
5. Adding tokens before solving ride completion.
6. Ignoring mobile background restrictions.
7. Creating one “decentralized” operator with hidden control.
8. Underestimating abuse, support, and dispute handling.
9. Depending on one relay, messaging service, or map provider.
10. Launching with a manifesto but no testable specification.

## PactRide differentiation

PactRide does not claim novelty in decentralized rideshare. Its proposed contribution is a professionally specified, payment-neutral, interoperable ride lifecycle combining:

- Coarse public discovery.
- Encrypted exact negotiation.
- Bilateral state transitions.
- Physical pickup verification.
- Portable evidence-based reputation.
- Plural community attestations.
- Replaceable relay infrastructure.
- Bounded nearby/offline fallback.
- Public conformance tests and governance.

## Citation policy

Every prior-art claim should eventually link to a primary repository, specification, paper, or official project statement. Contributors should avoid marketing claims and clearly mark abandoned, experimental, and production systems.
