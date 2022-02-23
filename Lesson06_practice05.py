# Задание 5

# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title: str

    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Отрисовка, инструмент - ручка {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Отрисовка, инструмент - карандаш {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Отрисовка, инструмент - маркер {self.title}")


p = Pen("Brauberg")
p.draw()

pc = Pencil("Ko-Hi-Noor")
pc.draw()

h = Handle("Pentel")
h.draw()
