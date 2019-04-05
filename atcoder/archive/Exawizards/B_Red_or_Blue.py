import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/Exawizards/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
s = list(input())

r = 0
b = 0

for i in range(n):
    if s[i] == "R":
        r += 1
    else:
        b += 1

if r > b:
    print("Yes")
else:
    print("No")
