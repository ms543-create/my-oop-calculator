"""CLI prepares requests, invokes commands, and recovers from expected failures."""

from calculator.commands import (
    CalculateCommand,
    ClearHistoryCommand,
    CountCommand,
    HelpCommand,
    HistoryCommand,
)
from calculator.factory import CalculationFactory
from calculator.inputs import read_csv_values
from calculator.session import CalculatorSession


def prepare_command(text, session):
    parts = text.split()

    if not parts:
        raise ValueError("Enter a command; use help for examples.")

    name, *arguments = parts
    name = name.lower()

    if name == "csv":
        if len(arguments) < 2:
            raise ValueError("Usage: csv mean|stddev PATH [ddof=value]")

        operation_name = arguments[0]
        path = arguments[1]
        csv_arguments = arguments[2:]

        if operation_name not in ("mean", "stddev"):
            raise ValueError("CSV supports mean or stddev.")

        values = read_csv_values(path)
        options = {}

        for argument in csv_arguments:
            if "=" not in argument:
                raise ValueError("CSV options must use key=value.")

            key, value = argument.split("=", 1)

            if not key or key in options:
                raise ValueError("Options need unique names: key=value.")

            options[key] = value

        calculation = CalculationFactory.create(
            operation_name,
            *values,
            **options,
        )

        return CalculateCommand(session, calculation)

    actions = {
        "history": HistoryCommand,
        "clear": ClearHistoryCommand,
        "count": CountCommand,
    }

    if name in actions:
        if arguments:
            raise ValueError(f"{name} does not accept values.")

        return actions[name](session)

    if name == "help":
        if arguments:
            raise ValueError("help does not accept values.")

        return HelpCommand()

    values = []
    options = {}

    for argument in arguments:
        if "=" in argument:
            key, value = argument.split("=", 1)

            if not key or key in options:
                raise ValueError("Options need unique names: key=value.")

            options[key] = value
        else:
            values.append(argument)

    arguments = values

    calculation = CalculationFactory.create(
        name,
        *arguments,
        **options,
    )

    return CalculateCommand(session, calculation)


def run() -> None:
    session = CalculatorSession()

    print("Calculator")
    print(HelpCommand().execute())

    while True:
        try:
            text = input("> ").strip()

            if text.lower() == "exit":
                break

            command = prepare_command(text, session)
            print(command.execute())

        except (EOFError, KeyboardInterrupt):
            print()
            break

        except (
            ValueError,
            OSError,
            ZeroDivisionError,
            OverflowError,
        ) as error:
            print(f"Error: {error}")

    print("Goodbye!")