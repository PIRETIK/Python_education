# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:21:40 2022

@author: Leshk
"""
import os
import shutil
import sys
import json

with open ('file_5.txt','w') as f:
    f.write(input("Введите числа через пробел: "))

with open ('file_5.txt','r') as f:
    s = f.read()
a = s.split()
b = [int(x) for x in a]
c = sum(b)
print(f'Сумма всех чисел равна {c}')