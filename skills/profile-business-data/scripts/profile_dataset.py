from pathlib import Path
import json, sys
import pandas as pd

REQUIRED = ["feedback_id","product_name","feedback_text","rating","channel","submission_date","region"]

def profile(path: str) -> dict:
    p = Path(path)
    df = pd.read_excel(p, sheet_name="Feedback") if p.suffix.lower() in {".xlsx", ".xls"} else pd.read_csv(p)
    return {
        "rows": len(df),
        "columns": list(df.columns),
        "missing_required_columns": sorted(set(REQUIRED)-set(df.columns)),
        "nulls": df.isna().sum().astype(int).to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "duplicate_feedback_ids": int(df["feedback_id"].duplicated().sum()) if "feedback_id" in df else None,
    }

if __name__ == "__main__":
    result = profile(sys.argv[1])
    out = Path("exports/data_profile.json")
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))
