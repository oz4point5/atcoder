import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC118/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

a,b = map(int,input().split())
if b % a== 0:
    print(a+b)
else:
    print(b-a)
