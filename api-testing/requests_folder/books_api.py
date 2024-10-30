import random

import requests

from requests_folder.generate_token import get_token

token = get_token()

def get_api_status():
    endpoint = "https://simple-books-api.glitch.me/status"
    response = requests.get(endpoint)
    return response

def get_list_of_books(book_type="", limit_size=""):
    endpoint = f"https://simple-books-api.glitch.me/books?type={book_type}&limit={limit_size}"
    return requests.get(endpoint)

def get_book_by_id(id):
    endpoint = f"https://simple-books-api.glitch.me/books/{id}"
    return requests.get(endpoint)

def submit_order(book_id, customer_name):
    endpoint = "https://simple-books-api.glitch.me/orders"

    header_params = {
        "Authorization": token
    }

    request_body = {
      "bookId": book_id,
      "customerName": customer_name
    }

    return requests.post(endpoint, headers=header_params, json=request_body)

def get_order_by_id(order_id):
    endpoint = f"https://simple-books-api.glitch.me/orders/{order_id}"

    header_params = {
        "Authorization": token
    }

    return requests.get(endpoint, headers=header_params)
