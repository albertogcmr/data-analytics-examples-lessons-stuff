
import sys

def main():

    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))

    pelicula = sys.argv[-1]

    print(pelicula)

if __name__ == '__main__':
    main()