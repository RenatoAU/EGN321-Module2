import pytest

from src.calculation import calculate_pump_performance


def test_reference_case_1():
    result = calculate_pump_performance(110, 420, 145, 180, 1.0, 72)

    assert result["pump_head_ft"] == pytest.approx(103.86148321333883)
    assert result["brake_hp"] == pytest.approx(5.281956743102599)
    assert result["flow_margin_gpm"] == pytest.approx(35)


def test_reference_case_2():
    result = calculate_pump_performance(95, 360, 120, 160, 0.92, 75)

    assert result["pump_head_ft"] == pytest.approx(96.50523510355818)
    assert result["brake_hp"] == pytest.approx(3.5872653048595367)


def test_reference_case_3():
    result = calculate_pump_performance(150, 510, 150, 190, 1.1, 68)

    assert result["pump_head_ft"] == pytest.approx(109.64848667683866)
    assert result["brake_hp"] == pytest.approx(6.718657271865115)


def test_unit_boundary_integration():
    result = calculate_pump_performance(110, 420, 145, 180, 1.0, 72)

    assert result["suction_pressure_psi"] == pytest.approx(15.9541448868)
    assert result["discharge_pressure_psi"] == pytest.approx(60.9158259316)
    assert result["differential_pressure_psi"] == pytest.approx(44.9616810447)
    assert result["pump_head_ft"] == pytest.approx(103.8614832133)


def test_double_conversion_defect_is_not_repeated():
    result = calculate_pump_performance(110, 420, 145, 180, 1.0, 72)

    # The broken workbook gives about 15.06 ft after converting twice.
    assert result["pump_head_ft"] != pytest.approx(15.0638286486)
    assert result["pump_head_ft"] == pytest.approx(103.8614832133)


def test_boundary_case():
    # BC-01 uses exact accepted limits from the supplemental data.
    result = calculate_pump_performance(0, 150, 1, 1, 0.85, 100)

    assert result["flow_margin_gpm"] == 0
    assert result["efficiency_fraction"] == 1.0
    assert result["pump_head_ft"] > 0

