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

dp = [[0] * (W + 1)] * (n + 1)

for i in range(n-1,-1,-1):
    for j in range(W+1):
        if(j < w[i]):
            dp[i][j] = dp[i + 1][j]
        else:
            dp[i][j] = max(dp[i+1][j],dp[i+1][j-w[i]]+v[i])

print(dp[0][W])

print(dp)
