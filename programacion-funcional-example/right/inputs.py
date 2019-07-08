MESSAGE_INPUT = '(f)orward, (r)ight, (l)eft, (q)quit: '
WRONG_INPUT = 'comando no reconocido'

def get_command(): 
    ''' returns 'l', 'r' or 'f' depending of the choice of the user '''
    while True: 
        option = input(MESSAGE_INPUT)
        if option in 'frlq': 
            break
        else: 
            print(WRONG_INPUT)
            
    return option