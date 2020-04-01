# 1. Функция lambda может содержать только выражения и не может включать опреаторы в свое тело
# 2. Она пишется как одна строка
# 3. Не поддерживает аннотацию типов
# 4. Может быть немедленно вызвана
# 5. Не может содержать утверждения. Не может содержать опреаторы return, pass, asert, erase

def ident(x):
    return x

print(ident(10))

print( (lambda x: x)(10) )

ident_lambda = lambda x: x
print(ident_lambda(10))

car = lambda brend, engine_volume, price: f'Car: {brend.title()}, Engine_volume: {engine_volume}, Price: {price}'
print(car('Volvo', 1.5, 130000000))

print(type(ident_lambda), type(ident))

