import requests
from bs4 import BeautifulSoup as BS

source = requests.get('https://www.imdb.com/chart/top')
soup = BS(source.text, 'lxml')

all = soup.select('tbody.lister-list')

for i in all:
    href = ['https://www.imdb.com' + j.get('href') for j in i.select('a')]
    href2 = []
    for element in href:
        if element not in href2:
            href2.append(element)
    title = [j.text.strip() for j in i.select('a')]
    for i in title:
        if i == '':
            title.remove(i)

    title_list = list(zip(title, href2))

    print(title_list)

