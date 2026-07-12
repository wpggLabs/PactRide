#!/usr/bin/env python3
"""Validate PactRide schemas and regression vectors without network access."""

from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
from typing import Any

import rfc8785
from jsonschema import Draft202012Validator
from jsonschema.exceptions import ValidationError
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
VECTORS = ROOT / "test-vectors"


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def build_registry(*schemas: dict[str, Any]) -> Registry:
    resources = [(schema["$id"], Resource.from_contents(schema)) for schema in schemas]
    return Registry().with_resources(resources)


def expect_invalid(validator: Draft202012Validator, instance: dict[str, Any], label: str) -> None:
    try:
        validator.validate(instance)
    except ValidationError:
        return
    raise AssertionError(f"Expected invalid instance: {label}")


def canonical_bytes(value: dict[str, Any]) -> bytes:
    encoded = rfc8785.dumps(value)
    return encoded.encode("utf-8") if isinstance(encoded, str) else encoded


def recompute_event_id(event: dict[str, Any]) -> str:
    signing_object = copy.deepcopy(event)
    signing_object.pop("event_id", None)
    signing_object.pop("proofs", None)
    digest = hashlib.sha256(canonical_bytes(signing_object)).hexdigest()
    return f"sha256:{digest}"


def validate_proof_semantics(event: dict[str, Any]) -> None:
    proofs = event["proofs"]
    signers = [proof["signer"] for proof in proofs]

    if len(signers) != len(set(signers)):
        raise AssertionError("duplicate proof signer")
    if signers.count(event["actor"]) != 1:
        raise AssertionError("primary actor must appear exactly once in proofs")

    if event["type"] in {"pickup.proof", "ride.completed.receipt"}:
        expected = {event["payload"]["rider"], event["payload"]["driver"]}
        if set(signers) != expected or len(signers) != 2:
            raise AssertionError("bilateral ride proof signer set mismatch")

    if event["type"] == "identity.binding":
        expected = {
            event["payload"]["discovery_key"],
            event["payload"]["identity_key"],
        }
        if set(signers) != expected or len(signers) != 2:
            raise AssertionError("identity binding signer set mismatch")



EXPECTED_V01_EVENT_TYPES = {
    "ride.request", "driver.availability", "ride.withdraw", "ride.offer", "ride.counter",
    "identity.binding", "ride.accept", "ride.decline", "ride.cancel", "driver.departing",
    "driver.arrived", "pickup.challenge", "pickup.proof", "ride.started", "ride.progress",
    "ride.abort", "ride.completed.claim", "ride.completed.receipt", "ride.disputed",
    "ride.rating", "identity.attestation", "vehicle.attestation", "credential.revocation",
    "key.rotation", "moderation.warning",
}


