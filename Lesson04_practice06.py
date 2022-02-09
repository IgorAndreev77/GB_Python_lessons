# Задание 6
# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

# а)
from itertools import count

for i in count(3, 3):
    if i <= 20:
        print(i)
    else:
        break

# б)
from itertools import cycle

x = 0
a = ['Ученье - свет,', 'а неученье -', 'тьма!', ]
for i in cycle(a):
    if x == 12:
        break
    else:
        print(i)
        x +=1
