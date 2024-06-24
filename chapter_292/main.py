import datetime as dt

# Function to print a greeting message based on the current time
def print_greeting():
    now = dt.datetime.now()
    hour = now.hour
    
    if 5 <= hour < 12:
        greeting = "Good morning!"
    elif 12 <= hour < 17:
        greeting = "Good afternoon!"
    elif 17 <= hour < 21:
        greeting = "Good evening!"
    else:
        greeting = "Good night!"
    
    print(greeting)

# Function to check if today is the user's birthday
def check_birthday(birthdate):
    now = dt.datetime.now()
    if now.month == birthdate.month and now.day == birthdate.day:
        print("Happy Birthday!")
    else:
        print("Today is not your birthday.")

# Main function
def main():
    print_greeting()
    
    # Example birthdate
    birthdate = dt.datetime(year=1995, month=6, day=23)
    check_birthday(birthdate)

if __name__ == "__main__":
    main()
