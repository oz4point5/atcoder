import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int,input().split()))

flag = False
cnt = 0

for i in range(10000000000):
    for j in range(n):
        if a[j] % 2 == 0:
            a[j] = int(a[j] / 2)
        else:
            flag = True
            break
    if flag == True:
        break
    else:
        cnt += 1

print(cnt)
