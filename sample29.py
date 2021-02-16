import requests
from bs4 import BeautifulSoup

res = requests.get('https://blog.narito.ninja/')
soup = BeautifulSoup(res.text, html)
print(soup)