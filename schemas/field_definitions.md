# Workflow-Control Field Definitions

## agent

Identifies the agent generating the current output.

Allowed values:

- EAA
- PAA
- CIA
- CRA
- RGA

## c_k_operator

Identifies the C–K operator associated with the current agent.

Allowed values:

- C–C
- C–K
- K–K
- K–C
- K–C/K–K

## stage_status

Indicates whether the output satisfies the completion conditions of the
current stage.

### READY

The current output contains the mandatory information required by the
next stage and passes internal consistency checks.

### NEEDS_REVISION

Mandatory information, evidence, conflict analysis, action feasibility,
or rule fields remain insufficient.

## task_output

Contains the agent-specific output.

Examples include:

- structured requirements;
- cause–evidence pairs;
- conflict sets;
- candidate actions;
- candidate EBOMs;
- decision cards;
- candidate rules.

## missing_information

Lists information required to complete the current stage.

No missing information should be hidden or replaced with unsupported
generated content.

## return_to

Indicates the agent or human participant responsible for supplementary
analysis or confirmation.

## next_agent

Indicates the next workflow participant after the current stage has been
completed.

The workflow controller should invoke `next_agent` only when:

`stage_status = READY`