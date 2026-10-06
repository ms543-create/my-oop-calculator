"""Store two operands and a callable; run math only in get_result."""

from math import isfinite

from calculator.validation import numeric_values


class Calculation:
    """Store operands and the operation used to calculate their result."""

    def __init__(self, a, b, operation) -> None:
        numbers = numeric_values([a, b])
        self.a = numbers[0]
        self.b = numbers[1]
        self.operation = operation

    def get_result(self) -> float:
        """Run the stored operation and return its finite result."""
        result = float(self.operation(self.a, self.b))

        if not isfinite(result):
            raise ValueError("Result is outside the supported range.")

        return result