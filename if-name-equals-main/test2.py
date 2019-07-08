
# se ejecuta siempre que test2.py es importado o llamado
print('test2.py: fuera del if')

if __name__ == "__main__":

    # se ejecuta sólo cuando test2.py es archivo principal
    print('test2.py: dentro del if')