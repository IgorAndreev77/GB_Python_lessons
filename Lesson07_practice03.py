# Задание 3

# Реализовать программу работы с органическими клетками, состоящими из ячеек.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (add()), вычитание (sub()), умножение (mul()), деление (truediv()).
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение,
# умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

# Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек
# двух клеток больше нуля, иначе выводить соответствующее сообщение.

# Умножение. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.

# Деление. Создается общая клетка из двух.
# Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам. Метод должен возвращать строку вида
# *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.

# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cellula:
    def __init__(self, cell: int):
        self.cell = cell

    def __add__(self, other):
        if isinstance(other, Cellula):
            return self.cell + other.cell

    def __sub__(self, other):
        if isinstance(other, Cellula):
            if self.cell > other.cell:
                return self.cell - other.cell

    def __mul__(self, other):
        if isinstance(other, Cellula):
            return self.cell * other.cell

    def __truediv__(self, other):
        if isinstance(other, Cellula):
            return self.cell // other.cell

    def make_order(self, cells_in_row: int):
        self.cells_in_row = cells_in_row
        d = []
        total = self.cell
        row = self.cells_in_row
        counter = total
        if counter > row:
            for f in range(total // row):
                s = ''
                for i in range(row):
                    s += '*'
                    counter -= 1
                d.append(s)
        s = ''
        for k in range(total % row):
            s += '*'
        d.append(s)
        y = r'\n'.join(d)
        if y.endswith(r'\n'):
            y = y[:-2]
        return y

c1 = Cellula(5)
c2 = Cellula(5)
c12 = c1 + c2
print(c12)
c3 = Cellula(7)
c4 = Cellula(6)
c34 = c3 - c4
print(c34)
c5 = Cellula(2)
c6 = Cellula(4)
c56 = c5 * c6
print(c56)
c7 = Cellula(7)
c8 = Cellula(2)
c78 = c7 / c8
print(c78)
c9 = Cellula(12)
print(c9.make_order(5))
c10 = Cellula(23)
print(c10.make_order(6))
c11 = Cellula(15)
print(c11.make_order(5))
