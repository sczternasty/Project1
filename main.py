import requests
import pandas as pd
from bs4 import BeautifulSoup

res = requests.get('https://kamernet.nl/en/for-rent/rooms-amsterdam?radius=5&minSize=&maxRent=')
soup = BeautifulSoup(res.text, 'html.parser')
data = soup.select('.tile-data')
tab = []
for element in data:
    partial_data = {}
    partial_data["Title"] = element.find('a').getText().strip()
    partial_data["Location"] = element.select('.tile-city')[0].getText().strip()
    partial_data["Type"] = element.select(('.tile-room-type'))[0].getText().strip().split(" ")[-1]


    tab.append(partial_data)

df = pd.DataFrame(tab)
print(df)
