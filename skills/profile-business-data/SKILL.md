---
name: profile-business-data
description: Profile Excel or CSV business data before analysis. Use when asked to inspect, validate, clean, diagnose, or prepare tabular input.
---
# Profile business data

1. Read `references/quality-rules.md` before profiling.
2. Inspect sheet names, row count, columns, types, nulls, duplicates, date ranges and categorical values.
3. Run `scripts/profile_dataset.py` when a reproducible profile is required.
4. Compare required columns with the data contract.
5. Separate valid, warning and rejected records. Never silently alter source data.
6. Write a machine-readable profile to `exports/data_profile.json` and a concise business summary.
7. Recommend the smallest safe correction and tests.

## Output contract
Return: schema status, issue counts, affected fields, sample row identifiers, business impact, treatment, residual risk.
