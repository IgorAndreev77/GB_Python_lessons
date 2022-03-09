# Задание 3

# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список
# только числами. Класс-исключение должен контролировать типы данных элементов списка.

class Num_list:
    input_list: list
    list_el: str

    def __init__(self):
        self.list_el = ''
        self.input_list = []
        while True:
            try:
                self.list_el = input(
                    'Введите любое целое или вещественное число для добавления в список; чтобы закончить ввод, наберите "stop": ')
                if not self.list_el.startswith('-') and self.list_el.isdigit():
                    self.input_list.append(self.list_el)
                elif self.list_el.startswith('-') and self.list_el.replace('-', '', 1).isdigit():
                    self.input_list.append(self.list_el)
                elif not self.list_el.startswith('-') and self.list_el.replace(',', '', 1).isdigit():
                    self.input_list.append(self.list_el.replace(',', '.'))
                elif self.list_el.startswith('-') and self.list_el.replace('-', '', 1).replace(',', '', 1).isdigit():
                    self.input_list.append(self.list_el.replace(',', '.'))
                elif not self.list_el.startswith('-') and self.list_el.replace('.', '', 1).isdigit():
                    self.input_list.append(self.list_el)
                elif self.list_el.startswith('-') and self.list_el.replace('-', '', 1).replace('.', '', 1).isdigit():
                    self.input_list.append(self.list_el)
                elif self.list_el == 'stop':
                    print(f"Ваш список: {self.input_list}. Ввод закончен.")
                    break
                else:
                    raise Num_exception
            except Num_exception as NE:
                print(NE)


class Num_exception(Exception):
    pass

    def __str__(self):
        return "Ошибка ввода. Вы ввели не число. Будьте внимательны и вводите только числа!"

l = Num_list()
