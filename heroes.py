class Hero:
    def __init__(self, attack:int, defence:int, hp:int, name:str, f_id:int) -> None:
        """
            attack: Урон
            defence: Защита,
            hp: Жизни,
            name: Название персонажа,
            f_id: Id фракции
        """
        self.attack = attack
        self.defence = defence
        self.hp = hp
        self.name = name
        self.f_id = f_id

        # ! Выдача бафаов в зависимости от фракции
        if self.fraction_buff.get(f_id) == "hp":
            self.hp *= 1.25
        elif self.fraction_buff.get(f_id) == "defence":
            self.defence *= 1.25
        elif self.fraction_buff.get(f_id) == "attack":
            self.attack *= 1.25

    # Бафы фракций по Id
    fraction_buff = {
        1: "hp",
        2: "attack",
        3: "defence"
    }

    # Названия фракций по Id
    fractions = {
        1:"Люди",
        2:"Эльфы",
        3:"Хомяки"
    }

    def get_fraction(self):
        """
            Получение названия фракции героя
        """
        return self.fractions.get(self.f_id, "")

    def print_stats(self):
        """
            Вывод статистики в консоль
        """
        print(str(self.name) + ":" + str(self.attack), self.defence, self.hp, self.get_fraction())

    def dealDamage(self):
        return self.attack
    

#1
class Archer(Hero):
    def __init__(self, name: str, f_id:int, attack = 50, defence = 30, hp = 85) -> None:
        super().__init__(attack, defence, hp, name, f_id)

#2
class Warrior(Hero):
    def __init__(self, name: str, f_id:int, attack = 60, defence = 30, hp = 130) -> None:
        super().__init__(attack, defence, hp, name, f_id)

#3
class Mage(Hero):
    def __init__(self, name: str, f_id:int, attack = 50, defence = 30, hp = 70) -> None:
        super().__init__(attack, defence, hp, name, f_id)

#4
class Medic(Hero):
    def __init__(self, name: str, f_id:int, attack = 10, defence = 30, hp = 100) -> None:
        super().__init__(attack, defence, hp, name, f_id)

#5
class Assasion(Hero):
    def __init__(self, name: str, f_id:int, attack = 75, defence = 30, hp = 60) -> None:
        super().__init__(attack, defence, hp, name, f_id)


