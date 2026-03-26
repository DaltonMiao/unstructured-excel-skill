# Before / After Demo

This document shows what a typical non-2D business Excel looks like before transformation and what the IT-ready result looks like after Python-based cleaning.

## Before

The source workbook is presentation-oriented rather than system-oriented.

Typical characteristics:
- Multiple header rows instead of one schema row
- Left-side dimensions and right-side metric matrix
- Semantic hierarchy spread across rows rather than fields
- Business labels with inconsistent naming
- Special metrics mixed together with standard metrics

### Source Shape Example

| Row1 | Row2 | Row3 | Row4 | Col5 | Col6 | Col7 | Col8 |
|---|---|---|---|---|---|---|---|
| Sufficiency % of GIV excl SKII |  |  |  | FY2425 1H DS |  |  |  |
|  |  |  |  | FY2425 1H | FY2425 1H | FY2425 1H | FY2425 1H |
|  |  |  |  | Hair | Fabric | PCC | Oral |
| Division | Market | RD group | RD | DS | DS | DS | DS |
| East | GJN | Hangzhou_Baotong | Hangzhou_Baotong | 57.36649791 | 4.6878368 | 21.74414326 | 5.43684032 |
| East | GJN | Shanghai_Dongfang | Shanghai_Dongfang | 64.82151512 | 20.37292182 | 76.07753955 | 14.55539767 |

### Why This Is Not 2D

This structure is not a standard 2D table because:
- the schema is split across multiple header rows
- one numeric cell only becomes meaningful after combining header layers
- metrics like `DS` are mixed with fund-rate metrics
- period meaning and date meaning are implicit, not explicit

## After

The transformed result is a clean 2D table where each row is one business fact and each column has a single explicit meaning.

### Final Target Shape Example

| division | market | rd_group | rd | subject | period | Start Date | End Date | category | metric | value | Direct Shipment | FCST_Fund |
|---|---|---|---|---|---|---|---|---|---|---:|---:|---:|
| East | GJN | Hangzhou_Baotong | Hangzhou_Baotong | Sufficiency % of GIV (excl. FQDD) | FY2425 1H | 2024.7.1 | 2025.6.30 | Hair | General Fund | 0.2 | 57366497.91 | 11473299.582 |
| East | GJN | Hangzhou_Baotong | Hangzhou_Baotong | Sufficiency % of GIV (excl. FQDD) | FY2425 1H | 2024.7.1 | 2025.6.30 | Hair | WS AKBD | 0 | 57366497.91 | 0 |
| East | GJN | Hangzhou_Baotong | Hangzhou_Baotong | Sufficiency % of GIV (excl. FQDD) | FY2425 1H | 2024.7.1 | 2025.6.30 | Hair | CP (LSR) | 0.0246206940729654 | 57366497.91 | 1412287.745991568714 |
| East | GJN | Hangzhou_Baotong | Hangzhou_Baotong | Sufficiency % of GIV | FY2526 1H | 2025.7.1 | 2026.6.30 | Hair | Retail AKBD with cap | 0.0102094741240585 | 144285202.735827 | 1473428.4987357973675095 |
| East | GJN | Hangzhou_Baotong | Hangzhou_Baotong | Changes vs YA | Delta |  |  | Hair | General Fund | -0.0716581497888318 |  |  |

## Sample Transformation Logic

The transformation usually performs the following steps:

1. Read the workbook and identify header depth.
2. Forward-fill blank header cells inherited from merged or visual grouping.
3. Normalize header names such as inconsistent metric labels.
4. Flatten metric columns into rows.
5. Split special metric `DS` out of metric rows and convert it from millions into actual shipment value.
6. Add explicit date columns based on `period`.
7. Add derived columns such as `FCST_Fund = value * Direct Shipment`.
8. Validate that source-derived expectations match the transformed table.

## What Improved After Transformation

### Before

- Hard for IT to load directly
- Hard to query by period, category, and metric
- Logic hidden in layout
- Derived fields not explicit
- Validation is manual and error-prone

### After

- Directly loadable into database tables or downstream services
- Easy to filter by `period`, `category`, `metric`, and dimensions
- Business rules become explicit Python logic
- Derived fields are materialized and traceable
- Validation can be automated and rerun

## Minimal Before / After Mapping

| Source Meaning | After Transformation |
|---|---|
| Multi-row header combination | `subject`, `period`, `category`, `metric` |
| `DS` metric in matrix | `Direct Shipment` column |
| Implicit period date range | `Start Date`, `End Date` |
| Rate x shipment logic | `FCST_Fund` |
| Visual grouping only | Explicit row-level fact table |

## Suitable Deliverables

For this kind of case, the recommended deliverables are:
- a transformation script
- a validation script
- a final cleaned CSV/XLSX
- a header mapping file
- a short before/after demo like this one