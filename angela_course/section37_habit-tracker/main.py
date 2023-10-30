import requests
import os
from datetime import datetime

pixela_token = os.environ.get("PIXELA_TOKEN")
if pixela_token is None:
    raise Exception("Please set your pixela token as environment variable.")

pixela_username = "saibi"
pixela_endpoint = "https://pixe.la/v1/users"

# create user : call only once
# user_params = {
#     "token": pixela_token,
#     "username": pixela_username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

headers = {
    "X-USER-TOKEN": pixela_token,
}

graph_id = "graph1"

# create graph : call once
# graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"

# graph_config = {
#     "id": graph_id,
#     "name": "Running Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai",
# }
# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now().strftime("%Y%m%d")
print(today)

# post new pixel
# pixel_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}"
# data_config = {
#     "date": today,
#     "quantity": "2.1",
# }

# response = requests.post(url=pixel_endpoint, json=data_config, headers=headers)
# print(response.text)


# update today's pixel
# update_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}/{today}"
# data_config = {
#     "quantity": "1.0",
# }
# response = requests.put(url=update_endpoint, json=data_config, headers=headers)
# print(response.text)

# delete today's pixel
# delete_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs/{graph_id}/{today}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
