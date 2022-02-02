# Задание 1

first_var = int(input("Введите делимое: "))
second_var = int(input("Введите делитель: "))

def div_func(a, b):
    try:
        return a / b
    except:
        ZeroDivisionError
        print("На нуль делить нельзя!")

print("Результат деления: ", div_func(first_var, second_var))

