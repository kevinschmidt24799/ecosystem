WINDOW_X = 1000
WINDOW_Y = 1000

WORLD_X = 100
WORLD_Y = 100

VISION = 3

NUM_TYPES = 3


# returns which type wins, given 2 ints. 0-> tie, 1-> first wins, 2-> second wins
def superior(me, other):
    t = me - other
    if not t:
        return 0
    return 1 if t % NUM_TYPES < NUM_TYPES/2 else 2
