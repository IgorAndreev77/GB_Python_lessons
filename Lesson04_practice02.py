# Задание 2
# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

original_list = [12, 34, 45, 122, 9, 34, 17, 202]


def create_new_list(a):
    for i in range(len(a) - 1):
        if a[i] < a[i + 1]:
            yield a[i + 1]


modified_list = list(create_new_list(original_list))
print(modified_list)
