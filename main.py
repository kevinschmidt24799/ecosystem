
import game

G = game.Game()
print(G.board)
while True:
    G.draw_game()
    G.one_step()

