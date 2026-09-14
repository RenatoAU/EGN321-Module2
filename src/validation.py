"""
EGN 321 - Module 2
Assignment 2.2 - Pump Input Validation
"""


def validate_pump_inputs(
    suction_pressure_kpa,
    discharge_pressure_kpa,
    flow_rate_gpm,
    rated_flow_gpm,
    specific_gravity,
    pump_efficiency_pct,
):
    """Raise ValueError if an input is outside the workbook limits."""

    # Individual validation rules
    if suction_pressure_kpa < 0:
        raise ValueError(
            f"suction_pressure_kpa must be >= 0; received {suction_pressure_kpa}"
        )

    if discharge_pressure_kpa < 0:
        raise ValueError(
            "discharge_pressure_kpa must be >= 0; "
            f"received {discharge_pressure_kpa}"
        )

    if flow_rate_gpm <= 0:
        raise ValueError(
            f"flow_rate_gpm must be > 0; received {flow_rate_gpm}"
        )

    if rated_flow_gpm <= 0:
        raise ValueError(
            f"rated_flow_gpm must be > 0; received {rated_flow_gpm}"
        )

    if specific_gravity <= 0:
        raise ValueError(
            f"specific_gravity must be > 0; received {specific_gravity}"
        )

    if pump_efficiency_pct <= 0 or pump_efficiency_pct > 100:
        raise ValueError(
            "pump_efficiency_pct must be > 0 and <= 100; "
            f"received {pump_efficiency_pct}"
        )

    # Combination rules. The values can be legal alone but wrong together.
    if discharge_pressure_kpa <= suction_pressure_kpa:
        raise ValueError(
            "discharge_pressure_kpa must be greater than "
            "suction_pressure_kpa"
        )

    if flow_rate_gpm > rated_flow_gpm:
        raise ValueError(
            "flow_rate_gpm cannot exceed rated_flow_gpm; "
            f"received {flow_rate_gpm} gpm and {rated_flow_gpm} gpm"
        )

