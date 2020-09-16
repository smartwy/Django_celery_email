#!/usr/bin/python3
# -*- coding:utf-8 -*-
#P-Name:    Data_Analysis
#F-Name:    code_10.py
#Login:     Administrator   
#Descripton:
#__Author__  Smartwy
#Date:      2020/5/22 13:51:30
#Version:

'''
    
'''


import string
import random

def create_code():
    code = string.ascii_letters+string.digits+string.ascii_uppercase
    codes = [''.join(random.choices(code,k=5)) for _ in range(4)]
    col = '-'.join(codes)
    print(col)
    return col

if __name__ == '__main__':
    create_code()