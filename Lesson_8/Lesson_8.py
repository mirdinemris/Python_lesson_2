'''
LIGHT:

1. Написать декоратор, замеряющий время выполнение декорируемой функции.

2. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).

PRO

Light +

3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.

4. Сравнить объем оперативной памяти для функции создания генератора и функции создания списка с элементами: натуральные числа от 1 до 1000000.
'''
# 3. Написать декоратор, замеряющий объем оперативной памяти, потребляемый декорируемой функцией.
import psutil

def deco_memory(f,num=None):
    def wrapper(*args):
        f(*args)
        mem = psutil.virtual_memory()
        res=mem.used
        if num == None:
            print('Used memory: ', mem.used)
            return f
        if num is not None:
            return res
    return wrapper()

# 1. Написать декоратор, замеряющий время выполнение декорируемой функции.

def deco_time(f, num=None):
    def wrapper(*args):
        from time import perf_counter
        start = perf_counter()
        f(*args)
        stop = perf_counter()
        res = stop - start
        if num == None:
            print("Used time: ", stop - start)
            return f
        if num is not None:
            return res
    return wrapper()

def deco_time2(f):
    """Как вариант фунуции подсчета затрачиваемого времени"""
    def wrapper(*args):
        if __name__ == '__main__':
            from timeit import Timer
            t = Timer(lambda: f(*args))
            print('Потрачено времени: ', t.timeit(number=1))
        return f
    return wrapper()

@deco_memory
@deco_time
def func():
    print('Декорируемая функция')
print()

# 2. Сравнить время создания генератора и списка с элементами: натуральные числа от 1 до 1000000 (создание объектов оформить в виде функций).

print('Лист')
@deco_memory
@deco_time
# @deco_time2
def list_numb():
    l = [x for x in range(1,1000000)]
    return l
print()

print('Генератор')
@deco_memory
@deco_time
# @deco_time2
def gen_numb():
    g = (x for x in range(1,1000000))
    return g
print()


comp_time = deco_time(list_numb, 1) - deco_time(gen_numb, 1)
if comp_time < 0:
    print('Лист быстрее от на столько: ')
else:
    print('Генератор быстрее от на столько: ')
print(comp_time)



# 4. Сравнить объем оперативной памяти для функции создания генератора и функции создания списка с элементами: натуральные числа от 1 до 1000000.

print()
comp_mem = deco_memory(gen_numb, 1) - deco_memory(list_numb,1)
if comp_mem > 0:
    print('Генератор толще от на столько: ')
else:
    print('Лист толще от на столько: ')
print(comp_mem)

""" 
Вывод:
Если все сделано правильно, то генератор стабильно работает быстрее. А лист как правило занимает больше места, но не всегда. 
"""

