# Дополнительное практическое задание по модулю: "Основные операторы".

import random

numbers = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
rand_numbers = random.choice(numbers)
print('Случайное число в левой вставке: ', rand_numbers)

def generate_password(rand_numbers):
    res = ''
    for i in range(1, rand_numbers):
        for j in range(i+1, rand_numbers+1):
            if rand_numbers % (i + j) == 0:
                res += str(i) + str(j)
    return res

result = generate_password(rand_numbers)
print('Пароль:', result)
