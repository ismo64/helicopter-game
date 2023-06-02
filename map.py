from utils import randbool, randcell, randcell2
from helicopter import Helicopter
from clouds import Clouds
import os



# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - апгрейд-шоп
# 5 - огонь

CELL_TYPES = '🟩🌲🌊🏥🏬🔥'
BONUS = 100
UPGRADE_COST = 500
# TO DO: 10000
LIFE_COST = 1000


class Map:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0] * w for i in range(h)]
        self.generate_forest(3, 10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_upgrade_shop()
        self.generate_hospital()
        self.clouds = Clouds(w, h)
    
    def check_bounds(self, x, y):
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True
    
    def print_map(self, helico):
        print('⬛' * (self.w + 2))
        for ri in range(self.h):
            print('⬛', end='')
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if self.clouds.cells[ri][ci] == 1:
                    print('⬜', end='')
                elif self.clouds.cells[ri][ci] == 2:
                    print('🟥', end='')
                elif (helico.x == ri and helico.y == ci):
                    print('🚁', end='')
                elif cell >= 0 and cell < len(CELL_TYPES):
                    print(CELL_TYPES[cell], end='')
            print('⬛')
        print('⬛' * (self.w + 2))

    # Генерация лесов и рек
    def generate_tree(self):
        rx, ry = randcell(self.h, self.w)
        if self.cells[rx][ry] == 0:
            self.cells[rx][ry] = 1
    def generate_river(self, l):
        rc = randcell(self.h, self.w)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx2, ry2):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1
    def generate_forest(self, r, mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, mxr):
                    self.cells[ri][ci] = 1
    def generate_upgrade_shop(self):
        c = randcell(self.h-1, self.w-1)
        cx, cy = c[0], c[1]
        self.cells[cx][cy] = 4

    def generate_hospital(self):
        c = randcell(self.h-1, self.w-1)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else:
            self.generate_hospital()
    
    # Настройки огня
    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(10):
            self.add_fire()
    def add_fire(self):
        rc = randcell(self.h, self.w)
        rx, ry = rc[0], rc[1]
        if self.cells[rx][ry] == 1:
            self.cells[rx][ry] = 5
    
    def proccess_helicopter(self, helico):
        c = self.cells[helico.x][helico.y]
        d = self.clouds.cells[helico.x][helico.y]
        if c == 2:
            helico.tank = helico.mxtank
        if c == 5 and helico.tank > 0:
            helico.tank -= 1
            helico.score += BONUS
            self.cells[helico.x][helico.y] = 1
        if c == 4 and helico.score >= UPGRADE_COST:
            helico.mxtank += 1
            helico.score -= UPGRADE_COST
        if c == 3 and helico.score >= LIFE_COST:
            helico.lives += 10
            helico.score -= LIFE_COST
        if d == 2:
            helico.lives -= 1
            if helico.lives == 0:
                os.system('cls')
                print('XXXXXXXXXXXXXXXXXXXXXXX')
                print('                       ')
                print(f'GAME_OVER! YOUR SCORE: {helico.score}')
                print('                       ')
                print('XXXXXXXXXXXXXXXXXXXXXXX')
                exit(0)
    
    def export_data(self):
        return {'cells': self.cells}

    def import_data(self, data):
        self.cells = data['cells'] or [[0 for i in range(self.w)] for i in range(self.h)]

        
        


