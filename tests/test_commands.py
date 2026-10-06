"""Tests for calculator commands."""
import pytest

from calculator.commands import (
    Command,
    CalculateCommand,
    ClearHistoryCommand,
    CountCommand,
    HistoryCommand,
    HelpCommand,
)
from calculator.factory import CalculationFactory
from calculator.session import CalculatorSession


def test_calculate_command():
    session = CalculatorSession()
    calculation = CalculationFactory.create("add", 2, 3)
    command = CalculateCommand(session, calculation)

    assert command.execute() == "Result: 5.0000"
    assert len(session.get_history()) == 1


def test_clear_history_command():
    session = CalculatorSession()
    calculation = CalculationFactory.create("add", 2, 3)

    session.calculate(calculation)

    command = ClearHistoryCommand(session)

    assert command.execute() == "History cleared."
    assert session.get_history() == []


def test_history_command_empty():
    session = CalculatorSession()
    command = HistoryCommand(session)

    assert command.execute() == "History is empty."


def test_history_command_with_entries():
    session = CalculatorSession()
    calculation = CalculationFactory.create("add", 2, 3)

    session.calculate(calculation)

    command = HistoryCommand(session)

    assert command.execute() == "add: 5.0000"


def test_help_command():
    command = HelpCommand()

    result = command.execute()

    assert "add 2 3" in result
    assert "history" in result
    assert "exit" in result


def test_command_requires_execute():
    class IncompleteCommand(Command):
        pass

    with pytest.raises(TypeError):
        IncompleteCommand()


def test_count_command():
    session = CalculatorSession()

    first = CalculationFactory.create("add", 2, 3)
    second = CalculationFactory.create("multiply", 4, 5)

    session.calculate(first)
    session.calculate(second)

    command = CountCommand(session)

    assert command.execute() == "Count: 2"


def test_count_ignores_failed_calculation():
    session = CalculatorSession()

    successful = CalculationFactory.create("add", 2, 3)
    failed = CalculationFactory.create("divide", 1, 0)

    session.calculate(successful)

    with pytest.raises(ZeroDivisionError):
        session.calculate(failed)

    command = CountCommand(session)

    assert command.execute() == "Count: 1"