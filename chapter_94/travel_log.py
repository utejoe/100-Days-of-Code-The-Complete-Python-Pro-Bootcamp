# Initializing a travel log with nested structures
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 3
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Munich"],
        "total_visits": 2
    }
]

# Adding more complex entries
travel_log.append({
    "country": "Japan",
    "cities_visited": [
        {"city": "Tokyo", "attractions": ["Shibuya Crossing", "Tokyo Tower"]},
        {"city": "Kyoto", "attractions": ["Fushimi Inari Shrine", "Kinkaku-ji"]},
        {"city": "Osaka", "attractions": ["Osaka Castle", "Dotonbori"]}
    ],
    "total_visits": 2,
    "visit_again": True
})

# Print the travel log
for entry in travel_log:
    print(f"Country: {entry['country']}")
    if isinstance(entry["cities_visited"], list):
        for city_info in entry["cities_visited"]:
            if isinstance(city_info, dict):
                print(f"City: {city_info['city']}")
                print(f"Attractions: {', '.join(city_info['attractions'])}")
            else:
                print(f"City: {city_info}")
    print(f"Total Visits: {entry['total_visits']}")
    if "visit_again" in entry:
        print(f"Visit Again: {entry['visit_again']}")
    print()
