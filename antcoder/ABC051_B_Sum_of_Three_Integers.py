import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

k,s = map(int,input().split())

cnt = 0

for i in range(k+1):
    for j in range(k+1):
        for l in range(k+1):
            if i + j + l == s:
                cnt += 1

print(cnt)
