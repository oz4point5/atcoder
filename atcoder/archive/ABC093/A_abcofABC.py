import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC093/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

a = list(input())

a.sort()

a = "".join(a)

if a == "abc":
    print("Yes")
else:
    print("No")
