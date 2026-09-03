# AutoTRIZ-style Baseline Prompts

## 1. Task Context

```text
Wearing feedback: {wearing_feedback}
Current configuration: {current_configuration}
Available domain knowledge: {domain_knowledge}
Configuration constraints: {configuration_constraints}

Task:
Use the AutoTRIZ reasoning flow to identify the configuration problem, detect one TRIZ engineering contradiction, retrieve the corresponding inventive principles, and generate an appropriate rehabilitation assistive device configuration solution.

Required final rule format:

If: <trigger condition>
Then: <configuration adjustment>
Unless: <exception or applicability boundary>
Verify: <verification condition>
```

## 2. Module 1 — Problem Identification Prompt

```text
Identify the specific engineering problem from the task context.

Extract only information directly relevant to:
- the current undesirable situation;
- the desired improvement;
- the applicable constraints.

Do not propose solutions.

Output:

## Problem Statement
<concise problem statement>
```

## 3. Module 2 — Contradiction Detection Prompt

```text
Problem Statement:
{problem_statement}

TRIZ Engineering Parameters:
{triz_39_engineering_parameters}

Identify one TRIZ engineering contradiction that best represents the main trade-off in the problem.

Select one Improving Feature and one Worsening Feature using only the provided TRIZ engineering parameters.

Output:

## Improving Feature
<index>: <parameter name>

## Worsening Feature
<index>: <parameter name>

## Rationale
<brief explanation>
```

## 4. Module 4 — Solution Generation Prompt

```text
Problem Statement:
{problem_statement}

Detected Engineering Contradiction:
Improving Feature: {improving_feature}
Worsening Feature: {worsening_feature}

Retrieved TRIZ Inventive Principles:
{retrieved_inventive_principles}

Current Configuration:
{current_configuration}

Available Domain Knowledge:
{domain_knowledge}

Configuration Constraints:
{configuration_constraints}

Apply the retrieved inventive principles to the specific rehabilitation assistive device configuration problem.

Generate only supported and feasible configuration solution candidates. Each candidate should state the applied inventive principle and the corresponding configuration solution.

Do not introduce unsupported modules, parameter values, or validation results.

Output:

## Generated Solutions

### Solution 1
Applied Principle: <principle>
Configuration Solution: <solution>

### Solution 2
Applied Principle: <principle>
Configuration Solution: <solution>
```

## 5. Final Rule Formatting Prompt

```text
Problem Statement:
{problem_statement}

Detected Engineering Contradiction:
{engineering_contradiction}

Generated Solutions:
{generated_solutions}

Configuration Constraints:
{configuration_constraints}

Select the most appropriate supported solution and convert it into the required final rule format.
```

## 6. Designer-Feedback Refinement Prompt

```text
Designer feedback:
{designer_feedback}

Current rule:
{current_rule}

Revise the current rule according to the designer feedback while preserving the TRIZ-derived solution logic and supported configuration constraints.

Return the revised rule in the required final format.
```
