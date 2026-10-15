import pandas as pd
from sklearn.model_selection import train_test_split

SEED = 42


def make_splits(df: pd.DataFrame, val=0.15, test=0.15, seed=SEED):
    """Stratified 70/15/15 split; saved to disk so every notebook reuses it."""
    train_val, test_df = train_test_split(df, test_size=test, stratify=df["label"], random_state=seed)
    train_df, val_df = train_test_split(
        train_val, test_size=val / (1 - test), stratify=train_val["label"], random_state=seed
    )
    return train_df, val_df, test_df
