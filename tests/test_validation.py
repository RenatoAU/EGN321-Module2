import pytest

from src.validation import validate_pump_inputs


NORMAL_INPUTS = {
    "suction_pressure_kpa": 110,
    "discharge_pressure_kpa": 420,
    "flow_rate_gpm": 145,
    "rated_flow_gpm": 180,
    "specific_gravity": 1.0,
    "pump_efficiency_pct": 72,
}


def changed(**changes):
    inputs = NORMAL_INPUTS.copy()
    inputs.update(changes)
    return inputs


def test_normal_inputs_are_accepted():
    assert validate_pump_inputs(**NORMAL_INPUTS) is None


def test_negative_suction_pressure_rejected():
    with pytest.raises(ValueError, match="suction_pressure_kpa"):
        validate_pump_inputs(**changed(suction_pressure_kpa=-5))


def test_negative_discharge_pressure_rejected():
    with pytest.raises(ValueError, match="discharge_pressure_kpa"):
        validate_pump_inputs(**changed(discharge_pressure_kpa=-1))


def test_zero_flow_rejected():
    with pytest.raises(ValueError, match="flow_rate_gpm"):
        validate_pump_inputs(**changed(flow_rate_gpm=0))


def test_zero_rated_flow_rejected():
    with pytest.raises(ValueError, match="rated_flow_gpm"):
        validate_pump_inputs(**changed(rated_flow_gpm=0))


def test_zero_specific_gravity_rejected():
    with pytest.raises(ValueError, match="specific_gravity"):
        validate_pump_inputs(**changed(specific_gravity=0))


@pytest.mark.parametrize("efficiency", [0, 100.001])
def test_unsupported_efficiency_rejected(efficiency):
    with pytest.raises(ValueError, match="pump_efficiency_pct"):
        validate_pump_inputs(**changed(pump_efficiency_pct=efficiency))


def test_discharge_not_above_suction_rejected():
    # Both pressures are non-negative, but their relationship is invalid.
    with pytest.raises(ValueError, match="greater than suction"):
        validate_pump_inputs(
            **changed(suction_pressure_kpa=420, discharge_pressure_kpa=110)
        )


def test_equal_pressures_rejected():
    with pytest.raises(ValueError, match="greater than suction"):
        validate_pump_inputs(
            **changed(suction_pressure_kpa=200, discharge_pressure_kpa=200)
        )


def test_requested_flow_above_rating_rejected():
    # Both flow values are positive, but the requested flow is too high.
    with pytest.raises(ValueError, match="cannot exceed"):
        validate_pump_inputs(**changed(flow_rate_gpm=200, rated_flow_gpm=180))

