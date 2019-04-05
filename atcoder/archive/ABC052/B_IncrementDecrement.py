import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC118/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
s = list(input())

x = 0
max_x = 0

for i in range(len(s)):
    if s[i] == "I":
        x += 1
    elif s[i] == "D":
        x -= 1
    max_x = max(max_x,x)

print(max_x)
