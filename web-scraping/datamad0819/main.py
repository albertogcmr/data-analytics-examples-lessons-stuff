# metro de madrid

from clases import MetroLineas, Linea
from outputs import print_file

def main(): 
    mm = MetroLineas()
    mm.scan()

    urls = mm.urls_lineas

    metro = {}
    for url in urls: 
        l = Linea(url)
        l.scan()
        metro[l.name] = l.paradas
    print(metro)
    print_file(metro)

 
    



    


if __name__ == "__main__": 
    main()