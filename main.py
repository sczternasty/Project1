import requests
from bs4 import BeautifulSoup

res = requests.get('https://kamernet.nl/en/for-rent/rooms-amsterdam?radius=5&minSize=&maxRent=')
x = BeautifulSoup(res.text, 'html.parser')

print(x)
