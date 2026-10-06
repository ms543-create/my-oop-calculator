"""Tests for processing a sequence of prepared calculations."""

from calculator.factory import CalculationFactory
from calculator.session import CalculatorSession
from calculator.sequence import execute_requests, execute_sequence

def test_sequence_continues_after_failure():
    """A failed item must not prevent a later calculation from running."""
    session = CalculatorSession()

    calculations = [
        CalculationFactory.create("add", 2, 3),
        CalculationFactory.create("divide", 1, 0),
        CalculationFactory.create("square", 3),
    ]

    results, errors = execute_sequence(session, calculations)

    assert results == [5.0, 9.0]
    assert len(errors) == 1
    assert len(session.get_history()) == 2


def test_empty_sequence_changes_no_state():
    """An empty sequence produces no results, errors, or history."""
    session = CalculatorSession()

    results, errors = execute_sequence(session, [])

    assert results == []
    assert errors == []
    assert session.get_history() == []


def test_requests_continue_after_preparation_failure():
    """An invalid request must not prevent a later valid request."""
    session = CalculatorSession()

    requests = [
        ("add", [2, 3], {}),
        ("unknown", [1, 2], {}),
        ("square", [4], {}),
    ]

    results, errors = execute_requests(session, requests)

    assert results == [5.0, 16.0]
    assert len(errors) == 1
    assert len(session.get_history()) == 2


def test_requests_continue_after_execution_failure():
    """An execution failure must not prevent later requests."""
    session = CalculatorSession()

    requests = [
        ("divide", [10, 0], {}),
        ("power", [3], {"exponent": 2}),
    ]

    results, errors = execute_requests(session, requests)

    assert results == [9.0]
    assert len(errors) == 1
    assert len(session.get_history()) == 1


def test_sequence_retains_failures_in_session():
    """Failures are retained separately from successful history."""
    session = CalculatorSession()

    calculations = [
        CalculationFactory.create("add", 2, 3),
        CalculationFactory.create("divide", 1, 0),
    ]

    results, errors = execute_sequence(session, calculations)

    assert results == [5.0]
    assert len(errors) == 1
    assert len(session.get_history()) == 1
    assert session.get_failures() == errors