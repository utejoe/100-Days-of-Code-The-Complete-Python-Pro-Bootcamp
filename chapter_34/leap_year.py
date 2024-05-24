# Ask the user to input a year and convert it to an integer
year = int(input("Enter year: \n"))

# Check if the year is divisible by 4
if year % 4 == 0:
    # If the year is divisible by 4, check if it is also divisible by 100
    if year % 100 == 0:
        # If the year is divisible by 100, check if it is also divisible by 400
        if year % 400 == 0:
            # If the year is divisible by 400, it is a leap year
            print("leap year")
        else:
            # If the year is not divisible by 400, it is not a leap year
            print("not leap year")
    else:
        # If the year is divisible by 4 but not by 100, it is a leap year
        print("leap year")
else:
    # If the year is not divisible by 4, it is not a leap year
    print("not leap year")
