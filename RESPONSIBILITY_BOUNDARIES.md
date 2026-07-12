# PactRide Responsibility Boundaries

## Purpose

PactRide defines an interoperable ride-coordination language. It does not turn every transportation, safety, legal, payment, or operational function into protocol behavior.

This matrix identifies which layer owns each responsibility and prevents optional services from becoming hidden mandatory infrastructure.

| Capability | Base PactRide protocol | Client application | Community or operator | External provider | Outside protocol guarantees |
|---|---|---|---|---|---|
| Identity keys and signatures | Defines identifiers, proofs, rotation events, and validation | Generates, stores, backs up, and uses keys | May set participation policy | Hardware keystore or recovery service may assist | A signature does not prove legal identity |
| Ride discovery | Defines coarse, TTL-bounded request and availability events | Publishes, subscribes, validates, filters, and ranks locally | Selects relay and participation policy | Relay distributes carriers | Matching density and availability are not guaranteed |
| Exact location | Requires encrypted disclosure and data minimization | Controls disclosure timing and map requests | May require operational procedures | Map, routing, and navigation providers process queries | Protocol cannot prevent a selected counterparty from misusing disclosed data |
| Price and terms | Defines complete offers, counters, terms hashes, and bilateral acceptance | Presents terms and records intentional consent | May define local fare or cancellation policy | Pricing tools may provide estimates | PactRide does not set fares or guarantee economic fairness |
| Payment and settlement | Carries optional settlement declarations | Invokes user-selected payment method and labels status accurately | Handles refunds or reconciliation when operating a service | Cash, bank, card, wallet, or processor moves funds | Signatures do not prove irreversible payment or eliminate chargebacks |
| Driver, rider, and vehicle credentials | Carries attestations, expiry, revocation, and provenance | Verifies evidence under transparent local policy | Chooses accepted issuers and minimum requirements | Government, insurer, cooperative, or verifier may issue claims | No universal "verified safe" status exists |
| Pickup verification | Defines challenge and bilateral pickup proof | Displays/scans code and signs one identical proof | May define required method | BLE, QR, or device APIs assist | Proximity proof does not prove intent, conduct, or safety |
| Ride lifecycle | Defines states, causal references, claims, receipts, aborts, and disputes | Applies deterministic transition rules and preserves conflicts | May add operational procedures | Notification infrastructure may carry alerts | Protocol events do not prove every physical fact |
| Reputation | Defines portable receipts, ratings, attestations, warnings, and revocations | Computes inspectable local conclusions | Publishes local policy and moderation decisions | Attestors or analytics may provide optional evidence | No global score is protocol truth |
| Moderation and exclusion | Preserves provenance for warnings and blocks | Applies local block and feed choices | Operates appeals, membership, and moderation process | Specialized safety service may assist | PactRide does not provide a global police or court system |
| Emergency response | Allows an event to state that outside help was requested | Opens device emergency or support flow | Maintains incident procedures for a service or pilot | Emergency services and dispatch providers respond | The protocol is not an emergency service |
| Insurance | Can reference an attestation or policy identifier | Displays known coverage and uncertainty | Ensures legally required coverage for its operation | Insurer underwrites and handles claims | PactRide does not create or guarantee insurance |
| Accessibility | Defines structured requirements and accepted commitments | Provides accessible UX and private disclosure controls | Ensures service delivery and nondiscrimination process | Accessibility specialists and transport providers assist | Schema support alone does not guarantee an accessible ride |
| Relay operation | Defines replaceability, deduplication, TTL, and failure behavior | Uses multiple relays and retains local state | May operate public or community relays | Independent relay hosts provide transport | No relay is authoritative or guaranteed available |
| Legal compliance | Defines no exemption or certification claim | Presents accurate limitations | Responsible entity evaluates local obligations | Qualified counsel and regulators provide guidance | Open-source availability is not legal authorization to operate rides |
| Customer support and disputes | Preserves signed evidence and conflicting claims | Exports evidence and explains confidence | Runs support, refunds, appeals, and incident ownership | Mediator or support vendor may assist | The base protocol does not resolve fault or damages |
| Fees and monetization | Prohibits no business model but requires no protocol tax | Discloses paid services, ranking, and provider choices | Chooses dues, subscription, grants, or service fees | Hosting and payment vendors charge separately | PactRide does not guarantee free rides or founder revenue |

## Mandatory separation rules

A compatible implementation MUST NOT claim that:

- relay acceptance means a ride was accepted;
- a signature proves legal identity, physical safety, route completion, or payment finality;
- a locally selected verifier is the universal PactRide authority;
- use of one map, payment, relay, identity, moderation, notification, or support provider is required by the protocol;
- passing a schema validator certifies transportation-law compliance or production safety.

## Operator checklist

Before any real pilot or service, the responsible operator must identify, outside the protocol specification:

- the legal entity and operating jurisdiction;
- driver, vehicle, licensing, insurance, and accessibility obligations;
- incident, emergency, support, privacy, breach, dispute, refund, and stop procedures;
- responsible humans for daily operations;
- all third-party services, fees, data access, retention, and failure dependencies;
- participant consent and a clear statement that the experiment is not protocol-certified as safe.
