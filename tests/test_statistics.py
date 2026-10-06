"""Tests for calculator statistics."""

import pytest

from calculator.statistics import mean, standard_deviation


def test_mean():
    assert mean([2, 4, 6]) == pytest.approx(4.0)


def test_mean_single_value():
    assert mean([5]) == pytest.approx(5.0)


def test_mean_requires_value():
    with pytest.raises(ValueError):
        mean([])

def test_standard_deviation_sample():
    assert standard_deviation([2, 4, 6]) == pytest.approx(2.0)


def test_standard_deviation_population():
    assert standard_deviation([2, 4, 6], ddof=0) == pytest.approx(1.632993, rel=1e-5)


def test_standard_deviation_requires_two_values():
    with pytest.raises(ValueError):
        standard_deviation([5])


def test_standard_deviation_rejects_invalid_ddof():
    with pytest.raises(ValueError):
        standard_deviation([2, 4, 6], ddof=2)