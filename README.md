# unstructured-excel-to-2d

Reusable GitHub Copilot skill for turning messy Excel workbooks into validated, IT-ready 2D tables with Python.

This repository is designed for cases where business teams deliver presentation-style spreadsheets that are difficult to load into databases, pipelines, or downstream systems without explicit transformation and reconciliation.

## What This Skill Solves

Use this skill when the source workbook has problems such as:

- Multi-row headers
- Matrix-style layouts with dimensions on the left and metrics spread across many columns
- Merged cells or inherited blank headers
- Inconsistent naming across header layers
- Business-only derived fields that must be materialized in the final dataset
- A requirement to prove the cleaned output still matches the source workbook

The skill guides Copilot to:

- Inspect the workbook structure before coding
- Diagnose why the file is not a true 2D table
- Propose a target schema first
- Implement a Python transformation script
- Implement a Python validation script
- Produce CSV/XLSX outputs plus reconciliation evidence

## Repository Layout

- `.github/skills/unstructured-excel-to-2d/SKILL.md`: main skill definition
- `.github/skills/unstructured-excel-to-2d/references/validation-checklist.md`: reusable validation checklist
- `.github/skills/unstructured-excel-to-2d/references/zh-cn-guide.md`: Chinese working guide
- `.github/skills/unstructured-excel-to-2d/references/before-after-demo.md`: before/after transformation example
- `.github/skills/unstructured-excel-to-2d/references/zh-cn-business-brief.md`: Chinese non-technical stakeholder brief
- `.github/skills/unstructured-excel-to-2d/assets/python-template/transform_template.py`: starter transform template
- `.github/skills/unstructured-excel-to-2d/assets/python-template/validate_template.py`: starter validation template

## Installation

### Option 1: Use As A Workspace Skill

Copy the `.github/skills/unstructured-excel-to-2d/` folder into your repository under `.github/skills/`.

Expected result:

```text
your-project/
	.github/
		skills/
			unstructured-excel-to-2d/
				SKILL.md
				references/
				assets/
```

This is the best option when you want the skill versioned together with a project or delivery repository.

### Option 2: Use As A Personal Skill

Copy the same folder into your local Copilot skills directory so it is available across repositories.

Typical Windows location:

```text
C:\Users\<your-user>\.copilot\skills\unstructured-excel-to-2d\
```

## How To Invoke

Ask Copilot with a prompt such as:

- `Analyze this workbook first. Tell me what is structurally wrong and propose a 2D schema before cleaning.`
- `Convert this messy Excel into a normalized long-form table with Python.`
- `Separate special metrics into dedicated columns and validate the results against the source workbook.`
- `把这个非结构化 Excel 转成 IT 可用二维表，并生成 Python 校验脚本。`

## Recommended Workflow

1. Let Copilot inspect the workbook structure first.
2. Confirm the target schema before transformation starts.
3. Encode all business derivations explicitly in Python.
4. Run the validation script against the transformed output.
5. Deliver the cleaned dataset together with the scripts and business rules.

## Typical Deliverables

For most projects, this skill should lead to outputs like:

- `clean_<project>.py`
- `validate_<project>.py`
- `<project> cleaned final.csv`
- `<project> cleaned final.xlsx`
- Optional header-mapping output when the source uses layered headers

## Included References

- Use `.github/skills/unstructured-excel-to-2d/references/validation-checklist.md` for reconciliation design and review.
- Use `.github/skills/unstructured-excel-to-2d/references/zh-cn-guide.md` when the delivery discussion is in Chinese.
- Use `.github/skills/unstructured-excel-to-2d/references/before-after-demo.md` to explain the transformation to stakeholders.
- Use `.github/skills/unstructured-excel-to-2d/references/zh-cn-business-brief.md` for non-technical business communication.

## Included Templates

Start new projects from:

- `.github/skills/unstructured-excel-to-2d/assets/python-template/transform_template.py`
- `.github/skills/unstructured-excel-to-2d/assets/python-template/validate_template.py`

## Best Fit

This skill is a strong fit for:

- Planning workbooks
- Funding matrices
- Sales or shipment trackers
- Region or market performance spreadsheets
- Excel files that mix presentation logic with data logic

## Not A Good Fit

This skill is not the right tool when:

- The source is already a clean row-column table
- The task is only visual formatting
- The goal is dashboard design rather than data normalization

## Success Standard

The outcome is successful when the final dataset is a true 2D table, all transformation rules are explicit in Python, and automated validation shows that the transformed output is consistent with the source workbook.