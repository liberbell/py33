import requests
from bs4 import BeautifulSoup

res = requests.get('https://blog.narito.ninja/')
soup = BeautifulSoup(res.text, 'html.parser')
for h1 in soup.find_all('h1'):
    print(h1.text)