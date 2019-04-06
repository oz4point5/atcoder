import sys
import os

f = open("C:/Users/user/Documents/atCoderProblem/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
s = list(input())

def list_intersection(a,b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c.append(a[i])
                a[i] = "_"
                b[j] = "&"
    return c

ans = 0
for i in range(1,n):
    inter = list_intersection(s[:i],s[i:])
    inter = set(inter)
    inter = list(inter)
    ans = max(ans,len(inter))

print(ans)
