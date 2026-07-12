# PactRide and CommonPact

**Status:** explanatory and non-normative  
**PactRide dependency:** none  
**CommonPact repository:** [`wpggLabs/CommonPact`](https://github.com/wpggLabs/CommonPact)

## Purpose

This document defines the intended relationship between PactRide and the planned CommonPact project.

PactRide is the complete, self-contained ride-coordination profile. CommonPact is a future attempt to extract coordination concepts that remain useful across multiple substantially different domains.

CommonPact is not currently a dependency, parent specification, compatibility requirement, or reason to delay PactRide review and implementation.

## Direction of development

The intended direction is:

```text
real domain work → repeated patterns → tested abstraction
```

It is not:

```text
unproven generic framework → forced domain behavior
```

PactRide therefore remains authoritative for ride coordination until CommonPact has been independently documented, tested against at least one substantially different profile, and adopted through an explicit PactRide RFC.

## Candidate CommonPact core concepts

The following PactRide concepts may later inform a reusable CommonPact coordination core.

| Candidate CommonPact concept | PactRide realization |
|---|---|
| Protocol and profile identifier | `protocol: "pactride"` and PactRide version rules |
| Signed event envelope | PactRide common event envelope |
| Deterministic event identifier | RFC 8785 canonicalization plus SHA-256 |
| Actor authorization | `actor` plus `proofs[]` |
| Interaction identifier | `ride_id` for ride-scoped events |
| Causal references | `previous[]` event references |
| Expiring public intent | `ride.request`, `driver.availability`, and `ride.withdraw` |
| Temporary discovery identity | rotating rider or driver discovery keys |
| Private identity binding | encrypted `identity.binding` |
| Provider proposal | `ride.offer` |
| Complete counterproposal | `ride.counter` |
| Bilateral agreement | matching `ride.accept` authorization over one terms hash |
| Decline | `ride.decline` scoped to one offer thread |
| Pre-activation cancellation | `ride.cancel` |
| Lifecycle update | departure, arrival, start, progress, and related ride events |
| Activation or handoff proof | bilateral `pickup.proof` |
| Abnormal termination | `ride.abort` |
| Completion claim | `ride.completed.claim` |
| Bilateral completion evidence | `ride.completed.receipt` |
| Conflict state | `ride.disputed` and preserved competing evidence |
| Feedback | `ride.rating` |
| External evidence | identity and vehicle attestations |
| Evidence invalidation | credential revocation and key rotation |
| Community warning | `moderation.warning` |
| Transport independence | relay, direct, and nearby transport adapters |
| Local trust policy | client-side evidence evaluation and moderation choices |
| Portable history | exportable receipts, attestations, and provenance |
| Extension discipline | versioned schemas and namespaced private extensions |

This table identifies possible reusable patterns. It does not make those elements CommonPact standards today.

## Concepts that must remain PactRide-specific

A future CommonPact core must not absorb domain behavior merely because PactRide currently contains it.

The following remain transportation-profile concerns unless broader evidence proves otherwise:

- rider and driver roles;
- pickup and destination semantics;
- geohash-based ride discovery policy;
- vehicle category, capacity, and vehicle attestations;
- driver departure and arrival;
- pickup challenge and physical pickup verification;
- service-animal, luggage, seating, and wheelchair-accessibility requirements;
- live trip progress;
- route and navigation interactions;
- ride cancellation and abort timing tied to pickup;
- transportation-specific rating dimensions;
- road-safety, insurance, licensing, and transportation-law boundaries;
- emergency and incident-response expectations;
- local ride-market density and dispatch behavior.

CommonPact may define generic extension points for a profile to express such concepts. It must not pretend to solve them generically.

## Candidate generic lifecycle

CommonPact may eventually test a lifecycle similar to:

```text
Discoverable
→ Negotiating
→ Agreed
→ Active
→ CompletionClaimed
→ Completed
```

Possible terminal or conflict outcomes may include:

```text
Withdrawn
Declined
Expired
Cancelled
Aborted
Disputed
ResolvedExternally
```

This generic vocabulary remains provisional. PactRide's normative ride lifecycle continues to use the states and transitions in [`RIDE_LIFECYCLE.md`](RIDE_LIFECYCLE.md).

## Profile responsibilities

If CommonPact becomes a specification, each profile should be required to define at least:

1. Domain roles and authority.
2. Public discovery payloads and prohibited public data.
3. Negotiable terms and canonical agreement input.
4. Domain lifecycle states and valid transitions.
5. Activation, handoff, completion, and conflict evidence.
6. Profile-specific privacy and metadata risks.
7. Safety, legal, accessibility, and operational responsibility boundaries.
8. Required schemas, semantic checks, and test vectors.
9. Compatible transports and any profile-specific carrier constraints.
10. Failure, migration, and older-client behavior.

A profile may impose stricter requirements than the generic core. It must not weaken core signature, canonicalization, versioning, provenance, or extension rules without an explicit incompatible version.

## PactRide independence rules

Until a future RFC says otherwise:

- PactRide implementations need only the PactRide repository.
- PactRide event validation does not require a CommonPact package, registry, service, relay, identifier, or approval.
- CommonPact changes do not automatically modify PactRide.
- PactRide changes do not automatically become CommonPact requirements.
- A CommonPact implementation is not automatically PactRide-compatible.
- A PactRide implementation is not required to advertise CommonPact support.
- PactRide version numbers and conformance claims remain independent.

## Extraction criteria

No PactRide concept should move into a normative CommonPact core until all of the following are true:

1. The concept works naturally in PactRide.
2. It also works in at least one substantially different, coherently documented profile.
3. The abstraction does not carry ride-specific terminology or assumptions.
4. Security and privacy consequences are documented for both domains.
5. Profile-specific rules remain expressible without bypassing the core.
6. At least two independent implementations can interpret the proposed core consistently.
7. Migration and compatibility effects on PactRide are explicit.
8. The change is accepted through the public governance process of both projects.

## Example comparison required before extraction

A useful second profile must differ materially from transportation. Plausible research examples include:

- milestone-based independent work;
- temporary asset rental;
- local service appointments;
- package custody and delivery.

The second profile is an abstraction test, not a commitment to launch another marketplace.

For example, a generic "activation proof" should only be extracted if it can represent both PactRide pickup verification and a genuinely different domain handoff without hiding important domain distinctions.

## Naming and wire compatibility

PactRide v0.1 uses ride-specific names such as `ride_id`, `ride.request`, and `pickup.proof`. A future CommonPact design may use generic terms such as `pact_id`, `coordination_id`, or profile-qualified event types.

CommonPact must not retroactively reinterpret existing PactRide events. Any future alignment must define one of these approaches explicitly:

- PactRide remains a standalone profile with an adapter to CommonPact;
- a future PactRide major version adopts a CommonPact envelope;
- shared libraries support both formats without claiming wire identity.

Silent field renaming or semantic aliasing is not acceptable.

## Safety preservation rule

Generalization must never weaken PactRide's transportation-specific safeguards.

In particular, a CommonPact core must not be used to justify:

- broader public location disclosure;
- weaker bilateral acceptance;
- weaker pickup verification;
- treating unilateral claims as receipts;
- suppressing conflicting evidence;
- hiding operator responsibilities;
- suggesting that generic cryptographic coordination proves transportation safety or legal compliance.

## Licensing relationship

The current PactRide specification repository remains licensed under Apache License 2.0.

CommonPact will publish its own license and contribution policy in its own repository. Creating CommonPact does not change the license already granted for PactRide releases, and CommonPact branding does not grant rights to use PactRide branding as official or certified.

## Current conclusion

PactRide is the first complete domain proposal and the source of the CommonPact hypothesis.

CommonPact should be documented only after PactRide's founder vision is complete. It should then prove that the reusable coordination model survives contact with another domain before PactRide considers adopting any shared core.

Until that evidence exists, PactRide remains self-contained, reviewable, and implementable on its own terms.