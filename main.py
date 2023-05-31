# search the page: https://pixe.la/v1/users/boboyu/graphs/graph1.html
import requests
import datetime as dt
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "boboyu"
TOKEN = "n2vn75ounfir"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

GRAPH_ID = "graph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Project",
    "unit": "page",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
# .strftime("%Y%m%d")
TODAY = dt.date.today().strftime("%Y%m%d")
TIME = dt.datetime.now().strftime("%H:%M:%S")
print(TIME)
print(TODAY)
pixel_config = {
    "date": TODAY,
    "quantity": input("How many pages did you read today? ")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_endpoint}/{TODAY}"

update_config = {
    "quantity": "20"
}

# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)

