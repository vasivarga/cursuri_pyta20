import requests

endpoint = "https://simple-books-api.glitch.me/status"

response = requests.get(endpoint)

# Returneaza body-ul sub forma de string
print(response.text)

# Returneaza status code sub forma de int
print(response.status_code)

# Salvam body-ul raspunsului sub forma de dict
response_dict = response.json()

print(type(response_dict))

print(response_dict)

# Scoatem valoarea cheii 'status din dictionar'
print(response_dict['status'])

assert response_dict['status'] == 'OK'
assert response.status_code == 200
