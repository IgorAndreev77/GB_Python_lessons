# Задание 1

# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

while True:

    content = input(
        "Введите текст строки для записи в файл. Чтобы закончить запись в файл, нажмите Enter, не вводя текст: ")

    my_file = open("Strings.txt", "a")
    my_file.write(f"{content}\n")
    my_file.close()
    if not content:
        break

# my_file = open("Strings.txt")
# print(my_file.read())
# my_file.close()
