# Задание 2
# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.


with open("Strings_count_and_words_count.txt") as my_verse:
    my_list = my_verse.readlines()

    print(f"В файле {len(my_list)} строк(и)")
    for i in my_list:
        print("В строке '", i.replace('\n', ''), "' -", len(i.split(' ')), "слов(а)")
