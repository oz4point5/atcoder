import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-
s = list(input())

cand = []

#bit全探索
n = len(s) - 1
arr = [0] * n
for i in range(2 ** n):
    diff = 0
    for j in range(n):
        if((1&i>>j) == 1):
            arr[j] = 1
        else:
            arr[j] = 0
    #ここに処理
    s_copy = s[:]
    diff = 0
    for j in range(len(arr)):
        if arr[j] == 1:
            s_copy = s_copy[:(j+diff+1)] + ["+"] + s_copy[(j+diff+1):]
            diff += 1
    cand.append(s_copy)

cand_sum = []

for i in range(len(cand)):
    t = "".join(cand[i])
    tt = []
    tt = t.split("+")
    tt = list(map(int,tt))
    cand_sum.append(sum(tt))

print(sum(cand_sum))
