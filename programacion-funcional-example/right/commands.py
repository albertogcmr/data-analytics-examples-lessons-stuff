from classes import Rober


def command(commands, rober): 
    for c in commands: 
        if c == 'l': 
            rober.turnLeft()
            print(rober)
        elif c == 'r': 
            rober.turnRight()
            print(rober)        
        elif c == 'f': 
            rober.moveForward()
            print(rober)  
    return rober.travelLog