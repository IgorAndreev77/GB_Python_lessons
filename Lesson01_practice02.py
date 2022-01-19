# Задание 2 - перевод секунд в часы-минуты-секунды
seconds = int(input("Введите количество секунд: "))

minutes = seconds // 60

seconds = seconds % 60

hours = minutes // 60

minutes = minutes % 60

print(f"Часы:минуты:секунды: {hours}:{minutes}:{seconds}")