def run_lifecycle_scenario(scenario: dict[str, Any]) -> str:
    state: str | None = None
    seen: set[str] = set()
    current_terms: str | None = None
    accepts: dict[str, set[str]] = {}

    for item in scenario["events"]:
        event_key = item["id"]
        if event_key in seen:
            continue
        seen.add(event_key)
        event_type = item["type"]

        if event_type == "ride.request":
            if state is not None:
                raise AssertionError(f"ride.request invalid from {state}")
            state = "Requested"
        elif event_type == "ride.offer":
            if state not in {"Requested", "Matching"}:
                raise AssertionError(f"ride.offer invalid from {state}")
            state = "Matching"
            current_terms = item["terms_hash"]
            accepts.clear()
        elif event_type == "ride.counter":
            if state != "Matching":
                raise AssertionError(f"ride.counter invalid from {state}")
            current_terms = item["terms_hash"]
            accepts.clear()
        elif event_type == "ride.accept":
            if state != "Matching":
                raise AssertionError(f"ride.accept invalid from {state}")
            terms_hash = item["terms_hash"]
            if terms_hash != current_terms:
                raise AssertionError("stale terms acceptance")
            accepts.setdefault(terms_hash, set()).add(item["actor"])
            if len(accepts[terms_hash]) == 2:
                state = "Accepted"
        elif event_type == "driver.departing":
            if state != "Accepted":
                raise AssertionError(f"driver.departing invalid from {state}")
            state = "DriverDeparting"
        elif event_type == "driver.arrived":
            if state != "DriverDeparting":
                raise AssertionError(f"driver.arrived invalid from {state}")
            state = "DriverArrived"
        elif event_type == "pickup.proof":
            if state != "DriverArrived":
                raise AssertionError(f"pickup.proof invalid from {state}")
            state = "PickupVerified"
        elif event_type == "ride.started":
            if state != "PickupVerified":
                raise AssertionError(f"ride.started invalid from {state}")
            state = "InProgress"
        elif event_type == "ride.completed.claim":
            if state != "InProgress":
                raise AssertionError(f"ride.completed.claim invalid from {state}")
            state = "CompletionClaimed"
        elif event_type == "ride.completed.receipt":
            if state != "CompletionClaimed":
                raise AssertionError(f"ride.completed.receipt invalid from {state}")
            state = "Completed"
        elif event_type == "ride.cancel":
            if state not in {"Requested", "Matching", "Accepted", "DriverDeparting", "DriverArrived"}:
                raise AssertionError(f"ride.cancel invalid from {state}")
            state = "Cancelled"
        elif event_type == "ride.abort":
            if state not in {"PickupVerified", "InProgress", "CompletionClaimed"}:
                raise AssertionError(f"ride.abort invalid from {state}")
            state = "Aborted"
        elif event_type == "ride.disputed":
            if state not in {"CompletionClaimed", "Completed", "Aborted"}:
                raise AssertionError(f"ride.disputed invalid from {state}")
            state = "Disputed"
        elif event_type == "clock.expire":
            if state not in {"Requested", "Matching"}:
                raise AssertionError(f"clock.expire invalid from {state}")
            state = "Expired"
        else:
            raise AssertionError(f"unsupported lifecycle fixture event: {event_type}")

    return state or "None"


def validate_extended_artifacts(registry: Registry) -> None:
    event_types_schema = load_json(SCHEMAS / "protocol-event-types.schema.json")
    event_types_validator = Draft202012Validator(event_types_schema, registry=registry)
    fixture_set = load_json(VECTORS / "protocol-event-types-v0.1.json")

    actual_types = {item["type"] for item in fixture_set["valid"]}
    actual_types.add("ride.request")  # covered by the existing normative public request vector
    assert actual_types == EXPECTED_V01_EVENT_TYPES, (
        f"Event fixture coverage mismatch; missing={sorted(EXPECTED_V01_EVENT_TYPES - actual_types)}, "
        f"extra={sorted(actual_types - EXPECTED_V01_EVENT_TYPES)}"
    )

    for item in fixture_set["valid"]:
        event_types_validator.validate(item)
        validate_proof_semantics(item)

    for case in fixture_set["invalid"]:
        if case.get("semantic"):
            event_types_validator.validate(case["event"])
            try:
                validate_proof_semantics(case["event"])
            except AssertionError:
                pass
            else:
                raise AssertionError(f"Expected semantic rejection: {case['id']}")
        else:
            expect_invalid(event_types_validator, case["event"], case["id"])

    lifecycle = load_json(VECTORS / "lifecycle-v0.1.json")
    scenario_ids: set[str] = set()
    for scenario in lifecycle["scenarios"]:
        assert scenario["id"] not in scenario_ids, f"duplicate lifecycle scenario id: {scenario['id']}"
        scenario_ids.add(scenario["id"])
        if "expected_error" in scenario:
            try:
                run_lifecycle_scenario(scenario)
            except AssertionError as exc:
                assert scenario["expected_error"] in str(exc), (
                    f"{scenario['id']} rejected for unexpected reason: {exc}"
                )
            else:
                raise AssertionError(f"Expected lifecycle rejection: {scenario['id']}")
        else:
            actual = run_lifecycle_scenario(scenario)
            assert actual == scenario["expected_state"], (
                f"{scenario['id']} expected {scenario['expected_state']}, got {actual}"
            )

