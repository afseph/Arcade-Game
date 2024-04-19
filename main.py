from story import shop, storyStartGame, shopForLVL1
from lvl import startLVL
import heroes

class Game():
    def __init__(self):
        pass

    curr_lvl = 1

    f_id = storyStartGame()

    # TODO Создать array с class для каждого отряда собранного на уровень
    otr = shop(f_id=f_id)

    for u in otr:
        u.print_stats()

    
if __name__ == "__main__":
    g = Game()