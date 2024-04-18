from heroes import *
from enemy import *

p = Mage("Гендальф", 1)
e = Enemy(30, 10, 100, "Гоблин")

def printStats():
    print(p.hp, e.hp)

def attackPlayer():
    e.hp -= (p.attack - e.defence)
def attackEnemy():
    p.hp -= (e.attack - p.defence)

printStats()
attackPlayer()
attackEnemy()
printStats()