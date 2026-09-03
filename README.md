# paper-dataset

This repository provides the public materials associated with the study on C–K-guided multi-agent extraction of designers’ meta-knowledge in rehabilitation assistive device configuration.

The repository includes anonymized reference cases, reference rules, prompt specifications, workflow-control definitions, output schemas, and lightweight implementation components used to describe and inspect the proposed multi-agent framework and the comparative baseline settings.

## Project overview

The proposed framework uses multiple specialized agents to extract and transform designers’ meta-knowledge during rehabilitation assistive device configuration.

The main agents include:

- EAA: Experience Analysis Agent;
- PAA: Problem Abstraction Agent;
- CIA: Contradiction Identification Agent;
- CRA: Configuration Reasoning Agent;
- RGA: Rule Generation Agent.

The workflow is organized according to C–K-based stage transitions, shared memory, structured agent outputs, and designer confirmation mechanisms.

## Repository structure

- `data/`
  - anonymized reference case records;
  - corresponding reference-rule records;
  - data scope and confidentiality information.

- `prompts/`
  - shared prompt for the proposed method;
  - agent-specific prompts for EAA, PAA, CIA, CRA, and RGA.

- `prompts/baselines/`
  - task-adapted prompt texts for the baseline implementations used in the comparative experiments;
  - accompanying notes describing framework basis, source mapping, task adaptation, and evaluation controls.

- `schemas/`
  - agent-specific output schemas;
  - shared fields;
  - unified workflow-control output template.

- `workflow/`
  - stage-transition rules;
  - stage gating;
  - rollback conditions;
  - designer-confirmation rules.

- `code/agent_definitions.py`
  - public definitions of EAA, PAA, CIA, CRA, and RGA.

- `code/workflow_controller.py`
  - agent handoff, stage transition, and rollback logic.

- `code/hierarchical_memory.py`
  - lightweight implementation of STM, LTM, and WM interaction.

## Baseline prompt specifications

The repository provides task-adapted prompt specifications for the following comparative baselines:

- Agents-style;
- AutoAgents-style;
- MetaGPT-style;
- AutoTRIZ-style;
- HermesAgent 0.12-style;
- OpenClaw 5.7-style.

These files are available under:

`prompts/baselines/`

Each `*_style.md` file contains the corresponding prompt texts, while each `*_style_notes.md` file provides brief information on the original framework basis and task adaptation.

## Public data

Because of confidentiality constraints, only a subset of the anonymized case data is publicly released.

The repository currently provides five anonymized case records and their corresponding reference-rule records. The reference rules are expert-confirmed reference data rather than model-generated outputs.

## Data and materials not included

To protect participant privacy and comply with data confidentiality and security requirements, the following materials are not publicly released:

- the complete case collection;
- patient-level split manifests;
- DMKG exports;
- model-provider API credentials;
- model-generated candidate rules;
- post-adjustment experimental outputs;
- expert scoring files;
- detailed quantitative evaluation records.

## Reproducibility

The released materials provide the main public specifications required to inspect the proposed agent architecture, workflow-control logic, prompt design, representative reference cases, and comparative baseline prompt configurations.

Some private data and experiment-specific records are excluded because of confidentiality and privacy constraints.
