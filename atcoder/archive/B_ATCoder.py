import sys
import os
f = open("C:/Users/user/Documents/python/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

s = input()

cur = 0
max = 0

for index,item in enumerate(s):
    if item == "A" or item == "T" or item == "G" or item == "C":
        cur += 1
        if cur >= max:
            max = cur
    else:
        cur = 0

print(max)
