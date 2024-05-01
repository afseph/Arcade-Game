from typing import List
from copy import deepcopy
from time import sleep
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
        # enemy = enemies.pop(random.randint(0, len(enemies)-1))
        # enemy_otr.append(enemy)
    return enemy_otr


class Fight:
    def setSelfOTR(self, otr:List[Hero]):
        self.otr = otr

    def setSelfEnemyOTR(self):
        self.enemy_otr = makeEnemyOtr()

    def dealDamage(self, u1, u2):
        total_dmg = (u2.attack - u1.defence * 0.5)
        if total_dmg < 0:
            total_dmg = 0
        if u1.hp < total_dmg:
            u1.hp = 0
        else:
            u1.hp -= total_dmg
        return total_dmg

    def printInfo(self, otr, hp_diff="0", a_index=10):
        if a_index == 0:
            # TODO Colorize hp diff for unit 1
            print(f"""
                    =============             =============
                    1:{otr[0].name}                    4:{self.enemy_otr[0].name}
                    {hp_diff}                    {self.enemy_otr[0].hp}
                    =============             =============
                    2:{otr[1].name}                       5:{self.enemy_otr[1].name}
                    {otr[1].hp}                    {self.enemy_otr[1].hp}
                    =============             =============
                    3:{otr[2].name}                    6:{self.enemy_otr[2].name}
                    {otr[2].hp}                    {self.enemy_otr[2].hp}
                    =============             =============
                    """)
        if a_index == 1:
            # TODO Colorize hp diff for unit 2
            print(f"""
                    =============             =============
                    1:{otr[0].name}                    4:{self.enemy_otr[0].name}
                    {otr[0].hp}                    {self.enemy_otr[0].hp}
                    =============             =============
                    2:{otr[1].name}                       5:{self.enemy_otr[1].name}
                    {hp_diff}                    {self.enemy_otr[1].hp}
                    =============             =============
                    3:{otr[2].name}                    6:{self.enemy_otr[2].name}
                    {otr[2].hp}                    {self.enemy_otr[2].hp}
                    =============             =============
                    """)
        if a_index == 2:
            # TODO Colorize hp diff for unit 3
            print(f"""
                    =============             =============
                    1:{otr[0].name}                    4:{self.enemy_otr[0].name}
                    {otr[0].hp}                    {self.enemy_otr[0].hp}
                    =============             =============
                    2:{otr[1].name}                       5:{self.enemy_otr[1].name}
                    {otr[1].hp}                    {self.enemy_otr[1].hp}
                    =============             =============
                    3:{otr[2].name}                    6:{self.enemy_otr[2].name}
                    {hp_diff}                    {self.enemy_otr[2].hp}
                    =============             =============
                    """)
        if a_index == 3:
            # TODO Colorize hp diff for unit 4
            print(f"""
                    =============             =============
                    1:{otr[0].name}                    4:{self.enemy_otr[0].name}
                    {otr[0].hp}                    {hp_diff}
                    =============             =============
                    2:{otr[1].name}                       5:{self.enemy_otr[1].name}
                    {otr[1].hp}                    {self.enemy_otr[1].hp}
                    =============             =============
                    3:{otr[2].name}                    6:{self.enemy_otr[2].name}
                    {otr[2].hp}                    {self.enemy_otr[2].hp}
                    =============             =============
                    """)
        if a_index == 4:
            # TODO Colorize hp diff for unit 5
            print(f"""
                    =============             =============
                    1:{otr[0].name}                    4:{self.enemy_otr[0].name}
                    {otr[0].hp}                    {self.enemy_otr[0].hp}
                    =============             =============
                    2:{otr[1].name}                       5:{self.enemy_otr[1].name}
                    {otr[1].hp}                    {hp_diff}
                    =============             =============
                    3:{otr[2].name}                    6:{self.enemy_otr[2].name}
                    {otr[2].hp}                    {self.enemy_otr[2].hp}
                    =============             =============
                    """)
        if a_index == 5:
            # TODO Colorize hp diff for unit 6
            print(f"""
                    =============             =============
                    1:{otr[0].name}                    4:{self.enemy_otr[0].name}
                    {otr[0].hp}                    {self.enemy_otr[0].hp}
                    =============             =============
                    2:{otr[1].name}                       5:{self.enemy_otr[1].name}
                    {otr[1].hp}                    {self.enemy_otr[1].hp}
                    =============             =============
                    3:{otr[2].name}                    6:{self.enemy_otr[2].name}
                    {otr[2].hp}                    {hp_diff}
                    =============             =============
                    """)
        if a_index == 10:
            # Just printing info
            print(f"""
                    =============             =============
                    1:{otr[0].name}                    4:{self.enemy_otr[0].name}
                    {otr[0].hp}                    {self.enemy_otr[0].hp}
                    =============             =============
                    2:{otr[1].name}                       5:{self.enemy_otr[1].name}
                    {otr[1].hp}                    {self.enemy_otr[1].hp}
                    =============             =============
                    3:{otr[2].name}                    6:{self.enemy_otr[2].name}
                    {otr[2].hp}                    {self.enemy_otr[2].hp}
                    =============             =============
                    """)
            
    def makeChoice():
         i = random.randint(1,3)
         return i
            
    def enemyMakeHit(self, otr, hitter, i):
        hp_diff = "-" + str(self.dealDamage(u1=otr[i], u2=self.enemy_otr[hitter]))
        self.printInfo(otr=otr, hp_diff=str(hp_diff), a_index=i)
        sleep(5)

    def makeMove(self, otr:List[Hero]):
        steps_count = 1
        curr_player = 0
        is_otr_dead = True if len([True for i in otr if i.hp <= 0]) == 3 else False
        is_enemy_otr_dead = True if len([True for i in self.enemy_otr if i.hp <= 0]) == 3 else False
        while not is_enemy_otr_dead and not is_otr_dead:

            hitter = random.randint(0,len(self.enemy_otr)-1)
            while self.enemy_otr[hitter].hp == 0:
                hitter = random.randint(0,len(self.enemy_otr)-1)
            i = random.randint(0,len(otr)-1)
            while otr[i].hp == 0:
                i = random.randint(0,len(otr)-1)
            while otr[curr_player].hp == 0:
                curr_player += 1

            if steps_count % 2 == 0:
                self.enemyMakeHit(otr=otr, hitter=hitter, i=i)
                steps_count += 1
            else:
                self.printInfo(otr=otr)
                if otr[curr_player].__class__.__name__ == "Medic":   
                    des = int(input("""
                                Выбирите действие:
                                    0. Отхилить команду
                                    1. Нанести удар
                                    2. Пропустить ход
                                """))
                else:
                    des = int(input("""
                                Выбирите действие:
                                    1. Нанести удар
                                    2. Пропустить ход
                                """))
                                        
                if des >= 2:
                    self.enemyMakeHit(otr=otr, hitter=hitter, i=i)
                    steps_count += 1
                elif des == 0:
                    for u in otr:
                        if u.hp != 0:
                            u.hp += 25
                    self.printInfo(otr=otr)
                    if curr_player == (len(otr)-1):
                        curr_player = 0
                    else:
                        curr_player += 1
                    steps_count += 1
                    sleep(5)
                elif steps_count % 2 != 0:
                    i = random.randint(0,len(self.enemy_otr)-1)
                    hp_diff = "-" + str(self.dealDamage(u1=self.enemy_otr[hitter], u2=otr[curr_player]))
                    self.printInfo(otr=otr, hp_diff=str(hp_diff), a_index=i+3)
                    if curr_player == (len(otr)-1):
                        curr_player = 0
                    else:
                        curr_player += 1
                    steps_count += 1
                    sleep(5)
            is_otr_dead = True if len([True for i in otr if i.hp == 0]) == 3 else False
            is_enemy_otr_dead = True if len([True for i in self.enemy_otr if i.hp == 0]) == 3 else False

        return {
            "is_enemy_otr_dead" : is_enemy_otr_dead,
            "is_otr_dead" : is_otr_dead
        }


    def startFight(self, otr, enemy_lvl = 1, otr_cost = 0):
        """
            В функцию требуется передать отряд, цену отряда и уровень соперников(не обязательно)
            Функция возвращает деньги полученные за битву
        """
        self.setSelfEnemyOTR()
        dead = self.makeMove(otr=otr)
        if dead.get("is_otr_dead"):
            print("Вы проиграли")
            return otr_cost + 200
        else:
            print("Вы выйграли")
            return otr_cost * 2


f = Fight()
f.startFight(otr=[Medic(1),Archer(1),Medic(1)])


