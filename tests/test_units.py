"""
EGN 321 — Module 2
Assignment 2.1 — Conversion Module Tests

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
    # TODO: Replace the placeholders with a verified known conversion.
    pytest.skip("Complete a known-value inches-to-feet test.")


def test_feet_to_inches_known_value():
    pytest.skip("Complete a known-value feet-to-inches test.")


def test_cubic_feet_to_gallons_known_value():
    pytest.skip("Complete a known-value cubic-feet-to-gallons test.")


def test_gallons_to_cubic_feet_known_value():
    pytest.skip("Complete a known-value gallons-to-cubic-feet test.")


def test_reverse_conversion_pair_1():
    # TODO: Verify that a forward and reverse conversion agree.
    pytest.skip("Complete a reverse-conversion test.")


def test_reverse_conversion_pair_2():
    pytest.skip("Complete a second reverse-conversion test.")


def test_round_trip_conversion():
    # Example idea:
    # original = ...
    # converted = ...
    # restored = ...
    # assert restored == pytest.approx(original)
    pytest.skip("Complete a round-trip test.")


def test_zero_value():
    pytest.skip("Complete a zero-value conversion test.")
