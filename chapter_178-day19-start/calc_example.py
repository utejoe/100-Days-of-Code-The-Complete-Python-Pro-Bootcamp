# Define basic arithmetic functions
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

# Define a higher-order function that takes another function as an argument
def calculator(n1, n2, func):
    return func(n1, n2)

# Call the calculator function with different operations
result = calculator(2, 3, add)
print(result)  # Output: 5

result = calculator(2, 3, multiply)
print(result)  # Output: 6
