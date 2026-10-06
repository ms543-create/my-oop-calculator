"""Application commands for the calculator."""

from abc import ABC, abstractmethod


class Command(ABC):
    """Define the execution contract for calculator commands."""

    @abstractmethod
    def execute(self) -> str:
        """Perform an action and return display text."""


class CalculateCommand(Command):
    """Execute a calculation through the calculator session."""

    def __init__(self, session, calculation):
        self.session = session
        self.calculation = calculation

    def execute(self):
        result = self.session.calculate(self.calculation)
        return f"Result: {result:.4f}"


class ClearHistoryCommand(Command):
    """Clear saved calculation history."""

    def __init__(self, session):
        self.session = session

    def execute(self):
        self.session.clear()
        return "History cleared."


class HistoryCommand(Command):
    """Display saved calculation history."""

    def __init__(self, session):
        self.session = session

    def execute(self):
        entries = self.session.get_history()

        if not entries:
            return "History is empty."

        lines = []
        for calculation, result in entries:
            lines.append(f"{calculation.operation.__name__}: {result:.4f}")

        return "\n".join(lines)


class HelpCommand(Command):
    """Display available calculator commands."""

    def execute(self):
        return (
            "Enter a calculation such as:\n"
            "  add 2 3\n"
            "  subtract 5 2\n"
            "  multiply 4 3\n"
            "  divide 10 2\n"
            "  square 4\n"
            "  sqrt 9\n"
            "  power 3 exponent=4\n"
            "  sum 1 2 3\n"
            "Commands: history, clear, help, exit"
        )


class CountCommand(Command):
    """Report the number of successful saved calculations."""

    def __init__(self, session):
        self.session = session

    def execute(self):
        count = len(self.session.get_history())
        return f"Count: {count}"