# Задание 3

# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        full_name = self.name + ' ' + self.surname
        return full_name

    def get_total_income(self):
        total_income = sum(self._income.values())
        return total_income


my_p = Position("John", "Smith", "analyst", {"wage": 2000, "bonus": 1000})

print(my_p.name)
print(my_p.surname)
print(my_p.position)
print(my_p._income) # указано на обращение к защищённому атрибуту
print(f"Полное имя работника: {my_p.get_full_name()}")
print(f"Суммарный доход работника: {my_p.get_total_income()}")

my_p2 = Position("Jane", "Coleman", "project_manager", {"wage": 2500, "bonus": 1500})
print(my_p2.name)
print(my_p2.surname)
print(my_p2.position)
print(my_p2._income) # указано на обращение к защищённому атрибуту
print(f"Полное имя работника: {my_p2.get_full_name()}")
print(f"Суммарный доход работника: {my_p2.get_total_income()}")
