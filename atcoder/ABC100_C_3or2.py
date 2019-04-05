import sys
import os
f = open("C://Users/OZ/Documents/python/atcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int,input().split()))

cnt = 0

for i in range(n):
    while(True):
        if a[i] % 2 != 0:
            break
        else:
            a[i] = int(a[i] / 2)
            cnt += 1

print(cnt)
