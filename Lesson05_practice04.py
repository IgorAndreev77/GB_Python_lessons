# Задание 4

# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
#
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
#
rus_num_dict = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
rus_list = {}
with open('Numbers.txt') as my_file:
    for k in rus_num_dict.keys():
        my_str = my_file.readline()
        my_str_new = my_str.replace('\n', '')
        my_list = my_str_new.split(' - ')
        eng_num_dict = {int(my_list[1]): (my_list[0])}
        eng_num_dict[k] = rus_num_dict.get(k)
        out_str = str(eng_num_dict[k]) + ' - ' + str(k)
        new_file = open('Rus_numbers.txt', 'a', encoding='UTF-8')
        new_file.writelines(f"{out_str}\n")
        new_file.close()