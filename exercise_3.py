# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:21:20 2022

@author: Leshk
"""

import os
import shutil
import sys
import json
with open ('file_3.txt','r', encoding='utf-8') as f:
    print(f.read())
with  open ('file_3.txt', 'r', encoding='utf-8' ) as f:  
    print('Сотрудники с доходом более 20000') 
    i = 0
    income = []
    for line in f:
        st = line.replace('\n','')
        sp = st.split()
        income.append(float(sp[1]))
        if float(sp[1])>20000.00:
            print(f'{sp[0]}')    
        i+=1
    res = sum(income) / i
    print (f"Средний доход на сотрудника - {res}")
         