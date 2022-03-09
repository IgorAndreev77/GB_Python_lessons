# Задание 4-6

# . Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для указания количества принтеров,
# отправленных на склад, нельзя использовать строковый тип данных.


class Store:
    remains: dict = {'printers': 0, 'scanners': 0, 'copiers': 0}
    free_space: float

    def __init__(self, f_s: float, p: int = 0, s: int = 0, c: int = 0):
        self.remains = {'printers': p, 'scanners': s, 'copiers': c}
        self.free_space = f_s

    def in_store(self, item_class: str, a, num: int):
        if item_class == 'printer':
            if isinstance(num, int):
                if self.free_space >= (a.ind_pack_vol * num):
                    self.remains['printers'] += num
                    print(
                        f"На складе прибавилось {num} шт. принтеров. Всего товаров на складе: принтеров {self.remains['printers']} шт., сканеров {self.remains['scanners']} шт., копиров {self.remains['copiers']} шт.")
                    self.free_space = self.free_space - (a.ind_pack_vol * num)
                    print(
                        f"На складе свободно {self.free_space} куб.м., свободное место уменьшилось на {a.ind_pack_vol * num} куб.м.")
                else:
                    raise OverLoadException
            else:
                raise NonDigitException
        elif item_class == 'scanner':
            if isinstance(num, int):
                if self.free_space >= (a.ind_pack_vol * num):
                    self.remains['scanners'] += num
                    print(
                        f"На складе прибавилось {num} шт. сканеров. Всего товаров на складе: принтеров {self.remains['printers']} шт., сканеров {self.remains['scanners']} шт., копиров {self.remains['copiers']} шт.")
                    self.free_space = self.free_space - (a.ind_pack_vol * num)
                    print(
                        f"На складе свободно {self.free_space} куб.м., свободное место уменьшилось на {a.ind_pack_vol * num :.2f} куб.м.")
                else:
                    raise OverLoadException
            else:
                raise NonDigitException
        elif item_class == 'copier':
            if isinstance(num, int):
                if self.free_space >= (a.ind_pack_vol * num):
                    self.remains['copiers'] += num
                    print(
                        f"На складе прибавилось {num} шт. копиров. Всего товаров на складе: принтеров {self.remains['printers']} шт., сканеров {self.remains['scanners']} шт., копиров {self.remains['copiers']} шт.")
                    self.free_space = self.free_space - (a.ind_pack_vol * num)
                    print(
                        f"На складе свободно {self.free_space} куб.м., свободное место уменьшилось на {a.ind_pack_vol * num :.2f} куб.м.")
                else:
                    raise OverLoadException
            else:
                raise NonDigitException
        else:
            raise ClassItemException

    def out_store(self, item_class, a, num):
        if item_class == 'printer':
            if isinstance(num, int):
                if self.remains['printers'] >= num:
                    self.remains['printers'] -= num
                    print(
                        f"На складе стало на {num} шт. меньше принтеров. Всего товаров на складе: принтеров {self.remains['printers']} шт., сканеров {self.remains['scanners']} шт., копиров {self.remains['copiers']} шт.")
                    self.free_space = self.free_space + (a.ind_pack_vol * num)
                    print(
                        f"На складе свободно {self.free_space} куб.м., свободное место увеличилось на {a.ind_pack_vol * num :.2f} куб.м.")
                else:
                    raise NotEnoughItemsException
            else:
                raise NonDigitException
        elif item_class == 'scanner':
            if isinstance(num, int):
                if self.remains['scanners'] >= num:
                    self.remains['scanners'] -= num
                    print(
                        f"На складе стало на {num} шт. меньше сканеров. Всего товаров на складе: принтеров {self.remains['printers']} шт., сканеров {self.remains['scanners']} шт., копиров {self.remains['copiers']} шт.")
                    self.free_space = self.free_space + (a.ind_pack_vol * num)
                    print(
                        f"На складе свободно {self.free_space} куб.м., свободное место увеличилось на {a.ind_pack_vol * num :.2f} куб.м.")
                else:
                    raise NotEnoughItemsException
            else:
                raise NonDigitException
        elif item_class == 'copier':
            if isinstance(num, int):
                if self.remains['copiers'] >= num:
                    self.remains['copiers'] -= num
                    print(
                        f"На складе стало на {num} шт. меньше копиров. Всего товаров на складе: принтеров {self.remains['printers']} шт., сканеров {self.remains['scanners']} шт., копиров {self.remains['copiers']} шт.")
                    self.free_space = self.free_space + (a.ind_pack_vol * num)
                    print(
                        f"На складе свободно {self.free_space} куб.м., свободное место увеличилось на {a.ind_pack_vol * num :.2f} куб.м.")
                else:
                    raise NotEnoughItemsException
            else:
                raise NonDigitException
        else:
            raise ClassItemException


class Office_equipment:
    ind_pack_lines: dict = {'lenght': 0, 'width': 0, 'height': 0}
    ind_pack_vol: float

    def __init__(self, x, y, z):
        self.ind_pack_lines = {'lenght': x, 'width': y, 'height': z}
        self.ind_pack_vol = self.ind_pack_lines['lenght'] * self.ind_pack_lines['width'] * self.ind_pack_lines['height']


class Printer(Office_equipment):
    type: tuple = ('matrix', 'jet', 'laser')

    def __init__(self, i, x, y, z):
        super().__init__(x, y, z)
        self.type = Printer.type[i]


class Scanner(Office_equipment):
    max_resolution: int

    def __init__(self, m_r, x, y, z):
        super().__init__(x, y, z)
        self.max_resolution = m_r


class Copier(Office_equipment):
    copies_per_min: int
    total_resourse: int

    def __init__(self, c_p_m, t_r, x, y, z):
        super().__init__(x, y, z)
        self.copies_per_min = c_p_m
        self.total_resourse = t_r


class ClassItemException(Exception):
    pass

    def __str__(self):
        return "Неверно выбран тип оргтехники!"


class NonDigitException(Exception):
    pass

    def __str__(self):
        return "При указании количества перемещаемой оргтехники введено не число!"


class OverLoadException(Exception):
    pass

    def __str__(self):
        return "Невозможно переместить на склад такое количество оргтехники, недостаточно свободного места!"


class NotEnoughItemsException(Exception):
    pass

    def __str__(self):
        return "Невозможно переместить со склада такое количество оргтехники, недостаточно единиц на остатках!"


s1 = Store(950, 1, 2, 3)

p1 = Printer(0, 0.2, 0.3, 0.4)
sc1 = Scanner(300, 0.3, 0.2, 0.7)
c1 = Copier(40, 15000, 0.7, 0.8, 0.9)

s1.in_store('printer', p1, 20)
s1.in_store('scanner', sc1, 30)
s1.in_store('copier', c1, 15)

s1.out_store('copier', c1, 10)
s1.out_store('printer', p1, 5)
s1.out_store('scanner', sc1, 15)
