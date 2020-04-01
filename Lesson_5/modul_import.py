import os               # импорт всего модуля

print(os.getcwd())

from os import mkdir    # импрот отдельных функций

mkdir('test')

from os import rmdir as remover

remover('test')

from os import *        # импорт модуля целиком


print(getcwd())

print(list(walk(getcwd())))