import random

import requests


def get_token():
    endpoint = "https://simple-books-api.glitch.me/api-clients/"

    request_body = {
        "clientName": "Postman",
        "clientEmail": f"py_ta{random.randint(9999, 999999999999999)}@gmail.com"
    }

    response = requests.post(endpoint, json=request_body)
    token = response.json()['accessToken']
    print(f"token: {token}")

    return token