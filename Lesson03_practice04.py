# Задание 4
# застрахуемся от неверного ввода исходных данных:
a = input("Введите положительное вещественное число: ")
if "," in a and a.replace(",", ".", 1).isdigit:
    a = a.replace(",", ".", 1)
while "." not in a or a.replace(".", "", 1).isdigit is False:
    print("Ошибка ввода, повторите ввод")
    a = input("Введите положительное вещественное число: ")
    if "," in a and a.replace(",", ".", 1).isdigit:
        a = a.replace(",", ".", 1)
a = float(a)
b = input("Введите целое отрицательное число: ")
while b.replace('-', '', 1).isdigit() is False or b.startswith('-') is False:
    print("Ошибка ввода, повторите ввод")
    b = input("Введите целое отрицательное число: ")
b = int(b)
# собственно, зададим функцию:

# Вариант 1
def my_func(x, y):
    return x ** y

print(my_func(a, b))

# Вариант 2
def my_func(x, y):
    y = abs(y)
    z = x
    for i in range(y - 1):
        x = x * z
    return 1 / x

print(my_func(a, b))

# Что любопытно: два разных способа вычисления возвращают в консоли два разных по степени точности результата!