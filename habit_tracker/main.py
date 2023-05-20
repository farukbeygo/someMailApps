import requests
from datetime import date


USERNAME = "farukbeygo"
TOKEN = "ffadv2dgd8s59a"
GRAPH_ID = "graph1"
DATE = str(date.today()).replace("-", "")
print(DATE)


user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


graph_config = {
    "id": GRAPH_ID,
    "name": "my_to_tracker",
    "unit": "number",
    "type": "int",
    "color": "momiji",
}


post_config = {
    "date": DATE,
    "quantity": "2",
}


headers = {
    "X-USER-TOKEN": TOKEN,
}


pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


response = requests.post(url=post_endpoint, json=post_config, headers=headers)
print(response.text)




