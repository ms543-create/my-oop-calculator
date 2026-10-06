"""Tests for centralized calculation creation."""

import pytest

from calculator.calculation import Calculation
from calculator.factory import CalculationFactory


def test_create_add():
    calculation = CalculationFactory.create("add", 2, 3)

    assert isinstance(calculation, Calculation)
    assert calculation.get_result() == 5


def test_factory_normalizes_operation_name():
    calculation = CalculationFactory.create(" ADD ", "2", "3")

    assert calculation.get_result() == 5


def test_create_multiply():
    calculation = CalculationFactory.create("multiply", 4, 3)

    assert calculation.get_result() == 12


def test_create_absolute_difference():
    calculation = CalculationFactory.create("absolute_difference", 3, 8)

    assert calculation.get_result() == 5


def test_unknown_operation():
    with pytest.raises(ValueError, match="Unknown operation: power"):
        CalculationFactory.create("power", 2, 3)


def test_creation_does_not_execute_division():
    calculation = CalculationFactory.create("divide", 10, 0)

    assert isinstance(calculation, Calculation)

    with pytest.raises(ZeroDivisionError):
        calculation.get_result()