# Задание 3

# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open("Workers_and_incomes.txt", encoding='UTF-8') as my_file:
    my_list = my_file.readlines()

    my_dict = {}
    for i in my_list:
        k = i.replace('\n', '')
        l = k.split(' ')
        my_dict[l[0]] = int(l[1])
    print("Следующие сотрудники:")
    for i in my_dict:
        if my_dict.get(i) < 20000:
            print(i)
    print("имеют оклад ниже 20 000.")
    avg = []
    for i in my_dict:
        avg.append(my_dict.get(i))
    print(f"Средний оклад сотрудников: {sum(avg) / len(avg) :.2f}")
