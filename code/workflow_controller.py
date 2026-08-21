"""Stage gating and identifier checks for the C-K workflow.

This module controls observable workflow transitions. It does not attempt to
control hidden token-level model reasoning.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

STAGES = ("EAA", "PAA", "CIA", "CRA", "RGA")
NEXT_STAGE = {"EAA": "PAA", "PAA": "CIA", "CIA": "CRA", "CRA": "RGA", "RGA": "DESIGNER"}


def validate_stage_output(payload: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    required = ("agent", "c_k_operator", "stage_status", "task_output", "missing_information", "return_to", "next_agent")
    errors.extend(f"missing field: {name}" for name in required if name not in payload)
    if errors:
        return errors
    if payload["agent"] not in STAGES:
        errors.append(f"unknown agent: {payload['agent']}")
    if payload["stage_status"] not in {"READY", "NEEDS_REVISION"}:
        errors.append("stage_status must be READY or NEEDS_REVISION")
    if not isinstance(payload["task_output"], dict):
        errors.append("task_output must be an object")
    if not isinstance(payload["missing_information"], list):
        errors.append("missing_information must be an array")
    return errors


def decide_transition(payload: dict[str, Any]) -> dict[str, Any]:
    """Return a transition decision without invoking a model."""

    errors = validate_stage_output(payload)
    if errors:
        return {"accepted": False, "action": "REJECT", "errors": errors}
    agent = payload["agent"]
    if payload["stage_status"] == "NEEDS_REVISION":
        return {
            "accepted": True,
            "action": "ROLLBACK",
            "return_to": payload["return_to"],
            "next_agent": "NONE",
        }
    expected = NEXT_STAGE[agent]
    if payload["next_agent"] != expected:
        return {"accepted": False, "action": "REJECT", "errors": [f"READY output must set next_agent={expected}"]}
    return {"accepted": True, "action": "ADVANCE", "next_agent": expected}


def _collect_ids(value: Any) -> set[str]:
    found: set[str] = set()
    if isinstance(value, dict):
        for key, item in value.items():
            if key.endswith("_id") and isinstance(item, str) and item:
                found.add(item)
            elif key.endswith("_ids") and isinstance(item, list):
                found.update(x for x in item if isinstance(x, str) and x)
            found.update(_collect_ids(item))
    elif isinstance(value, list):
        for item in value:
            found.update(_collect_ids(item))
    return found


def missing_identifiers(previous: dict[str, Any], current: dict[str, Any]) -> list[str]:
    """Find identifiers emitted by a stage but absent from the next output."""

    return sorted(_collect_ids(previous) - _collect_ids(current))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output_json", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.output_json.read_text(encoding="utf-8"))
    print(json.dumps(decide_transition(payload), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
