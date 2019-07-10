
# imports

import googlemaps
import requests
import os
from dotenv import load_dotenv
from random import randint


def get_lista_lon_lat(number): 
    res = [(float(randint(-180,180)), float(randint(-90,90))) for _ in range(number)]
    return res



def main(): 
    load_dotenv()
    key = os.getenv('KEY', 'No value found')

    query= "Calle Alcalá"
    # API: places
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}".format(query, key)

    # API: geocode
    # url = "https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key={}".format(key)
    response = requests.get(url)
    data = response.json()
    print(data)



if __name__ == "__main__":
    main()