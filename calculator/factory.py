"""A factory centralizes construction; it does not execute math."""

from calculator.calculation import Calculation
from calculator.operations import Operations


class CalculationFactory:
    """Create calculations from operation names."""

    operations = {
        "add": Operations.add,
        "subtract": Operations.subtract,
        "multiply": Operations.multiply,
        "divide": Operations.divide,
        "absolute_difference": Operations.absolute_difference,
    }

    @staticmethod
    def create(name, a, b):
        """Create a calculation without executing it."""
        name = name.strip().lower()

        try:
            operation = CalculationFactory.operations[name]
        except KeyError:
            raise ValueError(f"Unknown operation: {name}") from None

        return Calculation(a, b, operation)