# Задание 5

user_input = []
total_sum = 0
while True:
    user_input = input(
        'Вводите целые и вещественные числа, разделяя их пробелом. Для суммирования чисел нажмите Enter, для прекращения работы введите "!" >> ')
    l = user_input.split(' ')


    def sum_func():
        sum = 0
        while l != []:
            m = l.pop(0)
            if m.replace('-', '', 1).isdigit() == True:
                m = int(m)
            elif m.replace(',', '', 1).isdigit() == True or m.startswith('-') == True:
                m = float(m.replace(',', '.', 1))
            elif m.replace('.', '', 1).isdigit() == True or m.startswith('-') == True:
                m = float(m)
            elif '!' in m:
                print(
                    'Вы запросили прекращение работы. Введённые перед символом "!" числа будут добавлены к сумме введённых чисел.')
                break
            else:
                print(
                    'Внимание: в строке ввода содержатся не только числа. Избегайте ввода лишних пробелов. Корректно введённые числа будут добавлены к сумме введённых чисел.')
                continue
            sum = sum + m
        return sum


    total_sum = total_sum + sum_func()
    print("Сумма введённых чисел:", total_sum)
