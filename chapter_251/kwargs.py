def calculate(n, **kwargs):
    if 'add' in kwargs:
        n += kwargs['add']
    if 'multiply' in kwargs:
        n *= kwargs['multiply']
    return n

# Testing the calculate function
result = calculate(2, add=3, multiply=5)
print(result)  # Output: 25
