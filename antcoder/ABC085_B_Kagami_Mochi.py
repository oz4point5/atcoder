import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
d = [0] * n
for i in range(n):
    d[i] = int(input())

d = set(d)
d = list(d)

print(len(d))
