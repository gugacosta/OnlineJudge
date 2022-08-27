# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 21:48:21 2022

@author: gusta
"""

a,b,c = map(int, input().split())

if  ((a+b)>c) and ((a+c)>b) and ((b+c)>a):
    print(("YES"))
    
else:
    print("NO")