# Contributing to PactRide

PactRide needs criticism, protocol design, security analysis, driver and rider workflows, accessibility research, independent implementations, tests, and documentation. Contributors do not need to agree with the proposal.

PactRide is maintained at limited capacity. Response times and merge schedules are not guaranteed. Read [`MAINTENANCE.md`](MAINTENANCE.md) before proposing large implementation work and [`MAINTAINERS.md`](MAINTAINERS.md) for current stewardship.

## License

PactRide is licensed under the **Apache License 2.0**. Unless a file contains a different explicit notice, contributions intentionally submitted for inclusion are provided under Apache-2.0 as described in Section 5 of the license.

By submitting work, you confirm that you have the right to contribute it and that third-party material, employer ownership, and significant provenance concerns are disclosed. Read [`CONTRIBUTOR_POLICY.md`](CONTRIBUTOR_POLICY.md) before opening a pull request.

## Start here

New contributors should begin with the repository's [good first issues](https://github.com/wpggLabs/PactRide/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).

Good beginner work includes:

- plain-language documentation and glossary improvements;
- primary-source citations;
- small website accessibility corrections;
- one documented invalid fixture;
- terminology and link audits;
- non-normative translations.

Cryptography, identity binding, normative lifecycle changes, safety claims, and production pilot design are not beginner tasks unless a maintainer explicitly narrows and supervises the work.

## Useful contribution paths

### Drivers and riders

- Describe a concrete dispatch, payment, safety, accessibility, or deactivation failure.
- Review whether the ride lifecycle reflects real behavior.
- Identify information that should not be public.
- Test terminology and user warnings.

### Protocol engineers

- Review event schemas and state transitions.
- Improve serialization, proof, encryption, and transport profiles.
- Build independent parsers and validators.
- Add conformance vectors.

### Security and privacy researchers

- Attack the threat model.
- Model location correlation.
- Simulate Sybil and reputation-farming attacks.
- Review key custody, rotation, encryption, and nearby-device behavior.

### Mobile developers

- Prototype key storage, relay transport, QR pickup proof, background delivery, and encrypted local storage.
- Measure battery and operating-system restrictions rather than assuming reliability.

### Designers and accessibility specialists

- Design understandable trust evidence.
- Review screen-reader, mobility, hearing, language, and cognitive accessibility requirements.
- Prevent privacy controls from becoming unusable.

### Institutions and operators

Universities, cooperatives, nonprofits, municipalities, and research groups should open an issue describing:

- the proposed research or pilot scope;
- who is responsible for technical and operational work;
- funding and conflicts of interest;
- participant safety, insurance, privacy, and accessibility boundaries;
- what evidence the work would produce for the public protocol.

General interest without committed people, funding, or a bounded study is not treated as an active pilot.

## Before opening a pull request

1. Search existing issues and RFCs.
2. State whether the change is normative, explanatory, experimental, or implementation-specific.
3. Explain privacy, security, compatibility, accessibility, and migration impact.
4. Add tests or a test plan for protocol changes.
5. Do not claim unverified safety, decentralization, anonymity, or reliability.
6. Disclose relevant commercial interests.
7. Confirm that you can submit the work under Apache-2.0.
8. Identify third-party material and required notices.
9. Disclose significant AI assistance when it creates provenance or review concerns.
10. Do not include private keys, identity documents, real trip histories, or confidential data.
11. Keep changes narrowly scoped and avoid unrelated refactors.

## RFC template

Create `rfcs/NNNN-short-name.md` containing:

- Summary.
- Motivation.
- User stories.
- Normative specification.
- Event and schema changes.
- Privacy analysis.
- Threat analysis.
- Compatibility and migration.
- Alternatives considered.
- Test plan.
- Open questions.
- Implementation status.

## Commit style

Use focused commits:

- `docs:` documentation.
- `rfc:` protocol proposals.
- `schema:` machine-readable definitions.
- `test:` conformance vectors.
- `security:` security changes.
- `governance:` process changes.
- `legal:` licensing, trademark, or contribution-policy changes.
- `website:` public-site changes.

## Review standards

Reviewers should ask:

- Does this create a hidden mandatory service?
- Does it expose more location or identity data?
- Can two independent clients implement it identically?
- What happens with duplicate, delayed, conflicting, or malicious events?
- Is the claim testable?
- Is the feature part of the base protocol or a local policy?
- Is the contribution compatible with Apache-2.0 and all third-party notices?
- Does the change imply staffing, funding, safety, or production readiness that does not exist?

## Small first contributions

- Add a primary-source citation to `PRIOR_ART.md`.
- Create or improve a plain-language glossary entry.
- Create one invalid event fixture for an existing rule.
- Review one schema for personal-data leakage.
- Document a real ride cancellation edge case.
- Test the website at keyboard-only navigation and 200% zoom.
- Translate non-normative introductory material.

## Prohibited contributions

- Copied code or text without compatible licensing.
- Embedded secrets, identity documents, or real trip data.
- Token sales or investment promotion.
- Claims that PactRide bypasses all law or guarantees safety.
- Backdoors, hidden telemetry, or undisclosed centralized dependencies.
- Code or documentation submitted under terms that conflict with Apache-2.0.
- Unreviewed production deployment instructions presented as safe operating guidance.

## Discussion quality

Critique the design, evidence, and tradeoffs. Do not attack contributors. Strong disagreement is acceptable; harassment is not.
