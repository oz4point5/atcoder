import sys
import os
f = open("C://Users/OZ/Documents/python/atcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-
s = list(input())
k = int(input())

part = [[]]

for i in range(len(s)):
    for j in range(1,k+1):
        if i + j > len(s):
            break
        part.append(s[i:i+j])
del part[0]

part.sort()

delete = []

for i in range(1,len(part)):
    if part[i-1] == part[i]:
        delete.append(i)

diff = 0
for i in range(len(delete)):
    del part[delete[i] - diff]
    diff += 1

print("".join(part[k-1]))
