"""
EGN 321 — Module 2
Assignment 2.1 — Conversion Module

Build reusable unit-conversion functions here.

Design requirements:
- Use explicit source_to_destination naming.
- Keep functions small and focused.
- Use named constants when appropriate.
- Do not call input() or print() inside conversion functions.
- Do not mix engineering-context validation into a general conversion function unless there is a documented reason.
"""

# TODO: Define named conversion constants where appropriate.
# Example pattern:
# INCHES_PER_FOOT = 12.0

INCHES_PER_FOOT = 12.0
GALLONS_PER_CUBIC_FOOT = 7.48052


def inches_to_feet(inches):
    """Convert inches to feet."""
    return inches / INCHES_PER_FOOT


def feet_to_inches(feet):
    """Convert feet to inches."""
    return feet * INCHES_PER_FOOT


def cubic_feet_to_gallons(cubic_feet):
    """Convert cubic feet to US gallons."""
    return cubic_feet * GALLONS_PER_CUBIC_FOOT


def gallons_to_cubic_feet(gallons):
    """Convert US gallons to cubic feet."""
    return gallons / GALLONS_PER_CUBIC_FOOT


# TODO:
# Add any additional conversions required by your assigned Module 2 workbook.
# Keep each conversion in a separate, clearly named function.
