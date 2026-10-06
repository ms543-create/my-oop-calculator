"""Tests for the calculator's mathematical operations."""

import pytest

from calculator.operations import Operations


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        (Operations.add, 2, 3, 5),
        (Operations.subtract, 2, 3, -1),
        (Operations.multiply, -2, 3, -6),
        (Operations.divide, 7, 2, 3.5),
        (Operations.absolute_difference, 3, 8, 5),
    ],
)
def test_arithmetic(operation, a, b, expected):
    assert operation(a, b) == pytest.approx(expected)


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        Operations.divide(1, 0)


def test_unary_operations():
    assert Operations.square(3) == 9
    assert Operations.sqrt(9) == 3


def test_power_keyword_only_option():
    assert Operations.power(3, exponent=4) == 81


def test_power_default_exponent():
    assert Operations.power(3) == 9


def test_square_root_domain():
    with pytest.raises(ValueError):
        Operations.sqrt(-1)


def test_sum_accepts_many_values():
    assert Operations.sum(2, 4, 6) == 12


def test_sum_rejects_empty_input():
    with pytest.raises(ValueError):
        Operations.sum()