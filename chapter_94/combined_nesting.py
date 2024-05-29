complex_structure = {
    "countries": [
        {
            "name": "France",
            "cities": ["Paris", "Lille", "Dijon"]
        },
        {
            "name": "Germany",
            "cities": ["Berlin", "Hamburg", "Munich"]
        }
    ]
}

# Accessing elements
print(complex_structure["countries"][0])           # Output: {'name': 'France', 'cities': ['Paris', 'Lille', 'Dijon']}
print(complex_structure["countries"][0]["name"])   # Output: France
print(complex_structure["countries"][0]["cities"]) # Output: ['Paris', 'Lille', 'Dijon']
print(complex_structure["countries"][0]["cities"][1]) # Output: Lille
