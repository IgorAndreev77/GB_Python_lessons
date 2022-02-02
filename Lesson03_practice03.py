# Задание 3

def my_func(el_1, el_2, el_3):
    my_list = [el_1, el_2, el_3]
    x = max(my_list)
    my_list.remove(x)
    y =  max(my_list)
    return x + y
# значения аргументов заданы
print(my_func(1, 3, 4))

# значения аргументов запрошены у пользователя
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

print(f"Сумма двух наибольших чисел: {my_func(a, b, c)}")