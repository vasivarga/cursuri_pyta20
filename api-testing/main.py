import requests

"""
Exemplu de utilizare a librariei requests
"""

# Declaram endpointul pe care il vom apela
endpoint = "https://simple-books-api.glitch.me/status"

# Pentru un request de tip GET apelam requests.get(endpoint)
# Raspunsul il punem obligatoriu intr-o variabila (response),
# ca apoi sa putem extrage informatiile din el pentru a face verificari
response = requests.get(endpoint)

# .text returneaza body-ul sub forma de string
print(response.text)

# .status_code returneaza status code-ul sub forma de int
print(response.status_code)

### Extrage informatiilor necesare din body-ul raspunsului ###
# Pasul 1: salvam body-ul raspunsului sub forma de dict cu metoda .json()
response_dict = response.json()
print(type(response_dict))
print(response_dict)

# Pasul 2: scoatem valoarea cheii 'status' din dictionar
print(response_dict['status'])

assert response_dict['status'] == 'OK'
assert response.status_code == 200
