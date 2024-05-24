# Input: A particular number.
# Convert the input to an integer to ensure numerical operations.
target = int(input("Your target number: "))

# Initialize a variable `even_sum` to 0 to accumulate the sum.
even_sum = 0

# Use a for loop to iterate over each even number in the range from 2 to the target number (inclusive).
# Ensure that the range function receives integer arguments.
for number in range(2, target + 1, 2):
    # Add each even number to the `even_sum`.
    even_sum += number

# Print the sum of even numbers.
print(f"The sum of all even numbers from 1 to {target} is: {even_sum}")