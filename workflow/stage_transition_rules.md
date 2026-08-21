
---

# 8. workflow/stage_transition_rules.md

```markdown
# Stage Transition and Rollback Rules

## 1. Normal Execution Sequence

The standard workflow is:

EAA → PAA → CIA → CRA → RGA → Designer

## 2. EAA Completion Rule

EAA returns `READY` when:

- each requirement is grounded in the original wearing feedback;
- mandatory requirement fields are complete;
- uncertain information is explicitly marked.

Otherwise:

- `stage_status = NEEDS_REVISION`
- `return_to = USER_OR_DESIGNER` or `EAA`

## 3. PAA Completion Rule

PAA returns `READY` when:

- each critical requirement is associated with supporting evidence; or
- unsupported elements are explicitly marked and do not prevent
  downstream conflict analysis.

Otherwise:

- `stage_status = NEEDS_REVISION`
- `return_to = EAA`, `PAA`, or `DESIGNER`

## 4. CIA Completion Rule

CIA returns `READY` when:

- each critical conflict has identifiable objects;
- supporting evidence is available;
- risk and severity are specified.

Otherwise:

- `stage_status = NEEDS_REVISION`
- `return_to = PAA`, `CIA`, or `DESIGNER`

## 5. CRA Completion Rule

CRA returns `READY` when:

- candidate actions are feasible;
- candidate actions are supported by evidence;
- no unresolved critical conflict remains.

Otherwise:

- `stage_status = NEEDS_REVISION`
- `return_to = CIA`, `CRA`, or `DESIGNER`

## 6. RGA Completion Rule

RGA generates a candidate rule only when:

- EAA, PAA, CIA, and CRA return `READY`;
- no unresolved critical conflict remains;
- all candidate actions are feasible;
- all rule fields have supporting evidence.

The candidate rule remains:

`rule_status = CANDIDATE`

until explicit designer approval is provided.

## 7. Designer Feedback Rule

The designer may:

- approve;
- reject;
- modify;
- request supplementary evidence;
- request another candidate option.

When the rule is rejected or modified:

- `rule_status = REVISION_REQUIRED`
- `next_agent = RGA`

When new evidence or conflict analysis is required:

- the workflow returns to PAA, CIA, or CRA.

When the designer explicitly approves the rule:

- `rule_status = FINAL`
- `next_agent = LTM`

## 8. Long-Term Memory Consolidation Rule

Only final designer-approved rules may be consolidated into long-term
memory.

Candidate rules, rejected rules, intermediate evidence, and interaction
records remain in short-term memory or task logs.

## 9. Identifier Preservation

The following mapping must be retained:

`requirement_id → evidence_id → conflict_id → action_id → rule_id`

This mapping supports source inspection and consistency checking across
workflow stages.
```
