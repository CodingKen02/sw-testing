def calculate_bmi(height_ft, height_in, weight_lb):
    # Convert height to inches
    height_inches = height_ft * 12 + height_in

    # Convert height to meters
    height_meters = height_inches * 0.025

    # Convert weight to kilograms
    weight_kg = weight_lb * 0.45

    # Calculate BMI
    bmi = weight_kg / (height_meters ** 2)
    return bmi


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    height_feet = int(input("Enter height (feet): "))
    height_inches = int(input("Enter height (inches): "))
    weight_pounds = float(input("Enter weight (pounds): "))
    bmi_value = calculate_bmi(height_feet, height_inches, weight_pounds)
    print(f"Your BMI value: {bmi_value:.2f}")

    
    bmi_value = float(input("Enter your BMI value: "))
    bmi_cat = bmi_category(bmi_value)
    print(f"BMI Category: {bmi_cat}")


if __name__ == "__main__":
    main()
