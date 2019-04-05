import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

MAX_N = 100000

N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

itv = [0] * N

for i in range(N):
    itv[i] = (T[i],S[i])
itv.sort()

ans = 0
t = 0
for i in range(N):
    if t < itv[i][1]:
        ans += 1
        t = itv[i][0]

print(ans)
