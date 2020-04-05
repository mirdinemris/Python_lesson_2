import my_mat_modul
print(__name__)
print(my_mat_modul.my_add(3,8))

# {f_n}^2 + {f_{n+1}}^2 = f_{2n+1}

n = 10
print(my_mat_modul.fib_num_l(n)**2 + my_mat_modul.fib_num_l(n+1)**2)
print(my_mat_modul.fib_num_l(2*n+1))

# 1
from packet import math_op

print(math_op.my_add(1,2))
# 2
from packet.math_op import my_add

print(my_add(1,2))

3 Используем __init__.py

from packet import my_add
print(my_add(1,2))
from packet import my_sub
print(my_sub(1,2))
import sys
print(sys.path)
sys.path.append('.....') # Для подтягивания пакетов из других дирректорий
