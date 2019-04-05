import sys
import os
f = open("C:/Users/user/Documents/python/ant/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

n = int(input())
w = list(map(int,input().split()))
v = list(map(int,input().split()))
W = int(input())

dp = [[0 for i in range(W + 1)] for j in range(n+1)]

for i in range(n):
    for j in range(W):
        k = 0
        while k * w[i] <= j:
            dp[i + 1][j] = max (dp[i+1][j], dp[i][j - k * w[i]] + k * v[i])
            k += 1

print(dp[n][W])
