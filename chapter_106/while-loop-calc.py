def add(n1, n2):
    """Return the sum of two numbers."""
    return n1 + n2

def subtract(n1, n2):
    """Return the difference between two numbers."""
    return n1 - n2

def multiply(n1, n2):
    """Return the product of two numbers."""
    return n1 * n2

def divide(n1, n2):
    """Return the quotient of two numbers."""
    if n2 != 0:
        return n1 / n2
    else:
        return "Cannot divide by zero"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number? "))
    
    for symbol in operations:
        print(symbol)
        
    should_continue = True

    while should_continue:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number? "))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            if input("Do you want to start a new calculation? Type 'y' for yes or any other key to exit: ") == 'y':
                calculator()
            else:
                print("Goodbye!")

calculator()
