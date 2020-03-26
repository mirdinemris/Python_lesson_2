# Тип данных - список (List)

  # Инициализация (генераторы)
list_temp = [] # Пустой список
print(type(list_temp))
list_temp = [1.2, 123, 'Volvo', [1,2,3,]]
for el in list_temp:
    print(el, type(el))

    # инициализация с помощью команды - list
list_str = list('Volvo')
print(list_str)

    # Обращение к элементам списка, подсписки

for i in range(len(list_temp)):
    print(i, ':', list_temp[i])
for i in range(len(list_temp)):
    print(i, ':', list_temp[i:])
for i in range(len(list_temp)):
    print(i, ':', list_temp[:i])

    # Функции со списками

print(len(list_temp))

    # Опреции со списками

print(list_temp + list_str)
print(list_temp*2)

    # Методы
# append - для добавления в конец
integer_list = []
for i in range(5):
    integer_list.append(i)
print(integer_list)
integer_list.append(100)
print(integer_list)

# remove - метод удаления элемента из списка
integer_list.remove(3) # удаляет первый встретившийся элемент
print(integer_list)
del integer_list[1] # удаляет по индексу
print(integer_list)
# reverse
integer_list.reverse()
print(integer_list)
# sort
integer_list = [1, 4,2, 8, 6, 98, 2]
integer_list.sort()
print(integer_list)
# insert
integer_list.insert(2, 100) # (индекс, значение)
print(integer_list)

    # Обработка списков (map, filter, reduce)

# map - функция применяемая к каждому элементу списка
integer_list = [9,2,4,5,8,7]
# map(function, list) -----> map ------> list(map)
new_integer_list = list(map(lambda x: x**2, integer_list))
print(new_integer_list)
new_integer_list = list(map(str, new_integer_list))
print(new_integer_list)

# filter - фильтрация списка согласно некоторому условию
integer_list = [9,2,4,5,8,7]
new_integer_list = list(filter(lambda x: x<5, integer_list))
print(new_integer_list)

# reduce - применяется ко всем элементам списка возвращая им один определенный элемент
from functools import reduce

integer_list = [1,2,3,4]

sum = reduce(lambda x,y: x+y, integer_list)
product = reduce(lambda x,y: x*y, integer_list)
print(sum, product)
