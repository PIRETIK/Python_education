# -*- coding: utf-8 -*-
"""
Created on Tue May  3 03:42:07 2022

@author: Leshk
"""

# Домашнее задание к четвертому уроку.

# ---------------------------- Задание первое ---------------------------------

from sys import argv
name_script,a,b,c = argv 
print('Имя скрипта',name_script)
print('Выработка в часах: ',a)
print('Ставка в час: ',b)
print('Премия: ',c)
print('ИТОГО: ',(int(a) * int(b)) + int(c) )
# Через консоль Spider не смог запустить.
# Через комендную строку Wind все работало.
# ---------------------------- Задание второе ---------------------------------

from random import randint 
list_1 = [ randint(5, 250) for x in  range(20) ]
print(list_1)
list_2 = [list_1[i] for i in  range(len(list_1)) if list_1[i-1]<list_1[i]]
print(list_2)

# ---------------------------- Задание третье ---------------------------------

my_list = [ x for x in range(20,240) if x%20==0 or x%21==0 ]
print(my_list)

# ---------------------------- Задание четвертое ---------------------------------

from random import randint 
my_list = [ randint(0,100) for x in  range(30)   ]
print(my_list)
# в новый список добавляем только те элементы количесво
# вхождений которых равно 1

new_list = [x for x in my_list if my_list.count(x) == 1]
print(new_list)

# ---------------------------- Задание пятое -----------------------------------
from functools import reduce
my_list = [ x for x in range(100,1001,2)]
result = reduce(lambda x,y: x * y, my_list)
print (result)

# ---------------------------- Задание шестое ---------------------------------

from itertools import count
for x in count(3):
    if x > 10:
        break
    else:
        print(x)
        
from itertools import cycle
i = 0
for x in cycle("BLABLA"):
    if i > 20:
        break
    print(f"{i} - {x}")
    i += 1       

# ---------------------------- Задание седьмое ---------------------------------
