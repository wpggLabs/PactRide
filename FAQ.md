# PactRide FAQ

## Is PactRide an app?

No. PactRide is first a protocol proposal. Compatible apps may be created by different communities and organizations.

## Is the founder vision finished?

Yes, in the bounded documentation sense defined by [`FOUNDER_VISION.md`](FOUNDER_VISION.md). The initial vision, protocol behavior, risks, limits, governance, licensing, implementation path, and CommonPact relationship are now represented publicly.

That does not mean PactRide is implemented, independently validated, production-safe, legally approved, funded, or operating rides.

## Is it an Uber competitor?

Not in the conventional sense. A company competes by owning a marketplace. PactRide aims to make the coordination layer interoperable so no single company must own it.

## Is it Bluetooth-only?

No. Practical city-scale discovery requires internet relays. Bluetooth and nearby networking are fallback and physical-verification channels.

## Does PactRide remove all costs?

No. Maps, relay hosting, identity checks, support, insurance, moderation, payment processing, and software maintenance still cost money. The protocol avoids requiring a mandatory commission collector; communities choose how infrastructure is funded.

## Can companies use it?

Yes. The current PactRide specification repository is licensed under Apache-2.0, which permits commercial use, modification, and distribution subject to the license conditions.

## Does Apache-2.0 make companies pay PactRide?

No. The license does not require royalties, revenue sharing, or a per-ride fee. PactRide can earn money through optional services, hosting, consulting, grants, support, certification, official products, and separately licensed official software, but another party may also build and monetize an independent implementation.

## Does AGPL make every user pay the founder?

No. AGPL is a strong software copyleft license. In covered circumstances it can require source availability for modified software offered over a network, but it does not automatically require a royalty, revenue share, or per-use payment.

It also does not make an independent implementation of a public protocol derivative of AGPL software merely because both implement the same idea.

## Could future official PactRide software use AGPL or a commercial license?

Yes, if that software is placed in a separate repository with explicit terms and PactRide controls the rights needed to offer those terms.

A possible model is AGPL-3.0-only or a separate paid commercial license. That would apply to the covered official software, not retroactively to the Apache-2.0 protocol specification or clean-room independent implementations.

## Must companies publish their modifications to this repository's Apache-2.0 material?

No. Apache-2.0 is a permissive license. It requires preservation of the license and applicable notices and requires modified files to carry notices when distributed, but it does not impose copyleft source-publication requirements.

## Why use Apache-2.0 for the specification?

It is a standard GitHub-recognized license, permits broad adoption, includes an express patent grant from contributors, and supports commercial, nonprofit, cooperative, municipal, and independent implementations under one understandable repository license.

## Why not ban commercial use?

A license that prohibits commercial use is not generally considered open source. It would also make compatibility and adoption harder. PactRide instead prevents mandatory ownership through replaceable infrastructure, interoperability, public governance, and conformance tests.

## Can the founder get paid?

Potentially, but not automatically because someone uses the idea.

Realistic revenue can come from official applications, commercial software licenses, managed infrastructure, support, consulting, integration, audits, training, authorized certification, trademarks, partnerships, grants, and sponsorships.

See [`LICENSING.md`](LICENSING.md) and [`MONETIZATION.md`](MONETIZATION.md).

## Why no blockchain?

A ride is primarily a bilateral state machine. Rider and driver signatures can represent agreement without global consensus. A blockchain adds cost, latency, privacy exposure, and governance complexity without solving physical safety or local adoption.

## How are drivers and riders verified?

The base protocol does not create one universal verifier. Communities and independent attestors may sign claims. Clients choose which attestations they trust and show their provenance.

## Can signatures prove a ride happened?

They prove that keys signed statements. A bilateral receipt is stronger evidence than a one-sided claim, but it does not prove every physical fact.

## How is location protected?

Public discovery uses coarse, short-lived regions. Exact pickup, destination, contact, and negotiation details use end-to-end encryption.

## What happens if relays disappear?

Clients publish to multiple relays and preserve accepted state locally. No one relay is authoritative.

## Who handles disputes?

The base protocol preserves claims, receipts, and provenance. Communities or external services may offer dispute processes, but none is mandatory globally.

## How does PactRide prevent fake ratings?

Ratings should reference signed ride receipts. Clients may examine distinct counterparties, key age, attestations, disputes, and graph diversity. No method completely prevents coordinated fake activity.

## How does PactRide make money?

The protocol itself does not require monetization. Compatible operators may use donations, subscriptions, cooperative dues, municipal funding, paid support, hosting, consulting, official applications, or transparent service fees.

## Is PactRide safe to use now?

No. It is a research RFC with no endorsed production client.

## Why start with documentation?

The difficult problems are interoperability, privacy, trust, state conflict, governance, and failure behavior. Building an app before specifying these would likely create another incompatible platform.

## What is the first technical milestone?

Two independently implemented command-line clients completing the same signed and encrypted ride lifecycle through replaceable relays.

## Can an existing project become PactRide-compatible?

Yes. Compatibility should depend on conformance tests, not permission from maintainers.

## What is CommonPact?

CommonPact is a planned future project that may extract reusable coordination concepts such as discovery, private negotiation, bilateral agreement, lifecycle events, and portable evidence.

PactRide does not currently depend on it. See [`COMMONPACT_RELATIONSHIP.md`](COMMONPACT_RELATIONSHIP.md).

## What prevents the founder from controlling it?

The repository is openly licensed, governance is public, infrastructure is replaceable, and the roadmap requires multiple maintainers and independent implementations.