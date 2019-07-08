def open_textfile(filename): 
    print('abriendo archivo:', filename)
    with open(filename) as file: 
        text = file.read()
    return text