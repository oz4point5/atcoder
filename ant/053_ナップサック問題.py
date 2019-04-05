import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
w = []
v = []
for i in range(0,n):
    temp = list(map(int,input().split()))
    w.append(temp[0])
    v.append(temp[1])
W = int(input())

dp = [[-1] * (n + 2)] * (W + 2)

def rec(i,j):
    if 0 <= i < n and 1 <= j < n:
        if dp[i][j] >= 0:
            return dp[i][j]
    if i == n:
        res = 0
    elif j < w[i]:
        res = rec(i + 1, j)
    else:
        res = max(rec(i + 1,j), rec(i + 1,j - w[i]) + v[i])
    if 0 <= i < n and 1 <= j < n:
            dp[i][j] = res
    return res

print(rec(0,W))
