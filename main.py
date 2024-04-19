from story import shop, storyStartGame, shopForLVL1
import fights
from lvl import startLVL
import heroes
from enemy import *

class Game():
    def __init__(self):
        pass

    curr_lvl = 1

    f_id = storyStartGame()

    # TODO Создать array с class для каждого отряда собранного на уровень
    otr = shop(f_id=f_id)
    otr[0].print_stats()
    f = fights.Figth(otr = otr)
    f.startFight()

    
if __name__ == "__main__":
    g = Game()