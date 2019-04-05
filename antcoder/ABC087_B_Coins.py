import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-
a = int(input())
b = int(input())
c = int(input())
x = int(input())

cnt = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if 500 * i + 100 * j + 50 * k == x:
                cnt += 1

print(cnt)
