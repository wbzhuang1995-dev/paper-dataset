"""Reviewer-facing definitions of the five C-K workflow agents.

This file describes observable responsibilities and handoff contracts. It is
deliberately independent of any model provider, private dataset, or
evaluation result.
"""

from __future__ import annotations

from typing import Any


AGENTS: dict[str, dict[str, Any]] = {
    "EAA": {
        "operator": "C-C",
        "purpose": "Transform wearing feedback into structured requirements.",
        "input": ["wearing_feedback", "current_EBOM", "rehabilitation_stage", "short_term_memory"],
        "output": "requirements",
        "next_agent": "PAA",
        "prohibited": ["mechanical causes", "conflicts", "configuration actions", "design rules"],
    },
    "PAA": {
        "operator": "C-K",
        "purpose": "Associate requirements with possible causes and supplied evidence.",
        "input": ["structured_requirements", "current_EBOM", "DMKG_evidence", "working_memory", "long_term_memory"],
        "output": "cause_evidence",
        "next_agent": "CIA",
        "prohibited": ["unsupported evidence", "conflict identification", "configuration actions"],
    },
    "CIA": {
        "operator": "K-K",
        "purpose": "Identify supported target, structural, parameter, boundary, and validation conflicts.",
        "input": ["structured_requirements", "cause_evidence", "current_EBOM", "DMKG_evidence", "long_term_memory"],
        "output": "conflicts",
        "next_agent": "CRA",
        "prohibited": ["solution proposals", "parameter adjustments"],
    },
    "CRA": {
        "operator": "K-C/K-K",
        "purpose": "Generate feasible, evidence-backed candidate resolution actions.",
        "input": ["structured_requirements", "cause_evidence", "conflicts", "current_EBOM", "DMKG_evidence", "working_memory", "long_term_memory"],
        "output": "candidate_actions",
        "next_agent": "RGA",
        "prohibited": ["unsupported modules", "unsupported parameters", "final rules"],
    },
    "RGA": {
        "operator": "K-C/K-K",
        "purpose": "Integrate validated actions into a candidate EBOM, decision card, and If-Then-Unless-Verify rule.",
        "input": ["wearing_feedback", "structured_requirements", "cause_evidence", "conflicts", "candidate_actions", "current_EBOM", "working_memory", "designer_feedback"],
        "output": "candidate_rule_and_decision_card",
        "next_agent": "DESIGNER",
        "prohibited": ["new unsupported causes", "new unsupported conflicts", "new unsupported actions", "final status without designer approval"],
    },
}

WORKFLOW_SEQUENCE = ("EAA", "PAA", "CIA", "CRA", "RGA", "DESIGNER")


def agent_definition(agent: str) -> dict[str, Any]:
    """Return a copy of one public agent definition."""

    if agent not in AGENTS:
        raise KeyError(f"unknown agent: {agent}")
    return dict(AGENTS[agent])
