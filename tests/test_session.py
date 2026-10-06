"""Tests for CalculatorSession."""

import pytest

from calculator.factory import CalculationFactory
from calculator.session import CalculatorSession


def test_successful_calculation_is_recorded():
    session = CalculatorSession()
    calculation = CalculationFactory.create("add", 2, 3)

    result = session.calculate(calculation)

    assert result == 5.0
    assert session.get_history() == [(calculation, 5.0)]


def test_failed_calculation_is_not_recorded():
    session = CalculatorSession()
    calculation = CalculationFactory.create("divide", 1, 0)

    with pytest.raises(ZeroDivisionError):
        session.calculate(calculation)

    assert session.get_history() == []


def test_clear_history():
    session = CalculatorSession()
    calculation = CalculationFactory.create("add", 2, 3)

    session.calculate(calculation)
    session.clear()

    assert session.get_history() == []


def test_sessions_have_independent_history():
    first_session = CalculatorSession()
    second_session = CalculatorSession()

    calculation = CalculationFactory.create("add", 2, 3)
    first_session.calculate(calculation)

    assert len(first_session.get_history()) == 1
    assert second_session.get_history() == []


def test_returned_history_cannot_change_internal_history():
    session = CalculatorSession()
    calculation = CalculationFactory.create("add", 2, 3)

    session.calculate(calculation)

    returned_history = session.get_history()
    returned_history.clear()

    assert len(session.get_history()) == 1