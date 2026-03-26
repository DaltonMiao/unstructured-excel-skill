# Validation Checklist

Use this checklist when converting an irregular Excel workbook into a 2D table.

## Structure Checks

- Confirm which rows are headers and which rows are data
- Confirm whether merged cells or blank inherited headers exist
- Confirm stable dimension columns versus repeated metric columns
- Confirm whether totals, deltas, or ratios are mixed into the same matrix

## Naming Checks

- Normalize whitespace and line breaks
- Unify inconsistent labels with the same meaning
- Preserve a mapping from original labels to standardized labels

## Transformation Checks

- Verify target row count matches the intended transformation logic
- Verify special metrics moved to standalone columns are removed from metric rows
- Verify all required derived columns are populated only where logically valid
- Verify units are converted correctly
- Verify period-to-date mappings are correct

## Formula Checks

- Recompute each derived formula from source-aligned inputs
- Compare expected and actual values exactly when precision allows
- Use decimal arithmetic when financial precision matters

## Reconciliation Checks

- Compare source-derived key coverage against target key coverage
- Check for duplicate keys after transformation
- Check for unexpected blanks in mandatory fields
- Check that no rows were silently dropped

## Handover Checks

- Provide final schema
- Provide scripts used to transform and validate
- Provide output files in CSV/XLSX
- State any remaining assumptions explicitly