# imprime año y pais

# ejemplo: 
# $ python3 args-year-country.py -c Portugal -y 1900

# imports
from args_getter import get_args

def main(): 
    parser = get_args()

    print('parser -->', parser)
    print('country -->', parser.country)
    print('year -->', parser.year)




if __name__=='__main__':
	main()
