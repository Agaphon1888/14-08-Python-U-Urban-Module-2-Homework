# Домашняя работа по уроку "Стиль кода часть II. Цикл While."
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
item = 0
while item < len(my_list):
    if my_list[item] < 0:
        break
    if my_list[item] > 0:
        print(my_list[item])
    item = item + 1
