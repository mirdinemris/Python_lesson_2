# Тип данных СТРОКА (str)------------------------
#------------------------------------------
    # Инициализация
temp_str = 'Марка авто \\ Volvo \\'
#temp_str = ""
print(temp_str)

     # Обращения к символам, подстрокам

# Вывод строки посимвольно
for i in range(len(temp_str)):
    print(temp_str[i])

# Срезы
print(temp_str[1:])
print(temp_str[:4])

print(temp_str[1:4])
print(temp_str[1:-3])

     # Функции со строкаи
print(temp_str, len(temp_str))

     # Операции со строками
temp_str_2 = 'Mercedes'
print(temp_str + temp_str_2)
print(temp_str_2*2)

     # Форматирование строк

brend = 'Volvo'
price = 1.5
car = 'Марка: {} цена: {}'.format(brend, price)
print(car)

car = f'Марка: {brend} цена: {price}'
print(car)
     # Методы
print('SPLIT')
print(temp_str.split())

cars ='volvo,Audi,Lada'
print(cars.split())
print(cars.split(','))

# Методы форматирования строк
print(cars.upper())
print(cars.title())
print(cars.lower())

# Замена подстроки в строке

email_adress = 'eMail: _mail_'
email = 'my_email@gmail.com'
print(email_adress.replace('_mail_',email))