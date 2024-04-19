def storyStartGame():
    f_id = input("Выберите класс --->")
    return int(f_id)

def shop(f_u):
    """
        Пример использования массива с классами для вывода их характеристики
    """
    for u in f_u:
        u.print_stats()