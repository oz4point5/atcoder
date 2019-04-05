import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC053/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

x = input()

a = 0
z = 0

for i in range(len(x)):
    if x[i] == "A":
        a = i
        break

for i in range(len(x)):
    if x[-(i+1)] == "Z":
        z = len(x) - i
        break

print(len(x[a:z]))
