# Unit Map — Module 2

Complete this before or while building `units.py`.

| Quantity | Incoming Unit | Internal Unit | Conversion Function | Conversion Source |
|---|---|---|---|---|
| Length | feet (ft) | feet (ft) | No conversion needed | Tank workbook input |
| Depth | inches (in)| feet (ft)| depth_ft = depth_in/12|12 inches = 1 foot |
| Volume | cubic_feet (ft^3) | gallons (US gal) | gallons_US_gal = cubic_feet * 7.48052 | 1 ft^3 = 7.48052 US gal |
| Pressure | kPa (kPa) | psi (psi) | psi = kPa / 6.894760| 1 psi = 6.894760 kPa|
| Flow | | | | |
| Other | | | | |

## Boundary Rule
All incoming values are converted to their internal units in units.py before the volume calculation.

## Duplicate-Conversion Risk
Depth could be divided by 12 in units.py and divided by 12 again in the volume calculation.
