from pprint import pprint
import requests
from bs4 import BeautifulSoup

METRO_MADRID_ROOT_URL = "https://www.metromadrid.es"
RECURSE =  "/es"
METRO_MADRID_URL = METRO_MADRID_ROOT_URL + RECURSE

class Lines_href: 
    def __init__(self, root=METRO_MADRID_ROOT_URL, recurse=RECURSE): 
        self.root = root
        self.url = root + recurse
        self.lines_href = []

    def scan(self): 
        response = requests.get(METRO_MADRID_URL)
        soup = BeautifulSoup(response.text, "html.parser")

        lines_container = soup.find('ul', {'class': 'list__otraslineas'})
        lines = lines_container.find_all('a')
        self.lines_href = [line.get('href') for line in lines]

    def compose(self): 
        self.lines_href = [self.root + url for url in self.lines_href]

class Stations: 
    def __init__(self, line): 
        self.line = line
        self.line_url = line.lines_href
        self.stops = []

    def scan(self): 
        response = requests.get(line_href)
        soup = BeautifulSoup(response.text, "html.parser")

        line_title = soup.find('span', {'class': 'text-line'}).text.strip()

        stops = soup.find_all('p', {'class': 'list-line__btn__text'})
        self.stops = [stop.text for stop in stops]

class MetroScraper: 
    def __init__(self, root=METRO_MADRID_ROOT_URL, recurse=RECURSE): 
        self.urls = []

    def scan(self): 
        lines = Lines_href()
        lines.scan()
        lines.compose()
        self.urls = lines.lines_href

def test_lines(): 
    lines = Lines_href()
    pprint(lines.lines_href)
    lines.scan()
    pprint(lines.lines_href)
    lines.compose()
    pprint(lines.lines_href)

def test_metro_scraper(): 
    metro = MetroScraper()
    metro.scan()
    pprint(metro.urls)



def test(): 
    pass



if __name__ == '__main__': 
    test_lines()
    # test_metro_scraper()