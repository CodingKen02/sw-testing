import pytest
from bmi_calculator import calculate_bmi, bmi_category

def test_calculate_bmi_normal_weight():
    # Test case: Height 5'7", Weight 150 lbs (Normal weight)
    assert abs(calculate_bmi(5, 7, 150) - 24.06) < 0.01

def test_calculate_bmi_string_values():
    # Test case: Height 5'7", Weight "sixty" lbs (Error handling)
    height_ft = 5
    height_in = 7
    weight_lb = "sixty"
    with pytest.raises(TypeError):
        calculate_bmi(height_ft, height_in, weight_lb)

def test_calculate_bmi_zero_values():
    # Test case: Zero height and weight (Error handling)
    height_ft = 0
    height_in = 0
    weight_lb = 0
    with pytest.raises(ZeroDivisionError):
        calculate_bmi(height_ft, height_in, weight_lb)


def test_bmi_category_underweight():
    # Test case: Underweight BMI (less than 18.5)
    assert bmi_category(13.49) == "Underweight"

def test_bmi_category_boundary_values():
    # Test case: BMI of 18.5 (boundary value)
    assert bmi_category(18.5) == "Normal weight"

    # Test case: BMI of 25 (boundary value)
    assert bmi_category(25) == "Overweight"

def test_bmi_category_incorrect_category():
    # Test case: BMI value that doesn't match the expected category
    assert bmi_category(23.49) != "Obese"
