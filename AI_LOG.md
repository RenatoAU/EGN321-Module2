# AI Usage Log
## EGN 321 — Module 2, Assignment 2.1

Use this file if you use ChatGPT, Claude, Copilot, or another approved generative AI tool.

**Student:** Renato Jacinto  
**Course:** EGN 321  
**Tool used:** ChatGPT  
**Date:** September 14, 2026

## How I Used AI

I used ChatGPT as a helper while I was working on this assignment. I mainly used it to understand some parts of the instructions, check the order of the pump calculations, and get ideas for test cases. I did not accept the answers without checking them. I compared the suggestions with the workbook, especially the `Operating Limits` and `Reference Cases` sheets.

## Interaction 1 - Understanding the Calculation

**Prompt:**

> Explain the pump calculation chain in simple steps and help me identify where the pressure conversion should happen.

**AI recommendation:**

The AI explained that suction and discharge pressure enter in kPa and should be converted to psi one time. Then the program calculates differential pressure, pump head, hydraulic horsepower, brake horsepower, and flow margin.

**What I used:**

I used the explanation to organize the calculation with separate variable names such as `suction_pressure_psi`, `differential_pressure_psi`, and `pump_head_ft`.

**What I verified:**

I checked the formulas in the workbook. I found that cell `Calculation Chain!D6` divides by 6.89476 after both pressures were already converted. This causes a double conversion. I removed that extra conversion in the Python version.

## Interaction 2 - Validation Ideas

**Prompt:**

> Give me examples of individual input validation and combination validation for this pump problem.

**AI recommendation:**

The AI suggested checking negative pressures, zero flow, zero specific gravity, invalid efficiency, discharge pressure that is not above suction pressure, and requested flow above rated flow.

**What I used:**

I used the suggestions that matched the workbook's `Operating Limits` sheet. The AI also showed short examples using `ValueError`, which helped me understand how to give a clear error message.

**What I changed or rejected:**

I did not add extra pressure maximums or other limits that were not in the workbook. I kept only the rules supported by the assignment files.

## Interaction 3 - Test Examples

**Prompt:**

> Show me a basic example of how to test a calculated value with `pytest.approx` and how to test a `ValueError` with `pytest.raises`.

**AI recommendation:**

The AI gave small examples of both pytest methods and suggested checking normal values, invalid values, relationships between inputs, and boundary values.

**What I used:**

I used those examples as a starting point for my test structure. I entered the RC-1, RC-2, and RC-3 expected results from the workbook. I also added a test that checks that the double conversion defect does not happen again.

**How I verified the work:**

I ran the complete test suite with `python -m pytest`. All 24 tests passed. The reference tests use expected answers from the workbook instead of answers produced by my own Python function.

## What I Learned

The AI helped me understand the difference between checking one input and checking a relationship. For example, two pressure values can both be positive, but the combination is still invalid when discharge pressure is not greater than suction pressure. I also learned that putting units in variable names helps prevent converting the same value twice.

