"""
EGN 321 — Module 2
Assignment 2.2 — Conversion Module Tests

Minimum expectations:
- 4 known-value conversion tests
- 2 reverse conversion tests
- 1 round-trip test
- 1 zero-value test
"""

import pytest

from src.units import (
    inches_to_feet,
    feet_to_inches,
    cubic_feet_to_gallons,
    gallons_to_cubic_feet,
)


def test_inches_to_feet_known_value():
    assert inches_to_feet(12) == pytest.approx(1)


def test_feet_to_inches_known_value():
    assert feet_to_inches(1) == pytest.approx(12)


def test_cubic_feet_to_gallons_known_value():
    assert cubic_feet_to_gallons(1) == pytest.approx(7.48052)


def test_gallons_to_cubic_feet_known_value():
    assert gallons_to_cubic_feet(7.48052) == pytest.approx(1)


def test_reverse_conversion_pair_1():
    original_inches = 30.0
    result = feet_to_inches(inches_to_feet(original_inches))
    assert result == pytest.approx(original_inches)


def test_reverse_conversion_pair_2():
    original_cubic_feet = 10.0
    result = gallons_to_cubic_feet(
        cubic_feet_to_gallons(original_cubic_feet)
    )
    assert result == pytest.approx(original_cubic_feet)


def test_round_trip_conversion():
    original_feet = 2.5
    inches = feet_to_inches(original_feet)
    restored_feet = inches_to_feet(inches)
    assert restored_feet == pytest.approx(original_feet)


def test_zero_value():
    assert inches_to_feet(0) == pytest.approx(0)
    assert feet_to_inches(0) == pytest.approx(0)
    assert cubic_feet_to_gallons(0) == pytest.approx(0)
    assert gallons_to_cubic_feet(0) == pytest.approx(0)



import pytest

from src.units import kpa_to_psi, psi_to_kpa


def test_kpa_to_psi_known_value():
    assert kpa_to_psi(6.89476) == pytest.approx(1.0)


def test_psi_to_kpa_known_value():
    assert psi_to_kpa(1.0) == pytest.approx(6.89476)


def test_pressure_round_trip():
    starting_kpa = 350
    restored_kpa = psi_to_kpa(kpa_to_psi(starting_kpa))
    assert restored_kpa == pytest.approx(starting_kpa)


def test_zero_pressure_conversions():
    assert kpa_to_psi(0) == 0
    assert psi_to_kpa(0) == 0
