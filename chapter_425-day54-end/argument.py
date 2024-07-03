def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def calculate(operation, a, b):
    return operation(a, b)

result = calculate(add, 5, 3)
print(result)  # Output: 8

result = calculate(subtract, 5, 3)
print(result)  # Output: 2
