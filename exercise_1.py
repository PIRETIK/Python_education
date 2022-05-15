# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:20:30 2022

@author: Leshk
"""

import os
import shutil
import sys
import json

with open ('file_1.txt','w') as f:
    while True:
        content = input("Введите текст: ")
        f.write(content +'\n')
        if not content:
            break
with open ('file_1.txt','r') as f:
    print(f.read())