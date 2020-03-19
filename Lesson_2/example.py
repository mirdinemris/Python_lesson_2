                                # Задачи на циклы и оператор условия

'''
Задача 1
Вывести на экран циклом пять строк из нулей,
причем каждая строка должна быть пронумерована.
'''

'''Условие задачи, неоднозначно. Поэтому предлогается два варианта решения.'''

# Вариант №1

print('Задача №1 Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.')
print()
print('Вариант №1')
i = 1                 # Переменная левого столбика нумерации.
a = 0                 # Переменная правого столбика для вывода нулей.

while i < 10:
    print('Строка № ', i, ': ', a, sep='')
    i = i + 1
    if i == 6: break

# Вариант №2

print()
print('Вариант №2')
i = 1
a = str(0)

while i < 10:
    print(i, a*999)
    i = i + 1
    if i == 6: break


'''
Задача 2

Пользователь в цикле вводит 10 цифр.
Найти количество введенных пользователем цифр 5.
'''

'''Удалось реализовать решение при помощи, как функции цикла "while", так и функции "For".'''

# Вариат №1 - это решение подойдет для ситуации когда от пользователя требуется ввести строгое колличество цифр.
import random

print()
print('-' * 125)
print()
print('Задача №2 Пользователь в цикле вводит 10 цифр. Найти количество введенных пользователем цифр 5.')
print('Вариант №1')
print()
а = 0
i = 1
result_sum = 0

print('Введите 10 цифр на свое усмотрение.')
while i < 11:

    '''Возник вопрос:"Возможно ли реализовать данный замысел:
    entered_numb = int(input('Ввод цифры №', i))? Если да, то как?".
    Я нашел что-то по теме:
    https://fooobar.com/questions/12314069/how-can-i-put-two-arguments-in-one-string-for-a-input-function-in-python
    но осуществить мне не удалось.
    '''

    print('Ввод цифры №', i, ': ')
    try:
        entered_numb = int(input())
    except ValueError:
        threat_list = ['Я не устану повтрять: "Вводи цифру!', 'Ану, Води цифру!', 'Будте любезны, ввести цифру!!!', 'Вводи цифру! А то пожалеешь...', 'Я не сдамся пока ты не введешь цифру!']
        threat = random.choice(threat_list)
        print(threat)
        continue
    if entered_numb == 5:
        result_sum = (result_sum + 1)
    i = i + 1

print()
print('Результат:')
if result_sum == 0:
    print("Вы не ввели ни одной цифры 5. =(")
elif result_sum ==1:
    print('Поздравляю! Вы ввели', result_sum, 'цифру пять.')
elif result_sum > 4:
    print ('Поздравляю! Вы ввели', result_sum, 'цифр пять.')
elif result_sum >= 2 or result_sum <= 4:
    print('Поздравляю! Вы ввели', result_sum, 'цифры пять.')

# Вариат №2 - в этом решении у пользователя есть всего 10 попыток для ввода.

print()
print('Вариант №2')
print()
print('У вас есть всего 10 попыток для ввода пятерок!')
result_sum = 0
entered_numb = 0
for i in range(10):
    try:
        entered_numb = int(input('Ввод: '))
    except ValueError:
        print('Пожалуйста, Введите цифру!!!')
    if entered_numb == 5:
     result_sum = (result_sum + 1)

print()
print('Результат:')
if result_sum == 0:
    print("Вы не ввели ни одной цифры 5. =(")
elif result_sum ==1:
    print('Поздравляю! Вы ввели', result_sum, 'цифру пять.')
elif result_sum > 4:
    print ('Поздравляю! Вы ввели', result_sum, 'цифр пять.')
elif result_sum >= 2 or result_sum <= 4:
    print ('Поздравляю! Вы ввели', result_sum, 'цифры пять.')


'''
Задача 3

Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

print()
print('-' * 125)
print()
print('Задача №3 Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.')
print('Предложенный вариант')
sum = 0

for i in range(1,101):
    sum += i
print('Сумма ряда от 1 до 100 Выполненая циклом For', ' = ', sum)
print()
print('Вариант №2')
i = 0
sum = 0

while i < 100:
    i = i + 1
    sum += i
print('Сумма ряда от 1 до 100 Выполненая циклом While', ' = ', sum)



'''
Задача 5

Вывести цифры числа на каждой строчке. (В порядке их расположения)
'''
print()
print('-' * 125)
print()
print('Задача №5 Вывести цифры числа на каждой строчке. (В порядке их расположения)')
print()
str_number = str(input('Введите число: '))

print('Результат в виде текстовых данных, получен при помощи функции reversed.')
for stroks in reversed (str_number):
    print(stroks)
print()


print('Результат в виде - числовых данных, получен при помощи математических опреаторов.')
integer_number = int(str_number)
while integer_number > 0:
    print(integer_number%10)
    integer_number = integer_number//10

another_order = str_number [::-1]
another_order = int(another_order)
print()
print('Результат представлен в обратном порядке, получен при помощи среза.')
while another_order > 0:
    print(another_order%10)
    another_order = another_order//10

'''
Задача 6

Найти сумму цифр числа.
'''
print()
print('-' * 125)
print()
print('Задача №6 Найти сумму цифр числа.')
print()
term1 = 0
term2 = 0
result = 0
results = 0
integer_number = int(input('Введите сумируемое число: '))

while integer_number > 0:
     term1 = integer_number%10
     integer_number = integer_number//10
     term2 = integer_number % 10
     integer_number = integer_number//10
     results = term1 + term2
     result = result + results

print()
print('Результат суммы: ', result)
'''
Задача 7

Найти произведение цифр числа.
'''
print()
print('-' * 125)
print()
print('Задача №7 Найти произведение цифр числа.')
print()
term1 = 0
term2 = 0
result = 1
results = 0
integer_number = int(input('Введите перемножаемое число: '))

while integer_number > 0:
     term1 = integer_number%10
     integer_number = integer_number//10
     if integer_number == 0:
         result = result * term1
         break
     term2 = integer_number % 10
     integer_number = integer_number//10
     results = term1 * term2
     result = result * results

print()
print('Результат произведения: ', result)
'''
Задача №8

Дать ответ на вопрос: есть ли среди цифр числа 5?
'''
print()
print('-' * 125)
print()
print('Задача №8 Дать ответ на вопрос: есть ли среди цифр числа 5?' )
print()
integer_number = 0
integer_number = int(input('Введите число: '))
while integer_number > 0:
    if integer_number%10 == 5:
        print()
        print("Среди числа есть 5'ка!")
        break
    integer_number = integer_number//10
else:
    print()
    print ("Среди числа нет 5'ки.")

'''
Задача 9

Найти максимальную цифру в числе.
'''
print()
print('-' * 125)
print()
print('Задача №9 Найти максимальную цифру в числе.')
print()
result = 0
relation_1 = 0
integer_number = 0
integer_number = int(input('Введите число: '))
while integer_number > 0:
    relation_1 = integer_number%10
    if relation_1 >= result:
        result = relation_1
    integer_number = integer_number//10
print()
print('Цифра ', result, ' Самая большая!')

'''
Задача 10

Найти колличество цифр 5 в числе.
'''
print()
print('-' * 125)
print()
print('Задача №10 Найти колличество цифр 5 в числе.')
print()

sum = 0
integer_number = int(input('Введите число произвольной длинны: '))

while integer_number > 0:
    if integer_number%10 == 5:
        sum = (sum + 1)
    integer_number = integer_number//10

print()
print('Количество пятерок, в вашем числе: ', sum)