import sys
import os
f = open("C://Users/OZ/Documents/python/antcoder/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

import math

d,g = map(int,input().split())
p = [0] * d
c = [0] * d
for i in range(d):
    p[i],c[i] = map(int,input().split())

ans = 1000000000
#bit全探索
n = d
arr = [0] * n
for i in range(2 ** n):
    for j in range(n):
        if((1&i>>j) == 1):
            arr[j] = 1
        else:
            arr[j] = 0
    #ここに処理
    score = 0
    question = 0
    for j in range(len(arr)):
        if arr[j] == 1:
            score += (j+1)*100*p[j] + c[j]
            question += p[j]
    if score >= g:
        ans = min(ans,question)
    else:
        for j in range(len(arr)-1,-1,-1):
            if arr[j] == 0:
                if g - score <= (j+1)*100*(p[j]-1):
                    temp = math.ceil((g - score) / ((j+1)*100))
                    question += temp
                    ans = min(ans,question)
                break


print(ans)
