import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

# 入力
N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))

# 仕事をソートするためのpairの配列
itv = [[0,0] for _ in range(N)]

# pairは辞書順で比較される
# 終了時間の早い順にしたいため、Tをfirstに、Sをsecondに入れる
for i in range(N):
    itv[i][0] = T[i]
    itv[i][1] = S[i]

# tは最後に選んだ仕事の終了時間
ans,t = 0,0
for i in range(N):
    if t < itv[i][1]:
        ans += 1
        t = itv[i][0]

print(ans)
