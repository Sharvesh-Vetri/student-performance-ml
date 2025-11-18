# ================================================================
# cleaning.py : Robust cleaning for student datasets
# ================================================================

import pandas as pd
import numpy as np
import os

DATA_PATH = "data/"
OUTPUT_PATH = "output/"

FILES = [
    "student-mat.csv",
    "student-por.csv"
]

os.makedirs(OUTPUT_PATH, exist_ok=True)

def smart_read(path):
    """Auto-detect separator + fix collapsed CSV."""
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        first = f.readline()

    # Detect separator
    for sep in [";", ",", "\t", "|"]:
        if sep in first:
            df = pd.read_csv(path, sep=sep)
            break
    else:
        df = pd.read_csv(path)

    # Fix 1-column issue
    if df.shape[1] == 1:
        raw = df.iloc[:, 0].astype(str)
        if ";" in raw.iloc[0]:
            df = raw.str.split(";", expand=True)
        elif "," in raw.iloc[0]:
            df = raw.str.split(",", expand=True)

        df.columns = df.iloc[0]
        df = df[1:].reset_index(drop=True)

    return df


def clean_dataset(df):
    """Apply cleaning transformations."""
    
    # Strip column names
    df.columns = [c.strip() for c in df.columns]

    # Clean string columns
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = (
            df[col]
            .astype(str)
            .str.strip()
            .replace({"": np.nan, "NA": np.nan, "na": np.nan, "?" : np.nan})
        )

    # Convert numeric-like fields
    for col in df.columns:
        try:
            df[col] = pd.to_numeric(df[col])
        except:
            pass

    # Missing values
    num_cols = df.select_dtypes(include=[np.number]).columns
    cat_cols = df.select_dtypes(include=["object"]).columns

    df[num_cols] = df[num_cols].fillna(df[num_cols].median())
    df[cat_cols] = df[cat_cols].fillna("missing")

    # Target creation
    if "G3" in df.columns:
        df["passed"] = (df["G3"] >= 10).astype(int)

    return df


# ================================================================
# MAIN EXECUTION
# ================================================================

for file in FILES:
    input_path = DATA_PATH + file
    print(f"\nProcessing: {input_path}")

    df = smart_read(input_path)
    df = clean_dataset(df)

    # Save
    output_path = OUTPUT_PATH + f"cleaned_{file}"
    df.to_csv(output_path, index=False)

    print(f"Saved cleaned file → {output_path}")

print("\nAll datasets cleaned successfully.")
