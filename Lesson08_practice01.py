# Задание 1

#  Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
#  В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
#  и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
#  месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.

class Date:
    date: str
    def __init__(self, d: str):
        self.date = d

    @classmethod
    def str_to_num(cls, d: str):
        cls.date = d
        l = cls.date.split('-')
        day = int(l[0])
        month = int(l[1])
        year = int(l[2])
        return day, month, year

    @staticmethod
    def is_valid(d: str):
        l = d.split('-')
        if int(l[0]) > 31 or int(l[0]) == 0:
            return "Число не может быть больше 31 или равно 0"
        elif int(l[1]) > 12 or int(l[1]) == 0:
            return "Месяц не может быть больше 12 или равен 0"
        elif int(l[1]) == 2 and int(l[0]) > 29:
            return "В феврале может быть только 28 или 29 дней"
        else:
            return "Дата валидна"


date1 = Date("01-13-1977")
date2 = Date("29-02-2000")

print(Date.str_to_num("01-02-1977"))
print(date1.str_to_num("01-02-1977"))
print(date1.is_valid("01-02-1977"))
print(Date.is_valid("32-02-2000"))
print(date2.is_valid("32-02-2000"))