def main() -> None:
    envelope_schema = load_json(SCHEMAS / "event-envelope.schema.json")
    request_schema = load_json(SCHEMAS / "ride-request.schema.json")
    public_schema = load_json(SCHEMAS / "public-ride-request-event.schema.json")

    registry = build_registry(envelope_schema, request_schema, public_schema)
    envelope_validator = Draft202012Validator(envelope_schema, registry=registry)
    public_validator = Draft202012Validator(public_schema, registry=registry)

    vector = load_json(VECTORS / "event-id-v0.1.json")
    complete_event = vector["complete_event"]

    # Validate every JSON artifact parses before deeper checks.
    for path in sorted(ROOT.rglob("*.json")):
        load_json(path)

    # Normative event-ID vector.
    canonical = canonical_bytes(vector["signing_object"])
    assert canonical.decode("utf-8") == vector["canonical_json"]
    digest = hashlib.sha256(canonical).hexdigest()
    assert digest == vector["expected_digest_hex"]
    assert f"sha256:{digest}" == vector["expected_event_id"]
    assert recompute_event_id(complete_event) == complete_event["event_id"]

    # The public request passes the whole-envelope validator.
    public_validator.validate(complete_event)
    validate_proof_semantics(complete_event)

    # P1: undeclared and sensitive top-level fields are rejected.
    with_phone = copy.deepcopy(complete_event)
    with_phone["phone"] = "+1-555-0100"
    expect_invalid(public_validator, with_phone, "public top-level phone")

    with_extensions = copy.deepcopy(complete_event)
    with_extensions["extensions"] = {"example.com/contact": {"phone": "+1-555-0100"}}
    expect_invalid(public_validator, with_extensions, "public extensions")

    # P2: contradictory geohash precision cannot be represented.
    with_precision = copy.deepcopy(complete_event)
    with_precision["payload"]["pickup"]["precision"] = 3
    expect_invalid(public_validator, with_precision, "separate geohash precision")

    # P2: legacy earliest/latest windows are rejected.
    reversed_window = copy.deepcopy(complete_event)
    reversed_window["payload"]["window"] = {
        "earliest": 1783743600,
        "latest": 1783742700,
    }
    expect_invalid(public_validator, reversed_window, "legacy reversed window")

    # P2: expiry is after creation by construction because TTL is positive.
    zero_ttl = copy.deepcopy(complete_event)
    zero_ttl["ttl_seconds"] = 0
    expect_invalid(public_validator, zero_ttl, "nonpositive TTL")

    # P1: non-ride-scoped identity evidence does not require a fake ride ID.
    cases = load_json(VECTORS / "review-cases-v0.1.json")
    non_ride_case = next(
        case for case in cases["cases"] if case["id"] == "P1-non-ride-attestation-without-ride-id"
    )
    envelope_validator.validate(non_ride_case["event"])

    # P1: bilateral events require an array with at least two proof entries.
    pickup = copy.deepcopy(complete_event)
    pickup.pop("ttl_seconds", None)
    pickup["type"] = "pickup.proof"
    pickup["actor"] = "npub-rider-A-000000"
    pickup["payload"] = {
        "rider": "npub-rider-A-000000",
        "driver": "npub-driver-B-000000",
        "challenge_hash": "sha256:" + "1" * 64,
    }
    pickup["proofs"] = [
        {
            "signer": "npub-rider-A-000000",
            "algorithm": "schnorr-secp256k1",
            "signature": "0" * 128,
        }
    ]
    pickup["event_id"] = recompute_event_id(pickup)
    expect_invalid(envelope_validator, pickup, "single-proof bilateral event")

    pickup["proofs"].append(
        {
            "signer": "npub-driver-B-000000",
            "algorithm": "schnorr-secp256k1",
            "signature": "1" * 128,
        }
    )
    pickup["event_id"] = recompute_event_id(pickup)
    envelope_validator.validate(pickup)
    validate_proof_semantics(pickup)

    required_review_ids = {
        "P1-event-id-self-reference",
        "P1-bilateral-single-signature",
        "P1-public-sensitive-top-level-field",
        "P1-public-extension-object",
        "P1-non-ride-attestation-without-ride-id",
        "P2-contradictory-geohash-precision",
        "P2-reversed-window-legacy-shape",
        "P2-nonpositive-expiry",
        "P2-post-pickup-cancel",
        "P2-decline-after-acceptance",
        "P2-request-expiry",
        "P2-unbound-identity-switch",
    }
    actual_review_ids = {case["id"] for case in cases["cases"]}
    missing = required_review_ids - actual_review_ids
    assert not missing, f"Missing review regression cases: {sorted(missing)}"

    validate_extended_artifacts(registry)

    print("PactRide protocol artifacts validated successfully.")


if __name__ == "__main__":
    main()
