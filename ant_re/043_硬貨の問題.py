import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

# コインの金額
V = [1,5,10,50,100,500]

# 入力
C = list(map(int,input().split()))
A = int(input())

ans = 0

for i in range(5,-1,-1):
    t = min(int(A / V[i]), C[i])    # コインiを使う枚数
    A -= t * V[i]
    ans += t

print(ans)
