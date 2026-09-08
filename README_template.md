# EGN 321 — Module 2 Conversion Module

## Purpose
Explain why this module exists and how later tools will reuse it.

## Supported Conversions

| Function | Input Unit | Output Unit | Notes |
|---|---|---|---|
| `inches_to_feet()` | inches | feet | |
| `feet_to_inches()` | feet | inches | |
| `cubic_feet_to_gallons()` | cubic feet | US gallons | |
| `gallons_to_cubic_feet()` | US gallons | cubic feet | |

Add any additional conversions required by your Module 2 workbook.

## Design Rules
Explain your naming pattern, constants, and why each function performs one conversion only.

## Conversion Sources
Document where each conversion factor came from.

## Running the Tests

```bash
pytest
```

## Test Strategy
Explain:
- known-value tests,
- reverse tests,
- round-trip tests,
- zero-value tests,
- any additional edge cases.

## Reuse in Later Modules
Explain how later calculations will import and reuse `units.py`.

## Known Limitations
Document what the module does not handle.

## AI Use
If AI was used, summarize it here and provide details in `AI_LOG.md`.
