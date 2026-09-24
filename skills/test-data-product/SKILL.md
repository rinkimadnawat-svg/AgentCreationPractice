---
name: test-data-product
description: Test an analytics or Streamlit data product. Use for review, regression, release readiness, data validation, KPI reconciliation, or export integrity.
---
# Test data product

1. Read `references/test-matrix.md`.
2. Reproduce before fixing.
3. Add a failing regression test for each confirmed defect.
4. Cover unit, data-contract, integration and smoke tests.
5. Reconcile displayed KPIs with clean record-level data.
6. Test malformed, empty, duplicate, missing and out-of-range inputs.
7. Do not approve release with failing critical tests.
8. Produce evidence, residual risk and release decision.
