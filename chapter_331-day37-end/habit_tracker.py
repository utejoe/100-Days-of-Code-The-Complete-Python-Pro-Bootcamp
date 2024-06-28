import requests
from datetime import datetime

# Define constants
USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_SECRET_TOKEN"
GRAPH_ID = "graph1"

# Pixela endpoint
pixela_endpoint = "https://pixe.la/v1/users"

# Function to get the formatted date
def get_formatted_date(date):
    return date.strftime("%Y%m%d")

# Get today's date
today = get_formatted_date(datetime.now())

# Create the pixel data for today
pixel_data = {
    "date": today,
    "quantity": "9.74"  # Replace with the quantity you want to log
}

# Make the POST request to create a pixel
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
headers = {
    "X-USER-TOKEN": TOKEN
}
response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=headers)
print("Post Response:", response.text)

# Log a Habit for Yesterday
yesterday = get_formatted_date(datetime.now().replace(day=datetime.now().day - 1))

pixel_data_yesterday = {
    "date": yesterday,
    "quantity": "15"  # Replace with the quantity you want to log for yesterday
}

response = requests.post(pixel_creation_endpoint, json=pixel_data_yesterday, headers=headers)
print("Post Response for Yesterday:", response.text)

# Update Yesterday's Pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"
pixel_update_data = {
    "quantity": "4.5"  # New quantity to update
}

response = requests.put(update_endpoint, json=pixel_update_data, headers=headers)
print("Update Response:", response.text)

# Delete Yesterday's Pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday}"

response = requests.delete(delete_endpoint, headers=headers)
print("Delete Response:", response.text)
