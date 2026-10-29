from abc import ABC, abstractmethod

# Базовый класс
class Account(ABC):
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @abstractmethod
    def Info(self):
        pass

    @abstractmethod
    def Accrue(self):
        pass


# Сберегательный счёт (начисляется процент на остаток)
class Savings(Account):
    def __init__(self, owner, balance, percent):
        super().__init__(owner, balance)
        self.percent = percent

    def Info(self):
        return f"Сберегательный счёт: {self.owner}, баланс: {self.balance} руб., ставка: {self.percent}%"

    def Accrue(self):
        # Начисляем процент и добавляем к балансу
        bonus = self.balance * self.percent / 100
        self.balance += bonus
        print(f"Начислено {bonus} руб. Новый баланс: {self.balance} руб.")


# Кредитный счёт (начисляются проценты по кредиту, баланс уходит в минус)
class Credit(Account):
    def __init__(self, owner, balance, percent):
        super().__init__(owner, balance)
        self.percent = percent

    def Info(self):
        return f"Кредитный счёт: {self.owner}, долг: {abs(self.balance)} руб., ставка: {self.percent}%"

    def Accrue(self):
        # Увеличиваем долг на процент
        debt = self.balance * self.percent / 100
        self.balance += debt
        print(f"Начислены проценты {debt} руб. Текущий долг: {abs(self.balance)} руб.")


# Зарплатный счёт (начисляется фиксированный кэшбэк)
class Salary(Account):
    def __init__(self, owner, balance, cashback):
        super().__init__(owner, balance)
        self.cashback = cashback

    def Info(self):
        return f"Зарплатный счёт: {self.owner}, баланс: {self.balance} руб., кэшбэк: {self.cashback} руб."

    def Accrue(self):
        # Начисляем фиксированный кэшбэк
        self.balance += self.cashback
        print(f"Начислен кэшбэк {self.cashback} руб. Новый баланс: {self.balance} руб.")


# Создание счёта
def create_account():
    print("\n1 - Сберегательный, 2 - Кредитный, 3 - Зарплатный")
    choice = input("Выбор: ")

    owner = input("Владелец счёта: ")
    balance = float(input("Начальный баланс (для кредита можно ввести с минусом): "))

    if choice == "1":
        percent = float(input("Процентная ставка (%): "))
        return Savings(owner, balance, percent)
    elif choice == "2":
        percent = float(input("Процент по кредиту (%): "))
        return Credit(owner, balance, percent)
    elif choice == "3":
        cashback = float(input("Сумма кэшбэка (руб.): "))
        return Salary(owner, balance, cashback)
    else:
        print("Неверный выбор")
        return None


# Главный цикл
def main():
    accounts = []

    while True:
        print("\n1 - Добавить счёт, 2 - Показать счета, 3 - Начислить по всем, 0 - Выход")
        choice = input("Выбор: ")

        if choice == "1":
            acc = create_account()
            if acc != None:
                accounts.append(acc)
                print("Счёт добавлен")

        elif choice == "2":
            if len(accounts) == 0:
                print("Список пуст")
            else:
                for acc in accounts:
                    print(acc.Info())
                    print("-" * 30)

        elif choice == "3":
            if len(accounts) == 0:
                print("Список пуст")
            else:
                for acc in accounts:
                    # Полиморфизм: у каждого счёта своя логика начисления
                    acc.Accrue()

        elif choice == "0":
            break


if __name__ == "__main__":
    main()