# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 21:16:42 2022

@author: gusta
"""

N, K = map(int, input().split())
Lista = list(map(int, input().split()))

print(N, K, Lista)
for i in range(N):
    if Lista[i]==K:
        print("1")
        break
    elif i==(N-1):
        print("-1")
    
    
    