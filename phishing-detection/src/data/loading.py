"""Load and standardise the Kaggle Phishing Email Dataset files.

The dataset ships as several CSVs (some per-source such as CEAS_08, Enron,
Ling, Nazario, Nigerian_Fraud, SpamAssassin, and/or a combined file).
Schemas differ between files, so we map to a common one:
    source, subject, body, text, label   (label: 1 = phishing/spam, 0 = legitimate)
"""
from pathlib import Path
import pandas as pd

RAW_DIR = Path(__file__).resolve().parents[2] / "data" / "raw"

SUBJECT_COLS = ["subject", "Subject", "Email_Subject"]
BODY_COLS = ["body", "Body", "email_text", "Email Text", "text", "text_combined", "Email_Content"]
LABEL_COLS = ["label", "Label", "class", "Email Type"]

# PHISHING_ONLY_FILES: set[str] = set()
PHISHING_ONLY_FILES: set[str] = {"PhishingEmailData"}

# Files that aren't raw labeled email data (e.g. someone else's derived
# analysis output) and should be skipped entirely rather than force-mapped.
EXCLUDED_FILES: set[str] = {"spamResults"}


def _first_present(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    return None


def standardise(df: pd.DataFrame, source: str) -> pd.DataFrame:
    subj_c = _first_present(df, SUBJECT_COLS)
    body_c = _first_present(df, BODY_COLS)
    label_c = _first_present(df, LABEL_COLS)

    if body_c is None:
        raise ValueError(f"{source}: cannot find a body column in {list(df.columns)}")

    out = pd.DataFrame(index=df.index)
    out["source"] = source
    out["subject"] = df[subj_c].fillna("").astype(str) if subj_c else ""
    out["body"] = df[body_c].fillna("").astype(str)
    out["text"] = (out["subject"] + " " + out["body"]).str.strip()

    if label_c is not None:
        lab = df[label_c]
        if lab.dtype == object:
            mapping = {"phishing email": 1, "phishing": 1, "spam": 1, "1": 1,
                       "safe email": 0, "legitimate": 0, "ham": 0, "0": 0}
            lab = lab.astype(str).str.strip().str.lower().map(mapping)
        out["label"] = lab
    elif source in PHISHING_ONLY_FILES:
        out["label"] = 1
    else:
        raise ValueError(
            f"{source}: no recognized label column in {list(df.columns)}. "
            "Add it to LABEL_COLS, or to PHISHING_ONLY_FILES if every row here is phishing, "
            "or add custom label-derivation logic for this source."
        )
    return out

def load_raw(raw_dir: Path = RAW_DIR) -> pd.DataFrame:
    files = sorted(raw_dir.glob("*.csv"))
    if not files:
        raise FileNotFoundError(f"No CSV files in {raw_dir}. Download the Kaggle dataset first.")
    frames = []
    skipped = []
    for f in files:
        if f.stem in EXCLUDED_FILES:
            skipped.append(f.stem)
            continue
        try:
            df = pd.read_csv(f, low_memory=False)
        except UnicodeDecodeError:
            df = pd.read_csv(f, low_memory=False, encoding="latin-1")
        frames.append(standardise(df, source=f.stem))
    if skipped:
        print(f"Skipped (not raw labeled email data): {skipped}")
    return pd.concat(frames, ignore_index=True)