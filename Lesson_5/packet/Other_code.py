# Необходимо реализовать модуль divisor_master. Все функции модуля принимают на вход натуральные числа от 1 до 1000.
# Модуль содержит функции:
# 1) проверка числа на простоту (простые числа - это те числа у которых делители единица и они сами);
import random
def PrimeNumber(number):
   divisor = 2
   while number % divisor!= 0:
       divisor += 1
   return divisor == number
sequence_num = list( range(1, 1001))
x=random.choice(sequence_num)
print("число для анализа:", x)
print("проверка числа на простоту:", PrimeNumber(x))

# 2) выводит список всех делителей числа;
from itertools import chain
divs = lambda n: chain(*((d, n // d) for d in range(1, int(n ** 0.5) + 1) if n % d == 0))
print("список всех делителей числа:", list(divs(x)))

# 3) выводит самый большой простой делитель числа;
def PrimeDiv(r, n=2):
    while n <= r:
        if r % n:
            n += 1
        else:
            r //= n
            yield n
print("наибольший простой делитель числа:", max(PrimeDiv(x)))

# 4) функция выводит каноническое разложение числа на простые множители;
def factors(num, d=2):
    while num > 1:
        n1, n2 = divmod(num, d)
        if n2:
            d += 1
        else:
            yield d
            num = n1
n = int(input("укажите число для анализа: "))
print('{} = {}' .format(n, ' * '.join(map(str, factors(n)))))

# 5) функция выводит самый большой делитель (не обязательно простой) числа.
from functools import reduce
def max_div(x):
    max_number = divs(x)
    max_number = reduce(lambda a,b: a if a>b else b, max_number)
    return(max_number)
print("наибольший делитель числа:", max_div(x))