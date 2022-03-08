import random
import tensorflow as tf
import math
import constants


class Creature:
    def __init__(self, x, y, t):
        self.x = x
        self.y = y
        self.type = t


class StillCreature(Creature):
    def move(self, view):
        return 0, 0


class RandomCreature(Creature):
    def move(self, view):
        return random.randint(-1, 1), random.randint(-1, 1)


class SimpleCreature(Creature):
    def move(self, view):
        x = 0
        y = 0
        for x1 in range(constants.VISION):
            for y1 in range(constants.VISION):
                if view[x1][y1] < 1:
                    continue
                if constants.superior(self.type, view[x1][y1]) == 1:
                    x += x1 - (constants.VISION-1)/2
                    y += y1 - (constants.VISION-1)/2
                elif constants.superior(self.type, view[x1][y1]) == 2:
                    x -= x1 - (constants.VISION-1)/2
                    y -= y1 - (constants.VISION-1)/2
        x = 1 if x > 0 else (-1 if x < 0 else random.randint(-1, 1))
        y = 1 if y > 0 else (-1 if y < 0 else random.randint(-1, 1))
        return x, y


# does not work for num_types > 3
class PatientCreature(Creature):
    def move(self, view):
        for x1 in range(constants.VISION):
            for y1 in range(constants.VISION):
                if view[x1][y1] < 1:
                    continue
                if constants.superior(self.type, view[x1][y1]) == 1:
                    return x1-1, y1-1
        return 0, 0


class SmartCreature(Creature):
    def __init__(self, x, y, ctype, model):
        self.x = x
        self.y = y
        self.type = ctype
        self.model = model

    def move(self, view):
        t = tf.convert_to_tensor(view)
        t = tf.reshape(t, [1, -1])
        x = self.model.call(t, training=None, mask=None)
        x = tf.reshape(x, [-1])
        mi = tf.argmax(x, axis=None, name=None)
        d = int(mi)
        return math.floor(d/3) - 1, d%3 - 1