"""Tests for the calculator CLI."""

import pytest

from calculator import session
from calculator.cli import prepare_command, run
from calculator.commands import (
    CalculateCommand,
    ClearHistoryCommand,
    CountCommand,
    HelpCommand,
    HistoryCommand,
)
from calculator.session import CalculatorSession


def test_prepare_calculation_command():
    session = CalculatorSession()

    command = prepare_command("add 2 3", session)

    assert isinstance(command, CalculateCommand)
    assert command.execute() == "Result: 5.0000"


def test_prepare_power_with_option():
    session = CalculatorSession()

    command = prepare_command("power 3 exponent=4", session)

    assert command.execute() == "Result: 81.0000"


def test_prepare_application_commands():
    session = CalculatorSession()

    assert isinstance(prepare_command("history", session), HistoryCommand)
    assert isinstance(prepare_command("clear", session), ClearHistoryCommand)
    assert isinstance(prepare_command("help", session), HelpCommand)
    assert prepare_command("count", session).execute() == "Count: 0"

@pytest.mark.parametrize("text", ["history 1", "clear 1", "help 1"])
def test_actions_reject_values(text):
    session = CalculatorSession()

    with pytest.raises(ValueError):
        prepare_command(text, session)


def test_empty_command_rejected():
    session = CalculatorSession()

    with pytest.raises(ValueError):
        prepare_command("", session)


def test_duplicate_options_rejected():
    session = CalculatorSession()

    with pytest.raises(ValueError):
        prepare_command("power 3 exponent=2 exponent=4", session)


def test_empty_option_name_rejected():
    session = CalculatorSession()

    with pytest.raises(ValueError):
        prepare_command("power 3 =4", session)


def test_run_calculation_and_exit(monkeypatch, capsys):
    responses = iter(["add 2 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    run()

    output = capsys.readouterr().out

    assert "Calculator" in output
    assert "Result: 5.0000" in output
    assert "Goodbye!" in output


def test_run_recovers_from_error(monkeypatch, capsys):
    responses = iter(["divide 1 0", "add 2 3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    run()

    output = capsys.readouterr().out

    assert "Error:" in output
    assert "Result: 5.0000" in output
    assert "Goodbye!" in output


def test_run_handles_eof(monkeypatch, capsys):
    def raise_eof(_):
        raise EOFError

    monkeypatch.setattr("builtins.input", raise_eof)

    run()

    output = capsys.readouterr().out

    assert "Calculator" in output
    assert "Goodbye!" in output


def test_module_entrypoint(monkeypatch):
    import runpy

    monkeypatch.setattr("builtins.input", lambda _: "exit")

    runpy.run_module("calculator", run_name="__main__")


def test_prepare_csv_mean():
    session = CalculatorSession()

    command = prepare_command("csv mean values.csv", session)

    assert command.execute() == "Result: 30.0000"


def test_prepare_csv_stddev():
    session = CalculatorSession()

    command = prepare_command("csv stddev values.csv", session)

    assert command.execute() == "Result: 15.8114"


def test_prepare_csv_stddev_with_ddof():
    session = CalculatorSession()

    command = prepare_command("csv stddev values.csv ddof=0", session)

    assert command.execute() == "Result: 14.1421"


@pytest.mark.parametrize(
    "text",
    [
        "csv",
        "csv mean",
        "csv add values.csv",
        "csv mean values.csv badoption",
        "csv stddev values.csv =0",
        "csv stddev values.csv ddof=0 ddof=1",
    ],
)
def test_reject_invalid_csv_commands(text):
    session = CalculatorSession()

    with pytest.raises(ValueError):
        prepare_command(text, session)