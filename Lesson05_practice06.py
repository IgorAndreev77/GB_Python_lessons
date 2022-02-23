# Задание 6

# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
common_dict = {}
with open("Disciplines.txt", encoding='UTF-8') as m_f:
    while True:
        line = m_f.readline()
        l = 0
        discip_dict = {}
        for i in range(1, len(line.split(' '))):
            if line.split(' ')[i].replace('(л)', '').isdigit():
                l += int(line.split(' ')[i].replace('(л)', ''))
            elif line.split(' ')[i].replace('(пр)', '').isdigit():
                l += int(line.split(' ')[i].replace('(пр)', ''))
            elif line.split(' ')[i].replace('(лаб)', '').replace('\n', '').isdigit():
                l += int(line.split(' ')[i].replace('(лаб)', '').replace('\n', ''))
            discip_dict[line.split(' ')[0].replace(':', '')] = l
            common_dict.update(discip_dict)
        if not line:
            break
    print(common_dict)
