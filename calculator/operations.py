"""Provide mathematical operations for calculations."""


class Operations:
    """Group the mathematical operations used by the calculator."""

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        return a / b

    @staticmethod
    def absolute_difference(a: float, b: float) -> float:
        return abs(a - b)