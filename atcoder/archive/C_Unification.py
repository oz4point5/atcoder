import sys
import os
f = open("C:/Users/user/Documents/python/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

s = str(input())

one = 0
zero = 0

for i in s:
    if i == "0":
        zero += 1
    else:
        one += 1
if zero > one:
    print(one * 2)
else:
    print(zero * 2)
