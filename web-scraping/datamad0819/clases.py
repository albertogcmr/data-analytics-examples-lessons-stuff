import requests
from bs4 import BeautifulSoup

URL = "https://www.metromadrid.es"

class MetroLineas: 
    def __init__(self, url=URL): 
        self.url_metro = url
        self.urls_lineas = []

    def scan(self): 
        response = requests.get(self.url_metro)
        soup = BeautifulSoup(response.text, "html.parser")
        lineas = soup.find('ul', {"class": "list__otraslineas"})
        lineas = lineas.find_all('a')
        self.urls_lineas = [self.url_metro + linea.get('href') for linea in lineas]

class Linea: 
    def __init__(self, url): 
        self.url = url
        self.name = ""
        self.paradas = []

    def scan(self): 
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, "html.parser")
        # lista de estaciones
        estaciones = soup.find('ul', {"class": "list-line accordion"})
        estaciones = estaciones.find_all('p', {"class": "list-line__btn__text"})
        self.paradas = [estacion.text for estacion in estaciones]
        # nombre de la linea
        self.name = soup.find('span', {"class": "text-line"}).text.strip()
