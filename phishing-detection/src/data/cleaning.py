import re
import pandas as pd

WS = re.compile(r"\s+")


def clean_dataset(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    """Return (cleaned_df, log) recording how many rows each step removed."""
    log = {"start": len(df)}
    df = df.copy()

    df = df.dropna(subset=["label"])
    df["label"] = df["label"].astype(int)
    log["after_drop_missing_label"] = len(df)

    df["text"] = df["text"].str.replace(WS, " ", regex=True).str.strip()
    df = df[df["text"].str.len() > 0]
    log["after_drop_empty_text"] = len(df)

    # Identical text with conflicting labels is unreliable: drop every copy.
    n_labels = df.groupby("text")["label"].transform("nunique")
    df = df[n_labels == 1]
    log["after_drop_conflicting_labels"] = len(df)

    df = df.drop_duplicates(subset=["text"], keep="first")
    log["after_exact_dedup"] = len(df)

    return df.reset_index(drop=True), log
