from abc import ABC, abstractmethod

# Интерфейс 1: аренда
class IRentable(ABC):
    @abstractmethod
    def Rent(self, days):
        pass

    @abstractmethod
    def ReturnItem(self):
        pass


# Интерфейс 2: страхование
class IInsurable(ABC):
    @abstractmethod
    def Insure(self, cost):
        pass

    @abstractmethod
    def GetInsuranceInfo(self):
        pass


# Базовый класс для всего, что сдаётся в аренду
class BaseRental(ABC):
    def __init__(self, name, price_per_day):
        self.name = name
        self.price_per_day = price_per_day

    @abstractmethod
    def Info(self):
        pass


# 1. Автомобиль (можно арендовать и застраховать)
class CarRental(BaseRental, IRentable, IInsurable):
    def __init__(self, name, price_per_day, insurance_cost):
        super().__init__(name, price_per_day)
        self.insurance_cost = insurance_cost
        self.is_rented = False

    def Info(self):
        return f"Автомобиль: {self.name}, цена за день: {self.price_per_day} руб."

    def Rent(self, days):
        if self.is_rented:
            print(f"{self.name} уже арендован!")
            return
        self.is_rented = True
        total = self.price_per_day * days
        print(f"Вы арендовали {self.name} на {days} дн. Стоимость: {total} руб.")

    def ReturnItem(self):
        if not self.is_rented:
            print(f"{self.name} и так свободен.")
            return
        self.is_rented = False
        print(f"{self.name} возвращён.")

    def Insure(self, cost):
        print(f"Автомобиль {self.name} застрахован. Стоимость страховки: {cost} руб.")

    def GetInsuranceInfo(self):
        return f"Страховка для {self.name}: {self.insurance_cost} руб./год"


# 2. Квартира (можно арендовать и застраховать)
class ApartmentRental(BaseRental, IRentable, IInsurable):
    def __init__(self, name, price_per_day, insurance_cost):
        super().__init__(name, price_per_day)
        self.insurance_cost = insurance_cost
        self.is_rented = False

    def Info(self):
        return f"Квартира: {self.name}, цена за день: {self.price_per_day} руб."

    def Rent(self, days):
        if self.is_rented:
            print(f"{self.name} уже арендована!")
            return
        self.is_rented = True
        total = self.price_per_day * days
        print(f"Вы арендовали {self.name} на {days} дн. Стоимость: {total} руб.")

    def ReturnItem(self):
        if not self.is_rented:
            print(f"{self.name} и так свободна.")
            return
        self.is_rented = False
        print(f"{self.name} возвращена.")

    def Insure(self, cost):
        print(f"Квартира {self.name} застрахована. Стоимость: {cost} руб.")

    def GetInsuranceInfo(self):
        return f"Страховка для {self.name}: {self.insurance_cost} руб./год"


# 3. Инструмент (только аренда, без страхования)
class ToolRental(BaseRental, IRentable):
    def __init__(self, name, price_per_day):
        super().__init__(name, price_per_day)
        self.is_rented = False

    def Info(self):
        return f"Инструмент: {self.name}, цена за день: {self.price_per_day} руб."

    def Rent(self, days):
        if self.is_rented:
            print(f"{self.name} уже арендован!")
            return
        self.is_rented = True
        total = self.price_per_day * days
        print(f"Вы арендовали {self.name} на {days} дн. Стоимость: {total} руб.")

    def ReturnItem(self):
        if not self.is_rented:
            print(f"{self.name} и так свободен.")
            return
        self.is_rented = False
        print(f"{self.name} возвращён.")


# Демонстрация
def main():
    print("--- Создаём объекты аренды ---")
    car = CarRental("Toyota Camry", 3000, 15000)
    flat = ApartmentRental("Двушка на Ленина", 2000, 10000)
    drill = ToolRental("Перфоратор Bosch", 500)

    items = [car, flat, drill]

    print("\n--- Информация о всех объектах ---")
    for item in items:
        print(item.Info())

    print("\n--- Арендуем всё на 3 дня ---")
    for item in items:
        item.Rent(3)

    print("\n--- Страхуем то, что можно ---")
    for item in items:
        # Проверяем, поддерживает ли объект интерфейс IInsurable
        if isinstance(item, IInsurable):
            item.Insure(5000)
            print(item.GetInsuranceInfo())
        else:
            print(f"{item.name} нельзя застраховать (нет интерфейса IInsurable).")

    print("\n--- Возвращаем всё ---")
    for item in items:
        item.ReturnItem()


if __name__ == "__main__":
    main()