import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

# 入力
L = int(input())
n = int(input())
x = list(map(int,input().split()))

# 最小の時間を計算
minT = 0
for i in range(n):
    minT = max(minT, min(x[i], L - x[i]))

# 最大の時間を計算
maxT = 0
for i in range(n):
    maxT = max(maxT, x[i], L - x[i])

print(minT)
print(maxT)
