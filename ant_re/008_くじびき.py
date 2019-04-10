import sys
import os
f = open("C:/Users/user/Documents/python/ant_re/import.txt","r")
sys.stdin = f

# -*- coding: utf-8 -*-

MAX_N = 50


# 標準入力より入力
n = int(input())
m = int(input())
k = list(map(int,input().split()))

# 和がmになる組合せが見つかったかどうかのフラグ
f = False

# 4重ループにより全通りの出方を試す
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                if k[a] + k[b] + k[c] + k[d] == m:
                    f = True

# 標準出力へ出力
if f:
    print("Yes")
else:
    print("No")
