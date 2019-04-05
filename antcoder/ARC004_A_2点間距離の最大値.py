import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i],y[i] = map(int,input().split())

length = 0

for i in range(n):
    for j in range(i,n):
        length = max(length,((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5)

print(length)
