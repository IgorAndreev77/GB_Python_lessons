# Задание 6
# Первая часть задания

def int_func(a):
    x = a[0]
    y = x.upper()
    z = a[1:]
    return y + z


l_w = input("Введите любое слово строчными латинскими буквами: ")

print(int_func(l_w))


# Вторая часть задания - вариант 1


def int_func(a):
    x = a[0]
    y = x.upper()
    z = a[1:]
    return y + z


l_w = input("Введите строчными латинскими буквами несколько слов через пробел: ")
while l_w.endswith(' ') == True:  # пробел в конце строки приводит к ошибке, избавимся от него
    l_w = l_w[0:-1]
l = l_w.split(' ')
m = ''
for i in l:
    n = int_func(i)
    m = m + n + ' '
m = m[0:-1]
print(m)


# Вторая часть задания - вариант 2


def int_func(a):
    x = a[0]
    y = x.upper()
    z = a[1:]
    return y + z


l_w = input("Введите строчными латинскими буквами несколько слов через пробел: ")
if l_w.endswith(' ') == False: # в этом варианте, наоборот, нам нужен пробел в конце строки; добавим его
    l_w = l_w + ' '
p = ''
l = l_w
for i in range(1, (l_w.count(' ') + 1)):
    n = l[0:l.index(' ')]
    m = l[(l.index(' ') + 1):]
    o = int_func(n)
    l = m
    p = p + o + ' '
p = p[0:-1]
print(p)

# решение задания c помощью встроенной функции

def int_func(s):
    return s.title()


l_w = input("Введите любое слово или несколько слов строчными латинскими буквами: ")

print(int_func(l_w))
