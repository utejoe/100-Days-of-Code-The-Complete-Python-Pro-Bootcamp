# main.py

import requests
import json
import geocoder

API_KEY = "8ff5fd7bff234edadb01c5141c463a08"  # Replace with your actual API key
CITY = "Lagos"

# Fetch latitude and longitude using geocoder
g = geocoder.ip('me')
LAT, LON = g.latlng

# Fetch current weather data
WEATHER_API_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}"
response = requests.get(WEATHER_API_URL)
response.raise_for_status()
weather_data = response.json()
print("Current weather data:")
print(json.dumps(weather_data, indent=4))

# Fetch 5-day weather forecast data
FORECAST_API_URL = f"http://api.openweathermap.org/data/2.5/forecast?lat={LAT}&lon={LON}&appid={API_KEY}"
forecast_response = requests.get(FORECAST_API_URL)
forecast_response.raise_for_status()
forecast_data = forecast_response.json()
print("5-day weather forecast data:")
print(json.dumps(forecast_data, indent=4))

# Parse and display the forecast data
for forecast in forecast_data['list']:
    time = forecast['dt_txt']
    weather_description = forecast['weather'][0]['description']
    print(f"At {time}, the weather will be: {weather_description}")
