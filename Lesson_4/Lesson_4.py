"""
LIGHT:

1. Напишите функцию (F):
на вход список имен и целое число N;
на выходе список длины N случайных имен из первого списка
(могут повторяться, можно взять значения: количество имен 20,
N = 100, рекомендуется использовать функцию random);

2. Напишите функцию вывода самого частого
имени из списка на выходе функции F;

3. Напишите функцию вывода самой редкой буквы,
с которого начинаются имена в списке на выходе функции F.

PRO:

LIGHT +

4.  В файле с логами найти дату самого позднего лога
(по метке времени): https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8
"""

# №1

def f (l, N=357):
    import random
    # while len(l) < N:                 # Данное решение изменяет исходный список, добавляя случайный имена
    #         name = random.choice(l)
    #         l.append(name)
    # return l
    new_list_name = []
    i = 0                               # Данный вариант создает новый список из случайных имен (что все же, ближе к условию задачи)
    for i in range(N):
        if len(l) < N:
            name = random.choice(l)
            new_list_name.append(name)
    print('\n\tВыход по заданию №1:', '\n', new_list_name, '\n', 'Колличество имен(N): ', len(new_list_name))

# Задание №2 вариант 1 (использованы наработки из прошлых д\з)
    def f2(new_list_name):
        set_word = set(new_list_name)
        dict_word = {x: new_list_name.count(x) for x in set_word}
        list_d = list(dict_word.items())
        list_d.sort(key=lambda i: i[1], reverse=True)
        return print('\n\tЗадание №2.', '\nСамое частое имя из списка на выходе','\n', list_d[0])  # list_d[0][0] - для вывода только слова

    # Вариант 2 (по материалу текущего вебинара, выглядит более оптимально).
    # Как проверить какой из вариантов оптимальней?
    def f2_2 (new_list_name):
        from functools import reduce
        often_name = reduce(lambda x, y: x if new_list_name.count(x) > new_list_name.count(y) else y, new_list_name)
        return print('Тот же результат, при помощи reduce:', '\n', often_name)

# Задание №3 вариант 1 (соответственно)
    def f3(new_list_name):
        x = 0
        list_syl = []
        for i in range(len(new_list_name)):
            syl = new_list_name[x][0]
            list_syl.append(syl)
            x += 1
        set_syl = set(list_syl)
        dict_syl = {x: list_syl.count(x) for x in set_syl}
        list_s = list(dict_syl.items())
        list_s.sort(key=lambda i: i[1])
        return print('\n\tЗадание №3.', '\nСамя редкая буква с которой начинаются слова из списка на выходе','\n',list_s[0]) # list_s[0][0] - для вывода только буквы

    # вариант 2 (соответственно)
    # Вопрос соответственный?
    def f3_2(new_list_name):
        from functools import reduce
        character = list(map(lambda x: x[0], new_list_name))
        rarely_сhar = reduce(lambda x, y: x if character.count(x) < character.count(y) else y, character)
        return print('Тот же результат при помощи функций map и reduce:','\n',rarely_сhar)
    return new_list_name, f2(new_list_name), f2_2(new_list_name), f3(new_list_name), f3_2(new_list_name)

list_names =  ['Алиса', 'Анна', 'Алиса', 'Амелия', 'Адель',
'Александра', 'Александр', 'Антон', 'Андрей', 'Бьянка', 'Берта',
'Белла', 'Борис', 'Билл', 'Бруно', 'Бен', 'София', 'Сара', 'Сабина',
'Сандра', 'Александра', 'Сэнди', 'Селена', 'Стелла', 'Степан', 'Стефан',
'Самуил', 'Сэм', 'Симон', 'Саймон', 'Тара', 'Тея', 'Таисия', 'Тая',
'Тайлер', 'Тим', 'Ума', 'Фрейя', 'Флора', 'Флоренция', 'Фиона', 'Филипп',
'Фил', 'Фридрих', 'Эвелина', 'Эмма', 'Эмма', 'Эмили', 'Эдуард', 'Эрик', 'Юлия', 'Джулия']

f(list_names)
print()

import time
import pandas as pd
'''
Так я первый раз пытался загрузить табличку в data frame.))) 
'''
# log = open('log', 'rt', encoding='UTF-8')
    # dict_log = {}
    # data = []
    # for line in log:
    #     if len(dict_log) == 0:
    #         data = list(line.split(' - '))
    #         dict_log = dict(zip(['date', 'example', 'inf', 'coment'], [[(data[0])], [data[1]], [data[2]], [data[3]]]))
    #     else:
    #         data = list(line.split(' - '))
    #         dict_log['date'].append(data[0]), dict_log['example'].append(data[1]), dict_log['inf'].append(data[2]), dict_log[
    #             'coment'].append(data[3])
    # print(dict_log)
    # df = pd.DataFrame.from_dict(dict_log)
    # print(df)
'''
Так я пытался оптимизировать первый вариант.))) 
'''
# with open('log') as log:
#     log = log.read()
#     log = log.split('\n')
#     dict_log = {}
#     dict_log = dict(zip(['date', 'example', 'inf', 'coment'], [[line.split(' - ')[0] for line in log],
#                                                                [line.split(' - ')[1] for line in log],
#                                                                [line.split(' - ')[2] for line in log],
#                                                                [line.split(' - ')[3] for line in log]]))
# print(dict_log)
# df = pd.DataFrame.from_dict(dict_log)
# print(df.sort_values('date',  ascending=False).head(1))
'''
Все оказалось кудв проще!
'''
data = pd.read_csv("log", sep=' - ', names=['date', 'example', 'inf', 'coment'], engine = 'python')
print('\tЗадание №4','\nСамый простой вариант вывода:', '\n',data.sort_values('date',  ascending=False).head(1))
# print(data)


''' 
Черновики
'''
# from datetime import datetime
# for i in range(len(data['date'])):
#     data.loc[i, 'date'] = datetime.strptime(data.loc[i, 'date'], '%Y-%m-%d %H:%M:%S,%f')
#     # print('\t',data.loc[i, 'date'])
#     # print(type(data.loc[i, 'date']))

# def Dt (x):
#     from datetime import datetime
#     now = datetime.now()
#     delta = now - x
#     d = delta.days
#     return d
#
# # now = datetime.now()
# # delta = now - data.loc[0, 'date']
# # print(delta.days)
# # print(type(delta.days))
# # from functools import reduce
#
# # day = Dt(List_date[0])
# # day2 = Dt(List_date[7])
# # print(type(List_date[1]))
#
# # print(type(day))
# # print(day2)
# # print(List_date)
# # last_date = reduce(lambda x, y: x if Dt(List_date[x]) < Dt(List_date[y]) else y, List_date)

