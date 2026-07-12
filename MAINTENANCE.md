# PactRide Maintenance Policy

## Current posture

PactRide is maintained as a **limited-capacity public research project**. It is not a funded product team, operating transportation company, or production service.

The repository may receive documentation corrections, protocol clarifications, security fixes, schema improvements, test vectors, and contributor support. It does not promise continuous feature development, response times, release dates, or a production launch.

## What limited maintenance means

- Issues may remain open for extended periods.
- Roadmap phases have evidence gates, not delivery dates.
- Lack of recent commits does not mean the protocol is complete, safe, abandoned, or production-ready.
- Maintainers may prioritize correctness and review over implementation speed.
- Experimental work may happen in independent repositories before being proposed here.
- Real transportation pilots remain blocked on technical, legal, safety, insurance, privacy, accessibility, and operational evidence.

## Work that may continue without a funded implementation effort

- correcting inaccurate or stale public claims;
- improving schemas, semantic validation, and test vectors;
- recording prior art and research evidence;
- documenting driver and rider workflows;
- security, privacy, accessibility, and abuse analysis;
- small website and documentation improvements;
- evaluating external implementations or pilot proposals.

## Conditions for major development

Major implementation work should resume only when at least one of the following exists:

1. two or more capable developers commit to independent interoperability work;
2. a credible driver cooperative, university, nonprofit, municipal group, or transportation organization proposes a bounded research partnership;
3. a grant, sponsor, or institutional partner funds defined work without controlling the protocol;
4. a qualified technical maintainer assumes sustained responsibility for a reference implementation;
5. a legally reviewed, safety-bounded pilot has clear operators, insurance, support, and incident procedures.

Interest, stars, forks, social-media attention, or an unverified promise to contribute are not sufficient by themselves.

## No implied roadmap commitment

Roadmap phases describe the order in which evidence should be produced. They are not schedules, contractual commitments, fundraising promises, or statements that later phases will occur.

Any public estimate should identify its assumptions, responsible participants, funding source, and unresolved blockers.

## Inactivity and archival status

The repository may be marked inactive or archived when:

- no active maintainer is available;
- unresolved safety or legal risks make continued public development misleading;
- the work is superseded by a stronger interoperable project;
- maintenance costs exceed available capacity;
- the project no longer has a credible path to independent implementation.

Before archival, maintainers should update `STATUS.md`, preserve the research record, identify known successors or alternatives, and remove claims that imply active development.

Archival would not revoke the Apache-2.0 license or erase the project's history.

## Resuming after inactivity

A restart should begin with an updated audit of:

- current mobile-platform constraints;
- transport and encryption standards;
- schemas and conformance vectors;
- privacy and threat models;
- relevant transportation law and insurance requirements;
- maintainers, funding, and pilot partners;
- website and repository claims.

The project should not resume from an old roadmap as though technical and legal assumptions remained unchanged.

## Status source

`STATUS.md` is the canonical snapshot of current evidence. `MAINTAINERS.md` records current stewardship. This file records maintenance expectations and restart conditions.
