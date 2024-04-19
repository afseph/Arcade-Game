import heroes
from typing import List

def storyStartGame():
    f_id = input("Выберите класс --->")
    return int(f_id)

def shop(f_id) -> List[heroes.Hero]:
    otr = []
    while len(otr) != 3:
        buy_choice = int(input("Выберите персонажа которого хотите купить: 1<->5 >>> "))
        if buy_choice < 0 or buy_choice > 5:
            print("Введите число в диапозоне от 1 до 5")
            continue
        if len(otr) == 0:
            if buy_choice == 1:
                a = heroes.Archer(f_id=f_id, name="1")
            elif buy_choice == 2:
                a = heroes.Assasin(f_id=f_id, name="1")
            elif buy_choice == 3:
                a = heroes.Mage(f_id=f_id, name="1")
            elif buy_choice == 4:
                a = heroes.Medic(f_id=f_id, name="1")
            elif buy_choice == 5:
                a = heroes.Warrior(f_id=f_id, name="1")
            otr.append(a)
            continue
        if len(otr) == 1:
            if buy_choice == 1:
                b = heroes.Archer(f_id=f_id, name="1")
            elif buy_choice == 2:
                b = heroes.Assasin(f_id=f_id, name="1")
            elif buy_choice == 3:
                b = heroes.Mage(f_id=f_id, name="1")
            elif buy_choice == 4:
                b = heroes.Medic(f_id=f_id, name="1")
            elif buy_choice == 5:
                b = heroes.Warrior(f_id=f_id, name="1")
            otr.append(b)
            continue
        if len(otr) == 2:
            if buy_choice == 1:
                c = heroes.Archer(f_id=f_id, name="1")
            elif buy_choice == 2:
                c = heroes.Assasin(f_id=f_id, name="1")
            elif buy_choice == 3:
                c = heroes.Mage(f_id=f_id, name="1")
            elif buy_choice == 4:
                c = heroes.Medic(f_id=f_id, name="1")
            elif buy_choice == 5:
                c = heroes.Warrior(f_id=f_id, name="1")
            otr.append(c)
            continue
    return otr

def shopForLVL1(f_id):
    """
        Пример использования массива с классами для вывода их характеристики
    """ 
    pass