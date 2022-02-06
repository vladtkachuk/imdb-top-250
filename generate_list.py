import requests
from bs4 import BeautifulSoup
import re

imdb_chart_url = 'https://www.imdb.com/chart/top/'

headers = { "Accept-Language": "en-US,en" }

chart = requests.get(imdb_chart_url, headers=headers).content

soup = BeautifulSoup(chart, 'html.parser')

whitespace_regex = re.compile('\s+')

items = []

save = False

for item in soup.find_all("td", {"class": "titleColumn"}):
    item = whitespace_regex.sub(' ', item.text).strip()
    items.append(item)

all_items = "\n".join(items)

if save:
    with open("imdb-top-250.txt", "w") as f:
        f.writelines(all_items)
else:  
    print(all_items)
