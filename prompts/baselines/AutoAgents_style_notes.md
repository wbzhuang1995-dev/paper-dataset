# AutoAgents-style Baseline Notes

## Framework basis

This baseline is a task-adapted implementation of **AutoAgents: A Framework for Automatic Agent Generation**:

https://github.com/Link-AGI/AutoAgents

It preserves the original two-stage organization: a **Drafting Stage**, in which the Planner works with the Agent Observer and Plan Observer to construct an expert team and execution plan, and an **Execution Stage**, in which the Action Observer coordinates dynamically generated Custom Agents.

## Source mapping

The prompt design was derived from the corresponding prompt-bearing components in the official paper and repository, including:

- Planner
- Agent Observer
- Plan Observer
- Action Observer
- Custom Agent

The repository files used for source mapping include:

- `autoagents/actions/create_roles.py`
- `autoagents/actions/check_roles.py`
- `autoagents/actions/check_plans.py`
- `autoagents/actions/steps.py`
- `autoagents/actions/custom_action.py`

## Task adaptation

The adaptation was limited to the personalized rehabilitation assistive device configuration task and the unified **If–Then–Unless–Verify** output format used in the comparative experiments.

AutoAgents-style retains dynamic expert-role generation rather than replacing it with fixed roles from the proposed method. Case-specific information is inserted into the prompt placeholders at runtime.

## Evaluation controls

The AutoAgents-style baseline used the same backbone LLM, case inputs, available domain knowledge, maximum designer-feedback rounds, and generation budget as the other compared methods.

The designer-confirmed reference rules and post-adjustment outcomes were not provided to the generation prompts and were used only for evaluation.
