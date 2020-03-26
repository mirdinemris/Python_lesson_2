# Тип данных Кортеж (Tuple)

    # Инициализация
temp_list = [1,2,3]       # создание из листа
temp_tuple = tuple(temp_list)    # для редактирования кортежа его конвертируют в лист
print(type(temp_tuple), temp_tuple)
print()

temp_tuple = (1,2,3)    # создание с нуля
print(type(temp_tuple), temp_tuple)

    # Обращение к элементам кортежа

print(temp_tuple[0])
print()
for i in range(len(temp_tuple)):
    print(temp_tuple[i])

# temp_tuple[0] = 100 # в кортежах присваивание не доступно

''' Как в list'''
    # Функции с кортежами
    # Операции с кортежами
    # Методы

temp_list = [1,2,3]
temp_tuple = (1,2,3,)
print()
print(temp_list.__sizeof__())
print(temp_tuple.__sizeof__())