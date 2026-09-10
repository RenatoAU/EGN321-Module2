# EGN 321 — Module 2 Conversion Module

## Purpose
This module exists so I have one tested, reliable place to do unit conversions instead of retyping conversion math (and copy/paste errors) every time a later Module 2 workbook needs feet to inches or cubic feet to gallons. Instead of re-deriving the math in every notebook cell, later scripts just import units and call a function.

## Supported Conversions

| Function | Input Unit | Output Unit | Notes |
|---|---|---|---|
| inches_to_feet()| inches | feet | devides by 12|
| feet_to_inches() | feet | inches | multiplies by 12|
| cubic_feet_to_gallons() | cubic feet | US gallons | multiplies by 7.480519|
| gallons_to_cubic_feet() | US gallons | cubic feet | devides by 7.480519|

Add any additional conversions required by your Module 2 workbook.

## Design Rules
# Naming pattern: 
every function is named input_to_output() (e.g. inches_to_feet), so you can tell exactly what it does without opening the file.
# Constants: 
conversion factors (INCHES_PER_FOOT, GALLONS_PER_CUBIC_FOOT) are defined once at the top of units.py instead of hard-coded inside each function. That way if a factor ever needs correcting, it only has to change in one place, and it's obvious where each number in the math is coming from.
# One conversion per function: 
each function does exactly one job. This makes every function independently testable (see below) and means a bug in one conversion can't silently break another.

## Conversion Sources
INCHES_PER_FOOT = 12 — exact by definition (1 ft = 12 in).
GALLONS_PER_CUBIC_FOOT = 7.480519 — US gallons per cubic foot, per NIST Handbook 44 / standard US customary unit tables.

## Running the Tests

```bash 
pytest
```

## Test Strategy
Explain:
- Known-value tests: check each function against a hand-calculated example (e.g. 24 in → 2 ft) to confirm the basic math is right.
- Reverse tests: feed the output of one function into its inverse (e.g. inches_to_feet then feet_to_inches) and confirm it lands back on the original number.
- Round-trip tests: same idea as reverse tests, but parametrized across several different input values (including a small decimal) to make sure the relationship holds generally, not just for one lucky number.
- Zero-value tests: 0 of any unit should always convert to 0 — this catches any accidental additive offset in the conversion math.

## Reuse in Later Modules
# A growing toolkit: 
as later modules need new conversions, they can be added to this same file following the pattern already set here, so units.py keeps getting more useful instead of each module starting from zero.
# More reliable results: 
because every later calculation pulls from the same tested functions, results stay consistent across workbooks instead of small differences creeping in from retyped math.

## Known Limitations
No input validation: passing a string or a negative number will not raise a clear error (negative numbers will just silently produce a negative result, which isn't always physically meaningful for a length or volume).
Only supports the four conversions listed above — no metric units, no temperature, no mass.

## AI Use
If AI was used, summarize it here and provide details in `AI_LOG.md`.
