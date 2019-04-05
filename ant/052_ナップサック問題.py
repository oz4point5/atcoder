import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
w = []
v = []
for i in range(0,n):
    temp = list(map(int,input().split()))
    w.append(temp[0])
    v.append(temp[1])
W = int(input())

def rec(i,j):
    if i == n:
        res = 0
    elif j < w[i]:
        res = rec(i + 1,j)
    else:
        res = max(rec(i+1,j),rec(i+1,j-w[i])+v[i])
    return res

print(rec(0,W))
