import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
m = int(input())
s = list(input())
t = list(input())

def dpf(a,b):
    if a == 0:
        return 0
    if b == 0:
        return 0
    if s[a-1] == t[b-1]:
        return dpf(a-1,b-1)+1
    else:
        return max(dpf(a,b-1),dpf(a-1,b))

print(dpf(n,m))
