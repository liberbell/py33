import requests
from bs4 import BeautifulSoup

res = requests.get('https://blog.narito.ninja/')
soup = BeautifulSoup(res.text, 'html.parser')
for h2 in soup.find_all('h2'):
    print(h2.text)