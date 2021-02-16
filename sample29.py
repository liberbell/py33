import requests

res = requests.get('https://blog.narito.ninja/')
print(res.text)