# Задание 2

#  Реализовать проект расчета суммарного расхода ткани на производство одежды.
#  Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
#  К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
#  размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def matter_count(self):
        pass


class Coat(Clothes):
    def __init__(self, size: int):
        self.size = size
    @property
    def matter_count(self):
        c = f"{(self.size / 6.5) + .5 :.2f}"
        return c

    def __add__(self, other):
        if isinstance(other, Coat):
            return f"На пошив двух изделий ушло {(((self.size / 6.5) + .5) + ((other.size / 6.5) + .5)):.2f} кв.м.ткани"

    def __mul__(self, other):
        if isinstance(other, int):
            return f"На пошив {other} изделий ушло {(((self.size / 6.5) + .5) * other):.2f} кв.м. ткани"


class Suit(Clothes):
    def __init__(self, height: int):
        self.height = height
    @property
    def matter_count(self):
        c = f"{(self.height * 2) + .3 :.2f}"
        return c

    def __add__(self, other):
        if isinstance(other, Suit):
            return f"На пошив двух изделий ушло {(((self.height * 2) + .3) + ((other.height * 2) + .3)):.2f} кв.м. ткани"

    def __mul__(self, other):
        if isinstance(other, int):
            return f"На пошив {other} изделий ушло {(((self.height * 2) + .3) * other):.2f} кв.м. ткани"


coat1 = Coat(10)
coat2 = Coat(11)
coat3 = Coat(20)
suit1 = Suit(10)

print(coat1.matter_count)
print(coat2.matter_count)
print(suit1.matter_count)
print(coat1 + coat2)
print(suit1 * 2)
print(coat2 * 10)

