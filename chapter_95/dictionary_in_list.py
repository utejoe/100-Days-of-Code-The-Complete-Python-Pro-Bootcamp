# Existing travel_log with initial entries
travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]

# Function to add a new country to the travel_log
def add_new_country(name, visits, cities):
    # Create a new dictionary to store the details of the new country
    new_country = {
        "country": name,
        "visits": visits,
        "cities": cities
    }
    # Append the new dictionary to the travel_log list
    travel_log.append(new_country)

# Adding a new country to the travel_log
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# Print the updated travel_log to verify the new entry
print(travel_log)
