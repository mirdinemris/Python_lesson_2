# Тип данных СЛОВАРИ (dict)

    # Инициализация
dict_temp = {}

print(type(dict_temp), dict_temp)

dict_temp = {'dict1': 1, 'dict2': 2.1, 'dict3': 'name', 'dict4':[1,2,3]}
print(type(dict_temp), dict_temp)

# метод инициализации .fromkeys

dict_temp = dict.fromkeys(['a', 'b'], [12, '2020'])
print(type(dict_temp), dict_temp)

# метод инициализации dict

dict_temp = dict(brend = 'volvo', volume_engine = 1.5)
print(type(dict_temp), dict_temp)

# инициализация с помощью генератора

dict_temp = {a: a**2 for a in range(10)}
print(type(dict_temp), dict_temp)

    # Обращение к содержимому словаря

print(dict_temp[8], dict_temp[9])

    # Функции со словарями
# Кортеж - это неизменяемый list
print(dict_temp.keys())
print(list(dict_temp.keys())) # выводит ключи
print(list(dict_temp.values())) # выводит значение
print(list(dict_temp.items())) # выводит кортеж: ключ-значение

    # Работа с элементами

dict_temp[0] = 100 # изменение знасения существующего ключа
print(type(dict_temp), dict_temp)

dict_temp['name'] = 'Maxik'
print(type(dict_temp), dict_temp) # добавление пары ключ-значение

    # Методы

# keys, values, items см выше

dict_temp.pop('name') # удаляет значение по ключу
print(type(dict_temp), dict_temp)

dict_temp['name'] = 'Maxik'
print(type(dict_temp), dict_temp)

temp = dict_temp.pop('name') # Удаляет и возвращает значение по ключу
print(temp)
print(type(dict_temp), dict_temp)

    # Итерирование по словарю "Run"

for pair in dict_temp.items():
    print(pair)

for key, value in dict_temp.items():
    print(key, value)

for key in dict_temp.keys():
    print(key)

for value in dict_temp.values():
    print(value)

