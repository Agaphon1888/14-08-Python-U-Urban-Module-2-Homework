# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
print(f'Введите три любых числа, нажимая клавишу "Ввод" после каждого: ')
first_number, second_number, third_number = input(), input(), input()
if first_number == second_number and first_number == third_number:
    print('3')
elif (first_number == second_number
      or second_number == third_number
      or first_number == third_number):
    print('2')
else:
    print('0')