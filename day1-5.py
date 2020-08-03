# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:24:11 2020

@author: USER
"""
aa=input('hello')
aa=int(aa)
if aa>=0 and aa<=100:
    print('your level is')
    if aa>=90:
        print('A')
    elif aa>=80:
        print('B')
    else:
        print('c')
else:
     print('error') 