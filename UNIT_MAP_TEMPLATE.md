# Unit Map — Module 2

Complete this before or while building `units.py`.

| Quantity | Incoming Unit | Internal Unit | Conversion Function | Conversion Source |
|---|---|---|---|---|
| Length | | | | |
| Depth | inches (in)| feet (ft)| depth_ft = depth_in/12|12 inches = 1 foot |
| Volume | cubic_feet (ft^3) | gallons (US gal) | gallons_US_gal = cubic_feet * 7.48052 | 1 ft^3 = 7.48052 US gal |
| Pressure | kPa (kPa) | psi (psi) | psi = kPa / 6.894760| 1 psi = 6.894760 kPa|
| Flow | | | | |
| Other | | | | |

## Boundary Rule
Write one sentence describing where conversion happens in your tool.

## Duplicate-Conversion Risk
Identify one place where a conversion could accidentally be applied twice.
