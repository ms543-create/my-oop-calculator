"""Preserve the previous project's controlled history boundary."""

from calculator.calculation import Calculation


class History:
    """Store successful calculations and their results."""

    def __init__(self) -> None:
        self._entries = []

    def add(self, calculation: Calculation, result: float) -> None:
        if not isinstance(calculation, Calculation):
            raise TypeError("History accepts Calculation objects only.")

        self._entries.append((calculation, result))

    def get_history(self):
        """Return a shallow copy of the history entries."""
        return self._entries.copy()

    def clear(self) -> None:
        """Remove all entries from history."""
        self._entries.clear()