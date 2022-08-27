# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 22:30:54 2022

@author: gusta
"""

a,b = input().split(" ")
a = int(a)
b = int(b)
if (a>=b):
    a = 24-a+b
    print(f"O JOGO DUROU {a} HORA(S)") 
else:
    a=b-a
    print(f"O JOGO DUROU {a} HORA(S)")
    