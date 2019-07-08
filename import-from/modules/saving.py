def save_textfile(text, filename): 
    print('salvando archivo:', filename)
    with open(filename, 'w') as file: 
        file.write(text)