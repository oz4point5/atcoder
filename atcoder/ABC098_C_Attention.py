import sys
import os
f = open("C://Users/OZ/Documents/python/atcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
s = list(input())
w = [0] * n
e = [0] * n

cntw = 0
cnte = 0
for i in range(n):
    if s[i] == "W":
        cntw += 1
        w[i] = cntw
    else:
        w[i] = cntw
    if s[i] == "E":
        cnte += 1
        e[i] = cnte
    else:
        e[i] = cnte

ans = float("inf")

for i in range(n):
    num = 0
    if i-1 >= 0:
        num += w[i-1]
    num += e[-1] - e[i]
    ans = min(num,ans)

print(ans)
