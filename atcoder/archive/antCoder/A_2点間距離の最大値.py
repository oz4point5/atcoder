import sys
import os
f = open("C:/Users/user/Documents/python/atcoder/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
xy = [[0 for i in range(2)] for j in range(n)]
for i in range(n):
    temp = list(map(int,input().split()))
    xy[i][0] = temp[0]
    xy[i][1] = temp[1]

maxlen = 0

for i in range(n):
    for j in range(n):
        len = ((xy[i][0] - xy[j][0])**2 +(xy[i][1] - xy[j][1])**2)**0.5
        maxlen = max(maxlen,len)

print(maxlen)
