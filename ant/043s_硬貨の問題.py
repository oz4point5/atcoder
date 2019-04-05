import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

c = list(map(int,input().split()))
a = int(input())
v = [1,5,10,50,100,500]
coin = 0

for i in range(len(c)-1,-1,-1):
    temp = a // v[i]
    print(i)
    if temp <= c[i]:
        a -= temp * v[i]
        coin += temp
    else:
        a -= c[i] * v[i]
        coin += c[i]

print(coin)
