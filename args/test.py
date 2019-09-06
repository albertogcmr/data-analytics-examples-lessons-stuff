# print('inicio del prog...')

# name = input('¿cómo te llamas?: ')

# print('hola', name)

# import sys

# argumentos = sys.argv

# print(argumentos)

# print('feliz {} cumpleaños {}'.format(argumentos[2], argumentos[1]))

import sys

argumentos = sys.argv

# test.py 2 + 3

print(argumentos)

a, b = int(argumentos[1]), int(argumentos[3])

if argumentos[2] == '+': 
    print(a + b)

