import requests
import pandas as pd
from bs4 import BeautifulSoup
def web_scrape(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    pages = soup.find_all('li', class_='waves-effect')[-2].getText()
    tab = []
    for i in range(1, int(pages)+1):
        if i == 1:
            pass
        else:
            res = requests.get('https://kamernet.nl/en/for-rent/rooms-amsterdam?pageno=' + str(i))
            soup = BeautifulSoup(res.text, 'html.parser')
        data = soup.select('.tile-data')

        for element in data:
            partial_data = {}
            partial_data["Title"] = element.find('a').getText().strip()
            partial_data["Location"] = element.select('.tile-city')[0].getText().strip()
            partial_data["Type"] = element.select('.tile-room-type')[0].getText().strip().split(" ")[-1]
            partial_data["Price"] = element.select('.tile-rent')[0].getText().strip().split(" ")[1].split(",")[0]
            partial_data["Utilities_included"] = True if len(element.select('.tile-rent')[0].select('span')[0].getText().strip().split(" ")) > 1 else False
            partial_data["Surface"] = element.select('.tile-surface')[0].getText().strip().split(" ")[0]
            partial_data["Furnished"] = element.select('.tile-furnished')[0].getText().strip().split(" ")[0]
            partial_data["Availability_start_date"]= element.select('.tile-availability')[0].getText().strip().split(" ")[0]
            partial_data["Availability_end_date"] = element.select('.tile-availability')[0].getText().strip().split(" ")[1].split("\n")[-1]
            partial_data["URL"] = element.find('a').get('href')
            tab.append(partial_data)
        print(f"Collecting data {i}/{pages}" )

    df = pd.DataFrame(tab)
    pd.options.display.max_columns = 10
    pd.options.display.max_rows = 27
    pd.options.display.max_colwidth = 100

    return df
result_1 = web_scrape('https://kamernet.nl/en/for-rent/rooms-amsterdam?radius=5&minSize=&maxRent=')
result_1.to_csv('df')
