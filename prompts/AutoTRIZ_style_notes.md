# AutoTRIZ-style Baseline Notes

## Framework basis

This baseline is a task-adapted implementation of **AutoTRIZ: Automating engineering innovation with TRIZ and large language models**.

Official resources:

- Website: https://www.autotriz.ai/
- Repository: https://github.com/shuojiangcn/AutoTRIZ-Repository/

The original AutoTRIZ workflow is:

specific problem → engineering contradiction → contradiction-matrix lookup → inventive principles → specific solution.

Modules 1, 2, and 4 are LLM-driven, while Module 3 is a deterministic lookup in the TRIZ contradiction matrix.

## Source mapping

The official repository provides the project description and TRIZ case base, but does not expose the original implementation prompts.

Therefore, `AutoTRIZ_style.md` contains the task-adapted prompts used for the comparative implementation, organized according to the reasoning modules described in the paper rather than verbatim prompts extracted from the repository.

## Task adaptation

The original TRIZ reasoning flow was preserved and adapted only to rehabilitation assistive device configuration. The generated solution is finally converted into the common **If–Then–Unless–Verify** format used in the comparison.

## Evaluation controls

The AutoTRIZ-style baseline used the same backbone LLM, case inputs, available domain knowledge, maximum designer-feedback rounds, and generation budget as the other compared methods.

The designer-confirmed reference rules and post-adjustment outcomes were not provided to the generation prompts and were used only for evaluation.
