import requests
from datetime import datetime

# Step 1: Create a Pixela User
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "fehsnafdfieladfheo",
    "username": "utejoe",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(pixela_endpoint, json=user_params)
# print(response.text)

# Uncomment the following line after the user is created
# (to avoid recreating the user every time you run the script)
# response = {"message":"Success.","isSuccess":True} 

# Step 2: Create a Graph
graph_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs"
graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "shibafu"
}
headers = {
    "X-USER-TOKEN": user_params["token"]
}

response = requests.post(graph_endpoint, json=graph_params, headers=headers)
print(response.text)

# Step 3: Log a Habit
pixel_creation_endpoint = f"{pixela_endpoint}/{user_params['username']}/graphs/graph1"
today = datetime.now().strftime("%Y%m%d")
pixel_data = {
    "date": today,
    "quantity": "5"
}

# response = requests.post(pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)
