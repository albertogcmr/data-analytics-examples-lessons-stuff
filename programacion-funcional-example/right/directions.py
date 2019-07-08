DIRECTIONS = ["N", "E", "S", "W"]

'''
def turnl(actual): 
    i = DIRECTIONS.index(actual)
    return DIRECTIONS[i-1]

def turnr(actual): 
    i = DIRECTIONS.index(actual)
    return DIRECTIONS[(i+1)%len(DIRECTIONS)]
'''

def turn(actual, side='left'): 
    i = DIRECTIONS.index(actual)
    if side == 'left': 
        return DIRECTIONS[i-1]
    elif side == 'right': 
        return DIRECTIONS[(i+1)%len(DIRECTIONS)]
