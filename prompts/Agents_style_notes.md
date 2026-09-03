# Agents-style Baseline Notes

## Framework basis

The Agents-style baseline is a task-adapted implementation based on the open-source **AGENTS** framework described in *Agents: An Open-source Framework for Autonomous Language Agents* and released at:

https://github.com/aiwaves-cn/agents

The baseline retains the AGENTS organization of **Agent + Environment + SOP (Standard Operating Procedure)**, modular prompt components, shared interaction history, and LLM-based role routing. The adaptation is limited to the personalized rehabilitation assistive device (RAD) configuration task and the unified **If–Then–Unless–Verify** rule format used in the comparative experiments.

## Prompt organization

The released `Agents_style.md` contains only the prompt texts used for the task-adapted Agents-style implementation, including the shared case context, shared task instruction, role prompts, role-routing prompt, final-output prompt, and designer-feedback refinement prompt.

Case-specific information is inserted into the corresponding placeholders at runtime.

## Evaluation controls

For the comparative experiments, the Agents-style baseline used the same backbone LLM, case inputs, available domain knowledge, maximum designer-feedback rounds, and generation budget as the other compared methods.

The designer-confirmed reference rules and post-adjustment outcomes were not provided to the generation prompts and were used only for subsequent evaluation.

The Agents-style baseline did not use the proposed method's C–K-guided stage constraints, DMKG reasoning-chain mechanism, hierarchical LTM/STM/WM orchestration, decision-card mechanism, or TRIZ-assisted CIA–CRA workflow.
