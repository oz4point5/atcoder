import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

L = int(input())
n = int(input())
x = list(map(int,input().split()))

minT = 0
for i in range(n):
    minT = max(minT, min(x[i], L - x[i]))

maxT = 0
for i in range(n):
    maxT = max(maxT, max(x[i], L - x[i]))

print(minT)
print(maxT)
