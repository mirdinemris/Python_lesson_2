'''
В файле содержится текст. Считать/скопировать текст из файла и выполнить следующую последовательность действий:
LIGHT:
1) методами строк очистить текст от знаков препинания;
2) сформировать list со словами (split);
3) привести все слова к нижнему регистру (map);
4) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
5) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).

PRO:
6) выполнить light с условием: в пункте 3 дополнительно к приведению к нижнему регистру выполнить лемматизацию.
Подробнее о процедуре лемматизации:
https://pymorphy2.readthedocs.io/en/0.2/user/index.html
'''
file = open('text.txt', 'r+')
file = file.read()

    # Задание №1
'''Вариант №1 Первый что пришел в голову как концепт.
Но к сожалению своего ума для четкой его реализации не хватило.
Пришлось обращаться к примеру решения задачи:
https://pythoner.name/text-to-words
из перевода к документации к Python.
И адаптировать его к своей задаче.'''
wordlist = file.split()
punctuation = ['.', ',', ':', ';', '!', '?', '(', ')', '«', '»',]
a = 0

for a in range(4):                        # Цикл необходимо повторять,
    i = 0                                 # так как в тексте встречаются
    for word in wordlist:                 # такие варианты: '«(' , '!»'.
        if word[-1] in punctuation:
            wordlist[i] = word[:-1]
            word = wordlist[i]
        if word[0] in punctuation:
            wordlist[i] = word[1:]
        i += 1
i = 0                                     # Так же способ не избавляется
while i < len(wordlist):                  # от знака —
    if wordlist[i] == ('—'):              # Цикл while для его удаления.
        wordlist.remove('—')
    i += 1


'''Вариант №2.
Был подсмотрен в учебнике Марка Лутца, на стр. 141:
https://codernet.ru/books/python/izuchaem_python_5-e_izd_tom_1_mark_lutc/
Кажется что он гораздо изящнее!'''
import re

wordlist_sec = re.split(r'\W', file)            # Способ этот - похоже очень не простой!

for x in range(len(wordlist_sec)):              # До конца не очень представляю как он работает
    i = 0                                       # Но похоже что после него остается много
    while i < len(wordlist_sec):                # пробельных символов (типо таких: \n, \t)
        if wordlist_sec[i] == (''):             # Цикл while в цикле for для их удаления.
            wordlist_sec.remove('')
        i += 1

    # Задание №2 - лист формируется в обоих вариантах выполнения задания № 1


    # Задание №3 - все к нижнему регистру
wordlist = list(map(str.lower, wordlist))
wordlist_sec = list(map(str.lower, wordlist_sec))

print()
difference = list(set(wordlist_sec) - set(wordlist))
result = list(set(wordlist) - set(wordlist_sec))
print('Слова с удаленным дефисом из варианта №2')           # решил сравнить качество
print(difference)                                           # процедур удаления знаков пунктуации
print()                                                     # не смторя на то что в русском языке
print('Слова паразиты из варианта №1')                      # слова с частицами через дефис, это норма
print(result)                                               # успешным считаю вариант №2. Так как в нем
print()                                                     # появились: француженка с гувернанткой

    # Задание №6
import pymorphy2                               # импортируем модуль анализа текста
morph = pymorphy2.MorphAnalyzer()

morph_list = [morph.parse(x)[0] for x in wordlist_sec]
                        # Парсим текст????
a = 0
lemma = []                                     # вынимаем лемму в list
for x in morph_list:
    lemma.append(morph_list[a].normal_form)
    a += 1
print('Словоформы приведенные к леммам:')
print()
i = 0                                          # выводим результат на экран
while i < len(lemma):                          # по 8 слов в строке, для удобства чтения.
    print(lemma[i], end=' ')
    i += 1
    if i % 8 == 0:
        print()
# wordlist = lemma


    # Задание №4 - получить словарь

set_word = set(wordlist)                       # получаем множество уникальных ключей из списка
set_word_sec = set(wordlist_sec)
dict_word = {x: wordlist.count(x) for x in set_word}
'''
Посредством спискового включения, создаем словарь, где:
'x:' - ключ
'wordlist.count(x)' - значение ключа, полученное  с помощью метода str.count из списка wordlist
'for x in set_word' - условие выполнения, для всех слов из множества set_word
'''
# for key, value in dict_word.items():
#     print(key, ':', value, sep='')


    # Задание №5 вывести 5 наиболее часто встречающихся слов (sort),
    # вывести количество разных слов в тексте (set).

# list_values = list(dict_word.values())                   # Пытался мыслить в этом ключе
# list_values.sort(reverse=True)
# for value in list_values:
#     print(value)

print()
print('Пять наиболее часто втречающихся слов, это:')
print()
list_keys = sorted(set_word, key=dict_word.__getitem__, reverse=True)
for i in list_keys[0:5]:
        print(i)
'''
Пример сортировки взят из документации
https://docs.python.org/3/howto/sorting.html#sortinghowto
Не понимаю как оно работает(((
'''

# вывести количество разных слов в тексте
# можно так
amount = 0
for i in set_word:
    amount += 1
print()
print('Колличество уникальных слов в тексте(Вариант1): ', amount)
# но так короче)
print()
print('Колличество уникальных слов в тексте(Вариант2): ', len(set_word_sec))







