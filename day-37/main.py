import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
import requests

load_dotenv()

USERNAME = os.environ.get("USERNAME")
TOKEN = os.environ.get("TOKEN")
NAME = os.environ.get("NAME")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = os.environ.get('GRAPH_ID')
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_params = {
    "id": GRAPH_ID,
    "name": NAME,
    "unit": "session",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.today()
yesterday = today - timedelta(days=1)

pixel_params = {
    "date": yesterday.strftime('%Y%m%d'),
    "quantity": "1",
}

# Create user
user_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(user_response.text)

# Create a graph
graph_response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
print(graph_response.text)

# Add a pixel
pixel_response = requests.post(url=PIXEL_ENDPOINT, json=pixel_params, headers=headers)
print(pixel_response.text)

# Update a pixel
pixel_update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday.strftime('%Y%m%d')}"
# pixel_update_params = {
#     "quantity": "0",
# }
#
# update_pixel_response = requests.put(url=pixel_update_endpoint, json=pixel_update_params,
#                                      headers=headers)
# print(update_pixel_response.text)

# Delete a pixel
# delete_pixel_response = requests.delete(url=pixel_update_endpoint, headers=headers)
# print(delete_pixel_response.text)
