# Задание 2

# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Division:
    dividend: float
    divider: float

    def __init__(self, a, b):
        self.dividend = a
        self.divider = b

    def div_action(self):
        if self.divider != 0:
            return f"Результат деления с точностью до 4 знаков после запятой - {self.dividend / self.divider :.4f}"
        else:
            raise ZerDivExcept


class ZerDivExcept(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return f"Вы ввели в качестве делителя нуль, на нуль делить нельзя!"


d = Division(float(input("Введите делимое: ")), float(input("Введите делитель: ")))

try:
    print(d.div_action())
except ZerDivExcept as ZDE:
    print(ZDE)
