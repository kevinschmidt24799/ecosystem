import constants
import game
import time

import tensorflow as tf
from keras.layers import Dense
num_trials = 50

start = time.time()

f = open("creature_training.csv", "w")

for i in range(num_trials):
    G = game.Game()

    while True:
        G.one_step()
        if 0 in G.counts:
            G.draw_game()
            break

    win = 1 if G.counts[2] == 0 else -1
    for view in G.memory:
        temp = ''
        for j in view[:-1]:
            temp += str(j) + ','
        win_loss_move = [0]*9
        win_loss_move[view[-1]] = win
        for j in win_loss_move:
            temp += str(j) + ','
        f.write(temp[:-1]+'\n')
    print(i)

f.close()
end = time.time()
print(end - start)
