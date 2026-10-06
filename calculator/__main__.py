"""Demonstrate creating a calculation through the factory."""

from calculator.factory import CalculationFactory


calculation = CalculationFactory.create("add", 2, 3)
print(calculation.get_result())