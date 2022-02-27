import random
import sys

import numpy as np
import constants
import creature
import pygame


class Game:
    def __init__(self):
        self.board = np.zeros([constants.WORLD_X, constants.WORLD_Y])
        self.creatures = []

        for i in range(9):
            while True:
                x = random.randint(0, constants.WORLD_X-1)
                y = random.randint(0, constants.WORLD_Y-1)
                if self.board[x][y] == 0:
                    c = creature.RandomCreature(x, y, (i % 3) + 1)
                    self.creatures.append(c)
                    self.put_creature(c)
                    break

    def populate_board(self):
        self.board.fill(0)
        for c in self.creatures:
            self.put_creature(c)

    def put_creature(self, c):
        self.board[c.x][c.y] = c.type

    def draw_game(self):
        global SCREEN, CLOCK
        pygame.init()
        SCREEN = pygame.display.set_mode((constants.WINDOW_X, constants.WINDOW_Y))
        CLOCK = pygame.time.Clock()
        SCREEN.fill((255, 255, 255))

        for c in self.creatures:
            pygame.draw.rect(SCREEN, get_color(c.type), pygame.Rect(constants.WINDOW_X/constants.WORLD_X*c.x,
                                                                    constants.WINDOW_Y/constants.WORLD_Y*c.y,
                                                                    constants.WINDOW_X/constants.WORLD_X,
                                                                    constants.WINDOW_Y/constants.WORLD_Y))

        pygame.display.update()


def get_color(t):
        return (255 if t & 1 else 0, 255 if t & 2 else 0, 255 if t & 4 else 0)




