from keras.models import load_model

import constants
import game
import time
import pygame
import tensorflow as tf
from keras.layers import Dense

red_wins = 0
pygame.init()
constants.SCREEN = pygame.display.set_mode((constants.WINDOW_X, constants.WINDOW_Y))
constants.CLOCK = pygame.time.Clock()
for i in range(1):
    G = game.Game()
    while True:
        G.one_step()
        G.draw_game()
print(red_wins)

