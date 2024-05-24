# Ask the user for their height in meters and convert the input to a float
height = float(input("Enter your height in meters (e.g., 1.55): "))

# Ask the user for their weight in kilograms and convert the input to an integer
weight = int(input("Enter your weight in kilograms (e.g., 59): "))

# Calculate the BMI using the formula: weight (kg) / (height (m) * height (m))
bmi = weight / (height * height)

# Check the BMI category based on standard BMI ranges
if bmi < 18.5:
    # If BMI is less than 18.5, the user is underweight
    print(f"Your BMI is {bmi:.2f}, you are underweight.")
elif bmi < 25:
    # If BMI is between 18.5 and 24.9, the user has a normal weight
    print(f"Your BMI is {bmi:.2f}, you have a normal weight.")
elif bmi < 30:
    # If BMI is between 25 and 29.9, the user is slightly overweight
    print(f"Your BMI is {bmi:.2f}, you are slightly overweight.")
elif bmi < 35:
    # If BMI is between 30 and 34.9, the user is obese
    print(f"Your BMI is {bmi:.2f}, you are obese.")
else:
    # If BMI is 35 or greater, the user is clinically obese
    print(f"Your BMI is {bmi:.2f}, you are clinically obese.")

# Explanation of the `:.2f` format specifier:
# The `:.2f` within the curly braces in the f-string is a format specifier
# It formats the floating-point number (bmi) to 2 decimal places
# For example, if bmi is 22.456, it will be displayed as 22.46