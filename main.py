import constants
import game
import time

start = time.time()
wins = 0
for i in range(100):
    G = game.Game()
    while True:
        # G.draw_game()
        G.one_step()
        dist = [0, 0, 0]
        for c in G.creatures:
            dist[c.type - 1] += 1
        if dist[2] == 0:
            wins += 1
            break
        elif dist[0] == 0 or dist[1] == 0:
            break
    print(i)
end = time.time()
print(end - start)
print(wins)
