# Debugging Exercise
# Error in Code: The message "You got it" is not being printed when the loop reaches 20.
def print_message():
    # for i in range(1, 20):  # Iterate from 1 to 19 (not including 20)
    for i in range(1, 21):  # Iterate from 1 to 20 (not including 20)
        if i == 20:
            print("You got it")

print_message()  # Call the function
