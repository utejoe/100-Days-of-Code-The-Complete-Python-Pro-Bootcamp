import requests

# Define the API endpoint
API_ENDPOINT = "http://api.open-notify.org/iss-now.json"

try:
    # Make the GET request to the API
    response = requests.get(API_ENDPOINT)
    # Raise an HTTPError for bad responses (4xx and 5xx)
    response.raise_for_status()
    # Extract the JSON data
    data = response.json()
    # Parse the latitude and longitude
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    print(f"The ISS is currently at latitude: {latitude}, longitude: {longitude}")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except Exception as err:
    print(f"Other error occurred: {err}")
