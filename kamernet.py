import requests
import pandas as pd
from bs4 import BeautifulSoup


def web_scrape(file_path):
    res = requests.get('https://kamernet.nl/en/for-rent/rooms-amsterdam?radius=5&minSize=&maxRent=&searchview=1')
    soup = BeautifulSoup(res.text, 'html.parser')
    tab = []
    pages = soup.find_all('ul', class_='MuiPagination-ul mui-style-nhb8h9')[0].getText().split('…')[-1]
    for i in range(1, int(pages) + 1):
        if i == 1:
            pass
        else:
            res = requests.get(
                'https://kamernet.nl/en/for-rent/rooms-amsterdam?radius=5&minSize=&maxRent=0&searchview=1&typeAndCity=rooms-amsterdam&pageNo=' + str(
                    i))
            soup = BeautifulSoup(res.text, 'html.parser')
        data = soup.select('.GridGenerator_root__LBMuh')
        for section in data:
            for element in section:
                partial_data = {}
                partial_data["Title"] = element.select('h6')[0].getText()[:-1]
                partial_data["Location"] = element.select('h6')[1].getText()
                partial_data["Price"] = int(element.select('h5')[0].getText().strip().replace(',','').replace('€',''))
                partial_data["Utilities_included"] = True if len(element.select('p')[4].getText().split()) > 1 else False
                partial_data["Surface"] = int(element.select('p')[0].getText().strip().split()[0])
                partial_data["Furnished"] = element.select('p')[1].getText()
                if len(element.select('p')) == 5:
                    partial_data["Type"] = element.select('p')[2].getText()
                    partial_data["Availability_date"] = element.select('p')[3].getText()
                elif len(element.select('p')) == 6:
                    partial_data["Type"] = element.select('p')[2].getText() + ' ' + element.select('p')[3].getText()
                    partial_data["Availability_date"] = element.select('p')[4].getText()
                partial_data["URL"] = 'https://kamernet.nl' + element.get('href')
                tab.append(partial_data)
        print(f"Collecting data {i}/{pages}")

    df = pd.DataFrame(tab)
    df.to_csv(file_path, index=False)
    return df


