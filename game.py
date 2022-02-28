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
        self.board = np.zeros([constants.WORLD_X, constants.WORLD_Y])
        self.creatures = []

        for i in range(2000):
            while True:
                x = random.randint(0, constants.WORLD_X-1)
                y = random.randint(0, constants.WORLD_Y-1)
                if self.board[x][y] == 0:
                    c = creature.RandomCreature(x, y, (i % 3) + 1)
                    self.creatures.append(c)
                    self.put_creature(c)
                    break
        global SCREEN, CLOCK
        pygame.init()
        SCREEN = pygame.display.set_mode((constants.WINDOW_X, constants.WINDOW_Y))
        CLOCK = pygame.time.Clock()

    def populate_board(self):
        self.board.fill(0)
        for c in self.creatures:
            self.put_creature(c)

    def put_creature(self, c):
        self.board[c.x][c.y] = c.type

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
                    v[x][y] = self.board[x1][y1]
            x, y = c.move(v)
            x2 = c.x + x
            y2 = c.y + y
            if x2 < 0 or x2 >= constants.WORLD_X:
                x2 = c.x
            if y2 < 0 or y2 >= constants.WORLD_Y:
                y2 = c.y
            end = self.board[x2][y2]
            c.x = x2

            c.y = y2




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
    return 255 if t & 1 else 0, 255 if t & 2 else 0, 255 if t & 4 else 0




