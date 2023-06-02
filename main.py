# 🌲🌊🚁🟩🔥🏥💛🧺🏬⬜🟥🏆
from pynput.keyboard import Key, Listener
from map import Map
from helicopter import Helicopter
from clouds import Clouds
import json
import time
import os


tick = 1
TIME_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
CLOUDS_UPDATE = 30
MAP_W, MAP_H = 20, 10


tmp = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
helico = Helicopter(MAP_W, MAP_H)


MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1, 0), 'a': (0, -1)}
# f - сохранение, g - восстановление
def proccess_key(key):
    global helico
    global tick
    c = key.char
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
    elif c == 'f':
        data = {'helicopter': helico.export_data(), 'clouds': clouds.export_data(),
                    'field': tmp.export_data(), 'tick': tick}
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)
    elif c == 'g':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            helico.import_data(data['helicopter'])
            tick = data['tick'] or 0
            tmp.import_data(data['field'])
            clouds.import_data(data['clouds'])


listener = Listener(
        on_press=None,
        on_release=proccess_key,)

listener.start()

while tick:
    os.system('cls')
    tmp.proccess_helicopter(helico)
    helico.print_stats()
    tmp.print_map(helico)
    tick += 1
    time.sleep(TIME_SLEEP)
    if tick % TREE_UPDATE == 0:
        tmp.generate_tree()
    if tick % FIRE_UPDATE == 0:
        tmp.update_fires()
    if tick % CLOUDS_UPDATE == 0:
        tmp.clouds.update()