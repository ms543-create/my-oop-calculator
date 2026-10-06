"""Validate numeric values used by calculations."""

from math import isfinite


def numeric_values(values) -> tuple[float, ...]:
    """Convert values to finite floats."""
    numbers = []

    for value in values:
        number = float(value)

        if not isfinite(number):
            raise ValueError("A finite number is required.")

        numbers.append(number)

    return tuple(numbers)