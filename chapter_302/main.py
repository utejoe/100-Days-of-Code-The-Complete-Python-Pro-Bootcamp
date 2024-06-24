import requests
from datetime import datetime

# Constants for latitude and longitude (e.g., London)
MY_LAT = 6.5965
MY_LONG = 3.342

def get_sun_times(lat, lng):
    # API endpoint and parameters
    endpoint = "https://api.sunrise-sunset.org/json"
    params = {
        "lat": lat,
        "lng": lng,
        "formatted": 0  # Use 24-hour time format
    }

    # Make API request
    response = requests.get(endpoint, params=params)
    response.raise_for_status()  # Raise an exception for bad requests

    # Parse JSON response
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    return sunrise, sunset

def format_time(time_str):
    # Convert time string to datetime object
    time_obj = datetime.fromisoformat(time_str)
    return time_obj.hour, time_obj.minute

def is_daytime(sunrise, sunset):
    # Get current time in UTC
    now = datetime.utcnow()
    current_hour = now.hour
    current_minute = now.minute

    # Format sunrise and sunset times
    sunrise_hour, sunrise_minute = format_time(sunrise)
    sunset_hour, sunset_minute = format_time(sunset)

    # Compare current time with sunrise and sunset times
    if (current_hour > sunrise_hour or (current_hour == sunrise_hour and current_minute >= sunrise_minute)) and \
       (current_hour < sunset_hour or (current_hour == sunset_hour and current_minute < sunset_minute)):
        return True  # It's daytime
    else:
        return False  # It's nighttime

# Fetch sunrise and sunset times
sunrise, sunset = get_sun_times(MY_LAT, MY_LONG)
print(f"Sunrise: {sunrise}")
print(f"Sunset: {sunset}")

# Check if it's currently daytime
if is_daytime(sunrise, sunset):
    print("It's daytime.")
else:
    print("It's nighttime.")
