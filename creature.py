import random

import constants


class Creature:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.type = t


class StillCreature(Creature):
    def move(self, view):
        return 0,0


class RandomCreature(Creature):
    def move(self, view):
        return random.randint(-1, 1), random.randint(-1, 1)




