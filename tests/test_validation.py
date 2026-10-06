"""Tests for numeric value validation."""

import pytest

from calculator.validation import numeric_values


def test_numeric_values():
    assert numeric_values([2, 3]) == (2.0, 3.0)


def test_numeric_values_accept_numeric_strings():
    assert numeric_values(["2.5", "3"]) == (2.5, 3.0)


def test_numeric_values_reject_non_numeric_value():
    with pytest.raises(ValueError):
        numeric_values(["hello", 3])


def test_numeric_values_reject_nonfinite_value():
    with pytest.raises(ValueError):
        numeric_values([float("inf"), 3])