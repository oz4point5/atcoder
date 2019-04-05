import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/ABC093/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

#入力

q = int(input())
ab = [[0,0] for i in range(q)]
for i in range(q):
    temp = list(map(int,input().split()))
    ab[i][0] = temp[0]
    ab[i][1] = temp[1]

#解法

wall = 0
magic = 0
ans = 0

for i in range(q):
    if ab[i][0] >= ab[i][1]:
        a = ab[i][0]
        b = ab[i][1]
    else:
        a = ab[i][1]
        b = ab[i][0]
    wall = a * b
    magic = b - 1
    for j in range(a,b,-1):
        if j * (b + 1) < wall:
            magic = j
            break
    ans = magic + b - 1
    print(ans)
