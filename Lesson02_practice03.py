# Задание 3
# 1) Вариант решения c помощью списков

year_list = [0, 'зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
month = int(input("Введите номер месяца - целое число от 1 до 12: "))
season = year_list.pop(month)
print("Месяц с этим номером приходится на время года", season)
# на всякий случай вернём элемент в список
year_list.insert(month, season)

# 2) Вариант решения с помощью словарей

year_dict = {
    1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень', 10: 'осень',
    11: 'осень', 12: 'зима'}
month = int(input("Введите номер месяца - целое число от 1 до 12: "))
season = year_dict.get(month)
print("Месяц с этим номером приходится на время года", season)