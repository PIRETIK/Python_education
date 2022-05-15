# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:22:53 2022

@author: Leshk
"""

import os
import shutil
import sys
import json
import os

with  open ('file_7.txt', 'r', encoding='utf-8' ) as f:  
    # список выручка
    list_profit = []
    # словарь выручка
    dict_profit = {}
    dict_loss = {}
    for line in f:
        st = line.replace('\n','')
        sp = st.split()
           # создаем переменную выручка.
        profit = int(sp[2])-int(sp[3])
        if profit > 0:
            list_profit.append(profit)
        else:
            dict_loss [sp[0]] = profit
        average_profit = sum(list_profit) / len(list_profit)
        print(f'{sp[0]} выручка: {profit}')
        dict_profit [sp[0]] = profit
        dict_average_profit = {"Средняя выручка":  average_profit}
print (f'Средняя выручка - {average_profit}') 
# записываем результаты в новый файл
with  open ('file_7.1.json', 'a', encoding='utf-8' ) as f_1: 
    # print(dict_profit,dict_loss,dict_average_profit,  file = f_1)
    # Два варианта заполнения либо все сразу, либо построчно
    print(dict_profit,  file = f_1)
    print(dict_loss,  file = f_1)
    print(dict_average_profit,  file = f_1)








       