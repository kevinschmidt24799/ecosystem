from keras.models import load_model

import constants
import game
import time

import tensorflow as tf
from keras.layers import Dense

G = game.Game()

while True:
    G.one_step()
    G.draw_game()
