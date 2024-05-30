def is_leap(year):
    """
    Determine whether a given year is a leap year.

    Args:
    year (int): The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    """
    Return the number of days in a given month for a given year.

    Args:
    year (int): The year to consider.
    month (int): The month to consider (1-12).

    Returns:
    int: The number of days in the month for the given year.
    str: An error message if the month is not valid.
    """
    # List of days in each month for a common year
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if month < 1 or month > 12:
        return "Invalid month"
    
    # Check for February and leap year
    if month == 2 and is_leap(year):
        return 29
    else:
        return month_days[month - 1]

# Input year and month
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))

# Get the number of days in the month
days = days_in_month(year, month)

print(days)
