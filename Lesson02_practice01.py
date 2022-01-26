# Задание 1

# создадим списки:
first_list = [1, 1.2, 'any_text', None, True]
second_list = [-2, 22.22, 'another_text', False]

first_list.insert(1, complex(1, 2)) # добавим элемент на указанную позицию первого списка
print(first_list)

second_list.append(bin(7)) # добавим элемент в конец второго списка
print(second_list)

common_list = first_list.copy() # создадим копию первого списка
print(common_list)

second_list.reverse() # реверсируем второй список
print(second_list)

common_list.extend(second_list) # присоединим второй список к копии первого
print(common_list)

# проверим типы элементов полученного списка

for element in common_list:
    print(f"Тип элемента { {element} } - {type(element)}")
message = "Проверка типов завершена для всех элементов выбранного списка!"
print(message.upper())
