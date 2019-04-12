import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
w = []
for i in range(n):
    w.append(int(input()))

cb = [w[0]]
cnt = 1

for i in range(n):
    for j in range(len(cb)):
        if cb[j] >= w[i]:
            cb[j] = w[i]
            break
    else:
            cb.append(w[i])

print(len(cb))
