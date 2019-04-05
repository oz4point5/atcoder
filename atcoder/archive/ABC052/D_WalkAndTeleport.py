import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC118/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,a,b = map(int,input().split())
x = list(map(int,input().split()))

fatigue = 0

for i in range(1,n):
    if (x[i] - x[i-1]) * a <= b:
        fatigue += (x[i] - x[i-1]) * a
    else:
        fatigue += b

print(fatigue)
