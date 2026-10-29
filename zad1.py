# Класс Vehicle - это базовый класс для всего транспорта
class Vehicle:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    # Метод Info() будет переопределён в наследниках
    def Info(self):
        return f"Транспорт: {self.name}, скорость: {self.speed} км/ч"

    # Метод FuelConsumption() тоже будет переопределён
    def FuelConsumption(self):
        return 0


# Класс Car (легковая машина) наследуется от Vehicle
class Car(Vehicle):
    def __init__(self, name, speed, fuel_per_100km):
        super().__init__(name, speed) # вызываем конструктор родителя
        self.fuel_per_100km = fuel_per_100km

    # Переопределяем Info()
    def Info(self):
        return f"Машина: {self.name}, скорость: {self.speed} км/ч"

    # Переопределяем FuelConsumption()
    def FuelConsumption(self):
        return self.fuel_per_100km


# Класс Truck (грузовик) наследуется от Vehicle
class Truck(Vehicle):
    def __init__(self, name, speed, weight, fuel_per_100km):
        super().__init__(name, speed)
        self.weight = weight
        self.fuel_per_100km = fuel_per_100km

    def Info(self):
        return f"Грузовик: {self.name}, скорость: {self.speed} км/ч, груз: {self.weight} т"

    def FuelConsumption(self):
        # Грузовик тратит больше топлива, если везёт тяжелый груз
        return self.fuel_per_100km + self.weight


# Класс Motorcycle (мотоцикл) наследуется от Vehicle
class Motorcycle(Vehicle):
    def __init__(self, name, speed, engine_volume):
        super().__init__(name, speed)
        self.engine_volume = engine_volume

    def Info(self):
        return f"Мотоцикл: {self.name}, скорость: {self.speed} км/ч, объём двигателя: {self.engine_volume} куб.см"

    def FuelConsumption(self):
        # Примерный расход топлива для мотоцикла
        return round(self.engine_volume / 100, 1)


# Функция для создания объекта
def create_vehicle():
    print("\nВыберите тип:")
    print("1 - Машина")
    print("2 - Грузовик")
    print("3 - Мотоцикл")
    choice = input("Ваш выбор: ")

    name = input("Название: ")
    speed = int(input("Скорость (км/ч): "))

    if choice == "1":
        fuel = float(input("Расход топлива (л/100 км): "))
        return Car(name, speed, fuel)
    elif choice == "2":
        weight = float(input("Грузоподъёмность (т): "))
        fuel = float(input("Базовый расход топлива (л/100 км): "))
        return Truck(name, speed, weight, fuel)
    elif choice == "3":
        volume = int(input("Объём двигателя (куб. см): "))
        return Motorcycle(name, speed, volume)
    else:
        print("Неверный выбор")
        return None


# Основная программа
def main():
    transport = []

    while True:
        print("\n--- МЕНЮ ---")
        print("1 - Добавить транспорт")
        print("2 - Показать всё")
        print("0 - Выход")
        choice = input("Выбор: ")

        if choice == "1":
            v = create_vehicle()
            if v != None:
                transport.append(v)
                print("Добавлено!")

        elif choice == "2":
            if len(transport) == 0:
                print("Список пуст.")
            else:
                for v in transport:
                    # Полиморфизм: вызываем одни и те же методы,
                    # но для каждого объекта они работают по-своему
                    print(v.Info())
                    print("Расход топлива:", v.FuelConsumption(), "л/100 км")

        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неверный пункт меню.")


if __name__ == "__main__":
    main()