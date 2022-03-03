# Задание 1

# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix:
    def __init__(self, matrix_strings: list):
        self.matrixStrings = matrix_strings

    def __str__(self):
        for i in range(len(self.matrixStrings)):
            k = self.matrixStrings[i]
            l = str(k).replace(",", "").replace("[", "").replace("]", "")
            in_file = open("matrix.txt", "a")
            in_file.write(f"{l}\n")
            in_file.close()
            out_file = open("matrix.txt", "r")
            n = out_file.read()
            out_file.close()
        import os
        os.remove("matrix.txt")
        return n

    def __add__(self, other):
        z = []
        for i in range(len(self.matrixStrings)):
            k = self.matrixStrings[i]
            y = []
            for l in range(len(k)):
                x = self.matrixStrings[i][l] + other.matrixStrings[i][l]
                y.insert(l, x)
            z.insert(i, y)
        return Matrix(z)


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])

print(m)
print(m2)
print(m + m2)
