from typing import List
from copy import deepcopy
import random
from enemy import *
from heroes import *


def makeEnemyOtr() -> List[Enemy]:
    """
    Функция собирает отряд врагов
    """

    enemies = [Enemy(30, 20, 100, "Гоблин"),Enemy(35, 25, 105, "Орк"), Enemy(25, 15, 95, "Скелет"), Enemy(35, 10, 115, "Зомби"), Enemy(15, 50, 150, "Дракон")]

    enemy_otr = []
    while len(enemy_otr) != 3:
        enemy = deepcopy(random.choice(enemies))
        enemy_otr.append(enemy)
    return enemy_otr


class Figth:
    def __init__(self, otr:list) -> None:
        self.otr = otr
        self.enemy_otr = makeEnemyOtr()

    def dealDamage(self, u1, u2):
        u1.hp -= (u2.attack - u1.defence * 0.5)
    
    def startFight(self):
        self.dealDamage(u1 = self.otr[0], u2 = self.enemy_otr[0])
        self.otr[0].print_stats()
        self.dealDamage(u1 = self.enemy_otr[0], u2 = self.otr[0])
        self.enemy_otr[0].print_stats()
        





