"""Tests for the calculator's mathematical operations."""

import pytest

from calculator.operations import Operations


def test_add():
    assert Operations.add(2, 3) == 5


def test_subtract():
    assert Operations.subtract(5, 3) == 2


def test_multiply():
    assert Operations.multiply(4, 3) == 12


def test_divide():
    assert Operations.divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Operations.divide(10, 0)

def test_absolute_difference():
    assert Operations.absolute_difference(3, 8) == 5
    assert Operations.absolute_difference(8, 3) == 5