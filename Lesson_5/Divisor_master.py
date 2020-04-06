'''
Необходимо реализовать модуль divisor_master.
Все функции модуля принимают на вход натуральные числа от 1 до 1000. Модуль содержит функции:

1) проверка числа на простоту
(простые числа - это те числа у которых делители единица и они сами);

2) выводит список всех делителей числа;

3) выводит самый большой простой делитель числа.

PRO:

LIGHT +

4) функция выводит каноническое разложение числа
(https://zaochnik.com/spravochnik/matematika/delimost/razlozhenie-chisel-na-prostye-mnozhiteli/)
на простые множители;

5)функция выводит самый большой делитель (не обязательно простой) числа.
'''


"""Создание кортежа от 2 до 1000 """
a = 1
num_list = []
for i in range(1, 1000):
    a += 1
    num_list.append(a)
num_list = tuple(num_list)

''' Просеиваем список 'Решетом Эратосфена', получаем кортеж простых чисел от 2 до 1000'''

simple_nums = list(num_list)
p = simple_nums[0]
while p < simple_nums[-1]:
    for i in simple_nums:
        if i % p == 0 and i / p != 1.0:
            simple_nums.remove(i)
        # print(p)
    p += 1
simple_nums = tuple(simple_nums)

'''
Проверяем результат - со списком простых чисел с сайта https://math.wikia.org
Для работы функции этот раздел не принципиален. В принципе, можно было обойтись
копированием этого списка.
Вероятно это было бы более оптимально. Но это не так интересно!
'''


# set_list = str('''2 3 5 7 11 13 17 19 23 29
#
# 31 37 41 43 47 53 59 61 67 71
#
# 73 79 83 89 97 101 103 107 109 113
#
# 127 131 137 139 149 151 157 163 167 173
#
# 179 181 191 193 197 199 211 223 227 229
#
# 233 239 241 251 257 263 269 271 277 281
#
# 283 293 307 311 313 317 331 337 347 349
#
# 353 359 367 373 379 383 389 397 401 409
#
# 419 421 431 433 439 443 449 457 461 463
#
# 467 479 487 491 499 503 509 521 523 541
#
# 547 557 563 569 571 577 587 593 599 601
#
# 607 613 617 619 631 641 643 647 653 659
#
# 661 673 677 683 691 701 709 719 727 733
#
# 739 743 751 757 761 769 773 787 797 809
#
# 811 821 823 827 829 839 853 857 859 863
#
# 877 881 883 887 907 911 919 929 937 941
#
# 947 953 967 971 977 983 991 997''')
#
# set_list = set_list.replace('\n\n', ' ')
# set_list = set_list.split(' ')
# set_list = list(filter(lambda x: x != ('') , set_list))
# # print(set_list)
# set_list = list(map(lambda x: int(x), set_list))
# print(set_list)
# print(len(set_list))
# print(simple_nums)
# print(len(simple_nums))
# difference = list(set(set_list) - set(simple_nums))
# print(difference)

# Задача №1

def check_simple(natural_num):
    '''Функция принимает число от 0 до 1000, и проверяет простое ли оно'''

    if natural_num > 1000 or natural_num < 0:
        return False, print('\nЭто вне предела моих возможностей')
    elif natural_num in simple_nums:
        return True, print('\nЧисло', natural_num, 'является простым.')
    elif natural_num == 0:
        return False, print(natural_num, 'от лат. nullus — никакой.')
    elif natural_num == 1:
        return False, print('\nДревние греки даже не считали числом это:', natural_num, '!')
    else:
        return False, print('\nЧисло', natural_num, 'является составным.')

# Задача №2

def divider_list (natural_num):
    '''Функция находит все делители числа от 1 до 1000'''
    if natural_num == 0:
        return False, print(natural_num, 'от лат. nullus — никакой.')
    div_list = [1]
    n = 0
    for i in num_list:
        if natural_num % num_list[n] == 0:
            div_list.append(num_list[n])
        n += 1
    return div_list, print('\nДелителями числа ', natural_num, ' являются:', '\n',div_list, sep='')

# Задача №3

def big_simple_div(natural_num):
    """Функция принимает натуральное число от 1 до 1000
    и находит самый большой простой делитель числа"""
    if natural_num == 0:
        return False, print(natural_num, 'от лат. nullus — никакой.')
    div_list = []
    n = 0
    for i in num_list:
        if natural_num % num_list[n] == 0:
            div_list.append(num_list[n])
        n += 1

    div_list = list(filter(lambda x: x in simple_nums, div_list))
    div_list.insert(1,1)
    div_list = list(sorted(div_list, reverse=True))
    if div_list == [1]:
        return div_list[0], print('\nДелитель числа -', natural_num, 'это:', '\n', div_list[0])
    else:
        return div_list[0], print('\nCамый большой простой делитель числа -', natural_num, 'это:', '\n', div_list[0])

# Задача №4

multiplies = []
def multi_canon (natural_num):
    """функция прнимает натуральное число и выводит его каноническое разложение на простые множители."""
    if natural_num == 0:
        return False, print(natural_num, 'от лат. nullus — никакой.')
    if natural_num == 1:
        return False, print('\nКаноническое разложение числа на множители:', '\n', natural_num, 'Нераскладывается.')
    """Получаем список простых множителей """
    def multi (natural_num):
        natural_num = int(natural_num)
        if natural_num in simple_nums:
            multiplies.append(natural_num)
            return multiplies
        else:
            for i in range(len(simple_nums)):
                if natural_num % simple_nums[i] == 0:
                    m = natural_num / simple_nums[i]
                    sm = simple_nums[i]
                    multiplies.append(sm)
                    multi(m)
                    break

    """ Из него получаем, список содержащий в себе списки из пары: ['множитель', 'его степень'] """

    multi(natural_num)
    from collections import Counter
    result = dict(Counter(multiplies))
    result = list(result.items())
    result = list(map(lambda x: list(x), result))
    x = 0
    """ Делаем степени степенями """
    for i in range(len(result)):            # Возможно ли как то оптимизировать этот код?
        if result[x][1] == 1:
            result[x][1] = ('')
        elif result[x][1] == 2:
            result[x][1] = '²'
        elif result[x][1] == 3:
             result[x][1] = '³'
        elif result[x][1] == 4:
            result[x][1] = '⁴'
        elif result[x][1] == 5:
             result[x][1] = '⁵'
        elif result[x][1] == 6:
             result[x][1] = '⁶'
        elif result[x][1] == 7:
             result[x][1] = '⁷'
        elif result[x][1] == 8:
             result[x][1] = '⁸'
        elif result[x][1] == 9:
             result[x][1] = '⁹'
        x += 1

    """ Маленькая функция для красоты результата"""
    def printer (result):

        y = 0
        for i in result:
           print (result[y][0], result[y][1], sep='', end=  ' * ', file=file)
           y +=1
        return file.write
        # print(result)

    file = open('result.txt', 'w+', encoding='utf-8')
    printer(result)
    file.close()
    file = open('result.txt', 'r+', encoding='utf-8')
    res = str(file.readlines())
    return print('\nКаноническое разложение числа на множители:', '\n',natural_num, '=', res[2:-5])


# Задача №5
def big_divider (natural_num):
    '''Самый большой делитель числа'''
    if natural_num == 0:
        return False, print(natural_num, 'от лат. nullus — никакой.')
    return print('\nСамый большой делитель числа ', natural_num, ' это:', natural_num)

num = int(input('Вводи от 0 до 1000: '))
# num = 89792

check_simple(num)
divider_list(num)
big_simple_div(num)
multi_canon(num)
big_divider(num)

