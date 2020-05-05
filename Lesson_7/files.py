'''
Работа с текстовыми файлами
'''
# Простой считывание/ открытие файла в режиме чтения
f = open('data')
content = f.read()
print(content)
f.close

f = open('data', 'w')
f.close

# Считывание фала построчно
f = open('data')
for line in f:
    print(line)
f.close

# Менеджер контекста
with open('data') as f:
    for line in f:
        print(line)

# Считывание построчно
with open('data') as f:
    line = f.readline()
    print(line)

# Считывание побайтно
with open('data', 'r') as f:
    data = f.read(10) # считывание одной строки
    print(data, type(data))
# Запись в файл
with open('data_new', 'w') as f:
    f.write('This is new file')

data = ['1\n','2\n','3\n']
with open('data_new', 'w') as f:
    f.writelines(data)
