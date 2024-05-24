# Input: A particular number.
target = 100

# Initialize a variable `alternative_sum` to 0 to accumulate the sum of even numbers.
alternative_sum = 0

# Use a for loop to iterate over each number in the range from 1 to the target number (inclusive).
for number in range(1, target + 1):
    # Check if the number is even using the modulo operator (%).
    if number % 2 == 0:
        # If the number is even, add it to the `alternative_sum`.
        alternative_sum += number

# Print the sum of even numbers.
print(f"The sum of all even numbers from 1 to {target} is: {alternative_sum}")
