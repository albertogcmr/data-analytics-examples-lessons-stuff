from pprint import pprint

import requests
from bs4 import BeautifulSoup

METRO_MADRID_ROOT_URL = "https://www.metromadrid.es"
METRO_MADRID_URL = METRO_MADRID_ROOT_URL + "/es"

response = requests.get(METRO_MADRID_URL)
soup = BeautifulSoup(response.text, "html.parser")


print(len(str(soup)))

lines_container = soup.find('ul', {'class': 'list__otraslineas'})
lines = lines_container.find_all('a')
lines_href = [METRO_MADRID_ROOT_URL + line.get('href') for line in lines]


print(len(str(lines_container)))

print(lines_href)

for line in lines_href: 
    response = requests.get(line)
    soup = BeautifulSoup(response.text, "html.parser")

    line_title = soup.find('span', {'class': 'text-line'}).text.strip()

    stops = soup.find_all('p', {'class': 'list-line__btn__text'})
    stops = [stop.text for stop in stops]
    pprint(line_title)
    pprint(stops)
    