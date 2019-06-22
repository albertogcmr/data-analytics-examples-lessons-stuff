import requests
from pprint import pprint
from bs4 import BeautifulSoup

ELPAIS_URL = "https://elpais.com/"

response = requests.get(ELPAIS_URL)
soup = BeautifulSoup(response.text, "html.parser")

category_container = soup.find("ul", {'class': 'seccion-submenu-navegacion-listado'})
categories = category_container.find_all("a", {'itemprop': 'url'})

categories = [category.get('href') for category in categories]

pprint(categories)
