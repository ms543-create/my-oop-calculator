"""Tests for calculations with flexible inputs."""

import pytest

from calculator.calculation import Calculation
from calculator.operations import Operations


def test_construction_defers_execution_and_snapshots_inputs():
    calls = []

    def operation(a, b):
        calls.append((a, b))
        return a + b

    values = [2, 3]
    calculation = Calculation(values, operation)
    values.clear()

    assert calls == []
    assert calculation.get_result() == 5
    assert calls == [(2.0, 3.0)]


def test_zero_division_occurs_during_execution():
    calculation = Calculation([1, 0], Operations.divide)

    with pytest.raises(ZeroDivisionError):
        calculation.get_result()


def test_reject_nonfinite_result():
    calculation = Calculation([1e308, 1e308], Operations.multiply)

    with pytest.raises(ValueError, match="range"):
        calculation.get_result()


def test_unary_calculation():
    calculation = Calculation([3], Operations.square)

    assert calculation.get_result() == 9


def test_many_value_calculation():
    calculation = Calculation([2, 4, 6], Operations.sum)

    assert calculation.get_result() == 12


def test_calculation_forwards_options():
    calculation = Calculation([3], Operations.power, exponent=4)

    assert calculation.get_result() == 81