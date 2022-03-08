import math

WORLD_Y = 30
WORLD_X = 30

CREATURE_RATIO = 0.4

CREATURE_COUNT = math.floor(WORLD_X*WORLD_Y*CREATURE_RATIO)

WINDOW_X = 800
WINDOW_Y = 800 * WORLD_Y/WORLD_X

VISION = 5

NUM_TYPES = 3


# returns which type wins, given 2 ints. 0-> tie, 1-> first wins, 2-> second wins
def superior(me, other):
    t = me - other
    if not t:
        return 0
    return 1 if t % NUM_TYPES > NUM_TYPES/2 else 2
