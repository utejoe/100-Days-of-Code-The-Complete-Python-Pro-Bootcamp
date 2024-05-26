# Function to check if a number is prime
def prime_checker(number):
    # Check if the number is less than 2
    if number < 2:
        print(f"{number} is not a prime number.")
        return
    
    # Assume the number is prime initially
    is_prime = True
    
    # Iterate through numbers from 2 to the square root of the given number
    for i in range(2, int(number ** 0.5) + 1):
        # If the number is divisible by any number in this range, it's not prime
        if number % i == 0:
            is_prime = False
            break
    
    # Print whether the number is prime or not
    if is_prime:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

# Example inputs to test the prime_checker function
prime_checker(29)  # Output: 29 is a prime number.
prime_checker(15)  # Output: 15 is not a prime number.
prime_checker(1)   # Output: 1 is not a prime number.
prime_checker(2)   # Output: 2 is a prime number.
