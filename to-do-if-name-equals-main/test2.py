
# se ejecuta siempre que test2.py es importado o llamado
print('fuera del if-name de test2')

if __name__ == "__main__":

    # se ejecuta sólo cuando test2.py es archivo principal
    print('dentro del if-name de test2')