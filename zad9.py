from abc import ABC, abstractmethod

# Базовый класс
class Character(ABC):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    @abstractmethod
    def Info(self):
        pass

    @abstractmethod
    def Attack(self):
        pass


# Воин (сильная физическая атака)
class Warrior(Character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.strength = strength

    def Info(self):
        return f"Воин: {self.name}, здоровье: {self.hp}, сила: {self.strength}"

    def Attack(self):
        return f"{self.name} бьёт мечом! Урон: {self.strength * 2}"


# Маг (магическая атака)
class Mage(Character):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self.mana = mana

    def Info(self):
        return f"Маг: {self.name}, здоровье: {self.hp}, мана: {self.mana}"

    def Attack(self):
        return f"{self.name} кастует огненный шар! Урон: {self.mana * 3}"


# Лучник (дальняя атака)
class Archer(Character):
    def __init__(self, name, hp, accuracy):
        super().__init__(name, hp)
        self.accuracy = accuracy

    def Info(self):
        return f"Лучник: {self.name}, здоровье: {self.hp}, точность: {self.accuracy}"

    def Attack(self):
        return f"{self.name} стреляет из лука! Урон: {self.accuracy * 1.5}"


# Создание персонажа
def create_character():
    print("\n1 - Воин, 2 - Маг, 3 - Лучник")
    choice = input("Выбор: ")

    name = input("Имя персонажа: ")
    hp = int(input("Здоровье: "))

    if choice == "1":
        strength = int(input("Сила: "))
        return Warrior(name, hp, strength)
    elif choice == "2":
        mana = int(input("Мана: "))
        return Mage(name, hp, mana)
    elif choice == "3":
        accuracy = int(input("Точность: "))
        return Archer(name, hp, accuracy)
    else:
        print("Неверный выбор")
        return None


# Главный цикл
def main():
    characters = []

    while True:
        print("\n1 - Создать персонажа, 2 - Показать всех, 3 - Атаковать, 0 - Выход")
        choice = input("Выбор: ")

        if choice == "1":
            c = create_character()
            if c != None:
                characters.append(c)
                print("Персонаж создан")

        elif choice == "2":
            if len(characters) == 0:
                print("Список пуст")
            else:
                for c in characters:
                    print(c.Info())
                    print("-" * 30)

        elif choice == "3":
            if len(characters) == 0:
                print("Нет персонажей")
            else:
                for c in characters:
                    # Полиморфизм: каждый бьёт по-своему
                    print(c.Attack())
                    print("-" * 30)

        elif choice == "0":
            break


if __name__ == "__main__":
    main()