# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"

a = int(input("Введите любое целое число: "))   # Это чтобы два раза не вставать - можно не только 15, но и любое
                                                # другое число ввести

numbers = [i for i in range(1, a + 1)]

primes = []
not_primes = []

for num in numbers[1::]:    # Перебор начинаем сразу со второго элемента списка, чтобы исключить "1".
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

print("Primes: ", primes)
print("Not Primes: ", not_primes)
