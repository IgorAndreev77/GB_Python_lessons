# Задание 5

# Вариант 1 читерский
rating = [15, 12, 7, 3, 3, 1]
mark = int(input("Введите натуральное число: "))
rating.append(mark)
rating.sort(reverse=True)
# rating.reverse()
print(rating)

# Вариант 2 честный
rating = [15, 12, 7, 3, 3, 1]
mark = int(input("Введите натуральное число: "))
l = 0
m = 0
idx_list = []
for i in rating:
    if mark <= i:
        l = rating.index(i)
        m = rating.count(i)
rating.insert(l + m, mark)
print("Рейтинг:", rating)
