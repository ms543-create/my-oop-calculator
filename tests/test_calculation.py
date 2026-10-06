"""Tests for calculations that store operation callables."""

import pytest

from calculator.calculation import Calculation
from calculator.operations import Operations


def test_add_calculation():
    calculation = Calculation(2, 3, Operations.add)
    assert calculation.get_result() == 5


def test_subtract_calculation():
    calculation = Calculation(5, 3, Operations.subtract)
    assert calculation.get_result() == 2


def test_multiply_calculation():
    calculation = Calculation(4, 3, Operations.multiply)
    assert calculation.get_result() == 12


def test_divide_calculation():
    calculation = Calculation(10, 2, Operations.divide)
    assert calculation.get_result() == 5


def test_operation_is_not_called_during_construction():
    calls = []

    def spy(a, b):
        calls.append((a, b))
        return a + b

    calculation = Calculation(2, 3, spy)

    assert calls == []

    assert calculation.get_result() == 5
    assert calls == [(2.0, 3.0)]


def test_zero_divisor_fails_during_execution():
    calculation = Calculation(10, 0, Operations.divide)

    with pytest.raises(ZeroDivisionError):
        calculation.get_result()


def test_reject_non_numeric_operand():
    with pytest.raises(ValueError):
        Calculation("hello", 3, Operations.add)


def test_reject_nonfinite_operand():
    with pytest.raises(ValueError):
        Calculation(float("inf"), 3, Operations.add)


def test_reject_nonfinite_result():
    def infinite_result(a, b):
        return float("inf")

    calculation = Calculation(2, 3, infinite_result)

    with pytest.raises(ValueError):
        calculation.get_result()


def test_module_entrypoint():
    import runpy

    runpy.run_module("calculator", run_name="__main__")