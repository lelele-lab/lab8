from abc import ABC, abstractmethod

# Базовый класс
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def Area(self):
        pass

    @abstractmethod
    def Perimeter(self):
        pass


# Круг
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Круг")
        self.radius = radius

    def Area(self):
        return 3.14 * self.radius * self.radius

    def Perimeter(self):
        return 2 * 3.14 * self.radius


# Прямоугольник
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("Прямоугольник")
        self.width = width
        self.height = height

    def Area(self):
        return self.width * self.height

    def Perimeter(self):
        return 2 * (self.width + self.height)


# Треугольник
class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("Треугольник")
        self.a = a
        self.b = b
        self.c = c

    def Perimeter(self):
        return self.a + self.b + self.c

    def Area(self):
        # Формула Герона
        p = self.Perimeter() / 2
        return round((p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5, 2)


# Создание фигуры
def create_shape():
    print("\n1 - Круг, 2 - Прямоугольник, 3 - Треугольник")
    choice = input("Выбор: ")

    if choice == "1":
        r = float(input("Радиус: "))
        return Circle(r)
    elif choice == "2":
        w = float(input("Ширина: "))
        h = float(input("Высота: "))
        return Rectangle(w, h)
    elif choice == "3":
        a = float(input("Сторона a: "))
        b = float(input("Сторона b: "))
        c = float(input("Сторона c: "))
        return Triangle(a, b, c)
    else:
        print("Неверный выбор")
        return None


# Главный цикл
def main():
    figury = []

    while True:
        print("\n1 - Добавить, 2 - Показать, 0 - Выход")
        choice = input("Выбор: ")

        if choice == "1":
            f = create_shape()
            if f != None:
                figury.append(f)
                print("Добавлено")

        elif choice == "2":
            if len(figury) == 0:
                print("Пусто")
            else:
                for f in figury:
                    # Полиморфизм: методы работают по-разному для разных фигур
                    print(f"{f.name}: площадь = {f.Area()}, периметр = {f.Perimeter()}")

        elif choice == "0":
            break


if __name__ == "__main__":
    main()