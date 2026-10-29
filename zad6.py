from abc import ABC, abstractmethod

# Базовый класс
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def Info(self):
        pass

    @abstractmethod
    def FinalPrice(self):
        pass


# Продукты питания (срок годности)
class Food(Product):
    def __init__(self, name, price, days_left):
        super().__init__(name, price)
        self.days_left = days_left

    def Info(self):
        return f"Продукт: {self.name}, цена: {self.price} руб., срок годности: {self.days_left} дн."

    def FinalPrice(self):
        # Если срок подходит к концу, делаем скидку 30%
        if self.days_left <= 3:
            return self.price * 0.7
        return self.price


# Электроника (гарантия)
class Electronics(Product):
    def __init__(self, name, price, warranty_months):
        super().__init__(name, price)
        self.warranty_months = warranty_months

    def Info(self):
        return f"Электроника: {self.name}, цена: {self.price} руб., гарантия: {self.warranty_months} мес."

    def FinalPrice(self):
        # Если гарантия больше года, накидываем 10% к цене
        if self.warranty_months > 12:
            return self.price * 1.1
        return self.price


# Одежда (размер)
class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def Info(self):
        return f"Одежда: {self.name}, цена: {self.price} руб., размер: {self.size}"

    def FinalPrice(self):
        # Большие размеры (XXL и больше) стоят на 5% дороже
        if self.size in ["XXL", "3XL", "4XL"]:
            return self.price * 1.05
        return self.price


# Создание товара
def create_product():
    print("\n1 - Продукт, 2 - Электроника, 3 - Одежда")
    choice = input("Выбор: ")

    name = input("Название: ")
    price = float(input("Цена: "))

    if choice == "1":
        days = int(input("Сколько дней до истечения срока: "))
        return Food(name, price, days)
    elif choice == "2":
        warranty = int(input("Гарантия (месяцев): "))
        return Electronics(name, price, warranty)
    elif choice == "3":
        size = input("Размер (S/M/L/XL/XXL): ")
        return Clothing(name, price, size)
    else:
        print("Неверный выбор")
        return None


# Главный цикл
def main():
    tovary = []

    while True:
        print("\n1 - Добавить, 2 - Показать, 0 - Выход")
        choice = input("Выбор: ")

        if choice == "1":
            p = create_product()
            if p != None:
                tovary.append(p)
                print("Добавлено")

        elif choice == "2":
            if len(tovary) == 0:
                print("Список пуст")
            else:
                for p in tovary:
                    # Полиморфизм: каждый товар по-своему считает итоговую цену
                    print(p.Info())
                    print(f"Итоговая цена: {round(p.FinalPrice(), 2)} руб.")
                    print("-" * 30)

        elif choice == "0":
            break


if __name__ == "__main__":
    main()