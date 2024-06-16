# Dictionary of temperatures in Celsius
celsius_temps = {"New York": 22, "Los Angeles": 27, "Chicago": 20, "Houston": 25}

# Dictionary comprehension to convert Celsius to Fahrenheit
fahrenheit_temps = {city: (temp * 9/5) + 32 for city, temp in celsius_temps.items()}
print(fahrenheit_temps)  # Output: {'New York': 71.6, 'Los Angeles': 80.6, ...}
