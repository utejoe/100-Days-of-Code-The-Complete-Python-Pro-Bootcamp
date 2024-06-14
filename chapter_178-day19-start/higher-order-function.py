# Higher Order Functions
# A higher-order function is a function that can take another function as an argument or return a function as a result.
# This concept is useful for creating flexible and reusable code.

# Define basic arithmetic functions

def add(n1, n2):
    """
    Returns the sum of two numbers.

    Parameters:
    n1 (float): The first number.
    n2 (float): The second number.

    Returns:
    float: The sum of n1 and n2.
    """
    return n1 + n2

def subtract(n1, n2):
    """
    Returns the difference between two numbers.

    Parameters:
    n1 (float): The first number.
    n2 (float): The second number.

    Returns:
    float: The difference between n1 and n2.
    """
    return n1 - n2

def multiply(n1, n2):
    """
    Returns the product of two numbers.

    Parameters:
    n1 (float): The first number.
    n2 (float): The second number.

    Returns:
    float: The product of n1 and n2.
    """
    return n1 * n2

def divide(n1, n2):
    """
    Returns the quotient of two numbers.

    Parameters:
    n1 (float): The first number.
    n2 (float): The second number.

    Returns:
    float: The quotient of n1 and n2.

    Raises:
    ValueError: If n2 is zero.
    """
    if n2 == 0:
        raise ValueError("Cannot divide by zero.")
    return n1 / n2

# Example of a higher-order function

def operate(n1, n2, operation):
    """
    Applies an arithmetic operation to two numbers.

    Parameters:
    n1 (float): The first number.
    n2 (float): The second number.
    operation (function): A function that takes two arguments and returns a result.

    Returns:
    float: The result of applying the operation to n1 and n2.
    """
    return operation(n1, n2)

# Using the higher-order function with basic arithmetic functions

result_add = operate(10, 5, add)  # Should return 15
result_subtract = operate(10, 5, subtract)  # Should return 5
result_multiply = operate(10, 5, multiply)  # Should return 50
result_divide = operate(10, 5, divide)  # Should return 2.0

# Print results
print(f"Addition result: {result_add}")
print(f"Subtraction result: {result_subtract}")
print(f"Multiplication result: {result_multiply}")
print(f"Division result: {result_divide}")
