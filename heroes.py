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
        3:"Дракониды"
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


class Archer(Hero):
    def __init__(self, attack: int, defence: int, hp: int, name: str, f_id:int) -> None:
        super().__init__(attack, defence, hp, name, f_id)


a = Archer(attack=10, defence=20, hp=100, name="Друид", f_id=4)
a.print_stats()
