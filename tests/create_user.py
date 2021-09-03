import requests, json

headers = {'content-type': 'application/json'}
name = input('Enter name: ')
password = input('Enter password: ')
data = json.dumps({"name":name, "password": password})
response = requests.post("http://127.0.0.1:5000/user/create", data = data, headers=headers)
print(response.text)