# map (отображение) на вход подается функция и список
# к каждому элементу списка, применяет функцию которая подается в качестве аргумента.
def miles_to_km(miles):
    return miles*1.6
mile_dist = [1.0, 1.6, 2.3]

km_dist = list(map(miles_to_km, mile_dist))
print(type(km_dist), km_dist)

km_dist = list(map(lambda x: 1.6*x, mile_dist))
print(type(km_dist), km_dist)

list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = list(map(lambda x,y: x*y, list_1, list_2))

print(list_3)

# reduce - она производит какуюто операцию со всеми элементами в списке.
# например найти среднее арифметическое.
from functools import reduce # начиная с Python3.x import

list_temp = [43,12,41,100,101,4]
max = reduce(lambda a,b: a if a>b  else b, list_temp)
print(max)

# filter - выбор элемента из списка удовлетворяющего неторому требованию
list_temp = [43,12,41,100,101,4]
list_50 = list(filter(lambda x: x > 50 , list_temp))
print(list_50)
list_1 = list(filter(lambda x: x %10== 1 , list_temp))
print(list_1)

# sorted - сортировка, в обратном порядке, в прямом, сортировка по ключам.
list_temp_sort = sorted(list_temp)
print(list_temp_sort)

list_temp_sort_reverse = sorted(list_temp, reverse=True)
print(list_temp_sort_reverse)

#  сортировка по ключам
list_names = ['Kate', 'Dima', 'Ivan', 'Mike']
list_names_sort = sorted(list_names)
print(list_names_sort)

list_names_sort_key = sorted(list_names, key = lambda x: x[3])
print(list_names_sort_key)