"""Execute calculations and record successful results through History."""

from calculator.history import History


class CalculatorSession:
    """Manage calculation execution and history."""

    def __init__(self):
        self._history = History()
        self._failures = []

    def calculate(self, calculation) -> float:
        result = calculation.get_result()
        self._history.add(calculation, result)
        return result

    def record_failure(self, error) -> None:
        self._failures.append(str(error))

    def get_history(self):
        return self._history.get_history()

    def get_failures(self):
        return self._failures.copy()

    def clear(self) -> None:
        self._history.clear()
        self._failures.clear()