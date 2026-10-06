"""Process prepared calculations and requests independently."""

from calculator.factory import CalculationFactory


def execute_sequence(session, calculations):
    """Execute each prepared calculation independently."""
    results = []
    errors = []

    for calculation in calculations:
        try:
            result = session.calculate(calculation)
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            session.record_failure(error)
            errors.append(str(error))
        else:
            results.append(result)

    return results, errors


def execute_requests(session, requests):
    """Prepare and execute each request independently."""
    results = []
    errors = []

    for name, values, options in requests:
        try:
            calculation = CalculationFactory.create(
                name,
                *values,
                **options,
            )
            result = session.calculate(calculation)
        except (ValueError, ZeroDivisionError, OverflowError) as error:
            session.record_failure(error)
            errors.append(str(error))
        else:
            results.append(result)

    return results, errors