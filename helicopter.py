from utils import randcell

class Helicopter:
    def __init__(self, v, h):
        self.v = v
        self.h = h
        rc = randcell(h, v)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.tank = 0
        self.mxtank = 1
        self.score = 0
        self.lives = 20

    def move(self, dx, dy):
        nx = dx + self.x
        ny = dy + self.y
        if (nx >= 0 and ny >= 0 and nx < self.h and ny < self.v):
            self.x, self.y = nx, ny

    def print_stats(self):
        print('🧺 ', self.tank, '/', self.mxtank, sep='', end=' | ')
        print('🏆', self.score, end=' | ')
        print('💛', self.lives)
    
    def export_data(self):
        return {'x': self.x, 'y': self.y,
                'tank': self.tank, 'mxtank': self.mxtank,
                'score': self.score, 'lives': self.lives}   

    def import_data(self, data):
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.tank = data['tank'] or 0
        self.mxtank = data['mxtank'] or 1
        self.lives = data['lives'] or 3
        self.score = data['score'] or 1


    