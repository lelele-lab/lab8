from abc import ABC, abstractmethod

# Интерфейс 1: движение
class IMovable(ABC):
    @abstractmethod
    def Move(self, dx, dy):
        pass


# Интерфейс 2: отрисовка
class IDrawable(ABC):
    @abstractmethod
    def Draw(self):
        pass


# Интерфейс 3: изменение размера
class IResizable(ABC):
    @abstractmethod
    def Resize(self, factor):
        pass


# Класс, который реализует все три интерфейса
class GameSprite(IMovable, IDrawable, IResizable):
    def __init__(self, name, x, y, size):
        self.name = name
        self.x = x
        self.y = y
        self.size = size

    def Move(self, dx, dy):
        self.x += dx
        self.y += dy
        print(f"{self.name} перемещён в ({self.x}, {self.y})")

    def Draw(self):
        print(f"Рисуем {self.name} размером {self.size} в точке ({self.x}, {self.y})")

    def Resize(self, factor):
        self.size = self.size * factor
        print(f"{self.name} изменён в размере. Новый размер: {self.size}")


# Второй класс, который реализует только два интерфейса (например, фон)
class Background(IDrawable, IResizable):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def Draw(self):
        print(f"Рисуем фон {self.name} размером {self.size}")

    def Resize(self, factor):
        self.size = self.size * factor
        print(f"Фон {self.name} растянут. Новый размер: {self.size}")


# Демонстрация работы
def main():
    print("--- Создаём спрайт (умеет всё) ---")
    sprite = GameSprite("Герой", 10, 20, 50)
    
    sprite.Draw()
    sprite.Move(5, -10)
    sprite.Resize(1.5)
    
    print("\n--- Создаём фон (умеет только рисоваться и менять размер) ---")
    bg = Background("Лес", 1920)
    
    bg.Draw()
    bg.Resize(0.5)
    
    # Демонстрация интерфейсов через проверку типов
    print("\n--- Проверка поддержки интерфейсов ---")
    print("Спрайт поддерживает IMovable:", isinstance(sprite, IMovable))
    print("Спрайт поддерживает IDrawable:", isinstance(sprite, IDrawable))
    print("Спрайт поддерживает IResizable:", isinstance(sprite, IResizable))
    
    print("Фон поддерживает IMovable:", isinstance(bg, IMovable))
    print("Фон поддерживает IDrawable:", isinstance(bg, IDrawable))
    print("Фон поддерживает IResizable:", isinstance(bg, IResizable))


if __name__ == "__main__":
    main()