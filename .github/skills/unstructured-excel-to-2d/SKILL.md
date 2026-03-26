---
name: unstructured-excel-to-2d
description: 'Convert messy Excel workbooks, 非规则Excel, 非结构化表, 非二维表, multi-row headers, matrix-style business sheets into IT-ready 2D tables using Python. Use when business provides irregular Excel/XLSX files that need parsing, normalization, derived-field calculation, and self-validation to prove source and transformed data are consistent.'
argument-hint: 'Describe the source Excel, target 2D schema, required derived fields, and validation rules.'
user-invocable: true
disable-model-invocation: false
---

# Unstructured Excel To 2D

## What This Skill Does

Use this skill when a business team provides an Excel workbook that is hard for IT to use directly because it is not a clean 2D table.

Typical symptoms:
- Multi-row headers
- Matrix-style layout with dimensions on the left and metrics spread across hundreds of columns
- Merged cells, blank inherited headers, inconsistent naming, presentation-first formatting
- Derived values that must be materialized for IT consumption
- Need to prove the transformed table is correct with automated reconciliation

This skill turns that input into a reproducible Python-based workflow that:
- Identifies the real data shape
- Defines the target 2D schema
- Writes transformation scripts
- Produces clean outputs in CSV/XLSX
- Runs self-tests to verify row counts, mappings, formulas, and source-to-target consistency

## When To Use

Use this skill for requests such as:
- "Help me parse this messy Excel"
- "Convert this non-2D spreadsheet into a structured table"
- "Business gave an irregular workbook; make it usable for IT"
- "Flatten multi-level headers into a standard table"
- "Write Python to clean Excel and validate the result"
- "把业务提供的非结构化Excel转成IT可用二维表"
- "把非规则表清洗成标准明细表并验证前后一致"

Do not use this skill when:
- The source is already a clean row-column table
- The task is only formatting or cosmetic cleanup
- The task is BI/dashboard design rather than data normalization

## Required Outcome

The final deliverable should usually include:
- A clean 2D output table in CSV and/or XLSX
- A transformation script in Python
- A validation script in Python
- A short explanation of identified source issues
- Explicit formulas or mapping rules for any derived fields

## Procedure

1. Inspect the workbook structure.
Read sheet names, row counts, column counts, header depth, merged ranges, and representative samples. Confirm where data really begins and whether the workbook is presentation-oriented instead of table-oriented.

2. Diagnose why the file is not IT-ready.
Call out concrete structural issues such as multi-row headers, inherited blanks, mixed semantic layers, inconsistent metric names, totals embedded as columns, and units hidden in business context rather than explicit fields.

3. Define the target 2D schema before writing code.
Separate stable dimensions from repeated metric attributes. Prefer a long fact table when the source is a wide metric matrix. Only keep a wide table if the user explicitly needs one.

4. Normalize the header hierarchy.
Forward-fill inherited header cells, trim whitespace, standardize naming, and preserve a mapping from original headers to standardized fields.

5. Write a transformation script in Python.
The script should be deterministic and reusable. It should:
- Read the source workbook
- Normalize header layers
- Build the target rows
- Materialize derived fields when requested
- Output CSV/XLSX artifacts

6. Keep derivations explicit.
If business logic adds fields such as shipment values, date ranges, forecast amounts, or category groupings, encode each rule directly in the script and keep it readable.

7. Write a validation script.
Validation is not optional. The script should reconcile source and target by checking at least:
- Expected output row count
- Removal or relocation of special metrics
- Correct backfilling or joins for derived columns
- Exact formula results for derived fields
- Period/date mapping correctness
- Absence of unexpected duplicates or dropped records

8. Run full self-tests.
Execute the transformation script and the validation script. Do not stop at a few sample rows. Report pass/fail status and any residual assumptions.

9. Hand over the result in a way IT can use.
Provide the final schema, generated files, and the key business rules embedded in the transformation.

## Design Rules

- Prefer long-form fact tables for matrix-like business spreadsheets.
- Keep original traceability fields when useful, such as source sheet name and original column index.
- Standardize naming early to avoid downstream duplication.
- Preserve units explicitly. If a source value is in millions, convert it only when requested and document the rule.
- Keep calculations reproducible in code, not manual Excel edits.
- Never claim correctness without automated validation.

## Suggested Output Pattern

For most cases, produce these files:
- `clean_<project>.py`: transformation logic
- `validate_<project>.py`: source-to-target reconciliation checks
- `<project> cleaned final.csv`
- `<project> cleaned final.xlsx`
- Optional header-mapping file if the source used multi-row headers

## Validation Checklist

Use the checklist in [validation-checklist.md](./references/validation-checklist.md) when designing or reviewing the transformation.

## Chinese Guide

Use the Chinese walkthrough in [zh-cn-guide.md](./references/zh-cn-guide.md) when the working language with the business team is Chinese.

## Before / After Demo

Use [before-after-demo.md](./references/before-after-demo.md) when you need to show stakeholders what the source looked like before transformation and what the final 2D table looks like after conversion.

## Business Brief In Chinese

Use [zh-cn-business-brief.md](./references/zh-cn-business-brief.md) when you need a concise, non-technical explanation for business stakeholders.

## Template Assets

Start from [transform_template.py](./assets/python-template/transform_template.py) and [validate_template.py](./assets/python-template/validate_template.py) for new workbook-cleaning tasks.

## Response Pattern

When invoked, structure the work in this order:
1. Explain what makes the source non-2D.
2. Propose the target schema.
3. Implement the Python transformation.
4. Implement validation.
5. Run both.
6. Report outputs and verification results.

## Example Use Cases

- Sales planning workbook with four-layer headers and category-mechanism columns
- Funding matrix where `DS` must be separated into its own field and converted from millions
- Business planning file where `Period` must be mapped to `Start Date` and `End Date`
- Irregular Excel requiring `FCST_Fund = rate * Direct Shipment`

## Success Criteria

This skill is successful when:
- The final table is a true 2D table
- IT can load it directly into downstream systems or databases
- Every transformation rule is explicit in Python
- Validation proves the transformed data is consistent with the source