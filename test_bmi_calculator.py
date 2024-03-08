import pytest
from bmi_calculator import calculate_bmi, bmi_category

def test_calculate_bmi_normal_weight():
    # Test case: Height 5'7", Weight 150 lbs (Normal weight)
    assert calculate_bmi(5, 7, 150) == pytest.approx(23.49, rel=1e-2)

def test_calculate_bmi_string_values():
    # Test case: Height 5'7", Weight sixty lbs (Error handling)
    # The function should handle zero height and provide an appropriate error or warning.
    with pytest.raises(ValueError):
        calculate_bmi(5, 7, "sixty")

def test_calculate_bmi_negative_values():
    # Test case: Negative height and weight (Error handling)
    # The function should handle negative values and provide an appropriate error or warning.
    with pytest.raises(ValueError):
        calculate_bmi(-5, 7, -150)


def test_bmi_category_normal_weight():
    # Test case: Normal weight BMI (between 18.5 and 24.9)
    assert bmi_category(23.49) == "Normal weight"

def test_bmi_category_boundary_values():
    # Test case: BMI of 18.5 (boundary value)
    assert bmi_category(18.5) == "Normal weight"

    # Test case: BMI of 25 (boundary value)
    assert bmi_category(25) == "Overweight"

def test_bmi_category_incorrect_category():
    # Test case: BMI value that doesn't match the expected category
    # For example, a BMI of 23.49 should not be categorized as "Obese."
    assert bmi_category(23.49) != "Obese"
