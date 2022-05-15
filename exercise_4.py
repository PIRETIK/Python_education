# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:21:30 2022

@author: Leshk
"""

import os
import shutil
import sys
import json

def change(a,b):
        if sp[0] == "a":
            sp[0] = "b"
            with  open ('file_4.1.txt', 'a', encoding='utf-8' ) as f_1: 
                print(" ".join(sp), file = f_1)

with  open ('file_4.txt', 'r', encoding='utf-8' ) as f:       
    for line in f:
        st = line.replace('\n','')
        sp = st.split()        
        if sp[0] == "One":
            sp[0] = "Один"
            with  open ('file_4.1.txt', 'a', encoding='utf-8' ) as f_1: 
                print(" ".join(sp), file = f_1)
        if sp[0] == "Two":
            sp[0] = "Два"
            with  open ('file_4.1.txt', 'a', encoding='utf-8' ) as f_1: 
                print(" ".join(sp), file = f_1)
        if sp[0] == "Three":
            sp[0] = "Три"
            with  open ('file_4.1.txt', 'a', encoding='utf-8' ) as f_1: 
                print(" ".join(sp), file = f_1)
        if sp[0] == "Four":
            sp[0] = "Четыре"
            with  open ('file_4.1.txt', 'a', encoding='utf-8' ) as f_1: 
                print(" ".join(sp), file = f_1)        
 

         
         