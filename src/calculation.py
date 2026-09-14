"""
EGN 321 - Module 2
Assignment 2.2 - Validated Pump Calculation
"""

from src.units import kpa_to_psi
from src.validation import validate_pump_inputs


FT_HEAD_PER_PSI_WATER = 2.31
HP_CONSTANT = 3960.0


def calculate_pump_performance(
    suction_pressure_kpa,
    discharge_pressure_kpa,
    flow_rate_gpm,
    rated_flow_gpm,
    specific_gravity,
    pump_efficiency_pct,
):
    """Calculate pump head and horsepower after checking the inputs."""

    # Check the raw values before starting any calculation.
    validate_pump_inputs(
        suction_pressure_kpa,
        discharge_pressure_kpa,
        flow_rate_gpm,
        rated_flow_gpm,
        specific_gravity,
        pump_efficiency_pct,
    )

    # Convert both pressures once at the input boundary.
    suction_pressure_psi = kpa_to_psi(suction_pressure_kpa)
    discharge_pressure_psi = kpa_to_psi(discharge_pressure_kpa)

    # Use the converted pressures for the rest of the calculation.
    differential_pressure_psi = discharge_pressure_psi - suction_pressure_psi
    pump_head_ft = (
        differential_pressure_psi * FT_HEAD_PER_PSI_WATER / specific_gravity
    )
    hydraulic_hp = (
        flow_rate_gpm * pump_head_ft * specific_gravity / HP_CONSTANT
    )
    efficiency_fraction = pump_efficiency_pct / 100.0
    brake_hp = hydraulic_hp / efficiency_fraction
    flow_margin_gpm = rated_flow_gpm - flow_rate_gpm

    return {
        "suction_pressure_psi": suction_pressure_psi,
        "discharge_pressure_psi": discharge_pressure_psi,
        "differential_pressure_psi": differential_pressure_psi,
        "pump_head_ft": pump_head_ft,
        "hydraulic_hp": hydraulic_hp,
        "efficiency_fraction": efficiency_fraction,
        "brake_hp": brake_hp,
        "flow_margin_gpm": flow_margin_gpm,
    }

