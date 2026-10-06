"""Store operands and a callable; run math only in get_result."""

from math import isfinite

from calculator.validation import numeric_values


class Calculation:
    """Store numeric values, an operation, and optional configuration."""

    def __init__(self, values, operation, **options) -> None:
        self.values = numeric_values(values)
        self.operation = operation
        self.options = dict(options)

    def get_result(self) -> float:
        """Run the stored operation with its values and options."""
        result = float(self.operation(*self.values, **self.options))

        if not isfinite(result):
            raise ValueError("Result is outside the supported range.")

        return result