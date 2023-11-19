import requests
from bs4 import BeautifulSoup

res = requests.get('https://kamernet.nl/en')
print(res.text)
