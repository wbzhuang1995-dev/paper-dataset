# MetaGPT-style Baseline Notes

## Framework basis

This baseline is a task-adapted implementation of **MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework**:

https://github.com/geekan/MetaGPT

It preserves MetaGPT's fixed role-specialized SOP: Product Manager → Architect → Project Manager → Engineer → QA Engineer, with structured intermediate outputs passed between roles.

## Source mapping

The implementation was organized with reference to the corresponding official repository components, including:

- `metagpt/roles/product_manager.py`
- `metagpt/roles/architect.py`
- `metagpt/roles/project_manager.py`
- `metagpt/roles/engineer.py`
- `metagpt/roles/qa_engineer.py`

Relevant action/prompt components include `write_prd_an.py`, `design_api_an.py`, `project_management_an.py`, `write_code.py`, `write_code_review.py`, and `write_test.py`.

## Task adaptation

The original software-development handoffs were mapped to the RAD configuration task as follows:

- Product Manager → structured wearing/configuration requirements;
- Architect → configuration design;
- Project Manager → ordered task plan;
- Engineer → candidate If–Then–Unless–Verify rule;
- QA Engineer → rule review and revision feedback.

The fixed SOP and structured handoff principle were retained; no dynamic role generation was introduced.

## Evaluation controls

The MetaGPT-style baseline used the same backbone LLM, case inputs, available domain knowledge, maximum designer-feedback rounds, and generation budget as the other compared methods.

The designer-confirmed reference rules and post-adjustment outcomes were not provided to the generation prompts and were used only for evaluation.
