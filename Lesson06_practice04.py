# Задание 4

# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    speed: int
    color: str
    name: str
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"Автомобиль {self.name}, цвет {self.color}, начал движение.")

    def stop(self):
        print(f"Автомобиль {self.name}, цвет {self.color}, остановился.")

    def turn(self):
        direction: tuple = ("налево", "направо")
        i = int(input("Выберите направление поворота (0 - налево, 1 - направо) : "))
        change_dir = direction[i]
        print(f"Автомобиль {self.name}, цвет {self.color}, повернул {change_dir}")

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name}, цвет {self.color}, составляет {self.speed} км/ч")


class TownCar(Car):
    def __init__(self, speed, color, name, is_police=0):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name}, цвет {self.color}, составляет {self.speed} км/ч")
        if self.speed > 60:
            print("Превышена предельно допустимая скорость движения!")


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=0):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=0):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f"Текущая скорость автомобиля {self.name}, цвет {self.color}, составляет {self.speed} км/ч")
        if self.speed > 40:
            print("Превышена предельно допустимая скорость движения!")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=1):
        super().__init__(speed, color, name, is_police)


my_car = Car(200, "красный", "Toyota", 0)
my_car2 = Car(190, "синий", "Nissan", 0)
my_t_car = TownCar(180, "белый", "Lincoln")
my_s_car = SportCar(220, "чёрный", "Lamborgini")
my_w_car = WorkCar(90, "жёлтый", "Ярославец")
my_p_car = PoliceCar(220, "белый", "Ford")

print(my_p_car.name)
print(my_s_car.color)
print(my_w_car.speed)
print(my_t_car.is_police)

my_car.go()
my_car2.go()
my_car.stop()
my_car2.stop()
my_car.turn()
my_car2.turn()
my_car.show_speed()
my_car2.show_speed()
my_t_car.go()
my_t_car.show_speed()
my_t_car.turn()
my_s_car.go()
my_w_car.show_speed()
