from abc import ABC, abstractmethod

# Базовый класс
class Document(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def Open(self):
        pass

    @abstractmethod
    def Print(self):
        pass


# Текстовый документ
class Text(Document):
    def __init__(self, name, pages):
        super().__init__(name)
        self.pages = pages

    def Open(self):
        return f"Открыт текстовый документ '{self.name}'"

    def Print(self):
        return f"Печать текста '{self.name}' на {self.pages} страницах"


# Изображение
class Image(Document):
    def __init__(self, name, format):
        super().__init__(name)
        self.format = format

    def Open(self):
        return f"Открыто изображение '{self.name}' в формате {self.format}"

    def Print(self):
        return f"Печать изображения '{self.name}' (формат {self.format})"


# PDF документ
class Pdf(Document):
    def __init__(self, name, size):
        super().__init__(name)
        self.size = size

    def Open(self):
        return f"Открыт PDF документ '{self.name}' ({self.size} МБ)"

    def Print(self):
        return f"Печать PDF '{self.name}' ({self.size} МБ)"


# Создание документа
def create_document():
    print("\n1 - Текст, 2 - Изображение, 3 - PDF")
    choice = input("Выбор: ")

    name = input("Название файла: ")

    if choice == "1":
        pages = int(input("Количество страниц: "))
        return Text(name, pages)
    elif choice == "2":
        format = input("Формат (jpg/png): ")
        return Image(name, format)
    elif choice == "3":
        size = float(input("Размер (МБ): "))
        return Pdf(name, size)
    else:
        print("Неверный выбор")
        return None


# Главный цикл
def main():
    documents = []

    while True:
        print("\n1 - Добавить, 2 - Показать, 0 - Выход")
        choice = input("Выбор: ")

        if choice == "1":
            d = create_document()
            if d != None:
                documents.append(d)
                print("Добавлено")

        elif choice == "2":
            if len(documents) == 0:
                print("Список пуст")
            else:
                for d in documents:
                    # Полиморфизм: методы работают по-своему для каждого типа
                    print(d.Open())
                    print(d.Print())
                    print("-" * 30)

        elif choice == "0":
            break


if __name__ == "__main__":
    main()