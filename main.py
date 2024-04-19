from story import shop, storyStartGame
import heroes

class Game():
    def __init__(self):
        pass

    f_id = storyStartGame()

    a = heroes.Archer("Друид", f_id=f_id)
    b = heroes.Mage("Маг", f_id=f_id)

    # TODO Создать array с class для каждого отряда собранного на уровень
    shop([a,b])

    
if __name__ == "__main__":
    g = Game()