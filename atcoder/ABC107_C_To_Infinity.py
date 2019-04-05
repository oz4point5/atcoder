import sys
import os
f = open("C://Users/OZ/Documents/python/atcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-
s = list(map(int,list(input())))
k = int(input())

flag = 0

for i in range(len(s)):
    if flag == 0 and s[i] == 1:
        s[i] = 1
    elif flag == 0:
        s[i] = s[i]
        flag = s[i]
    else:
        s[i] = flag

if k > len(s):
    print(s[-1])
else:
    print(s[k-1])
