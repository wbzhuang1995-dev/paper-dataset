# Dataset organization

## Confidentiality-limited reference release

This release contains five anonymized case records in total. `C-010` is the anonymized case used for the manuscript's Mr. Zhang analysis, with its complete released source fields and corresponding reference rule retained. Four additional anonymized cases and their corresponding reference-rule records are provided as representative reference examples. The released rules are reference data rather than model-generated outputs.

No model-generated rule, intermediate agent output, evaluation result, or
experiment log is included.

## Source tables

- `cases/reference_cases.csv` contains the five anonymized raw case records.
- `rules/reference_rules.csv` contains the five reference-rule records corresponding to the five released cases.

The case fields cover rehabilitation stage, record source, wearing feedback,
current EBOM status, confirmed EBOM difference, rationale, constraints, and
reference-rule information. The rule fields cover trigger, action, exception
boundary, verification method, supporting cases, and rule category.

The records are preserved as reference data. No missing records are inferred,
no patient history is reconstructed, and no synthetic examples are added.

## Excluded materials

The full private dataset, generated results, evaluation annotations,
patient-level split files, DMKG exports, and quantitative experiment outputs
are outside this confidentiality-limited release.
