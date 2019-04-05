import sys
import os
f = open("C:/Users/user/Documents/python/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

N,M,C = map(int,input().split())
B = list(map(int,input().split()))
A = [0] * N
for i in range(0,N):
    A[i] = list(map(int,input().split()))

ans = 0

for index, item in enumerate(range(0,N)):
    sum = 0
    for ind, itm in enumerate(range(0,M)):
        sum += B[ind] * A[index][ind]
    sum += C
    if sum > 0:
        ans += 1

print(ans)
