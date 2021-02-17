import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.yahoo.co.jp')
soup = BeautifulSoup(res.text, 'html.parser')
for h1 in soup.find_all('h1'):
    print(h1.text)