[README.md](https://github.com/user-attachments/files/32177920/README.md)# EGN 321 — Module 2 Conversion Module

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
### Naming pattern: 
every function is named input_to_output() (e.g. inches_to_feet), so you can tell exactly what it does without opening the file.
### Constants: 
conversion factors (INCHES_PER_FOOT, GALLONS_PER_CUBIC_FOOT) are defined once at the top of units.py instead of hard-coded inside each function. That way if a factor ever needs correcting, it only has to change in one place, and it's obvious where each number in the math is coming from.
### One conversion per function: 
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
### A growing toolkit: 
as later modules need new conversions, they can be added to this same file following the pattern already set here, so units.py keeps getting more useful instead of each module starting from zero.
### More reliable results: 
because every later calculation pulls from the same tested functions, results stay consistent across workbooks instead of small differences creeping in from retyped math.

## Known Limitations
No input validation: passing a string or a negative number will not raise a clear error (negative numbers will just silently produce a negative result, which isn't always physically meaningful for a length or volume).
Only supports the four conversions listed above — no metric units, no temperature, no mass.

## AI Use
If AI was used, summarize it here and provide details in `AI_LOG.md`.

## Commits

### Add Module 2 project structure
Set up src/ and tests/ folders, requirements.txt, and placeholder README/AI_LOG files.
### Implement length and volume conversions with named constants
Add inches_to_feet, feet_to_inches, cubic_feet_to_gallons, gallons_to_cubic_feet with INCHES_PER_FOOT and GALLONS_PER_CUBIC_FOOT as named constants.
### Add known-value, reverse, round-trip, and zero-value tests
19 tests covering all four required categories; all passing.
### Document conversion sources and reuse in README
Add NIST sources, the convert-at-the-boundary design rule, test strategy, and reuse rationale.

## Resource Links
NIST Unit Conversion: https://www.nist.gov/pml/owm/metric-si/unit-conversion
NIST SI Units: https://www.nist.gov/pml/owm/metric-si/si-units


# Module 2, Assignment 2.2

**Student:** Renato Jacinto  
**Student ID:** RJ05348  
**Course:** EGN 321 - Module 2, Assignment 2.2

## Purpose

This project replaces the calculation from `PUMP_HEAD_rev6.xlsx` with Python. It calculates pump head, hydraulic horsepower, brake horsepower, and remaining flow capacity. It also checks the inputs first because an engineering program should refuse a condition that does not make physical sense for this exercise.

## Original Artifact and Defect

The inherited file is included as `PUMP_HEAD_rev6.xlsx`. I traced the formulas before writing the program. The defect is in `Calculation Chain!D6`. The suction and discharge pressures were already changed from kPa to psi in D4 and D5, but D6 divides their difference by 6.89476 again. This is a double conversion. For RC-1, the workbook's broken chain gives about 15.06 ft of head while the corrected chain gives about 103.86 ft.

## External Inputs

| Input | Meaning | External Unit | Internal Unit |
|---|---|---|---|
| `suction_pressure_kpa` | Gauge pressure at the pump inlet | kPa | psi |
| `discharge_pressure_kpa` | Gauge pressure at the pump discharge | kPa | psi |
| `flow_rate_gpm` | Requested operating flow | gpm | gpm |
| `rated_flow_gpm` | Maximum flow used by this exercise | gpm | gpm |
| `specific_gravity` | Fluid density compared with water | ratio | ratio |
| `pump_efficiency_pct` | Estimated pump efficiency | percent | decimal fraction |

## Unit Boundary

The public function is `calculate_pump_performance()` in `src/calculation.py`. It first calls `validate_pump_inputs()`. Then it calls `kpa_to_psi()` once for suction pressure and once for discharge pressure. From that point, the calculation uses the new variables ending in `_psi`. It does not divide the differential pressure by the conversion factor a second time.

`src/units.py` keeps each conversion in a small function so it can be tested and reused. The pressure constant follows the factor used in the assigned workbook and agrees with the NIST pressure conversion of about 6.894757 kPa per psi. The file also keeps the length and volume conversions from my earlier conversion work.

## Calculation Chain

1. Convert suction and discharge pressure from kPa to psi.
2. Subtract suction pressure from discharge pressure to get differential pressure.
3. Calculate head: `differential pressure * 2.31 / specific gravity`.
4. Calculate hydraulic horsepower: `flow * head * specific gravity / 3960`.
5. Change efficiency percent to a decimal fraction.
6. Calculate brake horsepower: `hydraulic horsepower / efficiency fraction`.
7. Calculate flow margin: `rated flow - requested flow`.

The result is a dictionary. I return the intermediate values because it makes debugging easier if a final answer is wrong. The full table is in `CALCULATION_CHAIN.md`.

## Validation Rules

### Individual Rules

| Input | Accepted Range |
|---|---|
| Suction pressure | `>= 0 kPa` |
| Discharge pressure | `>= 0 kPa` |
| Flow rate | `> 0 gpm` |
| Rated flow | `> 0 gpm` |
| Specific gravity | `> 0` |
| Pump efficiency | `> 0%` and `<= 100%` |

### Combination Rules

- Discharge pressure must be greater than suction pressure because this model assumes that the pump adds pressure.
- Requested flow must be less than or equal to rated flow.

These checks are different from individual checks. For example, 200 gpm and 180 gpm are both positive values, but a request of 200 gpm cannot be used with a rating of 180 gpm in this exercise.

## Rejection Behavior

The validation function raises `ValueError` and names the problem. For example:

```text
flow_rate_gpm must be > 0; received 0
```

```text
flow_rate_gpm cannot exceed rated_flow_gpm; received 200 gpm and 180 gpm
```

The program stops before unit conversion and the pump calculation when one of these errors occurs.

## Verification

I used all three cases from the workbook's `Reference Cases` sheet. The tests compare both head and brake horsepower with the independent values supplied in that sheet.

| Case | Expected Head (ft) | Expected Brake HP |
|---|---:|---:|
| RC-1 | 103.861483 | 5.281957 |
| RC-2 | 96.505235 | 3.587265 |
| RC-3 | 109.648487 | 6.718657 |

The suite has 24 passing tests. It covers every rejection rule, known results, conversions, the accepted boundary BC-01, the kPa input boundary, and a regression test for the double conversion defect.

## Running the Tests

In a VS Code terminal opened in this repository, run:

```bash
python -m venv .venv
```

On Windows PowerShell, activate it and install the test dependency:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest
```

The last command should report `24 passed`.

## Assumptions

- Both pressures are gauge pressures measured in kPa.
- The pump is operating with forward flow and adds pressure.
- The head relation uses 2.31 feet per psi for water and adjusts it by specific gravity.
- The horsepower calculation uses the workbook constant 3960.
- Flow and efficiency are steady during one calculation.

## Known Limitations

- This is a class model and not a complete pump selection program.
- It does not check cavitation, NPSH, motor size, pipe friction, temperature, or changes in fluid properties.
- Inputs must be numeric and use the units stated in the table.
- The workbook only gives lower limits for most inputs. The tool does not invent maximum pressures, flow, or specific gravity.
- The pressure factor is rounded to match the workbook, so it is less precise than using more digits.

## Sources

- `PUMP_HEAD_rev6.xlsx`, especially `Calculation Chain`, `Operating Limits`, and `Reference Cases`.
- [NIST Guide to the SI, Appendix B: Conversion Factors](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors)
- [pytest documentation](https://docs.pytest.org/en/stable/)

## AI Use

I used ChatGPT to clarify some parts of the instructions, review the calculation order, and show me basic examples of validation and pytest. I compared every suggestion with the workbook limits and reference cases before using it. More details about how I used AI are included in AI_LOG.md.

