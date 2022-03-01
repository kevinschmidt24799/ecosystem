import constants
import game
import time

G = game.Game()
dist = [0, 0, 0]
while True:
    G.draw_game()
    G.one_step()
    dist = [0, 0, 0]
    for c in G.creatures:
        dist[c.type-1]+=1
    print(dist[0], dist[1], dist[2])

