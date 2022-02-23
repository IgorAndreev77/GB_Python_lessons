# Задание 5

#  Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
#  Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

# f_ile = open("Set of numbers.txt", "w")
# content = input("Введите числа через пробел: ")
# f_ile.write(content)
# f_ile.close()
#
# with open("Set of numbers.txt") as fi_le:
#     li_st = fi_le.readlines()
#     lis_t = (li_st[0].split())
#     l = 0
#     for i in range(len(lis_t)):
#        l += int(lis_t[i])
#        #print(l)
#     print(f"Сумма чисел: {l}")

with open("Set of numbers.txt") as fi_le:
    n = ''
    m = 0
    for i in fi_le.readline():
        if i != ' ':
            n += i
            m = int(n)
        # else:
        #     m += int(n)
            #continue


    #print(n)
        print(m)


