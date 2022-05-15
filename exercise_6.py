# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:22:45 2022

@author: Leshk
"""
import os
import shutil
import sys
import json
import os

my_dict = {}
with open ('file_6.txt','r', encoding='utf-8') as f:
    for line in f:
        st = line.replace('\n','')
        sp = st.split()
        s = []
        num = ''
        for char in st:
            if char.isdigit():
                num = num + char
            else:
                if num != '':
                        s.append(int(num))
                        num = ''
                        if num != '':
                            s.append(int(num))                
        my_dict[sp[0][:-1]] = sum(s)
print(my_dict)  
        
        
        
        
        
        