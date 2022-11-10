from practice4 import calculate_bmi, bmi_index
import pytest
from pytest import approx


def test_calculate_bmi():
    """Verify that the calculate bmi function works correctly."""
    assert calculate_bmi(47, 154) == approx(20)
    assert calculate_bmi(-95, 175) == approx(-31)
    assert calculate_bmi(4.5, 1.54) == approx(18975)

def test_bmi_index():
    """Verify that the bmi_index function works correctly."""
    assert bmi_index(31) == 'You are obese.'


pytest.main(["-v", "--tb=line", "-rN", __file__])