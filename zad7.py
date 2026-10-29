from abc import ABC, abstractmethod

# Базовый класс
class Institution(ABC):
    def __init__(self, name, students):
        self.name = name
        self.students = students

    @abstractmethod
    def Info(self):
        pass

    @abstractmethod
    def Degree(self):
        pass


# Школа
class School(Institution):
    def __init__(self, name, students, grades):
        super().__init__(name, students)
        self.grades = grades

    def Info(self):
        return f"Школа: {self.name}, учеников: {self.students}, классы: {self.grades}"

    def Degree(self):
        return "Аттестат об основном общем образовании"


# Колледж
class College(Institution):
    def __init__(self, name, students, specialty):
        super().__init__(name, students)
        self.specialty = specialty

    def Info(self):
        return f"Колледж: {self.name}, студентов: {self.students}, специальность: {self.specialty}"

    def Degree(self):
        return "Диплом о среднем профессиональном образовании"


# Университет
class University(Institution):
    def __init__(self, name, students, faculties):
        super().__init__(name, students)
        self.faculties = faculties

    def Info(self):
        return f"Университет: {self.name}, студентов: {self.students}, факультетов: {self.faculties}"

    def Degree(self):
        return "Диплом о высшем образовании (бакалавр/магистр)"


# Создание учреждения
def create_institution():
    print("\n1 - Школа, 2 - Колледж, 3 - Университет")
    choice = input("Выбор: ")

    name = input("Название: ")
    students = int(input("Количество обучающихся: "))

    if choice == "1":
        grades = input("Классы (например, 1-11): ")
        return School(name, students, grades)
    elif choice == "2":
        specialty = input("Специальность: ")
        return College(name, students, specialty)
    elif choice == "3":
        faculties = int(input("Количество факультетов: "))
        return University(name, students, faculties)
    else:
        print("Неверный выбор")
        return None


# Главный цикл
def main():
    institutions = []

    while True:
        print("\n1 - Добавить, 2 - Показать, 0 - Выход")
        choice = input("Выбор: ")

        if choice == "1":
            inst = create_institution()
            if inst != None:
                institutions.append(inst)
                print("Добавлено")

        elif choice == "2":
            if len(institutions) == 0:
                print("Список пуст")
            else:
                for inst in institutions:
                    # Полиморфизм: методы работают по-своему для каждого типа
                    print(inst.Info())
                    print(f"Выдаёт: {inst.Degree()}")
                    print("-" * 30)

        elif choice == "0":
            break


if __name__ == "__main__":
    main()