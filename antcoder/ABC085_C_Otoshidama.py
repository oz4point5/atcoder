import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,y = map(int,input().split())

is_searched = False

for i in range(n+1):
    for j in range(n+1):
        k = n - i - j
        if k < 0:
            continue
        if i * 10000 + j * 5000 + k * 1000 == y :
            print(i,j,k)
            is_searched = True
            break
    if is_searched:
        break
else:
    print(-1,-1,-1)
