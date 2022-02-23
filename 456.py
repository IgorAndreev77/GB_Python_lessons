# Задание 7

# Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки. # Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
out_list = []
sum_profit = 0
firm_dict = {}
avg_dict = {}
with open("Business.txt", encoding='UTF-8') as file:
    while True:
        str = file.readline()
        if str != '':
            str1 = str.split()
            profit = int(str1[2]) - int(str1[3])
            firm_dict[str1[0]] = profit
            if profit > 0:
                sum_profit += profit
            avg_profit = sum_profit / len(firm_dict)
            avg_dict['average_profit'] = avg_profit
        if not str:
            break
    out_list.append(firm_dict)
    out_list.append(avg_dict)
    print(out_list)
import json
# выгрузим в json
with open("Business.json", "w", encoding='UTF-8') as out_file:
    json.dump(out_list, out_file)
# загрузим из Json
with open("Business.json", "r", encoding='UTF-8') as new_file:
    new_list = json.load(new_file)
    print(new_list)