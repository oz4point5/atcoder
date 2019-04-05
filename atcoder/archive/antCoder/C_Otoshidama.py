import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,y = map(int,input().split())

r = y - 1000 * n

for i in range(0,n+1):
    temp = r - 9000 * i
    if temp % 4000 == 0:
        j = temp / 4000
        k = n - i - j
        if j >= 0 and k >= 0:
            print(int(i),int(j),int(k))
            break
else:
    print(-1,-1,-1)
