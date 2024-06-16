def add(*args):
    print(args)  # args is a tuple containing all positional arguments passed
    total_sum = 0
    for num in args:
        total_sum += num
    return total_sum

# Testing the add function
print(add(3, 5, 6))  # Output: 14
print(add(3, 5, 6, 2, 1))  # Output: 17
