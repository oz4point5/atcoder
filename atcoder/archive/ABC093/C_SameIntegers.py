import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC093/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

a,b,c = map(int,input().split())

magic = max(a,b,c)*3-a-b-c

if magic % 2 == 0:
    print(int(magic / 2))
else:
    print(int((magic + 1) / 2) + 1)
