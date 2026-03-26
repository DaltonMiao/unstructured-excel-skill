import csv
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[4]
OUTPUT_FILE = BASE_DIR / "output_cleaned.csv"

EXPECTED_HEADERS = [
    "dimension_1",
    "dimension_2",
    "dimension_3",
    "dimension_4",
    "subject",
    "period",
    "category",
    "metric",
    "value",
    "source_sheet",
    "source_col_index",
]


def validate_output():
    failures = []
    row_count = 0
    unique_keys = set()

    with OUTPUT_FILE.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)

        if reader.fieldnames != EXPECTED_HEADERS:
            failures.append({
                "type": "header_mismatch",
                "expected": EXPECTED_HEADERS,
                "actual": reader.fieldnames,
            })

        for row in reader:
            row_count += 1
            key = (
                row["dimension_1"],
                row["dimension_2"],
                row["dimension_3"],
                row["dimension_4"],
                row["subject"],
                row["period"],
                row["category"],
                row["metric"],
                row["source_col_index"],
            )
            if key in unique_keys:
                failures.append({
                    "type": "duplicate_transformed_key",
                    "row": row_count + 1,
                    "key": key,
                })
                break
            unique_keys.add(key)

            mandatory_fields = [
                row["dimension_1"],
                row["subject"],
                row["period"],
                row["category"],
                row["metric"],
            ]
            if any(value == "" for value in mandatory_fields):
                failures.append({
                    "type": "blank_mandatory_field",
                    "row": row_count + 1,
                })
                break

    summary = {
        "status": "passed" if not failures else "failed",
        "row_count": row_count,
        "failures": failures,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    validate_output()