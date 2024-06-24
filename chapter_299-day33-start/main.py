import requests

# Define the API endpoint
API_ENDPOINT = "http://api.open-notify.org/iss-now.json"

# Make the GET request to the API
response = requests.get(API_ENDPOINT)

# Check the status code
if response.status_code == 200:
    # Extract the JSON data
    data = response.json()
    print(data)
    
    # Extract latitude and longitude
    latitude = data["iss_position"]["latitude"]
    longitude = data["iss_position"]["longitude"]
    
    print(f"The ISS is currently at latitude: {latitude}, longitude: {longitude}, Status code {response.status_code}")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
