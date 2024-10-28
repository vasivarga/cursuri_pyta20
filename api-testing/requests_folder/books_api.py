import requests


def get_api_status():
    endpoint = "https://simple-books-api.glitch.me/status"
    response = requests.get(endpoint)

    return response
