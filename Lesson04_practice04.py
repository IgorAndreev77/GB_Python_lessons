# Задание 4
# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке.
# Для выполнения задания обязательно использовать генератор.

# Вариант 1

orig_list = [7, 4, 6, 5, 5, 12, 90, 123, 90]
new_list = [x for x in orig_list if orig_list.count(x) == 1]
print(new_list)

# Вариант 2

orig_list = [7, 4, 6, 5, 5, 12, 90, 123, 90]
orig_dict = {i: orig_list.count(i) for i in orig_list}
new_list = [i for i in orig_dict.keys() if orig_dict.get(i) == 1]
print(new_list)