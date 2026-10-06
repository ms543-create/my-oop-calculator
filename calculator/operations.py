"""Provide mathematical operations for calculations."""

from math import pow, sqrt


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

    @staticmethod
    def square(value: float) -> float:
        return value * value

    @staticmethod
    def sqrt(value: float) -> float:
        return sqrt(value)

    @staticmethod
    def sum(*values: float) -> float:
        if not values:
            raise ValueError("Sum requires at least one value.")
        return sum(values)

    @staticmethod
    def power(value: float, *, exponent: float = 2) -> float:
        return pow(value, exponent)

    @staticmethod
    def scale(value: float, *, factor: float = 1) -> float:
        return value / factor