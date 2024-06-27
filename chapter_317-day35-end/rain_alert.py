import os
import requests
import json
import geocoder
from twilio.rest import Client

# OpenWeatherMap API parameters
API_KEY = os.environ.get("OWM_API_KEY")  # Replace with your actual API key
CITY = "Lagos"

# Twilio API parameters
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_number = "+12059740432"
to_number = "+2348082666215"

try:
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

    # Check if it will rain in the next 12 hours
    will_rain = False
    for forecast in forecast_data['list'][:4]:  # Next 12 hours (4 data points)
        time = forecast['dt_txt']
        weather_description = forecast['weather'][0]['description']
        weather_id = forecast['weather'][0]['id']
        print(f"At {time}, the weather will be: {weather_description}")
        if weather_id < 700:  # Weather condition codes less than 700 indicate rain
            will_rain = True
            break

    # Send SMS alert if it will rain
    if will_rain:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body="It's going to rain today. Remember to bring an umbrella. ☔",
            from_=twilio_number,
            to=to_number
        )
        print(f"Message status: {message.status}")

except requests.exceptions.RequestException as e:
    print(f"Request error: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
