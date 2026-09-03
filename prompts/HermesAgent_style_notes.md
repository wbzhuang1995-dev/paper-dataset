# HermesAgent 0.12-style Baseline Notes

## Framework basis

This baseline is a task-adapted implementation of the open-source **Hermes Agent v0.12.0 (v2026.4.30)** project from Nous Research:

https://github.com/NousResearch/hermes-agent

Hermes Agent is organized around a primary tool-using agent that can maintain a task list and delegate focused subtasks to isolated subagents. Each subagent receives only the task and context explicitly passed by the parent, and its summary is returned to the parent for final synthesis.

## Source mapping

The prompt organization was derived from the supplied source, including:

- `agent/prompt_builder.py`
- `run_agent.py`
- `tools/todo_tool.py`
- `tools/delegate_tool.py`

These components define the main-agent prompt assembly, compact task planning, delegation behavior, and isolated subagent execution.

## Task adaptation

The adaptation was limited to the rehabilitation assistive device configuration task and the common **If–Then–Unless–Verify** output format.

No fixed expert-role chain was introduced. The main Hermes-style agent decides whether to solve the task directly or delegate focused subtasks.

## Evaluation controls

The HermesAgent-style baseline used the same backbone LLM, case inputs, available domain knowledge, maximum designer-feedback rounds, and generation budget as the other compared methods.

The designer-confirmed reference rules and post-adjustment outcomes were not provided to the generation prompts and were used only for evaluation.
