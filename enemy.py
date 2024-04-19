class Enemy:
    def __init__(self, attack:int, defence:int, hp:int, name:str) -> None:
        """
            attack: Урон
            defence: Защита,
            hp: Жизни,
            name: Название персонажа,
        """
        self.attack = attack
        self.defence = defence
        self.hp = hp
        self.name = name
    
    def print_stats(self):
        print(self.hp)
