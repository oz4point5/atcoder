import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/Exawizards/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,q = map(int,input().split())
s = list(input())
t = [0] * q
d = [0] * q
for i in range(q):
    t[i],d[i] = input().split()

gorem = [1] * n

for i in range(q):
    for j in range(n):
        if t[i] == s[j]:
            if d[i] == "L":
                if j == 0:
                    gorem[j] = 0
                else:
                    gorem[j-1] += gorem[j]
                    gorem[j] = 0
            else:
                if j >= n - 1:
                    gorem[j] = 0
                else:
                    gorem[j+1] += gorem[j]
                    gorem[j] = 0

print(sum(gorem))
