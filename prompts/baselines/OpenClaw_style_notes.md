# OpenClaw_5.7_style Baseline Notes

## Framework basis

This baseline is a task-adapted implementation of **OpenClaw 2026.5.7**:

https://github.com/openclaw/openclaw

OpenClaw uses a primary tool-enabled assistant with workspace context, optional memory access, and isolated-by-default sub-agent delegation rather than a fixed role-based SOP.

## Source mapping

The prompt design was derived from the supplied OpenClaw 2026.5.7 source, especially:

- `src/agents/system-prompt.ts` — main-agent system prompt and workspace/tool guidance;
- `src/agents/subagent-system-prompt.ts` — sub-agent focus and reporting behavior;
- `src/agents/tools/sessions-spawn-tool.ts` and `src/agents/subagent-spawn.ts` — sub-agent spawning and context isolation;
- `src/agents/tools/update-plan-tool.ts` — optional structured planning;
- `docs/reference/templates/AGENTS.md` and `docs/concepts/system-prompt.md` — workspace and memory-context behavior.

Only mechanisms relevant to the comparative configuration task were retained; unrelated messaging, CLI, sandbox, heartbeat, and deployment instructions were omitted.

## Task adaptation

The adaptation was limited to the rehabilitation assistive device configuration task and the common **If–Then–Unless–Verify** output format.

No fixed expert-role chain was introduced. The main agent remains responsible for tool use, optional focused delegation, and final synthesis.

## Evaluation controls

The OpenClaw-style baseline used the same backbone LLM, case inputs, available domain knowledge, maximum designer-feedback rounds, and generation budget as the other compared methods.

The designer-confirmed reference rules and post-adjustment outcomes were not provided to the generation prompts and were used only for evaluation.
