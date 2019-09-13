def print_linea(name, lista): 

    dictionary = {"name": name.upper(), "subra": "-"*len(name), "paradas": "\n".join(lista)}
    return "{name}\n{subra}\n{paradas}\n\n".format(**dictionary) 

def print_file(dictionary): 
    with open("metro.txt", "w") as file: 
        for nombre, lista in dictionary.items(): 
            file.write(print_linea(nombre, lista))
            