# Задание 7

#  Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
#  методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
#  и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.

from cmath import sqrt


class Complex_num:
    a: float
    b: float
    c: float

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = a + (b * sqrt(-1))

    def __str__(self):
        return f"({self.a}+{self.b}j)"

    def __add__(self, other):
        return (self.a + other.a) + ((self.b + other.b) * sqrt(-1))

    def __mul__(self, other):
        return (self.a * other.a - self.b * other.b) + ((self.a * other.b + other.a * self.b) * sqrt(-1))


c1 = Complex_num(2, 4)
print(c1)
c2 = Complex_num(1, -3)
print(c1 + c2)

c3 = Complex_num(1, 3)
c4 = Complex_num(2, -2)
print(c3 * c4)
