# Задание 4

my_str = input("Введите несколько слов через пробелы: ")

my_list = my_str.split()

number = 0
while my_list != []:
    word = my_list.pop(0)
    number += 1
    print(f"{number} {word :.10s}")
