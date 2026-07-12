# PactRide Licensing and Sustainability

## Status

This document explains the current licensing structure and the boundary between the open PactRide specification and any future official software or commercial services.

It is not legal advice. The unmodified root [`LICENSE`](LICENSE) text controls the current repository.

## Current repository license

The current PactRide specification repository is licensed under the **Apache License 2.0**.

Unless a file contains a different explicit notice, Apache-2.0 applies to material in this repository, including:

- protocol and research documents;
- schemas and test vectors;
- non-code examples;
- website source;
- validation scripts and workflow automation;
- code committed to this repository.

This structure gives contributors, independent implementers, companies, nonprofits, cooperatives, municipalities, and researchers one clear license for the public specification work.

## What Apache-2.0 allows

Apache-2.0 permits use, modification, distribution, sublicensing, and commercial use, subject to its conditions.

It also includes an express patent license from contributors for patent claims covered by their contributions and a patent-litigation termination provision.

Recipients distributing the work or derivative works must comply with the license, including providing a copy of the license, preserving applicable notices, and marking modified files where required.

## What Apache-2.0 does not provide

Apache-2.0 does not require a person or company to pay PactRide or its founder merely because it:

- reads or uses the specification;
- implements the protocol independently;
- modifies or distributes covered material;
- hosts covered software;
- operates a commercial compatible service;
- earns revenue using an implementation.

It also does not:

- require publication of modifications;
- require a per-ride fee, royalty, or revenue share;
- prevent a clean-room commercial implementation;
- grant permission to claim official endorsement or certification;
- grant rights in third-party material, personal data, patents not covered by the license grant, or rights a contributor does not control.

Copyright protects the repository's original expression and software. It does not by itself create ownership of every implementation of the underlying ride-coordination idea, system, process, or method.

## Existing releases cannot be made retroactively proprietary

Material already released under Apache-2.0 remains available under the rights granted by that release.

The project may change licensing for future material it owns, but it cannot revoke valid Apache-2.0 rights already granted, and it cannot relicense another contributor's copyright without the required permission.

This is why PactRide must choose contribution and software licensing deliberately before substantial implementation code is accepted.

## Why AGPL is not the repository license

The GNU Affero General Public License version 3 is a strong software copyleft license designed in part for modified software used over a network. It can require an operator of a modified covered program to offer corresponding source code to network users under the license's conditions.

AGPL does **not** automatically require:

- a royalty;
- a percentage of revenue;
- a payment for each ride;
- permission from the original author for ordinary AGPL-compliant use;
- payment by a person who independently implements a public protocol without copying covered software.

Applying AGPL to protocol documents would therefore not create a reliable right to payment from every PactRide-compatible implementation. It would also make protocol adoption and legal review harder without solving the underlying idea-versus-expression limitation.

## Future official software

PactRide does not currently contain official rider or driver applications, an operator platform, or production hosted infrastructure.

If official software is created later, it should normally live in a separate repository with an explicit license chosen for that product. Possible models include:

1. **Apache-2.0** for maximum adoption and ecosystem reuse.
2. **MPL-2.0** for file-level copyleft while allowing broader application integration.
3. **AGPL-3.0-only** for strong source-sharing obligations on covered network software.
4. **AGPL-3.0-only or a separate paid commercial license** when the project owns sufficient rights to offer dual licensing.
5. A proprietary license for software that is never represented as open source.

No future software-license choice may be described as active until it is published in that software's repository.

A separate official software license does not restrict independent implementations of the Apache-2.0 PactRide specification unless those implementations copy or derive from the separately licensed software.

## Conditions for dual licensing

A dual-licensing model works only when the commercial licensor controls the rights needed to offer the complete covered software under alternative terms.

Before accepting external contributions to dual-licensed official software, the project would need professionally reviewed contribution terms, such as an appropriate contributor license agreement or copyright assignment. A normal sign-off or Developer Certificate of Origin generally addresses provenance but should not be assumed to grant commercial relicensing authority.

The current specification repository does **not** require a contributor license agreement for ordinary Apache-2.0 contributions.

## Contributions to this repository

Under Section 5 of Apache-2.0, contributions intentionally submitted for inclusion are provided under Apache-2.0 unless the contributor explicitly states otherwise or a separate written agreement applies.

Contributors must have the right to submit their work. They must disclose third-party material, employer or client ownership constraints, and significant AI assistance that creates provenance concerns. See [`CONTRIBUTOR_POLICY.md`](CONTRIBUTOR_POLICY.md) and [`CONTRIBUTING.md`](CONTRIBUTING.md).

A future legal review may recommend a Developer Certificate of Origin, corporate contribution process, or other provenance control. Such a process must not be described as active until it is publicly adopted.

## Trademarks and official status

The Apache License does not grant broad rights to use the PactRide name, logos, or future certification marks as product branding.

Truthful descriptive statements such as "implements the PactRide protocol" should remain possible. Claims such as "Official PactRide," "PactRide certified," or "endorsed by PactRide" require authorization under the applicable trademark or certification policy.

See [`TRADEMARK.md`](TRADEMARK.md).

## Sustainable funding

Apache-2.0 does not make the founder part of every third party's revenue. PactRide can still be funded through optional value around the project, including:

- grants, sponsorships, and donations;
- paid implementation and integration work;
- security, privacy, accessibility, and interoperability audits;
- managed relays or other replaceable hosted infrastructure;
- support, training, and service-level agreements;
- official applications or operations products;
- paid commercial licenses for future official software when the project owns the required rights;
- authorized trademark, certification, or compatibility-review programs;
- partnerships with cooperatives, universities, nonprofits, municipalities, or commercial operators.

These activities must not turn one provider into mandatory protocol infrastructure or create a hidden fee for base protocol participation.

## Founder economic position

The realistic way for the founder to benefit is to create optional value and maintain recognized stewardship, not to assume that publishing the idea produces an automatic royalty right.

The strongest potential assets are:

- high-quality official software;
- implementation expertise;
- trusted project stewardship;
- official branding and authorized certification;
- hosted infrastructure and support;
- partnerships, grants, and funded research;
- commercial licenses for separately licensed software where rights permit.

The open specification remains usable without purchasing those offerings.

## Relationship to CommonPact

Creating CommonPact does not alter the license already granted for PactRide material. CommonPact must publish its own license and contribution policy in its own repository.

Shared concepts do not automatically transfer copyright ownership, trademark rights, dependency requirements, or commercial terms between the projects. See [`COMMONPACT_RELATIONSHIP.md`](COMMONPACT_RELATIONSHIP.md).

## Legal review triggers

Professional legal review is appropriate before:

- changing the specification repository's license;
- starting a dual-licensed official software project;
- adopting a contributor license agreement or copyright assignment;
- registering or licensing trademarks or certification marks;
- offering warranties, indemnities, safety commitments, or compatibility certification;
- accepting regulated funds or operating payment services;
- operating a real transportation service or pilot;
- asserting patent rights or negotiating royalty agreements.

## Controlling terms

This document is an explanatory project policy. It does not replace the license text or create a contract beyond the applicable licenses and separately executed agreements.

The root [`LICENSE`](LICENSE) file controls the current repository.