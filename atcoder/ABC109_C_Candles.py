import sys
import os
f = open("C://Users/OZ/Documents/python/atcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n,k = map(int,input().split())
x = list(map(int,input().split()))

x_minus = []
x_plus = []

for i in range(n):
    if x[i] >= 0:
        x_plus.append(x[i])
    else:
        x_minus.append(x[i])
x_minus.reverse()

ans = 100000000000
for i in range(len(x_minus)):
    if len(x_plus) + i >= k:
        length = abs(x_minus[i-1]) * 2 + x_plus[k-i-1]
        ans = min(ans,length)

if ans == 100000000000:
    ans = x_plus[k-1]

print(ans)
