import random
import sys

import numpy
import numpy as np
import constants
import creature
import pygame
import math


class Game:
    def __init__(self):
        self.board = [[None for i in range(constants.WORLD_Y)] for j in range(constants.WORLD_X)]
        self.creatures = []

        for i in range(5000):
            while True:
                x = random.randint(0, constants.WORLD_X-1)
                y = random.randint(0, constants.WORLD_Y-1)
                if self.board[x][y] is None:
                    c = creature.RandomCreature(x, y, i % (constants.NUM_TYPES) + 1 )
                    self.creatures.append(c)
                    self.board[x][y] = c
                    break
        global SCREEN, CLOCK
        pygame.init()
        SCREEN = pygame.display.set_mode((constants.WINDOW_X, constants.WINDOW_Y))
        CLOCK = pygame.time.Clock()

    def one_step(self):
        for c in self.creatures:
            v = numpy.zeros([constants.VISION, constants.VISION])
            for x in range(constants.VISION):
                x1 = c.x - math.floor(constants.VISION / 2) + x
                for y in range(constants.VISION):
                    y1 = c.y-math.floor(constants.VISION/2) + y
                    if x1 < 0 or x1 >= constants.WORLD_X or y1 < 0 or y1 >= constants.WORLD_Y:
                        v[x][y] = -1
                        continue
                    v[x][y] = 0 if not self.board[x1][y1] else self.board[x1][y1].type
            x, y = c.move(v)
            x2 = c.x + x
            y2 = c.y + y
            if x2 < 0 or x2 >= constants.WORLD_X:
                x2 = c.x
            if y2 < 0 or y2 >= constants.WORLD_Y:
                y2 = c.y
            end = self.board[x2][y2]
            if not end:
                self.board[c.x][c.y] = None
                self.board[x2][y2] = c
                c.x = x2
                c.y = y2
                continue
            wins = constants.superior(c.type, end.type)
            if wins == 1:
                end.type = c.type
                continue





    def draw_game(self):
        SCREEN.fill((255, 255, 255))

        for c in self.creatures:
            pygame.draw.rect(SCREEN, get_color(c.type), pygame.Rect(constants.WINDOW_X/constants.WORLD_X*c.x,
                                                                    constants.WINDOW_Y/constants.WORLD_Y*c.y,
                                                                    constants.WINDOW_X/constants.WORLD_X,
                                                                    constants.WINDOW_Y/constants.WORLD_Y))

        pygame.display.update()


def get_color(t):
    if t == 1:
        return 255, 0, 0
    if t == 2:
        return 0, 255, 0
    if t == 3:
        return 0, 0, 255
    if t == 4:
        return 0, 255, 255
    if t == 5:
        return 255, 255, 0
    return 255 if t & 1 else 0, 255 if t & 2 else 0, 255 if t & 4 else 0




