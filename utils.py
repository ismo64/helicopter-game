from random import randint as rand

def randbool(r, mxr):
    t = rand(0, mxr)
    return (t <= r)

def randcell(h, w):
    th = rand(0, h-1)
    tw = rand(0, w-1)
    return (th, tw)

# 0 - наверх, 1 - направо, 2 - вниз, 3 - налево
def randcell2(x, y):
    t = rand(0, 3)
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dx, dy = moves[t][0], moves[t][1]
    
    return (dx + x, dy + y)
