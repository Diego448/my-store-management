import requests

r = requests.post('http://localhost:5000/users')
print(r.text)