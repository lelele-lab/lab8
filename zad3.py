from abc import ABC, abstractmethod

# Базовый класс
class Employee(ABC):
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    @abstractmethod
    def Info(self):
        pass

    @abstractmethod
    def CalculateSalary(self):
        pass


# Менеджер (оклад + бонус за проект)
class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def Info(self):
        return f"Менеджер: {self.name}, оклад: {self.base_salary} руб."

    def CalculateSalary(self):
        return self.base_salary + self.bonus


# Разработчик (оклад + оплата за час переработки)
class Developer(Employee):
    def __init__(self, name, base_salary, hours, rate):
        super().__init__(name, base_salary)
        self.hours = hours
        self.rate = rate

    def Info(self):
        return f"Разработчик: {self.name}, оклад: {self.base_salary} руб., переработка: {self.hours} ч."

    def CalculateSalary(self):
        return self.base_salary + (self.hours * self.rate)


# Дизайнер (оклад + процент от выполненных заказов)
class Designer(Employee):
    def __init__(self, name, base_salary, orders, percent):
        super().__init__(name, base_salary)
        self.orders = orders
        self.percent = percent

    def Info(self):
        return f"Дизайнер: {self.name}, оклад: {self.base_salary} руб., заказов на сумму: {self.orders} руб."

    def CalculateSalary(self):
        return self.base_salary + (self.orders * self.percent / 100)


# Создание сотрудника
def create_employee():
    print("\n1 - Менеджер, 2 - Разработчик, 3 - Дизайнер")
    choice = input("Выбор: ")

    name = input("Имя: ")
    base_salary = float(input("Оклад: "))

    if choice == "1":
        bonus = float(input("Бонус за проект: "))
        return Manager(name, base_salary, bonus)
    elif choice == "2":
        hours = int(input("Часы переработки: "))
        rate = float(input("Ставка за час: "))
        return Developer(name, base_salary, hours, rate)
    elif choice == "3":
        orders = float(input("Сумма заказов: "))
        percent = float(input("Процент от заказов (%): "))
        return Designer(name, base_salary, orders, percent)
    else:
        print("Неверный выбор")
        return None


# Главный цикл
def main():
    sotrudniki = []

    while True:
        print("\n1 - Добавить, 2 - Показать ЗП, 0 - Выход")
        choice = input("Выбор: ")

        if choice == "1":
            e = create_employee()
            if e != None:
                sotrudniki.append(e)
                print("Добавлено")

        elif choice == "2":
            if len(sotrudniki) == 0:
                print("Список пуст")
            else:
                for e in sotrudniki:
                    # Полиморфизм: каждый считает свою зарплату
                    print(e.Info())
                    print(f"Итоговая зарплата: {round(e.CalculateSalary(), 2)} руб.")
                    print("-" * 30)

        elif choice == "0":
            break


if __name__ == "__main__":
    main()