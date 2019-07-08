from directions import turn


class Rober: 
    def __init__(self): 
        self.direction = 'N'
        self.x = 0
        self.y = 0
        self.travelLog = [(self.x, self.y)]
        
    def turnLeft(self): 
        self.direction = turn(self.direction, side='left')
        
    def turnRight(self): 
        self.direction = turn(self.direction, side='right')
        
    def moveForward(self): 
        d = self.direction
        if d == 'N': 
            self.y -= 1
        elif d == 'S': 
            self.y +=1
        elif d == 'W': 
            self.x -=1
        elif d == 'E': 
            self.x += 1
        self.travelLog.append( (self.x, self.y) )
        
    def __repr__(self): 
        return '({}, {}) {}'.format(self.x, self.y, self.direction)
        