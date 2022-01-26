# Задание 2
# Получим элементы списка путём запроса ввода от пользователя

q = int(input("Введите количество элементов в списке: "))
first_list = []
for x in range(q):
    element = input("Введите несколько любых чисел или наборов символов: ")
    second_list = [element]
    first_list = first_list + second_list
print("Ваш список:", first_list)

# поменяем местами все парные элементы списка:
indx = 0
for x in range(q // 2):
    n = first_list.pop(indx)
    first_list.insert(indx + 1, n)
    indx += 2
print("Ваш список после перемены мест парных элементов:", first_list)
