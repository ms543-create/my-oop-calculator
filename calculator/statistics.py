"""Calculate statistics using validated numeric observations."""

import pandas as pd

from calculator.validation import numeric_values


def mean(values) -> float:
    """Return the arithmetic mean of one or more observations."""
    numbers = numeric_values(values)

    if not numbers:
        raise ValueError("Mean requires at least one value.")

    series = pd.Series(numbers, dtype=float)
    result = float(series.mean())
    return result

def standard_deviation(values, *, ddof=1) -> float:
    """Return the standard deviation of two or more observations."""
    numbers = numeric_values(values)

    if len(numbers) < 2:
        raise ValueError("Standard deviation requires at least two values.")

    if ddof not in (0, 1):
        raise ValueError("ddof must be 0 or 1.")

    series = pd.Series(numbers, dtype=float)
    result = float(series.std(ddof=ddof))

    return result