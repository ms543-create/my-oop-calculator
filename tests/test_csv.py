"""Tests for CSV input."""

import pytest

from calculator.inputs import read_csv_values

from calculator.factory import CalculationFactory

def test_read_csv_values():
    values = read_csv_values("values.csv")

    assert values == [10, 20, 30, 40, 50]


def test_read_csv_values_from_temporary_file(tmp_path):
    csv_file = tmp_path / "numbers.csv"
    csv_file.write_text("value\n2\n4\n6\n", encoding="utf-8")

    values = read_csv_values(csv_file)

    assert values == [2, 4, 6]


def test_csv_requires_value_column(tmp_path):
    csv_file = tmp_path / "numbers.csv"
    csv_file.write_text("amount\n10\n20\n", encoding="utf-8")

    with pytest.raises(ValueError, match="value"):
        read_csv_values(csv_file)


from calculator.factory import CalculationFactory


def test_csv_and_manual_mean_match(tmp_path):
    csv_file = tmp_path / "observations.csv"
    csv_file.write_text("value\n5\n10\n15\n20\n", encoding="utf-8")

    csv_values = read_csv_values(csv_file)

    csv_result = CalculationFactory.create(
        "mean", *csv_values
    ).get_result()

    manual_result = CalculationFactory.create(
        "mean", 5, 10, 15, 20
    ).get_result()

    assert csv_result == pytest.approx(manual_result)


def test_csv_and_manual_stddev_match(tmp_path):
    csv_file = tmp_path / "observations.csv"
    csv_file.write_text("value\n5\n10\n15\n20\n", encoding="utf-8")

    csv_values = read_csv_values(csv_file)

    csv_result = CalculationFactory.create(
        "stddev", *csv_values
    ).get_result()

    manual_result = CalculationFactory.create(
        "stddev", 5, 10, 15, 20
    ).get_result()

    assert csv_result == pytest.approx(manual_result)


def test_read_different_csv_column(tmp_path):
    csv_file = tmp_path / "observations.csv"
    csv_file.write_text(
        "observation\n10\n20\n30\n",
        encoding="utf-8",
    )

    values = read_csv_values(csv_file, column="observation")

    assert values == [10, 20, 30]


def test_missing_selected_csv_column(tmp_path):
    csv_file = tmp_path / "observations.csv"
    csv_file.write_text(
        "value\n10\n20\n30\n",
        encoding="utf-8",
    )

    with pytest.raises(ValueError, match="observation"):
        read_csv_values(csv_file, column="observation")