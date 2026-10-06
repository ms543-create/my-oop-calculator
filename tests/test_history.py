"""Tests for calculation history."""

import pytest

from calculator.calculation import Calculation
from calculator.history import History
from calculator.operations import Operations


def test_empty_history():
    history = History()

    assert history.get_history() == []


def test_add_calculation_and_result():
    history = History()
    calculation = Calculation([2, 3], Operations.add)

    result = calculation.get_result()
    history.add(calculation, result)

    assert history.get_history() == [(calculation, 5.0)]


def test_history_copy_protects_membership():
    history = History()
    calculation = Calculation([2, 3], Operations.add)

    history.add(calculation, calculation.get_result())

    copied_history = history.get_history()
    copied_history.clear()

    assert len(history.get_history()) == 1


def test_history_preserves_order():
    history = History()

    addition = Calculation([2, 3], Operations.add)
    subtraction = Calculation([10, 4], Operations.subtract)

    history.add(addition, addition.get_result())
    history.add(subtraction, subtraction.get_result())

    entries = history.get_history()

    assert entries[0] == (addition, 5.0)
    assert entries[1] == (subtraction, 6.0)


def test_clear_history():
    history = History()
    calculation = Calculation([2, 3], Operations.add)

    history.add(calculation, calculation.get_result())
    history.clear()

    assert history.get_history() == []


def test_reject_non_calculation():
    history = History()

    with pytest.raises(TypeError):
        history.add("not a calculation", 5.0)