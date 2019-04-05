import sys
import os
f = open("C:/Users/user/Documents/python/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
money = []
sum = 0
for i in range(0,n):
    money.append(input().split())
for i in money:
    if i[1] == "JPY":
        sum += float(i[0])
    else:
        sum += float(i[0]) * 380000.0
print(sum)
