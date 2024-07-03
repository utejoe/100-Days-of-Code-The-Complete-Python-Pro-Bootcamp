def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function

# Calling outer_function and assigning the returned function to a variable
inner_func = outer_function()
# Output: I'm outer

# Calling the inner function
inner_func()
# Output: I'm inner
