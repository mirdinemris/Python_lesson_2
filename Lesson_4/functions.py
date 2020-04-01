def add(x, y):
    '''
    :param x: ....
    :param y: ....
    :return:
    '''
    return x + y

help(add)

print(add(100,101))
print(add('Maksik', "Polly"))

def f1(n):
    n = n+1
    print(n)
    def f2(m):
        return m + n
    return f2
new_f = f1(100)
print(new_f)
new_f = f1(100)
print(new_f(250))

def f():
    pass

print(f())

# Аргументы функций
def add(x, y, z = 10):
    '''
    :param x: ....
    :param y: ....
    :return:
    '''
    return x + y + z

print(add(1,2))
print(add(1,2,3))

def function(*args):
    print(type(args), args)
    return args
function(1,2,3,'Volvo')

def func(**kwargs):
    print(type(kwargs), kwargs)
    return kwargs

func(a = 1, b = 2, c = 'Volvo', d = 1.5)


def func_difficult(x, y = 2, *args, **kwargs):
    print(type(x), x)
    print(type(y), y)
    print(type(args), args)
    print(type(kwargs), kwargs)
    return kwargs

func_difficult(1,3,(1,2,3), temp = 12, temp_1 = 13)

        # Lambda функции

function = lambda x, y: x + y




