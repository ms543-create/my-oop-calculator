"""Read CSV input sources; choosing and performing math belong elsewhere."""

from pathlib import Path

import pandas as pd


def read_csv_values(path, column="value"):
    """Read observations from a selected CSV column."""
    frame = pd.read_csv(Path(path))

    if column not in frame.columns:
        raise ValueError(f"CSV must contain a column named {column}.")

    return frame[column].tolist()